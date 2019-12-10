"""
Function taking a list of string as parameter
And return a list of ascii code
"""


def convert_char_to_ascii(converted_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of character to ascii
    # Then returns the new list
    char_converted_to_ascii = []
    for letter in converted_list:
        char_converted_to_ascii.append(ord(letter))
    print(char_converted_to_ascii)
    return char_converted_to_ascii


convert_char_to_ascii(["A", "B"])
