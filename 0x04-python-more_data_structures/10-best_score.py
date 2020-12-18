#!/usr/bin/python3
def best_score(a_dictionary):
    sorted_dict = {}
    sorted_score = sorted(a_dictionary, key=a_dictionary.get)  # [1, 3, 2]

    for i in sorted_score:
        sorted_dict[i] = a_dictionary[i]

    return sorted_dict
