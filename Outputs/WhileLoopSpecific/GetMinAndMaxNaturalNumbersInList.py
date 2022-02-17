from Outputs.GetNaturalNumbersInList.GetNaturalNumbersInList import get_natural_numbers_in_list


def get_min_and_max_natural_numbers_in_list(input_list):
    natural_numbers = get_natural_numbers_in_list(input_list)

    if len(natural_numbers) == 0:
        return None

    return min(natural_numbers),  max(natural_numbers)
