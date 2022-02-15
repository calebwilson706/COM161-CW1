

def generate_list_with_while_loop():
    result = []

    while True:
        new_input = input("Enter string (leave blank to terminate): ")

        if new_input == "":
            return result
        else:
            result.append(new_input)
