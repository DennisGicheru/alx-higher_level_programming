#!/usr/bin/python3

"""functio writes a string to a text file"""


def write_file(filename="", text=""):
    """open file, then write
    to file"""
    with open(filename, "w", encoding="UTF-8") as f:
        """write to file"""
        f.write(text)
        return (len(text))
