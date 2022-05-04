#!/usr/bin/python3
def best_score(a_dictionary):
    result = None
    if (a_dictionary):
        result = max(a_dictionary, key=a_dictionary.get)
    return (result)
