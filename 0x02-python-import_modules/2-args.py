#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv

    arguments = len(argv)

    # __ arguments: if args passed in

    if arguments > 2:
        print("{:d} arguments:".format(arguments - 1))

        # 1 argument: if 2 args passed.

    elif arguments == 2:
        print("{:d} argument:".format(arguments - 1))

        # 0 arguments. if no args passed in
    else:
        print("{:d} arguments.".format(arguments - 1))

        # for each arg passed in, increment the position and argument in list

        for pos, arg in enumerate(argv[1:]):
            print("{:d}: {}".format(pos + 1, arg))
