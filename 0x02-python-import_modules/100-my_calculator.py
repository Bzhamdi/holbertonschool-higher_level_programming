#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == '+' or op == '-' or op == '*' or op == '/':
        if op == '+':
            r = add(a, b)
        if op == '-':
            r = sub(a, b)
        if op == '*':
            r = mul(a, b)
        if op == '/':
            r = div(a, b)
        print('{} {} {} = {}'.format(a, op, b, r))
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
