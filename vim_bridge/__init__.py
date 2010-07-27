from vim_bridge.registry import func_register

def bridged(fin):
    func_register[fin.func_name] = fin

    func_args = fin.func_code.co_varnames

    import vim
    lines = ['function %s(%s)' % (fin.func_name, ", ".join(func_args))]
    lines.append('python << endp')
    for arg in func_args:
        lines.append('__%s = vim.eval("a:%s")' % (arg, arg))
    lines.append('from vim_bridge.registry import func_register')
    lines.append('__result = func_register["%s"](%s)' % (fin.func_name, \
            ", ".join(map(lambda s: "__%s" % s, func_args))))
    lines.append('vim.command("return %s" % repr(__result))')
    lines.append('endp')
    lines.append('endf')
    vim.command("\n".join(lines))

    return fin

