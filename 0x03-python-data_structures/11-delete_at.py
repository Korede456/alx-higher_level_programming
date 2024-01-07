#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    pass


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = []
    for item in my_list:
        if item not in [my_list[idx]]:
            new_list.append(item)
    return new_list
