from queue import Queue


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
                    gate.connect(self._galactic_gates)

    def dial_home(self):
        queue = Queue()
        queue.put((self.start, []))
        visited = set()
        while queue.qsize() > 0:
            current, route = queue.get_nowait()
            visited.add(current)
            for gate in current.connections:
                if gate == self.goal:
                    return self._route(route)
                else:
                    if gate not in visited:
                        visited.add(gate)
                        queue.put((gate, route + [gate]))

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
        self.connections = []

    def __hash__(self):
        return hash(self.location)

    def __eq__(self, other_gate):
        return self.location == other_gate.location

    def connect(self, galactic_gates):  # pylint: disable=C0103
        up, down = (0, 1), (0, -1)  # pylint: disable=C0103
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
                if self not in neighbor.connections:
                    neighbor.connections.append(self)
                self.connections.append(neighbor)


def wire_DHD_SG1(existing_wires):  # pylint: disable=invalid-name
    """Code Wars entry point"""
    dhd = DialHomeDevice(existing_wires)
    return dhd.dial_home()
