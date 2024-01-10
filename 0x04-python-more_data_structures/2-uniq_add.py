#!/usr/bin/python3
def uniq_add(my_list=[]):
    pass


def uniq_add(my_list=[]):
    new_list = []
    uniq_sum = 0
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
            uniq_sum += item
    return uniq_sum
