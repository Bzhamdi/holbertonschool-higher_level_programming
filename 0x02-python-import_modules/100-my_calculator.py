#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    fn = [add, sub, mul, div]
    for i, j in enumerate(op):
        if argv[2] == j:
            print("{} {} {} = {}".format(a, j, b, fn[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
