#!/usr/bin/python3
def best_score(a_dictionary):
    pass


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = 0
    biggest_key = []
    for key, value in a_dictionary.items():
        if a_dictionary[key] > biggest:
            biggest = value
            biggest_key = key
    return biggest_key
