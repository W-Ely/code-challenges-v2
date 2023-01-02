"""
Given a string of digits, return the longest substring with alternating
odd/even or even/odd digits. If two or more substrings have the same
length, return the substring that occurs first.
"""


def longest_substring(digits):
    substring = current = ""
    trailing_is_even = int(digits[0]) % 2 != 0
    for digit in digits:
        leading_is_even = int(digit) % 2 == 0
        if leading_is_even == trailing_is_even:
            substring = max((substring, current), key=len)
            current = ""
        current += digit
        trailing_is_even = leading_is_even
    substring = max((substring, current), key=len)
    return substring
