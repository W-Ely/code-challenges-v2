"""
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".
"""
import math
from collections import Counter


def find_min_slice(string1, string2):
    shortest_length = math.inf
    shortest_slice = ""
    max_start = len(string1) - len(string2)
    if max_start < 0:
        return shortest_slice

    char_counts = Counter(string2)
    start = end = 0
    start_char = string1[start]
    if start_char in char_counts:
        char_counts[start_char] -= 1

    while end < len(string1) and start <= max_start:
        end_incremented = start_incremented = False
        if all(count <= 0 for count in char_counts.values()):
            length = end - start
            if shortest_length > length:
                shortest_length = length
                shortest_slice = string1[start : end + 1]
        while end < len(string1) - 1:
            end_incremented = True
            end += 1
            end_char = string1[end]
            if end_char not in char_counts:
                continue
            char_counts[end_char] -= 1
            if char_counts[end_char] <= 0:
                break
        while start <= max_start and char_counts.get(string1[start], -1) < 0:
            start_incremented = True
            start_char = string1[start]
            if start_char not in char_counts:
                start += 1
                continue
            start += 1
            char_counts[start_char] += 1
        if not start_incremented and not end_incremented:
            break

    return shortest_slice


class Solution:
    """LeetCode entry class"""

    def minWindow(self, string1, string2):  # pylint: disable=invalid-name
        """LeetCode entry method"""
        return find_min_slice(string1, string2)
