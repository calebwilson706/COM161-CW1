from unittest import TestCase
from unittest.mock import patch
from OutputNaturalNumberCountStatistics import output_natural_number_count_statistics


class TestOutputNaturalNumberCountStatistics(TestCase):
    @patch("OutputNaturalNumberCountStatistics.get_natural_numbers_in_list", return_value=[])
    def test_should_call_get_natural_numbers_function(self, mock):
        output_natural_number_count_statistics([])

        mock.assert_called_once_with([])

    @patch("builtins.print")
    def test_should_output_two_items(self, mock_print):
        output_natural_number_count_statistics([])

        self.assertEqual(mock_print.call_count, 2)

    @patch("builtins.print")
    def test_should_output_amount_of_natural_numbers(self, mock_print):
        output_natural_number_count_statistics(["1", "2", "3"])

        mock_print.assert_any_call("Number of positive whole numbers entered:", 3)

    @patch("builtins.print")
    def test_should_output_amount_of_other_strings(self, mock_print):
        output_natural_number_count_statistics(["1", "2.5", "a"])

        mock_print.assert_any_call("Number of other strings entered:", 2)