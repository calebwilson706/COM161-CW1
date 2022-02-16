from unittest import TestCase
from unittest.mock import patch
from GetTotalOfNaturalNumbersInList import get_total_of_natural_numbers_in_list


class TestGetTotalOfNaturalNumbersInList(TestCase):
    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def testShouldReturnAnInteger(self, mock):
        result = get_total_of_natural_numbers_in_list([])

        self.assertTrue(isinstance(result, int))

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def testShouldGetNaturalNumbersFromListInput(self, mock):
        get_total_of_natural_numbers_in_list(["a"])

        mock.assert_called_once_with(["a"])

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def testShouldReturnZeroIfThereAreNoNaturalNumbers(self, mock):
        result = get_total_of_natural_numbers_in_list([])

        self.assertEqual(result, 0)

    @patch("GetTotalOfNaturalNumbersInList.get_natural_numbers_in_list", return_value=[1,2,3])
    def testShouldReturnSumOfNaturalNumbersInList(self, mock):
        result = get_total_of_natural_numbers_in_list(["1", "2", "3"])

        self.assertEqual(result, 6)
