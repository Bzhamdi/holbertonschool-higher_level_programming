#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	r = len(my_list)
	if idx is None or idx > r:
		return (my_list)
	my_list[idx] = element
	return (my_list)
