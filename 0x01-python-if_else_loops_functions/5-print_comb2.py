#!/usr/bin/python3
for numbers in range (0, 100):
    if numbers != 99:
        print("{:02}".format(numbers), end=", ")
    else:
        print("{}".format(numbers), end=" ")
