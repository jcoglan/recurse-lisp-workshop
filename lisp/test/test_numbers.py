from .. import run_program


def test_int():
    source_code = """
        234
    """
    assert(run_program(source_code) == 234)


def test_float():
    source_code = """
        3.14
    """
    assert(run_program(source_code) == 3.14)


def test_negative_float():
    source_code = """
        -0.17
    """
    assert(run_program(source_code) == -0.17)
