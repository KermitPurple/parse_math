"""
Module for parsing math strings and calculating the result

1 + 2 + 3 is equal to 1 + (2 + 3)
but
2 * 2 + 3 is not equal to 2 * (2 + 3)
"""

import re

OPERAtORS = ['+', '-', '*', '/', '**', '^']

def perform_op(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**' or operator == '^':
        return num1 ** num2
    else:
        raise 'Invalid operator'

def calc_simple_string(s: str) -> int:
    # TODO: Order of operations
    equation = re.findall(r'\d+(?:\.\d+)?|[+*/\-]',s)
    while len(equation) > 1:
        equation.insert(0, perform_op(float(equation.pop(0)), equation.pop(0), float(equation.pop(0))))
    return equation[0]

def calc_complex_string(s: str) -> int:
    pat = r'\([^()]*?\)'
    while re.search(r'[()]+', s):
        matches = re.findall(pat, s)
        for match in matches:
            s = s.replace(match, str(calc_simple_string(match)))
            print(s)
    return calc_simple_string(s)

if __name__ == '__main__':
    while 1:
        s = input('Enter an equation> ')
        if s == 'exit':
            break
        print(calc_complex_string(s))
