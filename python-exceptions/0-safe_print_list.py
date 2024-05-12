#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0
    try:
        for num in range(x):
            print(my_list[num], end="")
            printed_count += 1
    except IndexError:
        pass

    print()

    return printed_count
