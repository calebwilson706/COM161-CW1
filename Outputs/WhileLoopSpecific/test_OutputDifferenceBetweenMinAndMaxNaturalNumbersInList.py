from unittest import TestCase
from unittest.mock import patch
from OutputDifferenceBetweenMinAndMaxNaturalNumbersInList \
    import output_difference_between_min_and_max_natural_numbers_in_list


class TestOutputDifferenceBetweenMinAndMaxNaturalNumbersInList(TestCase):
    @patch(
        "OutputDifferenceBetweenMinAndMaxNaturalNumbersInList"
        ".get_min_and_max_natural_numbers_in_list",
        return_value=None
    )
    def test_should_call_get_difference_between_min_and_max_function(self, mock):
        output_difference_between_min_and_max_natural_numbers_in_list([])

        mock.assert_called_once_with([])

    @patch("builtins.print")
    def test_should_not_output_when_list_is_empty(self, mock):
        output_difference_between_min_and_max_natural_numbers_in_list([])

        self.assertEqual(mock.call_count, 0)

    @patch("builtins.print")
    def test_should_output_one_item(self, mock):
        output_difference_between_min_and_max_natural_numbers_in_list(["1"])

        mock.assert_called_once()

    @patch("builtins.print")
    def test_should_output_correct_text(self, mock):
        output_difference_between_min_and_max_natural_numbers_in_list(["1", "2"])

        mock.assert_called_once_with(
            "The difference between the smallest number",
            1,
            "and the largest number",
            2,
            "is",
            1
        )
