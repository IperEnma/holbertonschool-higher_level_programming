#!/usr/bin/python3
def weight_average(my_list=[]):
    if (not(len(my_list))):
            return 0
    new = []
    result = 0
    div = 0
    for x in my_list:
        temp = x[0] * x[1]
        new.append(temp)
        div = div + x[1]
    for x in new:
        result = result + x
    result = result / div
    return result
