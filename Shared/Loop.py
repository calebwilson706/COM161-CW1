from enum import Enum


class Loop(Enum):
    FOR = 1
    WHILE = 2

    def get_display_name(self):
        return self.name.lower()

    def get_input_prompt(self):
        return str(self.value) + " for a '" + self.get_display_name() + "' loop"
