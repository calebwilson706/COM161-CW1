from unittest import TestCase
from unittest.mock import patch
from OutputTotalOfNaturalNumbersInList import output_total_of_natural_numbers_in_list


class TestOutputNaturalNumberCountStatistics(TestCase):
    @patch("OutputTotalOfNaturalNumbersInList.get_total_of_natural_numbers_in_list")
    def test_should_call_get_natural_numbers_total_function(self, mock):
        output_total_of_natural_numbers_in_list([])

        mock.assert_called_once_with([])

    @patch("builtins.print")
    def test_should_output_one_item(self, mock_print):
        output_total_of_natural_numbers_in_list([])

        self.assertEqual(mock_print.call_count, 1)

    @patch("builtins.print")
    @patch("OutputTotalOfNaturalNumbersInList.get_total_of_natural_numbers_in_list", return_value=1)
    def test_should_output_correct_text_with_total(self, _, mock_print):
        output_total_of_natural_numbers_in_list(["1"])

        mock_print.assert_called_once_with("Total of the positive numbers entered:", 1)
