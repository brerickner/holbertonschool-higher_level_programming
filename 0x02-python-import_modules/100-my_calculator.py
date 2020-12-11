#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        add = add(a, b)
        sub = sub(a, b)
        mul = mul(a, b)
        div = div(a, b)
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, add))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul))
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, div))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
