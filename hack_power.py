import math
import re


def hack_calculator(hack):
    '''
    Calculate hack power
    :param str hack: String representing the hack
    '''
    letters_with_powers = {'a': 1, 'b': 2, 'c': 3}
    letters_counter = dict((letter, 0) for letter in letters_with_powers)
    try:
        count_letters(hack, letters_counter)
    except ValueError:
        return 0
    letters_power = calculate_letters_power(
        letters_counter, letters_with_powers)
    print(letters_power)
    phrases_power = calculate_power_of_phrases(hack)
    total_power = letters_power + phrases_power
    return total_power


def count_letters(hack, letters_counter):
    '''
    Count the number of occurrences of each letter in the hack
    :param str hack: String representing the hack
    :param dict letters_counter: The number of occurrences of each letter in the hack
    '''
    for char in hack:
        if char not in letters_counter:
            raise ValueError("The hack contains illegal char")
        letters_counter[char] += 1


def calculate_power_of_phrases(hack):
    '''
    Calculate total contribution from special phrases to power
    :param str hack: String representing the hack
    '''
    valid_hack_phrases = {"ba": 10, "baa": 20}
    found = re.findall("baa?", hack)
    return sum(map(lambda x: valid_hack_phrases[x], found))


def calculate_power_multiplier(count):
    '''
    Calculate power multipler of letter that occure count times 
    :param int count: The number of occurrences of a letter in the hack
    '''
    return (((1 + count) * count) / 2)


def calculate_letters_power(letters_counter, letters_with_powers):
    '''
    Calculate total contribution from letters to power
    :param dict letters_counter: The number of occurrences of each letter in the hack
    :param dict letters_with_powers: Valid letters with assigned power values
    '''
    total_power = 0
    for letter, count in letters_counter.items():
        power = letters_with_powers[letter]
        total_power += power * calculate_power_multiplier(count)
    return total_power
