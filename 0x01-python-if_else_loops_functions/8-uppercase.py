#!/usr/bin/python3


def uppercase(str):

    for letters in str:
        letter = ord(letters)
        if (letter) >= 97 and (letter) <= 122:
            letter -= 32
        print("{:c}".format(letter), end=" ")
    else:
        print(" ")
