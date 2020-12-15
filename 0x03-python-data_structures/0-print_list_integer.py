#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list[:]:
        my_list.append(i)
        print("{:d}".format(i))
