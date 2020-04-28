#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdg = number % -10
else:
    lastdg = number % 10
print('Last digit of {:d} is {:d} '.format(number, lastdg), end="")
if lastdg == 0:
    print('and is 0')
elif lastdg > 5:
    print('and is greater than 5')
elif lastdg < 6:
    print('and is less than 6 and not 0')
