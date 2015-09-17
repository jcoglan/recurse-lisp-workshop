from .. import run_program, Function


def test_lambda_creates_a_function():
    source_code = """
        (lambda () (+ 5 6))
    """
    assert(type(run_program(source_code)) == Function)


def test_calling_a_nullary_function():
    source_code = """
        (define nine (lambda () + 4 5))

        (nine)
    """
    assert(run_program(source_code) == 9)


def test_calling_a_multi_line_function():
    source_code = """
        (define ten (lambda ()
                      (define x 7)
                      (define y 3)
                      (+ x y)))

        (ten)
    """
    assert(run_program(source_code) == 10)


def test_calling_a_binary_function():
    source_code = """
        (define max (lambda (x y)
                      (if (> x y)
                          x
                          y)))

        (max 3 6)
    """
    assert(run_program(source_code) == 6)


def test_variables_are_scoped_to_the_function():
    source_code = """
        (define square (lambda (x) (* x x)))

        (define x 8)

        (square 3)

        x
    """
    assert(run_program(source_code) == 8)


def test_recursion():
    source_code = """
        (define factorial (lambda (x)
                            (if (= x 0)
                                1
                                (* (factorial (- x 1))
                                   x))))

        (factorial 6)
    """
    assert(run_program(source_code) == 720)


def test_lexical_closures():
    source_code = """
        (define add (lambda (x)
                      (lambda (y)
                        (+ x y))))

        (define add2 (add 2))

        (add2 4)
    """
    assert(run_program(source_code) == 6)
