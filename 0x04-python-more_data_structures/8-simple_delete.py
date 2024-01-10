#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    pass


def simple_delete(a_dictionary, key=""):
    new_dict = {}

    for prop, value in a_dictionary.items():
        if prop != key:
            new_dict[prop] = value

    return new_dict
