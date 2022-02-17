from unittest import TestCase
from unittest.mock import patch
from GetMinAndMaxNaturalNumbersInList import get_min_and_max_natural_numbers_in_list


class TestGetMinAndMaxNaturalNumbersInList(TestCase):
    def test_should_return_two_integers(self):
        a, b = get_min_and_max_natural_numbers_in_list(["1"])

        self.assertTrue(isinstance(a, int))
        self.assertTrue(isinstance(b, int))

    @patch("GetMinAndMaxNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def test_should_return_none_when_no_natural_numbers(self, mock):
        result = get_min_and_max_natural_numbers_in_list([])

        self.assertEqual(result, None)

    @patch("builtins.max", return_value=10)
    def test_should_not_get_largest_number_when_list_is_empty(self, mock_max):
        get_min_and_max_natural_numbers_in_list([])

        self.assertEqual(mock_max.call_count, 0)

    @patch("builtins.min", return_value=0)
    def test_should_not_get_smallest_number_when_list_is_empty(self, mock_min):
        get_min_and_max_natural_numbers_in_list([])

        self.assertEqual(mock_min.call_count, 0)

    @patch("GetMinAndMaxNaturalNumbersInList.get_natural_numbers_in_list", return_value=[])
    def test_should_get_natural_numbers_from_list(self, mock):
        get_min_and_max_natural_numbers_in_list([])

        mock.assert_called_once_with([])

    @patch("builtins.max", return_value=10)
    def test_should_get_largest_natural_number(self, mock_max):
        get_min_and_max_natural_numbers_in_list(["1"])

        mock_max.assert_called_once_with([1])

    @patch("builtins.min", return_value=10)
    def test_should_get_smallest_natural_number(self, mock_min):
        get_min_and_max_natural_numbers_in_list(["1"])

        mock_min.assert_called_once_with([1])

    def test_should_return_correct_min_and_max(self):
        result = get_min_and_max_natural_numbers_in_list(["1", "2", "3"])

        self.assertEqual(result, (1, 3))
