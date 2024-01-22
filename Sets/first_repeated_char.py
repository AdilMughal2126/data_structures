def get_first_repeated_char(input_string):
    char_set = set()

    for char in input_string:
        if char in char_set:
            return char
        char_set.add(char)
    return None


input_str = "green apple"
print(get_first_repeated_char(input_str))
