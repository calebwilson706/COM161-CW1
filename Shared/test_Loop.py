from unittest import TestCase
from Loop import Loop


class TestLoop(TestCase):
    def test_get_display_name(self):
        result = Loop.FOR.get_display_name()

        assert result == "for"

    def test_should_get_correct_input_prompt(self):
        result = Loop.FOR.get_input_prompt()

        assert result == "1 for a 'for' loop"
