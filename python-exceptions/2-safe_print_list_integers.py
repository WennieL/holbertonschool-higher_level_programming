#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for num in range(x):
            if isinstance(my_list[num], int):
                print("{:d}".format(my_list[num]), end="")
                count += 1
    except ValueError:
        num += 1
    print()

    return (count)
