import math


class Board:
    def __init__(self game_map):
        # The x's and y's seem flipped to me in the solutions,
        # but I supose it's abstract
        #   y01234567
        # x
        # 0  ........
        # 1  ...B....
        # 2  ........
        # 3  ........
        # 4  ........
        # 5  ...B....
        self.graph = {}
        self.max_x = -math.inf
        self.min_x = math.inf
        self.max_y = -math.inf
        self.min_y = math.inf
        game_map = game_map.split("\n")
        game_map = game_map[1:len(game_map) - 1]
        self.blubs = set([
            self.create_bulb(x, y) for y, column in enumerate(row[1:len(row) - 1])
            for x, row in enumerate(game_map)
            if column == "B"
        ])
        self.build_graph()

    def build_graph(self):
        # bulbs (1, 3) (5,3)
        self.set_verticals()
        self.set_horizontals()

    def set_verticals(self):
        for x in range(self.min_x, self.max_x + 1):
            bulb = None
            for y in range(self.min_y, self.max_y + 1):
                if (x, y) in self.bulbs:
                    if bulb:
                        self.graph[bulb] = self.graph.get(bulb, set()).add((x, y))
                        self.graph[(x, y)] = self.graph.get((x, y), set()).add(bulb)
                    else:
                        bulb = x, y

    def set_horizontals(self):
        for y in range(self.min_y, self.max_y + 1):
            bulb = None
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.bulbs:
                    if bulb:
                        self.graph[bulb] = self.graph.get(bulb, set()).add((x, y))
                        self.graph[(x, y)] = self.graph.get((x, y), set()).add(bulb)
                    else:
                        bulb = x, y

    def create_bulb(self, x, y):
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)
        return x, y

def switch_bulbs(game_map):
    """Code Wars entry point"""
    pass
