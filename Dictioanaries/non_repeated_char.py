def get_first_non_repeated_char(input_string):
    char_dict = {}

    for char in input_string:
        char_dict[char] = char_dict.get(char, 0) + 1

    for key, value in char_dict.items():
        if value == 1:
            return key


input_str = "a green apple"
print(get_first_non_repeated_char(input_str))
