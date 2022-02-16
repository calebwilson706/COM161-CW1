from unittest import TestCase
from unittest.mock import patch
from LoopType import LoopType


class TestLoopType(TestCase):
    def test_get_display_name(self):
        result = LoopType.FOR.get_display_name()

        assert result == "for"

    def test_should_get_correct_input_prompt(self):
        result = LoopType.FOR.get_input_prompt()

        assert result == "1 for a 'for' loop"


class TestListGenerator(TestCase):
    @patch("builtins.input", return_value="")
    @patch("LoopType.generate_list_with_while_loop")
    def testShouldUseWhileLoop(self, mock_while_loop_generator, _):
        LoopType.WHILE.generate_list()

        mock_while_loop_generator.assert_called_once()

    @patch("builtins.input", return_value="0")
    @patch("LoopType.generate_list_with_for_loop")
    def testShouldUseForLoop(self, mock_for_loop_generator, _):
        LoopType.FOR.generate_list()

        mock_for_loop_generator.assert_called_once()


class TestStatisticsOutput(TestCase):
    @patch("builtins.input", return_value="0")
    @patch("LoopType.output_natural_number_count_statistics")
    def testShouldOutputSharedStatisticsWhenForIsSelected(self, mock, _):
        loop_type = LoopType.FOR
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="")
    @patch("LoopType.output_natural_number_count_statistics")
    def testShouldOutputSharedStatisticsWhenWhileIsSelected(self, mock, _):
        loop_type = LoopType.WHILE
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="0")
    @patch("LoopType.output_total_of_natural_numbers_in_list")
    def testShouldOutputTotalOfNaturalNumbersWhenForIsSelected(self, mock, _):
        loop_type = LoopType.FOR
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="")
    @patch("LoopType.output_total_of_natural_numbers_in_list")
    def testShouldNotOutputTotalOfNaturalNumbersWhenWhileIsSelected(self, mock, _):
        loop_type = LoopType.WHILE
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_not_called()
