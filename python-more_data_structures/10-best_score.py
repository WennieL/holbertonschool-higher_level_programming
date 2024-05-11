#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    keys_list = list(a_dictionary.keys())
    k = keys_list[0]
    max_value = a_dictionary[k]

    for key in keys_list:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            k = key
    return k
