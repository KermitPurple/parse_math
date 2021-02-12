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
    equation = re.findall(r'\d+(?:\.\d+)?|[+*/\-]',s)
    while len(equation) > 1:
        equation.insert(0, perform_op(float(equation.pop(0)), equation.pop(0), float(equation.pop(0))))
    return equation[0]

if __name__ == '__main__':
    pat = r'\([^()]*?\)'
    s =  '(12 * ((3 + 1) - (3 - 2))) - 1'
    while re.match(r'[()]', s):
        matches = re.findall(pat, s)
        for match in matches:
            s = s.replace(match, str(calc_simple_string(match)))
            print(s)
    print(calc_simple_string(s))
