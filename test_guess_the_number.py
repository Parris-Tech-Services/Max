import contextlib
import io
import unittest
from unittest.mock import patch

from guess_the_number import guess_the_number


class GuessTheNumberTests(unittest.TestCase):
    def play(self, inputs, target=42):
        output = io.StringIO()
        with patch('random.randint', return_value=target), patch('builtins.input', side_effect=inputs), contextlib.redirect_stdout(output):
            guess_the_number()
        return output.getvalue()

    def test_win_first_guess(self):
        self.assertIn('in 1 guesses!', self.play(['42']))

    def test_low_high_win(self):
        result = self.play(['10', '90', '42'])
        self.assertIn('Too low!', result)
        self.assertIn('Too high!', result)
        self.assertIn('in 3 guesses!', result)

    def test_invalid_and_out_of_range_do_not_count(self):
        result = self.play(['abc', '3.14', '', '0', '101', '42'])
        self.assertIn('Please enter a whole number', result)
        self.assertIn('Please enter a number', result)
        self.assertIn('in 1 guesses!', result)

    def test_eof_gracefully_ends(self):
        self.assertIn('Game ended.', self.play([EOFError()]))

    def test_keyboard_interrupt_gracefully_ends(self):
        self.assertIn('Game ended.', self.play([KeyboardInterrupt()]))


if __name__ == '__main__':
    unittest.main()
