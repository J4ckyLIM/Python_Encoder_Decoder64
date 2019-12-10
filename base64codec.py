import argparse
import string
import sys

"""Python decoder/encoder 64

"""

"""
Dictionary base64code
"""
n2ch = "".join([
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789-_",
])
ch2n = dict(zip(n2ch, range(len(n2ch))))
print(n2ch)



