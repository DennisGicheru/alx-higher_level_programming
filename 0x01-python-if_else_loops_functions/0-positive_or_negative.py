#!/usr/bin/python3
import random
number = random.randint(-10,10)
while number:
	if number > 0:
		print("{} is positive".format(number))
	if number == 0:
		print("{} is zero".format(number))
	if number < 0:
		print("{} is negative".format(number))
	break;
