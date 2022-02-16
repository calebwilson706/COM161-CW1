from enum import Enum
from ListGenerators.WhileLoop.GenerateListWithWhileLoop import generate_list_with_while_loop
from ListGenerators.ForLoop.GenerateListWithForLoop import generate_list_with_for_loop
from Outputs.Shared.OutputNaturalNumberCountStatistics import output_natural_number_count_statistics
from Outputs.ForLoopSpecific.OutputTotalOfNaturalNumbersInList import output_total_of_natural_numbers_in_list


class LoopType(Enum):
    FOR = 1
    WHILE = 2

    def get_display_name(self):
        return self.name.lower()

    def get_input_prompt(self):
        return str(self.value) + " for a '" + self.get_display_name() + "' loop"

    def generate_list(self):
        if self == LoopType.WHILE:
            return generate_list_with_while_loop()
        else:
            return generate_list_with_for_loop()

    def output_statistics(self, generated_list):
        output_natural_number_count_statistics(generated_list)

        if self == LoopType.FOR:
            output_total_of_natural_numbers_in_list(generated_list)
