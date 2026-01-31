import io
import unittest
from contextlib import redirect_stdout

import project1


class IndentationTestCase(unittest.TestCase):

    def test_function_with_indentation_prints_pass(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            project1.function_with_indentation()
        self.assertEqual(buf.getvalue().strip(), "pass")

    def test_if_two_is_greater_than_zero_prints_message(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            project1.function_if_two_is_greater_than_zero()
        self.assertEqual(buf.getvalue().strip(), "2 is greater than 0")

    def test_if_two_is_greater_than_zero_two_statements_prints_two_lines(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            project1.function_if_two_is_greater_two_statements()

        output_lines = [line.strip() for line in buf.getvalue().splitlines() if line.strip()]
        self.assertEqual(
            output_lines,
            ["2 is greater than 0", "This is another statement"],
        )


if __name__ == "__main__":
    unittest.main()
