"""
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".
"""
import math
from queue import PriorityQueue


class Graph:
    def __init__(self, string1, string2):
        char_counts = {}
        for char in string2:
            char_counts[char] = char_counts.get(char, 0) + 1

        neighbors = set()
        slice_graph = {}
        last_possible_start = math.inf
        for i in range(len(string1) - 1, -1, -1):
            if string1[i] not in char_counts:
                continue
            if len(neighbors) == len(string2):
                last_possible_start = i
            g[i] = neighbors.copy()
            neighbors.add(i)

        self.last_possible_start = last_possible_start
        self.char_counts = char_counts
        self.slice_graph = slice_graph

    def get_min_slice(self):
        queue = PriorityQueue()
        for i in self.slice_graph:
            counts = self.char_counts.copy()
            counts[string1[i]] -= 1
            queue.put((0, i, counts))
            if i == self.last_possible_start:
                break

        shortest_length = math.inf
        shortest_slice = ""

        while queue.qsize() > 0:
            previous_length, current, counts = queue.get()
            for index in current.neighbors:
                counts = self.char_counts.copy()
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



class Solution:
    """LeetCode entry class"""

    # def minWindow(self, string1, string2):
    #     """LeetCode entry method"""
    #     char_counts = {}
    #     for char in string2:
    #         char_counts[char] = char_counts.get(char, 0) + 1
    #
    #     shortest_length = math.inf
    #     shortest_slice = ""
    #
    #     slice_tracker = {}
    #
    #     for i, char in enumerate(string1):
    #         if char not in char_counts:
    #             continue
    #
    #         slice_tracker[i] = char_counts.copy()
    #
    #         start_indexes_to_remove = []
    #         for start_index, start_index_char_counts in slice_tracker.items():
    #             if char in start_index_char_counts:
    #                 start_index_char_counts[char] -= 1
    #                 if start_index_char_counts[char] == 0:
    #                     del start_index_char_counts[char]
    #             if not start_index_char_counts:
    #                 start_indexes_to_remove.append(start_index)
    #                 if i - start_index < shortest_length:
    #                     shortest_length = i - start_index
    #                     shortest_slice = string1[start_index:i + 1]
    #
    #         for start_index in start_indexes_to_remove:
    #             del slice_tracker[start_index]
    #
    #     return shortest_slice

    def minWindow(self, string1, string2):
        """LeetCode entry method"""
        graph = Graph(string1, string2)
        return graph.get_min_slice()
