from unittest import TestCase
from unittest.mock import patch
from LoopType import LoopType


class TestLoopType(TestCase):
    def test_get_display_name(self):
        result = LoopType.FOR.get_display_name()

        assert result == "for"

    def test_should_get_correct_input_prompt(self):
        result = LoopType.FOR.get_input_prompt()

        assert result == "1 for a 'for' loop"


class TestListGenerator(TestCase):
    @patch("builtins.input", return_value="")
    @patch("ListGenerators.WhileLoop.GenerateListWithWhileLoop.generate_list_with_while_loop")
    def testShouldUseWhileLoop(self, mock_input, mock_while_loop_generator):
        LoopType.WHILE.generate_list()

        mock_while_loop_generator.assert_called_once()

    @patch("builtins.input", return_value="0")
    @patch("ListGenerators.ForLoop.GenerateListWithForLoop.generate_list_with_for_loop")
    def testShouldUseForLoop(self, mock_input, mock_for_loop_generator):
        LoopType.FOR.generate_list()

        mock_for_loop_generator.assert_called_once()