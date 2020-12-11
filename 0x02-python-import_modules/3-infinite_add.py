#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
nums = len(argv)
total = 0

if nums > 2:
    for i in range(1, nums):
        argv[i] = int(argv[i])
        total += argv[i]
    print(total)
elif nums == 1:
    print(0)
else:
    print(argv[1])
