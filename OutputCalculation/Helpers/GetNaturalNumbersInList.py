def get_maybe_int_from_string(string):
    try:
        return int(string)
    except ValueError:
        return None


def remove_null_items_from(input_list):
    return [element for element in input_list if element is not None]


def get_integers_in_list(input_list):
    return remove_null_items_from(
        [get_maybe_int_from_string(element) for element in input_list]
    )


def get_natural_numbers_in_list(input_list):
    return [integer for integer in get_integers_in_list(input_list) if integer > 0]

