#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
	r = len(my_list)
	if idx < 0 or idx > r:
		return (my_list)
	del my_list[idx]
	return (my_list)
