from unittest import TestCase
from unittest.mock import patch
from GetTotalOfNaturalNumbersInList import get_total_of_natural_numbers_in_list


class TestGetTotalOfNaturalNumbersInList(TestCase):
    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def test_should_return_an_integer(self, mock):
        result = get_total_of_natural_numbers_in_list([])

        self.assertTrue(isinstance(result, int))

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def test_should_get_natural_numbers_from_list_input(self, mock):
        get_total_of_natural_numbers_in_list(["a"])

        mock.assert_called_once_with(["a"])

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def test_should_return_zero_if_there_are_no_natural_numbers(self, mock):
        result = get_total_of_natural_numbers_in_list([])

        self.assertEqual(result, 0)

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[1,2,3])
    def test_should_return_sum_of_natural_numbers_in_list(self, mock):
        result = get_total_of_natural_numbers_in_list(["1", "2", "3"])

        self.assertEqual(result, 6)
