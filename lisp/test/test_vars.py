from .. import run_program, Function


def test_builtin():
    source_code = """
        +
    """
    assert(type(run_program(source_code)) == Function)


def test_defining_a_var():
    source_code = """
        (define my-var 42)
        my-var
    """
    assert(run_program(source_code) == 42)
