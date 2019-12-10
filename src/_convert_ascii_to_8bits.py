"""
Function taking a list of ascii code
And returns a list of 8bits
"""


def convert_ascii_to_8bits(ascii_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of character to ascii
    # Then returns the new list
    ascii_converted_to_8bits = []
    for ascii in ascii_list:
        ascii_converted_to_8bits.append(format(ascii, '08b'))
    return ascii_converted_to_8bits

