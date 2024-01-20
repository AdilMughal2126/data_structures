stack = []
output = ""

input_str = "abcde"

for element in input_str:
    stack.append(element)

for element in input_str:
    popped_element = stack.pop()
    output += popped_element

print(output)


