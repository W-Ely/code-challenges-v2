import unittest

from src.code_wars.range_extraction import solution


class TestRangeExtraction(unittest.TestCase):
    def test_solution(self):
        cases = [
            ([-7, -5, -3, -1, 1, 3, 5, 7], "-7,-5,-3,-1,1,3,5,7"),
            ([-7, -5, -4, -3, -1, 1, 3, 4, 5, 7], "-7,-5--3,-1,1,3-5,7"),
            ([-9, -8, -7, -5, -4, -3, -1, 1, 3, 4, 5, 7], "-9--7,-5--3,-1,1,3-5,7"),
            ([-7, -5, -4, -3, -1, 1, 3, 4, 5, 7, 8, 9], "-7,-5--3,-1,1,3-5,7-9"),
            ([-8, -7, -5, -4, -3, -1, 1, 3, 4, 5, 7, 8], "-8,-7,-5--3,-1,1,3-5,7,8"),
            ([-7, -5, -4, -3, -1, 1, 3, 4, 5, 7, 8, 9], "-7,-5--3,-1,1,3-5,7-9"),
            ([-7, -5, -4, -3, -1, 1, 3, 4, 5, 7, 8], "-7,-5--3,-1,1,3-5,7,8"),
            (
                [
                    -6,
                    -3,
                    -2,
                    -1,
                    0,
                    1,
                    3,
                    4,
                    5,
                    7,
                    8,
                    9,
                    10,
                    11,
                    14,
                    15,
                    17,
                    18,
                    19,
                    20,
                ],
                "-6,-3-1,3-5,7-11,14,15,17-20",
            ),
        ]
        for numbers, expected in cases:
            with self.subTest(f"{numbers} --> {expected}"):
                self.assertEqual(solution(numbers), expected)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
