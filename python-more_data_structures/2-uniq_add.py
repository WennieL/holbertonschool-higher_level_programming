#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    sum = 0
    for num in my_list:
        sum += num
    return sum
