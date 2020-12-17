#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for stuff in sorted(a_dictionary):
        print("{}: {}".format(stuff, a_dictionary[stuff]))
