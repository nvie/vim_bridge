import unittest

# Fake the system path to direct "import vim" calls to our mock module
import sys
sys.path = ['tests/mocks'] + sys.path

# Stub out the random function
import vim_bridge
vim_bridge._rand = lambda: 3

from vim_bridge import bridged


class TestHelperFunctions(unittest.TestCase):

    def test_upcase_first(self):
        from vim_bridge import _upcase_first as ucf
        self.assertEquals(ucf(''), '')
        self.assertEquals(ucf('a'), 'A')
        self.assertEquals(ucf('A'), 'A')
        self.assertEquals(ucf('_foo'), '_foo')

    def test_convert_function(self):
        from vim_bridge import _convert_function_name as cfn
        self.assertEquals(cfn('foo'), (False, 'Foo'))
        self.assertEquals(cfn('_foo'), (True, 'Foo'))
        self.assertEquals(cfn('_ThiS_is_A_MiXed__case_'), \
                (True, 'ThiSIsAMiXedCase'))

    def test_get_arguments(self):
        from vim_bridge import _get_arguments as ga

        def foo(a,b,c): pass
        def bar(x,y):
            z = 3
            z = z + x + y
            return z
        self.assertEquals(ga(foo), ('a','b','c'))
        self.assertEquals(ga(bar), ('x','y'))

    def test_cast_to_vimsafe_result(self):
        from vim_bridge import _cast_to_vimsafe_result as cast

        self.assertEquals(cast(3), "3")
        self.assertEquals(cast('3'), "'3'")
        self.assertEquals(cast(''), "''")
        self.assertEquals(cast(None), "")
        self.assertEquals(cast(True), "1")
        self.assertEquals(cast(False), "0")
        self.assertEquals(cast([1,2,3]), "[1, 2, 3]")


class TestBridgedDecorator(unittest.TestCase):

    def _strip_whitespace(self, x):
        lines = x.split("\n")
        lines = [line.strip() for line in lines]
        x = "\n".join([s for s in lines if s])
        return x

    def assertCodeEquals(self, x, y):
        self.assertEquals(self._strip_whitespace(x), self._strip_whitespace(y))

    def test_no_bridges_yet(self):
        from vim_bridge.registry import func_register
        self.assertEquals(func_register, {})

    def test_simple_bridge(self):
        from vim_bridge.registry import func_register
        import vim

        self.assertFalse('foo' in func_register)
        self.assertFalse(vim.command.called)

        @bridged
        def foo(x,y): pass

        self.assertTrue('foo' in func_register)
        self.assertTrue(vim.command.called)
        self.assertCodeEquals(vim.command.call_args[0][0], \
           """
           fun! Foo(x, y)
           python << endp
           __vim_brdg_3_x = vim.eval("a:x")
           __vim_brdg_3_y = vim.eval("a:y")

           from vim_bridge.registry import func_register as fr
           from vim_bridge import _cast_to_vimsafe_result as c2v

           __vim_brdg_3_result = c2v(fr["foo"](__vim_brdg_3_x, __vim_brdg_3_y))
           vim.command("return %s" % repr(__vim_brdg_3_result))

           del __vim_brdg_3_x
           del __vim_brdg_3_y
           del __vim_brdg_3_result
           endp
           endf
           """)

