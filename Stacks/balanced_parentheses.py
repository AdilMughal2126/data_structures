def is_left_bracket(bracket):
    return bracket == "(" or bracket == "[" or bracket == "{" or bracket == "<"


def is_right_bracket(bracket):
    return bracket == ")" or bracket == "]" or bracket == "}" or bracket == ">"


def brackets_match(left, right):
    return (left == "(" and right != ")" or
            left == "{" and right != "}" or
            left == "[" and right != "]" or
            left == "<" and right != ">")


def validate_parentheses(input_str):
    stack = []

    for element in input_str:
        if is_left_bracket(element):
            stack.append(element)

        if is_right_bracket(element):
            if len(stack) == 0:
                return False

            popped_element = stack.pop()
            if brackets_match(element, popped_element):
                return False
    return len(stack) == 0


input_expression = "[(<a> + <b>)]"
print(validate_parentheses(input_expression))
