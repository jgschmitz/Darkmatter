#This code will create a 2D list based on the user's input, where each row is separated by commas. 
#The elements will be stripped of any leading or trailing whitespace and converted to integers (assuming they can be parsed as integers).
print 1,2,3,4,5,6,7,
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
