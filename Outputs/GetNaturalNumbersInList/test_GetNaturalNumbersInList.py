from unittest import TestCase
from GetNaturalNumbersInList import get_natural_numbers_in_list


class GetNaturalNumbersFromList(TestCase):
    def test_should_return_an_empty_list(self):
        result = get_natural_numbers_in_list([])

        self.assertEqual(result, [])

    def test_should_remove_non_integers(self):
        result = get_natural_numbers_in_list(["1", "2", "c", "4.0"])

        self.assertEqual(len(result), 2)

    def test_should_return_a_list_of_integers(self):
        result = get_natural_numbers_in_list(["1", "2", "a"])

        self.assertTrue(
            all(isinstance(value, int) for value in result)
        )

    def test_should_not_contain_any_negative_numbers(self):
        result = get_natural_numbers_in_list(["-1", "2", "a"])

        self.assertFalse(
            any(value < 0 for value in result)
        )

    def test_should_return_correct_list(self):
        result = get_natural_numbers_in_list(["-1", "0", "1", "2", "a", "1.5"])

        self.assertEqual(result, [1, 2])
