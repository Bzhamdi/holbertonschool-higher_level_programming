#!/usr/bin/python3
def text_indentation(text):
    check = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for x in text:
        if check == 0 and x == ' ':
            continue
        else:
            check = 1
        if x in '?.:':
            check = 0
            print(x)
            print()
        else:
            print(x, end="")
