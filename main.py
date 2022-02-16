from LoopSelector.LoopSelector import select_loop_type, select_loop_type_or_end_game
from Outputs.Shared.OutputNaturalNumberCountStatistics import output_natural_number_count_statistics


def main():
    loop_type = select_loop_type()

    while loop_type is not None:
        generated_list = loop_type.generate_list()

        output_natural_number_count_statistics(generated_list)

        loop_type = select_loop_type_or_end_game()


main()
