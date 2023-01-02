import unittest

from src.leet_code.zigzag_conversion import Solution


class TestRangeExtraction(unittest.TestCase):
    def test_solution(self):
        solution = Solution()                
        cases = [
            (("PAYPALISHIRING", 1), "PAYPALISHIRING"),
            (("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG"),
            (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
            (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        ]
        for (chracters, rows), expected in cases:
            with self.subTest(f"{(chracters, rows)} --> {expected}"):
                self.assertEqual(solution.convert(chracters, rows), expected)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
