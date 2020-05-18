#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        l = a / b
    except ZeroDivisionError:
        l = None
    finally:
        print("Inside result: {}".format(result))
    return l
