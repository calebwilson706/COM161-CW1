from LoopSelector.LoopSelector import select_loop_type, select_loop_type_or_end_game


def main():
    loop_type = select_loop_type()

    while loop_type is not None:
        print(loop_type.generate_list())

        loop_type = select_loop_type_or_end_game()


main()
