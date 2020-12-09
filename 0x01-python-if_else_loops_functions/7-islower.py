#!/usr/bin/python3
for numbers in range (0, 100):
    if(numbers < 10):
        print("0 + number{}".format(numbers), end=", ")
    else:
        print("{:}".format(numbers), end=", ")
