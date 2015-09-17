from src import parser
from src.function import Function
from src.scope import TopLevel


def run_program(source_code):
    syntax_tree = parser.parse(source_code)
    top_level = TopLevel()
    return syntax_tree.evaluate(top_level)
