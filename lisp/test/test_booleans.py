from .. import run_program


def test_true():
    source_code = """
        #t
    """
    assert(run_program(source_code) == True)


def test_false():
    source_code = """
        #f
    """
    assert(run_program(source_code) == False)
