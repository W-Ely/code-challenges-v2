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
        expected_route = ".S.\nP..\n.G."
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

    def test_dial_home__4x4_1(self):
        galactic_map = "S...\n....\n....\nG..."
        expected_route = "S...\nP...\n.P..\nG..."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_5x5_1(self):
        galactic_map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_5x5_no_route(self):
        galactic_map = ".S...\nXXX..\n.XXXX\n..X..\nG...X"
        expected_route = "Oh for crying out loud..."
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_code_wars_entry_point(self):
        galactic_map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        self.assertEqual(wire_DHD_SG1(galactic_map), expected_route)


if __name__ == "__main__":
    unittest.main()
