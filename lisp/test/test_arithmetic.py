from .. import run_program


def test_addition():
    source_code = """
        (+ 3 4)
    """
    assert(run_program(source_code) == 7)


def test_subtraction():
    source_code = """
        (- 8 2)
    """
    assert(run_program(source_code) == 6)


def test_multiplication():
    source_code = """
        (* 9 7)
    """
    assert(run_program(source_code) == 63)


def test_division():
    source_code = """
        (/ 12 4)
    """
    assert(run_program(source_code) == 3)


def test_combinations():
    source_code = """
        (* (+ (- 9 3)
              2)
           (/ 36 9))
    """
    assert(run_program(source_code) == 32)


def test_greater_than():
    source_code = """
        (> 4 3)
    """
    assert(run_program(source_code) == True)


def test_greater_than_failure():
    source_code = """
        (> 7 8)
    """
    assert(run_program(source_code) == False)


def test_less_than():
    source_code = """
        (< 7 8)
    """
    assert(run_program(source_code) == True)


def test_less_than_failure():
    source_code = """
        (< 4 3)
    """
    assert(run_program(source_code) == False)


def test_greater_than_or_equal():
    source_code = """
        (>= 3 3)
    """
    assert(run_program(source_code) == True)


def test_greater_than_or_equal_failure():
    source_code = """
        (>= 3 5)
    """
    assert(run_program(source_code) == False)


def test_less_than_or_equal():
    source_code = """
        (<= 3 3)
    """
    assert(run_program(source_code) == True)


def test_less_than_or_equal_failure():
    source_code = """
        (<= 5 3)
    """
    assert(run_program(source_code) == False)


def test_equal():
    source_code = """
        (= 7 7)
    """
    assert(run_program(source_code) == True)


def test_not_equal():
    source_code = """
        (= 9 2)
    """
    assert(run_program(source_code) == False)
