#!/usr/bin/python3
def best_score(a_dictionary):
    dict1 = a_dictionary
    sorted_dict = {}
    sorted_score = sorted(dict1, key=dict1.get)

    for i in sorted_score:
        sorted_dict[i] = dict1[i]

    return sorted_dict
