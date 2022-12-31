import unittest

from src.code_wars.switch_the_bulbs import Board, switch_bulbs

GAME_MAPS = [
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|........|\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|........|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|.....B..|\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|........|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|........|\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|.....B..|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|.B......|\n"
    + "|........|\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|.B...B..|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|.B......|\n"
    + "|........|\n"
    + "|........|\n"
    + "|...BB...|\n"
    + "|........|\n"
    + "|.B...B..|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|.B......|\n"
    + "|.B..B...|\n"
    + "|........|\n"
    + "|........|\n"
    + "|.B..B...|\n"
    + "|.B......|\n"
    + "|........|\n"
    + "+--------+",
]
GAME_SOLUTIONS = [
    ([(1, 3), (5, 3)],),
    ([(1, 3), (3, 5), (5, 3)], [(5, 3), (1, 3), (3, 5)]),
    ([(1, 3), (5, 3), (7, 5)],),
    ([(1, 3), (5, 3), (7, 5), (7, 1), (2, 1)],),
    (
        [(1, 3), (5, 3), (7, 5), (7, 1), (2, 1), (5, 4)],
        [(1, 3), (5, 3), (5, 4), (2, 1), (7, 1), (7, 5)],
    ),
    ([(1, 1), (2, 1), (2, 4), (5, 4), (5, 1), (6, 1)],),
]

GAME_MAPS_2 = [
    "+--------+\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|.B......|\n"
    + "|......B.|\n"
    + "|......B.|\n"
    + "|.B......|\n"
    + "|......BB|\n"
    + "|BB......|\n"
    + "+--------+",
    "+--------+\n"
    + "|...BB...|\n"
    + "|........|\n"
    + "|..B..B..|\n"
    + "|....B...|\n"
    + "|....B...|\n"
    + "|..B.....|\n"
    + "|.B....B.|\n"
    + "|........|\n"
    + "+--------+",
    "+--------+\n"
    + "|........|\n"
    + "|.B.B..B.|\n"
    + "|........|\n"
    + "|.B..B.B.|\n"
    + "|........|\n"
    + "|.B.B..B.|\n"
    + "|........|\n"
    + "+--------+",
    "+----------+\n"
    + "|..........|\n"
    + "|..........|\n"
    + "|..........|\n"
    + "|..B.B....B|\n"
    + "|.B...B...B|\n"
    + "|.....B....|\n"
    + "|..........|\n"
    + "|.B......B.|\n"
    + "|....B.....|\n"
    + "|.B..BB..B.|\n"
    + "+----------+",
    "+--------+\n"
    + "|........|\n"
    + "|.BBBBBB.|\n"
    + "|.BBBBBB.|\n"
    + "|.BBBBBB.|\n"
    + "|.BBBBBB.|\n"
    + "|.BBBBBB.|\n"
    + "|.BBBBBB.|\n"
    + "|........|\n"
    + "+--------+",
    "+---------+\n"
    + "|.........|\n"
    + "|.B.B.B.B.|\n"
    + "|..B.B.B..|\n"
    + "|.B.B.B.B.|\n"
    + "|..B.B.B..|\n"
    + "|.B.B.B.B.|\n"
    + "|..B.B.B..|\n"
    + "|.B.B.B.B.|\n"
    + "|.........|\n"
    + "+---------+",
    "+---------+\n"
    + "|.B......B|\n"
    + "|.B.......|\n"
    + "|......B..|\n"
    + "|.........|\n"
    + "|....B....|\n"
    + "|.....B...|\n"
    + "|.........|\n"
    + "|.......B.|\n"
    + "|.........|\n"
    + "+---------+",
    "+---------+\n"
    + "|.........|\n"
    + "|...BBB...|\n"
    + "|..B...B..|\n"
    + "|......B..|\n"
    + "|.....B...|\n"
    + "|....B....|\n"
    + "|....B....|\n"
    + "|.........|\n"
    + "|....B....|\n"
    + "|.........|\n"
    + "+---------+",
    "+----------------+\n"
    + "|B.............B.|\n"
    + "|.B..........B...|\n"
    + "|................|\n"
    + "|..B........B....|\n"
    + "|....B.....B.....|\n"
    + "|.....B..B.......|\n"
    + "|.......B........|\n"
    + "|......B.........|\n"
    + "|......B.B.......|\n"
    + "|.....B....B.....|\n"
    + "|................|\n"
    + "|....B......B....|\n"
    + "|..B.........B...|\n"
    + "|.B............B.|\n"
    + "|................|\n"
    + "|B..............B|\n"
    + "+----------------+",
    "+------------------+\n"
    + "|.B...B...B........|\n"
    + "|B.................|\n"
    + "|.....B.B.....B....|\n"
    + "|..............B...|\n"
    + "|..................|\n"
    + "|..............B...|\n"
    + "|.B.......B........|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|.......B.B........|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|..B........B......|\n"
    + "|...............B..|\n"
    + "|..................|\n"
    + "|..................|\n"
    + "|..............B...|\n"
    + "|..................|\n"
    + "|..........B.......|\n"
    + "+------------------+",
    "+------------------------+\n"
    + "|.....................B..|\n"
    + "|........................|\n"
    + "|............B...........|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|......B....B.........B..|\n"
    + "|........................|\n"
    + "|...................B....|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........B..B............|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........B...............|\n"
    + "|B.......................|\n"
    + "|.B......................|\n"
    + "|.............BB....B....|\n"
    + "|............B.....B.....|\n"
    + "|.................B......|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|............B...........|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "|........................|\n"
    + "+------------------------+",
]
GAME_MAPS_NO_SOLUTION = [
    "+--------+\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|..B.....|\n"
    + "|........|\n"
    + "|...B....|\n"
    + "|........|\n"
    + "|........|\n"
    + "+--------+",
]

GAME_MAPS_EXTREME = [
    "+------------------------+\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "|BBBBBBBBBBBBBBBBBBBBBBBB|\n"
    + "+------------------------+",
]


class TestSwitchTheBulbs(unittest.TestCase):
    def test__init__(self):
        cases = [
            (GAME_MAPS[0], set([(1, 3), (5, 3)]), {(1, 3): {(5, 3)}, (5, 3): {(1, 3)}}),
            (
                GAME_MAPS[1],
                set([(1, 3), (3, 5), (5, 3)]),
                {
                    (1, 3): {(3, 5), (5, 3)},
                    (3, 5): {(1, 3), (5, 3)},
                    (5, 3): {(1, 3), (3, 5)},
                },
            ),
            (
                GAME_MAPS[2],
                set([(1, 3), (7, 5), (5, 3)]),
                {
                    (1, 3): {(5, 3)},
                    (7, 5): {(5, 3)},
                    (5, 3): {(1, 3), (7, 5)},
                },
            ),
        ]
        for game_map, expected_bulbs, expected_graph in cases:
            with self.subTest(
                f"\n{game_map}\nBulbs: {expected_bulbs}\nGraph: {expected_graph}"
            ):
                board = Board(game_map)
                self.assertEqual(board.bulbs, expected_bulbs)
                self.assertEqual(board.graph, expected_graph)

    def test_no_route(self):
        cases = [
            GAME_MAPS_NO_SOLUTION[0],
        ]
        for game_map in cases:
            with self.subTest(f"\n{game_map} --> None"):
                board = Board(game_map)
                actual = board.switch_bulbs()
                self.assertIsNone(actual)

    def test_switch_bulbs(self):
        for i, game_map in enumerate(GAME_MAPS):
            expected = GAME_SOLUTIONS[i]
            with self.subTest(f"{game_map} --> {expected}"):
                board = Board(game_map)
                actual = board.switch_bulbs()
                self.assertIn(actual, expected)

    def test_switch_bulbs_all_paths(self):
        for game_map in GAME_MAPS:
            with self.subTest(f"{game_map} --> Should have solution"):
                board = Board(game_map)
                actual = board.switch_bulbs()
                self.assertEqual(len(actual), len(board.bulbs))

    def test_switch_bulbs_extream(self):
        for game_map in GAME_MAPS_EXTREME:
            with self.subTest(f"{game_map} --> Should have solution"):
                board = Board(game_map)
                actual = board.switch_bulbs()
                self.assertEqual(len(actual), len(board.bulbs))


class TestSwitchBulbsCodeWarsEntry(unittest.TestCase):
    def test_switch_bulbs(self):
        for i, game_map in enumerate(GAME_MAPS):
            expected = GAME_SOLUTIONS[i]
            with self.subTest(f"{game_map} --> {expected}"):
                actual = switch_bulbs(game_map)
                self.assertIn(actual, expected)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
