def get_next_value():
    return input("Enter string (leave blank to terminate): ")


def generate_list_with_while_loop():
    result = []

    while True:
        new_input = get_next_value()

        if new_input == "":
            return result

        result.append(new_input)
