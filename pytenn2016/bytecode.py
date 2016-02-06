from types import CodeType, FunctionType


def code_attrs(code):
    """Return a dict of attributes of a code object."""
    return {
        'co_argcount': code.co_argcount,
        'co_kwonlyargcount': code.co_kwonlyargcount,
        'co_nlocals': code.co_nlocals,
        'co_stacksize': code.co_stacksize,
        'co_flags': code.co_flags,
        'co_code': code.co_code,
        'co_consts': code.co_consts,
        'co_names': code.co_names,
        'co_varnames': code.co_varnames,
        'co_filename': code.co_filename,
        'co_name': code.co_name,
        'co_firstlineno': code.co_firstlineno,
        'co_lnotab': code.co_lnotab,
        'co_freevars': code.co_freevars,
        'co_cellvars': code.co_cellvars,
    }


def update_code(f, **kwargs):
    """Update attributes of a function's __code__."""

    code = f.__code__
    newcode = CodeType(
        kwargs.get('co_argcount', code.co_argcount),
        kwargs.get('co_kwonlyargcount', code.co_kwonlyargcount),
        kwargs.get('co_nlocals', code.co_nlocals),
        kwargs.get('co_stacksize', code.co_stacksize),
        kwargs.get('co_flags', code.co_flags),
        kwargs.get('co_code', code.co_code),
        kwargs.get('co_consts', code.co_consts),
        kwargs.get('co_names', code.co_names),
        kwargs.get('co_varnames', code.co_varnames),
        kwargs.get('co_filename', code.co_filename),
        kwargs.get('co_name', code.co_name),
        kwargs.get('co_firstlineno', code.co_firstlineno),
        kwargs.get('co_lnotab', code.co_lnotab),
        kwargs.get('co_freevars', code.co_freevars),
        kwargs.get('co_cellvars', code.co_cellvars),
    )

    return FunctionType(
        newcode,
        f.__globals__,
        f.__name__,
        f.__defaults__,
        f.__closure__,
    )
