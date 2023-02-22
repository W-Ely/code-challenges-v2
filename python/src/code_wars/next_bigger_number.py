# pylint: disable=invalid-name
import math


def find_i_of_n_with_larger_m_to_right(numbers):
    n_with_larger_to_right = None
    for i in range(len(numbers) - 1, 0, -1):
        left, right = numbers[i - 1], numbers[i]
        if left < right:
            n_with_larger_to_right = left
            break
    return None if n_with_larger_to_right is None else i - 1


def find_j_of_smallest_m_to_right_of_n(numbers, i):
    n = numbers[i]
    smallest_m_to_right_of_n = math.inf
    j_of_smallest_m_to_right_of_n = math.inf
    for j, number in enumerate(numbers[i + 1 :], start=i + 1):
        if n < number < smallest_m_to_right_of_n:
            smallest_m_to_right_of_n = number
            j_of_smallest_m_to_right_of_n = j
    return j_of_smallest_m_to_right_of_n


def next_bigger(n):
    """Code Wars entry point"""
    numbers = [int(n) for n in str(n)]
    i = find_i_of_n_with_larger_m_to_right(numbers)

    if i is None:
        return -1

    j = find_j_of_smallest_m_to_right_of_n(numbers, i)

    numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers = [str(n) for n in numbers[: i + 1] + sorted(numbers[i + 1 :])]
    return int("".join(numbers))


