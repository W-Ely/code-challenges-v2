import unittest

from src.code_wars.next_bigger_number import (
    find_i_of_n_with_larger_m_to_right,
    find_j_of_smallest_m_to_right_of_n,
    next_bigger,
)


class TestNextBiggerNumber(unittest.TestCase):
    def test_find_i_of_n_with_larger_m_to_right(self):
        cases = (
            (1000, None),
            (1001, 2),
            (1430, 0),
            (1340, 1),
            (1010, 1),
        )
        for number, expected in cases:
            numbers = [int(n) for n in str(number)]
            with self.subTest(f"{number} --> {expected}"):
                actual = find_i_of_n_with_larger_m_to_right(numbers)
                self.assertEqual(actual, expected)

    def test_find_j_of_smallest_m_to_right_of_n(self):
        cases = (
            (1001, 2, 3),
            (1430, 0, 2),
            (1340, 1, 2),
            (1010, 1, 2),
        )
        for number, i, expected in cases:
            numbers = [int(n) for n in str(number)]
            with self.subTest(f"{number} --> {expected}"):
                actual = find_j_of_smallest_m_to_right_of_n(numbers, i)
                self.assertEqual(actual, expected)

    def test_next_bigger(self):
        cases = [
            (1000, -1),
            (1001, (1010)),
            (1430, (3014)),
            (1340, (1403)),
            (1010, 1100),
        ]
        for number, expected in cases:
            with self.subTest(f"{number} --> {expected}"):
                actual = next_bigger(number)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
