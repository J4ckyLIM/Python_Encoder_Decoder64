"""
Fifth function
"""


def string_to_six_bit_list(string):
    # This function takes the string as parameter
    # Then creates a list of 6 characters for each index
    six_bit_list = []
    # You convert the string into items of 6 characters long into a list
    for i in range(0, len(string), 6):
        six_bit_list.append(string[i: i + 6])
    if len(string) % 6 != 0:
        # You extract the last item of the list which is not 6 character long
        str_pop = six_bit_list.pop()
        # Calculate how many 0 you need to add
        dif = 6 - (len(string) % 6)
        # Concat the pop and the number of "0" required
        str_app = str_pop + ("0" * dif)
        # And append the result into the list to have all entries 6 long
        six_bit_list.append(str_app)
    return six_bit_list
