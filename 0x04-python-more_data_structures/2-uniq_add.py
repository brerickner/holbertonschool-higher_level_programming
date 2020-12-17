#!/usr/bin/python
def uniq_add(my_list=[]):
    temp = 0
    for int in set(my_list):
        temp += int
    return temp
