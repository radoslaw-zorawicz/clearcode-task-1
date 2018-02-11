import math

def count_hack_letters(hack, letters_counter):
    for char in hack:
        if char not in letters_counter:
            raise ValueError("The hack contains illegal char")
        letters_counter[char] += 1

def calculate_sum(base, exp):
    if base is 1:
        return base * exp
    sum = (math.pow(base, exp + 1) - 1) / (base - 1) - 1
    return sum

def calculate_letters_power(letters_counter, letters_with_powers ):
    total_power = 0
    for letter, count in letters_counter.items():
        power = letters_with_powers[letter]
        total_power += calculate_sum(power, count)
    return total_power

def hack_calculator(hack):
    letters_with_powers = {'a': 1, 'b': 2, 'c': 3}
    letters_counter = dict((letter, 0) for letter in letters_with_powers)
    try:
        count_hack_letters(hack, letters_counter)
    except ValueError:
        return 0
    letters_power = calculate_letters_power(letters_counter, letters_with_powers)

    