import sys

from vim_bridge.registry import func_register

__all__ = ['bridged', '_cast_to_vimsafe_result', '__version__']

VERSION = (0, 5)
__version__ = ".".join(map(str, VERSION[0:2]))


def _rand():
    import random
    random.seed()
    return random.randint(1000, 9999)


def _upcase_first(s):
    if len(s) == 0:
        return s
    else:
        return s[0].upper() + s[1:]


def _convert_function_name(fname):
    private = fname.startswith('_')
    if private:
        fname = fname[1:]
    fname = "".join([_upcase_first(part) for part in fname.split('_')])
    return (private, fname)


def _get_arguments(func):
    return func.__code__.co_varnames[:func.__code__.co_argcount]


def _cast_to_vimsafe_result(value):
    if value is None:
        # The string 'None' means nothing in Vim
        return ''
    elif type(value) == bool:
        return str(int(value))
    else:
        # Default fallback is the Python representation as a string
        # The representation looks very similar to Vim's, so this should be
        # safe for most results
        return repr(value)


def bridged(fin):
    import vim
    func_register[fin.__name__] = fin

    func_args = _get_arguments(fin)

    private, vimname = _convert_function_name(fin.__name__)
    private = private and "s:" or ""

    prefix = '__vim_brdg_%d_' % _rand()

    lines = ['fun! %s%s(%s)' % (private, vimname, ", ".join(func_args))]
    # Execute with same Python that we are running.
    python = 'python' if sys.version_info == 2 else 'python3'
    lines.append(python + ' << endp')
    for arg in func_args:
        lines.append('%s%s = vim.eval("a:%s")' % (prefix, arg, arg))
    lines.append('from vim_bridge.registry import func_register as fr')
    lines.append('from vim_bridge import _cast_to_vimsafe_result as c2v')
    lines.append('%sresult = c2v(fr["%s"](%s))' % (prefix, fin.__name__,
            ", ".join([prefix + s for s in func_args])))
    lines.append('vim.command("return %%s" %% repr(%sresult))' % prefix)
    for arg in func_args:
        #lines.append('try:')
        lines.append('del %s%s' % (prefix, arg))
        #lines.append('except NameError: pass')
    lines.append('del %sresult' % prefix)
    lines.append('endp')
    lines.append('endf')
    vim.command("\n".join(lines))

    return fin
