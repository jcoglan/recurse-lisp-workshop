from src import parser
from src.function import Function
from src.scope import TopLevel


def run_program(source_code):
    program = parser.parse(source_code)
    print program
    top_level = TopLevel()
    return program.evaluate(top_level)
