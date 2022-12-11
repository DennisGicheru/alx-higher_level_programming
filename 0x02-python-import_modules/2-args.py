#!/usr/bin/python3
import sys
n = len(sys.argv)

if n == 1:
    print("{:d} arguments.".format(n-1))

elif n == 2:
    print("{:d} argument:".format(n-1))

else:
    print("{:d} arguments:".format(n-1))

for i in range(1, n):
    print("{:d}: {}".format(i, sys.argv[i]))
