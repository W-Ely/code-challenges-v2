import unittest

from src.code_wars.sg1 import DialHomeDevice, wire_DHD_SG1


class TestDialHomeDevice(unittest.TestCase):
    def test_dial_home__2x2(self):
        galactic_map = ".S\nG."
        expected_route = ".S\nG."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3x3_1(self):
        galactic_map = ".S.\n...\n.G."
        expected_route = ".S.\n.P.\n.G."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3x3_2(self):
        galactic_map = ".S.\nX..\n.G."
        expected_route = ".S.\nXP.\n.G."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3x3_3(self):
        galactic_map = "S..\nXX.\nG.."
        expected_route = "SP.\nXXP\nGP."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3x3_4(self):
        galactic_map = "...\nS.G\n..."
        expected_route = "...\nSPG\n..."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__4x4_1(self):
        galactic_map = "S...\n....\n....\nG..."
        expected_route = "S...\nP...\nP...\nG..."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__5x5_1(self):
        galactic_map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__5x5_no_route(self):
        galactic_map = ".S...\nXXX..\n.XXXX\n..X..\nG...X"
        expected_route = "Oh for crying out loud..."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_large(self):
        galactic_map = """..........
..........
.....XXX..
.....X.X..
..S..X.X..
XXXXXXGX..
.......X..
..XXXXXX..
..X....X..
..X.......
..XXXXXX..
..........
.........."""
        expected_route = """..........
.....PPP..
....PXXXP.
...P.X.XP.
..S..X.XP.
XXXXXXGXP.
..PPPP.XP.
.PXXXXXXP.
.PX....XP.
.PX.....P.
.PXXXXXXP.
..PPPPPP..
.........."""
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_massive(self):
        galactic_map = "S" + "\n".join(["." * 100 for _ in range(100)])[1:10098] + "G"
        expected_route = []
        for i in range(100):
            row = ("." * i) + "P" + ("." * (99 - i))
            expected_route.append(("." * i) + "P" + ("." * (99 - i)))
        expected_route = "S" + "\n".join(expected_route)[1:10098] + "G"
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_edge_case(self):
        galactic_map = """.X.X.X....XXXXXX...X
XX.XX.XXXXXXXXXXX..X
.X.X.XX..X..X.XXXXXX
X.X..XXX...XX.X.XXX.
X.X..X..XXX.X.X.X...
.XXX..XXXXX.X.X..XX.
X.XX.SX......XXX..X.
.XXXXX.XXX...XX..X..
....X.XX..X.XX.X..XX
....X..XX..XX..X.XX.
X...X..XX.X.X.XX...X
.XXX.........X.XX..G
..XX.XX.XX.X.XXXXXX.
.X.X...X.X.XXXX..X.X
..X..XXX.XX....XXXX.
XX..XXXXXXX.....XXXX
XXXX.X.X..XXXXXX...X
X...X..X..XXXX..X..X
X.XXXXX..XX..XXX.X.X
XX.X.XX.XXXX.X..X.XX"""
        expected_route = """.X.X.X....XXXXXX...X
XX.XX.XXXXXXXXXXX..X
.X.X.XX..X..X.XXXXXX
X.X..XXX...XX.X.XXX.
X.X..X..XXX.X.X.X...
.XXX..XXXXX.X.X..XX.
X.XX.SX......XXX..X.
.XXXXXPXXX...XXP.X..
....XPXX..X.XXPXP.XX
....XP.XX..XXP.XPXX.
X...X.PXX.X.XPXX.PPX
.XXX...PPPPPPX.XX..G
..XX.XX.XX.X.XXXXXX.
.X.X...X.X.XXXX..X.X
..X..XXX.XX....XXXX.
XX..XXXXXXX.....XXXX
XXXX.X.X..XXXXXX...X
X...X..X..XXXX..X..X
X.XXXXX..XX..XXX.X.X
XX.X.XX.XXXX.X..X.XX"""
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_edge_case_simplified(self):
        galactic_map = """SX......X
X.XXX...X
.XX..X.XX
..XX..XX.
..XX.X.XG
........X"""
        expected_route = """SX......X
XPXXX...X
PXX..X.XX
P.XX..XX.
.PXX.X.XG
..PPPPPPX"""
        print("\n" + galactic_map)
        print("\n" + expected_route)
        dial_home_device = DialHomeDevice(galactic_map)
        print("\n" + dial_home_device.dial_home())
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_code_wars_entry_point(self):
        galactic_map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        self.assertEqual(wire_DHD_SG1(galactic_map), expected_route)


if __name__ == "__main__":
    unittest.main()
