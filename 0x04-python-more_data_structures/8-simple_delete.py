#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    pass


def simple_delete(a_dictionary, key=""):
    new_dictionary = {}
    new_dictionary.update(a_dictionary)

    del((new_dictionary)[key])
    return new_dictionary
