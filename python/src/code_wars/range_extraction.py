def should_append_range(i, j, numbers):
    j_is_last_index = j == len(numbers) - 1

    def next_number_is_to_large():
        return numbers[j] + 1 != numbers[j + 1]

    range_is_more_than_2_long = j - i >= 2
    return (j_is_last_index or next_number_is_to_large()) and range_is_more_than_2_long


def solution(numbers):
    """Code Wars entry point"""
    formatted = []
    i = 0
    while i < len(numbers):
        j = i + 1
        range_found = False
        while j < len(numbers) and numbers[i] + (j - i) == numbers[j]:
            if should_append_range(i, j, numbers):
                formatted.append(f"{numbers[i]}-{numbers[j]}")
                range_found = True
            j += 1
        if not range_found:
            formatted.append(str(numbers[i]))
            i += 1
        else:
            i = j
    return ",".join(formatted)
