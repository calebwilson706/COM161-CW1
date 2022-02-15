from Shared.LoopType import LoopType


def get_input_prompt():
    return "Enter " + LoopType.FOR.get_input_prompt() + ", " + LoopType.WHILE.get_input_prompt() + ": "


def select_loop_type():
    index = int(input(get_input_prompt()))

    return LoopType(index)


def select_loop_type_or_end_game():
    users_input = input("Enter 'stop' to end the program or " + get_input_prompt())

    if users_input == "stop":
        return None

    return LoopType(int(users_input))
