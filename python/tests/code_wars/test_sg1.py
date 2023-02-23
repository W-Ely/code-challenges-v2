# pylint: disable=protected-access
import unittest

from src.code_wars.sg1 import DialHomeDevice, Gate, wire_DHD_SG1


class TestDialHomeDeviceFunctional(unittest.TestCase):
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
        dial_home_device = DialHomeDevice(galactic_map)
        self.assertEqual(dial_home_device.dial_home(), expected_route)

    def test_code_wars_entry_point(self):
        galactic_map = ".S...\nXXX..\n.X.XX\n..X..\nG...X"
        expected_route = ".SP..\nXXXP.\n.XPXX\n.PX..\nG...X"
        self.assertEqual(wire_DHD_SG1(galactic_map), expected_route)


class TestDialHomeDeviceUnit(unittest.TestCase):
    def setUp(self):  # pylint: disable=invalid-name
        self.galactic_map = "XS\nG."
        self.dial_home_device = DialHomeDevice(self.galactic_map)

    def test_dial_home_device__init__(self):
        self.assertEqual(len(self.dial_home_device._galactic_gates), 2)
        self.assertEqual(len(self.dial_home_device._galactic_gates[0]), 2)
        x, y = 0, 1
        self.assertEqual(self.dial_home_device._galactic_gates[y][x].location, (x, y))
        self.assertEqual(
            self.dial_home_device._galactic_gates[0][1], self.dial_home_device.start
        )
        self.assertEqual(
            self.dial_home_device._galactic_gates[1][0], self.dial_home_device.goal
        )
        self.assertIn(
            self.dial_home_device.goal,
            self.dial_home_device._galactic_gates[0][1].connections,
        )
        self.assertIsNone(self.dial_home_device._galactic_gates[0][0])

    def test_dial_home_device_create_gate(self):
        previoue_start = self.dial_home_device.start
        previoue_goal = self.dial_home_device.goal
        cases = [
            ((0, 0), "X", None),
            ((1, 0), "S", Gate(1, 0)),
            ((0, 1), "G", Gate(0, 1)),
            ((1, 1), ".", Gate(1, 1)),
        ]
        for (x, y), gate_key, expected in cases:
            with self.subTest(f"Case x: {x}, y: {y}, gate_key: {gate_key}"):
                actual_gate = self.dial_home_device._create_gate(x, y, gate_key)
                self.assertEqual(actual_gate, expected)
        self.assertEqual(self.dial_home_device.start, previoue_start)
        self.assertEqual(self.dial_home_device.goal, previoue_goal)

    def test_dial_home_device_set_connections(self):
        cases = [
            (
                self.dial_home_device._galactic_gates[0][1],
                set((Gate(0, 1), Gate(1, 1))),
            ),
            (
                self.dial_home_device._galactic_gates[1][0],
                set((Gate(1, 0), Gate(1, 1))),
            ),
            (
                self.dial_home_device._galactic_gates[1][1],
                set((Gate(0, 1), Gate(1, 0))),
            ),
        ]
        for gate, expected_connections in cases:
            with self.subTest(
                f"Case {gate}, expected_connections: {expected_connections}"
            ):
                self.assertEqual(gate.connections, expected_connections)
        self.assertIsNone(self.dial_home_device._galactic_gates[0][0])

    def test_dial_home_device_dial_home(self):
        self.assertEqual(self.dial_home_device.dial_home(), "XS\nG.")

    def test_dial_home_device_route(self):
        self.assertEqual(self.dial_home_device._route([]), "XS\nG.")


class TestGate(unittest.TestCase):
    def test_gate__init__(self):
        location = 0, 0
        gate = Gate(*location)
        self.assertEqual(gate.location, location)
        self.assertEqual(gate.connections, set())
        self.assertIsNone(gate.distance_from_goal)

    def test_gate__repr__(self):
        x, y = 0, 0
        gate = Gate(x, y)
        self.assertEqual(f"{gate}", f"Gate({x}, {y})")

    def test_gate__hash__(self):
        connections = set([Gate(0, 0)])
        self.assertIn(Gate(0, 0), connections)

    def test_gate__eq__(self):
        self.assertEqual(Gate(0, 0), Gate(0, 0))

    def test_gate__lt__(self):
        gate1 = Gate(0, 0)
        gate1.distance_from_goal = 1
        gate2 = Gate(0, 1)
        gate2.distance_from_goal = 2
        self.assertLess(gate1, gate2)

    def test_gate_connect(self):
        galactic_map = "XS\nG."
        galactic_gates = [
            [Gate(x, y) if gate != "X" else None for x, gate in enumerate(gates)]
            for y, gates in enumerate(galactic_map.split("\n"))
        ]
        gate = galactic_gates[0][1]
        goal = galactic_gates[1][0]
        gate.connect(galactic_gates, goal)
        self.assertEqual(
            gate.connections, set([galactic_gates[1][0], galactic_gates[1][1]])
        )
        self.assertEqual(gate.distance_from_goal, 1.4142135623730951)


if __name__ == "__main__":
    unittest.main()
