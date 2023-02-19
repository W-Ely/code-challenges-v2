import unittest

from src.edabit.minesweeper_i_grid import num_grid


class TestNextBiggerNumber(unittest.TestCase):
    def test_num_grid_1(self):

        self.assertEqual(
            num_grid(
                [
                    ["-", "-", "-", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                    ["-", "-", "#", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                ]
            ),
            [
                ["0", "0", "0", "0", "0"],
                ["0", "1", "1", "1", "0"],
                ["0", "1", "#", "1", "0"],
                ["0", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        )

    def test_num_grid_2(self):
        self.assertEqual(
            num_grid(
                [
                    ["-", "-", "-", "-", "#"],
                    ["-", "-", "-", "-", "-"],
                    ["-", "-", "#", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                    ["#", "-", "-", "-", "-"],
                ]
            ),
            [
                ["0", "0", "0", "1", "#"],
                ["0", "1", "1", "2", "1"],
                ["0", "1", "#", "1", "0"],
                ["1", "2", "1", "1", "0"],
                ["#", "1", "0", "0", "0"],
            ],
        )

    def test_num_grid_3(self):
        self.assertEqual(
            num_grid(
                [
                    ["-", "-", "-", "#", "#"],
                    ["-", "#", "-", "-", "-"],
                    ["-", "-", "#", "-", "-"],
                    ["-", "#", "#", "-", "-"],
                    ["-", "-", "-", "-", "-"],
                ]
            ),
            [
                ["1", "1", "2", "#", "#"],
                ["1", "#", "3", "3", "2"],
                ["2", "4", "#", "2", "0"],
                ["1", "#", "#", "2", "0"],
                ["1", "2", "2", "1", "0"],
            ],
        )


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
