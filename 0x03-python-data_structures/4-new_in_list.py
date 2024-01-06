#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pass


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for item in my_list:
        new_list.append(item)
    return new_list
