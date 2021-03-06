from Outputs.GetNaturalNumbersInList.GetNaturalNumbersInList import get_natural_numbers_in_list


def output_natural_number_count_statistics(input_list):
    natural_numbers = get_natural_numbers_in_list(input_list)
    natural_numbers_count = len(natural_numbers)
    other_strings_count = len(input_list) - natural_numbers_count

    print("Number of positive whole numbers entered:", natural_numbers_count)
    print("Number of other strings entered:", other_strings_count)