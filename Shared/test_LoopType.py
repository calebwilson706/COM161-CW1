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

    @patch("builtins.print")
    def test_should_display_correct_report_message(self, mock):
        LoopType.FOR.report_selection()

        mock.assert_called_once_with("\nYou choose a '", 'for', "' loop", sep='')


class TestListGenerator(TestCase):
    @patch("builtins.input", return_value="")
    @patch("LoopType.generate_list_with_while_loop")
    def test_should_use_while_loop(self, mock_while_loop_generator, _):
        LoopType.WHILE.generate_list()

        mock_while_loop_generator.assert_called_once()

    @patch("builtins.input", return_value="0")
    @patch("LoopType.generate_list_with_for_loop")
    def test_should_use_for_loop(self, mock_for_loop_generator, _):
        LoopType.FOR.generate_list()

        mock_for_loop_generator.assert_called_once()


class TestStatisticsOutput(TestCase):
    @patch("builtins.input", return_value="0")
    @patch("LoopType.output_natural_number_count_statistics")
    def test_should_output_shared_statistics_when_for_is_selected(self, mock, _):
        loop_type = LoopType.FOR
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="")
    @patch("LoopType.output_natural_number_count_statistics")
    def test_should_output_shared_statistics_when_while_Is_selected(self, mock, _):
        loop_type = LoopType.WHILE
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="0")
    @patch("LoopType.output_total_of_natural_numbers_in_list")
    def test_should_output_total_of_natural_numbers_when_for_is_selected(self, mock, _):
        loop_type = LoopType.FOR
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()

    @patch("builtins.input", return_value="")
    @patch("LoopType.output_total_of_natural_numbers_in_list")
    def test_should_not_output_total_of_natural_numbers_when_while_Is_selected(self, mock, _):
        loop_type = LoopType.WHILE
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_not_called()

    @patch("builtins.input", return_value="0")
    @patch("LoopType.output_difference_between_min_and_max_natural_numbers_in_list")
    def test_should_not_output_difference_between_min_and_max_natural_numbers_when_for_is_selected(self, mock, _):
        loop_type = LoopType.FOR
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_not_called()

    @patch("builtins.input", return_value="")
    @patch("LoopType.output_difference_between_min_and_max_natural_numbers_in_list")
    def test_should_output_difference_between_min_and_max_natural_numbers_when_while_Is_selected(self, mock, _):
        loop_type = LoopType.WHILE
        generated_list = loop_type.generate_list()

        loop_type.output_statistics(generated_list)

        mock.assert_called_once()
        