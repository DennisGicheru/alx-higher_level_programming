#!/usr/bin/python3

"""appends string at the end of a text file"""


def append_write(filename="", text=""):
    """open file, then append
    to file"""
    with open(filename, "a", encoding="UTF-8") as f:
        """write to file"""
        f.write(text)
        return (len(text))
