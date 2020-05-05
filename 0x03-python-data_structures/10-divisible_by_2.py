#!/usr/bin/python3
def divisible_by_2(my_list=[]):
	bool = []
	for i in my_list:
		if i % 2:
			bool.append(False)
		else:
			bool.append(True)
	return bool
