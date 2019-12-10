"""
Eighth function
"""


def add_equals_to_get4(base64_list) -> list:
    # This function takes the list as parameter
    # Then create a list
    # Then add "=" to the list if the length of the list isn't a multiple of 4
    # Then returns the new list
    equals_added_to_get4 = base64_list
    while len(equals_added_to_get4) % 4 != 0:
        equals_added_to_get4.append("=")
    print(equals_added_to_get4)
    return equals_added_to_get4


add_equals_to_get4(["Q", "U", "J", "D", "R", "A"])
