import unittest

from src.code_wars.sg1 import DialHomeDevice


class TestDialHomeDevice(unittest.TestCase):

    def test_dial_home__2X2(self):
        map = ".S\nG."
        expected_route = ".S\nG."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3X3_1(self):
        map = ".S.\n...\n.G."
        expected_route = ".S.\nP..\n.G."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3X3_2(self):
        map = ".S.\nX..\n.G."
        expected_route = ".S.\nXP.\n.G."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__3X3_3(self):
        map = "S..\nXX.\nG.."
        expected_route = "SP.\nXXP\nGP."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home__4X4_1(self):
        map = "S...\n....\n....\nG..."
        expected_route = "S...\nP...\n.P..\nG..."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_5X5_1(self):
        map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_dial_home_5X5_no_route(self):
        map = ".S...\nXXX..\n.XXXX\n..X..\nG...X"
        expected_route = "Oh for crying out loud..."
        dial_home_device = DialHomeDevice(map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)


if __name__ == '__main__':
    unittest.main()

#
# def test_dial_home_device_route_no_route():
#     map = """.S...
# XXXXX
# .X.XX
# ..X..
# G...X"""
#     expected_route = "Oh for crying out loud..."
#     assert dial_home_device.dial_home() == expected_route
