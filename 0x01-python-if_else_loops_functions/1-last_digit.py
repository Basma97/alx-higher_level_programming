#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > 0 else number % -10
if last == 0:
    print("Last digit of {:d} is {:d} and is 0"
    .format(number, last))
elif last < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
    .format(number, last))
else:
    print("Last digit of {:d} is {:d} and is greater than 5"
    .format(number, last))
