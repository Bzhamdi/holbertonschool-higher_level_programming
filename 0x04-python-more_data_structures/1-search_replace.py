#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list[:]
    for i in range(len(my_list) - 1):
        if i == search and i != 0:
            list[i - 1] = replace
        elif i == search:
            list[i] = replace
    return(list)
