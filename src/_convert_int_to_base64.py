"""
Function taking a list of int
And return a list of base64 code
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


def convert_int_to_base64(int_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of int to base64 value
    # Then returns the new list
    int_converted_to_base64 = []
    for integer in int_list:
        int_converted_to_base64.append(list(ch2n.keys())[list(ch2n.values()).index(integer)])
    return int_converted_to_base64
