from .. import run_program


def test_boolean_literal_true():
    source_code = """
        (if #t 33 45)
    """
    assert(run_program(source_code) == 33)


def test_boolean_literal_false():
    source_code = """
        (if #f 33 45)
    """
    assert(run_program(source_code) == 45)


def test_condition_with_expressions():
    source_code = """
        (if (>= 9 4)
            (+ 3 2)
            (* 8 9))
    """
    assert(run_program(source_code) == 5)


def test_only_one_branch_is_run():
    source_code = """
        (define x 21)

        (if #t
            (define x 99)
            (define x 55))
    """
    assert(run_program(source_code) == 99)
