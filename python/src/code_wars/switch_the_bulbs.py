import math
from collections import defaultdict
from queue import PriorityQueue


class Board:
    def __init__(self, game_map):
        self.graph = defaultdict(set)
        self.max_x = -math.inf
        self.min_x = math.inf
        self.max_y = -math.inf
        self.min_y = math.inf
        game_map = game_map.split("\n")
        game_map = game_map[1 : len(game_map) - 1]
        self.bulbs = {
            self.create_bulb(x, y)
            for x, row in enumerate(game_map)
            for y, column in enumerate(row[1 : len(row) - 1])
            if column == "B"
        }
        self.build_graph()

    def build_graph(self):
        self.set_verticals()
        self.set_horizontals()
        self.set_diagonals()

    def set_verticals(self):
        for x in range(self.min_x, self.max_x + 1):
            bulb = None
            for y in range(self.min_y, self.max_y + 1):
                if (x, y) in self.bulbs:
                    if bulb:
                        self.graph[bulb].add((x, y))
                        self.graph[(x, y)].add(bulb)
                    bulb = x, y

    def set_horizontals(self):
        for y in range(self.min_y, self.max_y + 1):
            bulb = None
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.bulbs:
                    if bulb:
                        self.graph[bulb].add((x, y))
                        self.graph[(x, y)].add(bulb)
                    bulb = x, y

    def set_diagonals(self):
        for bulb in self.bulbs:

            x, y = bulb
            while x < self.max_x and y > self.min_y:
                x += 1
                y -= 1
                if (x, y) in self.bulbs:
                    self.graph[bulb].add((x, y))
                    self.graph[(x, y)].add(bulb)
                    break

            x, y = bulb
            while x > self.min_x and y > self.min_y:
                x -= 1
                y -= 1
                if (x, y) in self.bulbs:
                    self.graph[bulb].add((x, y))
                    self.graph[(x, y)].add(bulb)
                    break

    def create_bulb(self, x, y):
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        return x, y

    def switch_bulbs(self):
        start = None
        for bulb in self.bulbs:
            if bulb not in self.graph:
                return None
            if len(self.graph[bulb]) == 1:
                start = bulb
        if not start:
            for bulb in self.bulbs:
                if route := self._find_route(bulb):
                    return route
        return self._find_route(start)

    def _find_route(self, start):
        queue = PriorityQueue()
        queue.put((0, start, {}))
        while queue.qsize() > 0:
            priority, current, route = queue.get_nowait()
            if route and len(route) == len(self.graph) - 1:
                return self._construct_route(start, route)
            for bulb in self.graph[current]:
                if bulb not in route:
                    queue.put((priority - 1, bulb, route | {current: bulb}))

    def _construct_route(self, start, route):
        constructed_route = [start]
        bulb = start
        while bulb in route:
            bulb = route[bulb]
            constructed_route.append(bulb)
        return constructed_route


def switch_bulbs(game_map):
    """Code Wars entry point"""
    board = Board(game_map)
    return board.switch_bulbs()
