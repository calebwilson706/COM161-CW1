from unittest import TestCase
from GenerateListWithWhileLoop import generate_list_with_while_loop
from unittest.mock import patch


class TestGenerateWithWhileLoop(TestCase):

    @patch("builtins.input", return_value="")
    def testShouldReturnEmptyList(self, mocked_input):
        result = generate_list_with_while_loop()

        self.assertEqual(result, [])

    @patch("builtins.input", return_value="")
    def testShouldCallInputFunction(self, mocked_input):
        generate_list_with_while_loop()

        self.assertTrue(mocked_input.called)

    @patch("builtins.input", side_effect=["1", ""])
    def testShouldTerminateAfterEmptyString(self, mocked_input):
        generate_list_with_while_loop()

        self.assertEqual(mocked_input.call_count, 2)

    @patch("builtins.input", side_effect=["1", "two", ""])
    def testShouldReturnInputList(self, mocked_input):
        result = generate_list_with_while_loop()

        self.assertEqual(result, ["1", "two"])
