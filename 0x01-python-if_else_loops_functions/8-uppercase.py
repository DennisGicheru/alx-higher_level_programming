#!/usr/bin/python3
def uppercase(str):
    new_char = ""

    for i in (str):
        n = ord(i)

        if (n >= 97) and (n < 123):
            n = n - 32
            new_char = chr(n)
        else:
            new_char = i

        print("{:s}".format(new_char), end="")
    print("")
