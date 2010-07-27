from vim_bridge.registry import func_register

class bridged(object):

    def __init__(self, *args):
        self.args = args

    def __call__(self, fin):
        func_register[fin.func_name] = fin

        import vim
        lines = ['function %s(%s)' % (fin.func_name, ", ".join(self.args))]
        lines.append('python << endp')
        for arg in self.args:
            lines.append('__%s = vim.eval("a:%s")' % (arg, arg))
        lines.append('from vim_bridge.registry import func_register')
        lines.append('__result = func_register["%s"](%s)' % (fin.func_name, ", ".join(map(lambda s: "__%s" % s, self.args))))
        lines.append('vim.command("return %s" % repr(__result))')
        lines.append('endp')
        lines.append('endf')
        vim.command("\n".join(lines))

        return fin

