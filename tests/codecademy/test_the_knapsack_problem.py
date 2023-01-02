import unittest

from src.codecademy.the_knapsack_problem import knapsack


class TestTheKnapsackProblem(unittest.TestCase):
    def test_knapsack_1(self):
        weight_cap = 10
        weights = [3, 6, 8]
        values = [50, 60, 100]
        self.assertEqual(knapsack(weight_cap, weights, values), 110)

    def test_knapsack_2(self):
        weight_cap = 10
        weights = [3, 6, 8, 10]
        values = [50, 60, 100, 111]
        self.assertEqual(knapsack(weight_cap, weights, values), 111)

    def test_knapsack_3(self):
        weight_cap = 5
        weights = [3, 6, 8]
        values = [50, 60, 100]
        self.assertEqual(knapsack(weight_cap, weights, values), 50)

    def test_knapsack_4(self):
        weight_cap = 20
        weights = [3, 6, 8, 10]
        values = [50, 60, 100, 110]
        self.assertEqual(knapsack(weight_cap, weights, values), 220)
