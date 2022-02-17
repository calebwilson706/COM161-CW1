from unittest import TestCase
from GenerateListWithWhileLoop import generate_list_with_while_loop
from unittest.mock import patch


class TestGenerateListWithWhileLoop(TestCase):
    @patch("builtins.input", return_value="")
    def test_should_return_empty_list(self, mocked_input):
        result = generate_list_with_while_loop()

        self.assertEqual(result, [])

    @patch("builtins.input", return_value="")
    def test_should_call_input_function(self, mocked_input):
        generate_list_with_while_loop()

        mocked_input.assert_called_once_with("Enter string (leave blank to terminate): ")

    @patch("builtins.input", side_effect=["1", ""])
    def test_should_terminate_after_empty_string(self, mocked_input):
        generate_list_with_while_loop()

        self.assertEqual(mocked_input.call_count, 2)

    @patch("builtins.input", side_effect=["1", "two", ""])
    def test_should_return_input_list(self, mocked_input):
        result = generate_list_with_while_loop()

        self.assertEqual(result, ["1", "two"])
