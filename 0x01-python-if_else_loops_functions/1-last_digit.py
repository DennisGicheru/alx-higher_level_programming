#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = abs(number) % 10
    last_digit = -(last_digit)
else:
    last_digit = number % 10

if last_digit > 5:
    last_str = "greater than 5"
elif last_digit == 0:
    last_str = "0"
else:
    last_str = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last_digit, last_str))
