from unittest import TestCase
from unittest.mock import patch
from LoopSelector import get_input_prompt, select_loop_type, select_loop_type_or_end_game
from Shared.LoopType import LoopType


class TestLoopSelector(TestCase):
    def test_get_input_prompt(self):
        result = get_input_prompt()

        self.assertEqual(result, "Enter 1 for a 'for' loop, 2 for a 'while' loop: ")

    @patch('builtins.input', return_value="1")
    def test_selector_calls_input(self, mock):
        select_loop_type()

        self.assertTrue(mock.called)

    @patch('builtins.input', return_value="1")
    def test_selector_selects_for_loop(self, mock):
        result = select_loop_type()

        self.assertEqual(result, LoopType.FOR)

    @patch('builtins.input', return_value="2")
    def test_selector_selects_while_loop(self, mock):
        result = select_loop_type()

        self.assertEqual(result, LoopType.WHILE)

    @patch('builtins.input', return_value="1")
    def test_selector_selects_for_loop_at_end_of_game(self, mock):
        result = select_loop_type_or_end_game()

        self.assertEqual(result, LoopType.FOR)

    @patch('builtins.input', return_value="2")
    def test_selector_selects_while_loop_at_end_of_game(self, mock):
        result = select_loop_type_or_end_game()

        self.assertEqual(result, LoopType.WHILE)

    @patch('builtins.input', return_value="stop")
    def test_selector_selects_None_at_end_of_game(self, mock):
        result = select_loop_type_or_end_game()

        self.assertEqual(result, None)
