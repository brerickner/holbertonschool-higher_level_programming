#!/usr/bin/python3
for left_most in range(0, 10):
    for right_most in range(left_most + 1, 10):
        if left_most == 8 and right_most == 9:
            print("{}{}".format(left_most, right_most))
        else:
            print("{}{}".format(left_most, right_most), end=", ")
