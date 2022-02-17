from LoopSelector.LoopSelector import select_loop_type, select_loop_type_or_end_game


def main():
    loop_type = select_loop_type()

    while loop_type is not None:
        loop_type.report_selection()

        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        loop_type = select_loop_type_or_end_game()


main()
