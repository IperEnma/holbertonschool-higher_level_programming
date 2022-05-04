#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not(isinstance(roman_string, str)) or not(len(roman_string))):
        return 0
    roman_dictionary = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'M': 1000}
    sig = 0
    result = 0
    numbers = []
    for x in roman_string:
        for key, value in roman_dictionary.items():
            if x == key:
                numbers.append(value)
    if (len(numbers) == 1):
        return (numbers[0])
    for actual, sig in zip(numbers, numbers[1:]):
        if actual >= sig:
            result += actual
        else:
            result -= actual
    return result + sig
