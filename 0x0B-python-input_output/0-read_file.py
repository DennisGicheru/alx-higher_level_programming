#!/usr/bin/python3
import os

"""simple function that reads a text file \
    and prints to stdout"""


def read_file(filename=""):
    """Open file, use read command to read files"""
    with open(filename, encoding="utf-8") as File1:
        """write output to stdout"""
        print(File1.read())
