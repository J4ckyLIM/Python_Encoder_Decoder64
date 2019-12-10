"""
Function taking a list of base64 code
And returns the same list if the list's length is a multiple of 4
Or add "=" until the list's length is a multiple of 4
"""


def add_equals_to_get4(base64_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then add "=" to the list if the length of the list isn't a multiple of 4
    # Then returns the new list
    equals_added_to_get4 = base64_list
    while len(equals_added_to_get4) % 4 != 0:
        equals_added_to_get4.append("=")
    return equals_added_to_get4
