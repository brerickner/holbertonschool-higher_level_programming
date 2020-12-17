#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    new = my_list.copy()
    for item in range(0, len(my_list)):
        if my_list[item] == search:
            new[item] = replace
    return new
