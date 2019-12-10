"""
Function taking a list of binaries
And return a list of int
"""


def convert_6bits_to_int(bits_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of bits to integer
    # Then returns the new list
    bits_converted_to_int = []
    for bits in bits_list:
        bits_converted_to_int.append(int(bits, 2))
    return bits_converted_to_int
