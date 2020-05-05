#!/usr/bin/python3
def no_c(my_string):
	str = ""
	for x in my_string:
		if x is not 'c' and x is not 'C':
            		str = str + x
	return(str)
