#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    od_set = set_1.difference(set_2)
    set_2 = set_2.difference(set_1)
    od_set = od_set.union(set_2)
    return od_set
