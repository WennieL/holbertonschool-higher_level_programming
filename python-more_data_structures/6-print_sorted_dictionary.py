#!/usr/bin/python3

# using .items() method
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    for key, value in sorted_items:
        print("{}: {}".format(key, value))

# using
# def print_sorted_dictionary(a_dictionary):
    # sorted_key = sorted(a_dictionary.keys())
    # for key in sorted_key:
        # print("{}: {}".format(key, a_dictionary[key]))
