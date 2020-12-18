#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    for wt in my_list:
        a += (wt[0] * wt[1])
        b += wt[1]
    return (a/b)
