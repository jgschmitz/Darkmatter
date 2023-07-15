my_list = []

user_input = input("Enter elements separated by commas: ")
elements = user_input.split(",")

row = []
for element in elements:
    stripped_element = element.strip()
    if stripped_element:  # Check if element is not empty after stripping whitespace
        row.append(int(stripped_element))
my_list.append(row)

print(my_list)
