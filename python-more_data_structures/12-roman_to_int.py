#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    pre_value = 0

    for char in reversed(roman_string):
        if char not in roman_num:
            return 0

        current_value = roman_num[char]

        if current_value < pre_value:
            total -= current_value
        else:
            total += current_value

        pre_value = current_value
    return total
