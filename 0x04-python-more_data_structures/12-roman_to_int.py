#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) != str or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 50, 'M': 1000
    }
    roman_int = 0
    for idx in roman_string:
        roman_int += (roman_dict)[idx]
    return roman_int
