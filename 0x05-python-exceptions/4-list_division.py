#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for y in range(0, list_length):
        try:
            new.append(my_list_1[y] / my_list_2[y])
        except TypeError:
            new.append(0)
            print(f"wrong type")
        except ZeroDivisionError:
            new.append(0)
            print(f"division by 0")
        except IndexError:
            new.append(0)
            print(f"out of range")
    return(new)
