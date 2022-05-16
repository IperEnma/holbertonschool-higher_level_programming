#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result = 0
    for y in range(0, list_length):
        try:
            result = my_list_1[y] / my_list_2[y]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new.append(result)
    return (new)
