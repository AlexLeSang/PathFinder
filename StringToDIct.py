import ast

__author__ = 'varg'


def string_to_dict(string):
    try:
        return ast.literal_eval(string)
    except SyntaxError:
        return None
