import math
from queue import PriorityQueue


class DialHomeDevice:
    def __init__(self, galactic_map):
        self.start, self.goal = None, None
        self._galactic_gates = [
            [self._create_gate(x, y, gate) for x, gate in enumerate(gates)]
            for y, gates in enumerate(galactic_map.split("\n"))
        ]
        self._set_connections()

    def _create_gate(self, x, y, gate_key):
        if gate_key == "X":
            return None
        gate = Gate(x, y)
        if gate_key == "S":
            self.start = gate
        elif gate_key == "G":
            self.goal = gate
        return gate

    def _set_connections(self):
        for gates in self._galactic_gates:
            for gate in gates:
                if gate:
                    gate.connect(self._galactic_gates, self.goal)

    def dial_home(self):
        queue = PriorityQueue()
        queue.put((0, self.start, []))
        visited = {}
        visited[self.start] = 0
        shortest_route = None
        shortest_distance = math.inf
        while queue.qsize() > 0:
            previous_distance, current, route = queue.get_nowait()
            for gate in current.connections:
                distance = previous_distance + math.dist(
                    gate.location, current.location
                )
                if gate == self.goal:
                    if distance < shortest_distance:
                        shortest_route = route
                        shortest_distance = distance
                else:
                    visited_distance = visited.get(gate, math.inf)
                    if visited_distance > distance:
                        queue.put((distance, gate, route + [gate]))
                        visited[gate] = distance
        if shortest_distance < math.inf:
            return self._route(shortest_route)
        return "Oh for crying out loud..."

    def _route(self, route):
        map_key = {None: "X", self.start: "S", self.goal: "G"}
        return "\n".join(
            [
                "".join(
                    [
                        "P" if gate and gate in route else map_key.get(gate, ".")
                        for gate in gates
                    ]
                )
                for gates in self._galactic_gates
            ]
        )


class Gate:
    def __init__(self, x, y):
        self.location = x, y
        self.connections = set()
        self.distance_from_goal = None

    def __repr__(self):
        x, y = self.location
        return f"Gate({x}, {y})"

    def __hash__(self):
        return hash(self.location)

    def __eq__(self, other_gate):
        return self.location == other_gate.location

    def __lt__(self, other_gate):
        return self.distance_from_goal < other_gate.distance_from_goal

    def connect(self, galactic_gates, goal):
        self.distance_from_goal = math.dist(self.location, goal.location)
        up, down = (0, 1), (0, -1)  # pylint: disable=invalid-name
        left, right = (-1, 0), (1, 0)
        up_left, up_right = (-1, 1), (1, 1)
        down_left, down_right = (-1, -1), (1, -1)
        directions = (up, left, right, down, up_left, up_right, down_left, down_right)
        max_x, max_y = len(galactic_gates[0]) - 1, len(galactic_gates) - 1
        for i, j in directions:
            x, y = self.location
            x, y = x + i, y + j
            if x < 0 or x > max_x or y < 0 or y > max_y:
                continue
            neighbor = galactic_gates[y][x]
            if neighbor:
                neighbor.connections.add(self)
                self.connections.add(neighbor)


def wire_DHD_SG1(existing_wires):  # pylint: disable=invalid-name
    """Code Wars entry point"""
    dhd = DialHomeDevice(existing_wires)
    return dhd.dial_home()
