"""
Nineth function
"""


def converts_list_to_string(string_list):
    # This function takes the list as parameter
    # Then creates a string concatenating the elements
    list_of_string = ""
    list_to_string = list_of_string.join(string_list)
    print(list_to_string)
    return list_to_string


converts_list_to_string(["Q", "U", "J", "D", "R", "A", "=", "="])
