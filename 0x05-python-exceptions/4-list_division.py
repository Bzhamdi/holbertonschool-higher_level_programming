#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        try:
            l = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            l = 0
        except (TypeError, ValueError):
            print("wrong type")
            l = 0
        except IndexError:
            print("out of range")
            l = 0
        finally:
            lst.append(l)
    return lst
