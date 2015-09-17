from ..src import parser

program = """
(define x 5)

#t

(define sq (lambda (x) (* x x)))
"""

print parser.parse(program)
