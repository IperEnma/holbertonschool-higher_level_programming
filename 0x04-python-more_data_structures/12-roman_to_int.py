#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not(isinstance(roman_string, str)) or roman_string == None):
        return 0
    roman_dictionary = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'M': 1000}
    result = 0
    save = 0
    for x in roman_string:
        for key, value in roman_dictionary.items():
            if x == key:
                if save < value:
                    result = value - result
                else:
                    result = result + value
                save = value
    return result
