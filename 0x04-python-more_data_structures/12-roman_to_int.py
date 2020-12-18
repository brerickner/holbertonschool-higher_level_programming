#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    romanDict = dict(i=1, v=5, x=10, c=100, m=100)
    for i in roman_string:
        num = 0
        if i == list(romanDict.keys())[0]:
            num += romanDict.values
            return num
        else:
            return num
