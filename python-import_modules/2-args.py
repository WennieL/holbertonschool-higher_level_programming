#!/usr/bin/python3
import sys

num_args = len(sys.argv)
i = 1

if i == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_args - 1, 's' if num_args > 2 else ''))
    for j in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
