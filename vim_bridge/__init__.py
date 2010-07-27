from vim_bridge.registry import func_register

def bridged(fin):
    func_register[fin.func_name] = fin

    func_args = fin.func_code.co_varnames

    import vim
    lines = ['function %s(%s)' % (fin.func_name, ", ".join(func_args))]
    lines.append('python << endp')
    for arg in func_args:
        lines.append('__vim_bridge_%s = vim.eval("a:%s")' % (arg, arg))
    lines.append('from vim_bridge.registry import func_register')
    lines.append('__vim_bridge_result = func_register["%s"](%s)' % (fin.func_name, \
            ", ".join(map(lambda s: "__vim_bridge_%s" % s, func_args))))
    lines.append('vim.command("return %s" % repr(__vim_bridge_result))')
    for arg in func_args:
        lines.append('del __vim_bridge_%s' % arg)
    lines.append('del __vim_bridge_result')
    lines.append('endp')
    lines.append('endf')
    vim.command("\n".join(lines))

    return fin

