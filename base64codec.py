import argparse
import string
import sys

from src._add_equals_to_get4 import add_equals_to_get4
from src._convert_6bits_to_int import convert_6bits_to_int
from src._convert_ascii_to_8bits import convert_ascii_to_8bits
from src._convert_char_to_ascii import convert_char_to_ascii
from src._convert_int_to_base64 import convert_int_to_base64
from src._converts_list_to_string import convert_string_to_list
from src._eight_bit_list_to_string import eight_bit_list_to_string
from src._final_conversion import converts_list_to_string
from src.string_to_6_bit_list import string_to_six_bit_list

"""Python decoder/encoder 64

"""

x = input("Type what you want to encode ")


def encode_to_base64(x) -> string:
    encode = convert_string_to_list(x)
    encode2 = convert_char_to_ascii(encode)
    encode3 = convert_ascii_to_8bits(encode2)
    encode4 = eight_bit_list_to_string(encode3)
    encode5 = string_to_six_bit_list(encode4)
    encode6 = convert_6bits_to_int(encode5)
    encode7 = convert_int_to_base64(encode6)
    encode8 = add_equals_to_get4(encode7)
    encode9 = converts_list_to_string(encode8)

    print("The encoded result is: " + "'" + encode9 + "'")
    return encode9


encode_to_base64(x)


