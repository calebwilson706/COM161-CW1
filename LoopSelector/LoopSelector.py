from Shared.Loop import Loop


def get_input_prompt():
    return "Enter " + Loop.FOR.get_input_prompt() + ", " + Loop.WHILE.get_input_prompt() + ": "


def select_loop_type():
    index = int(input(get_input_prompt()))

    return Loop(index)


def select_loop_type_or_end_game():
    users_input = input("Enter 'stop' to end the program or " + get_input_prompt())

    if users_input == "stop":
        return None

    return Loop(int(users_input))
