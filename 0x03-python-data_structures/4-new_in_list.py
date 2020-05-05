#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	r = len(my_list)
	list = my_list[:]
	if idx is None or idx > r:
		return (list)
	list[idx] = element
	return (list)
