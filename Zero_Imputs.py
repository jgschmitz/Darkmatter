# zero imputs
def create_2d_list():
    my_list = []
    user_input = input("Enter rows of elements separated by commas (use semicolons to separate rows): ")
    rows = user_input.split(";")

    for row in rows:
        elements = row.split(",")
        int_row = []
        for element in elements:
            stripped_element = element.strip()
            if stripped_element:  # Only process non-empty elements
                try:
                    int_row.append(int(stripped_element))
                except ValueError:
                    print(f"Invalid input: '{stripped_element}' is not an integer.")
                    return None  # Return None to indicate invalid input
        my_list.append(int_row)

    return my_list


result = create_2d_list()
if result is not None:
    print(result)
