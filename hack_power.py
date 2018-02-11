import math
import re


def count_hack_letters(hack, letters_counter):
    for char in hack:
        if char not in letters_counter:
            raise ValueError("The hack contains illegal char")
        letters_counter[char] += 1


def calculate_power_multiplier(count):
    return (((1 + count) * count) / 2)


def calculate_power_of_hack_phrases(hack):
    valid_hack_phrases = {"ba": 10, "baa": 20}
    found = re.findall("baa?", hack)
    return sum(map(lambda x: valid_hack_phrases[x], found))


def calculate_letters_power(letters_counter, letters_with_powers):
    total_power = 0
    for letter, count in letters_counter.items():
        power = letters_with_powers[letter]
        total_power += power * calculate_power_multiplier(count)
    return total_power


def hack_calculator(hack):
    letters_with_powers = {'a': 1, 'b': 2, 'c': 3}
    letters_counter = dict((letter, 0) for letter in letters_with_powers)
    try:
        count_hack_letters(hack, letters_counter)
    except ValueError:
        return 0
    letters_power = calculate_letters_power(
        letters_counter, letters_with_powers)
    print(letters_power)
    phrases_power = calculate_power_of_hack_phrases(hack)
    total_power = letters_power + phrases_power
    return total_power
