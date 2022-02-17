from unittest import TestCase
from unittest.mock import patch
from GenerateListWithForLoop import generate_list_with_for_loop


class TestGenerateListWithForLoop(TestCase):
    @patch("builtins.input", return_value="0")
    def test_should_request_amount_of_inputs(self, mock_input):
        generate_list_with_for_loop()

        mock_input.assert_called_once_with("How many strings do you want to enter? ")

    @patch("builtins.input", return_value="0")
    def test_should_return_the_empty_list(self, mock_input):
        result = generate_list_with_for_loop()

        self.assertEqual(result, [])

    @patch("builtins.input", return_value="5")
    def test_should_call_mock_input_requested_times_plus_one(self, mock_input):
        # plus one comes from requesting the amount of inputs
        generate_list_with_for_loop()

        self.assertEqual(mock_input.call_count, 6)

    @patch("builtins.input", return_value="2")
    def test_should_call_input_requesting_correctly_indexed_string(self, mock_input):
        generate_list_with_for_loop()

        mock_input.assert_any_call("Enter string 1: ")
        mock_input.assert_any_call("Enter string 2: ")

    @patch("builtins.input", side_effect=["2", "one", "two"])
    def test_should_return_the_input_list(self, mock_input):
        result = generate_list_with_for_loop()

        self.assertEqual(result, ["one", "two"])