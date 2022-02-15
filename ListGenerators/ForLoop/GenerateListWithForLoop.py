def get_amount_of_inputs():
    return int(input("How many strings do you want to enter?"))


def get_next_input(index):
    return input("Enter string " + str(index + 1) + ": ")


def generate_list_with_for_loop():
    amount_of_inputs = get_amount_of_inputs()
    result = []

    for i in range(amount_of_inputs):
        result.append(
            get_next_input(i)
        )

    return result
