import unittest

from src.edabit.longest_alternating_substring import longest_substring


class TestNextBiggerNumber(unittest.TestCase):
    def test_longest_substring_1(self):
        self.assertEqual(
            longest_substring("225424272163254474441338664823"), "272163254"
        )

    def test_longest_substring_2(self):
        self.assertEqual(
            longest_substring("594127169973391692147228678476"), "16921472"
        )

    def test_longest_substring_3(self):
        self.assertEqual(longest_substring("721449827599186159274227324466"), "7214")

    def test_longest_substring_4(self):
        self.assertEqual(longest_substring("22221"), "21")

    def test_longest_substring_5(self):
        self.assertEqual(longest_substring("12222"), "12")
