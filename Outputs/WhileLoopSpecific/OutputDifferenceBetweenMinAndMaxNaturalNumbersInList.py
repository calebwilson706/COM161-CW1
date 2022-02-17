from Outputs.WhileLoopSpecific.GetMinAndMaxNaturalNumbersInList import get_min_and_max_natural_numbers_in_list


def output_difference_between_min_and_max_natural_numbers_in_list(input_list):
    result = get_min_and_max_natural_numbers_in_list(input_list)

    if result is None:
        return

    smallest, largest = result

    print(
        "The difference between the smallest number",
        smallest,
        "and the largest number",
        largest,
        "is",
        largest - smallest
    )
