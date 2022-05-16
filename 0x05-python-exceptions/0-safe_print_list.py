#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(0, x):
        try:
            print("{}".format(my_list[y]), end="")
            count = count + 1
        except Exception:
            break
    print()
    return(count)
