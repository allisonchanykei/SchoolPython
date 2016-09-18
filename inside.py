#!/usr/bin/env python

def inside(sub,string):
	for x in range(len(string)-len(x)+1):
		y = string[x:x+len(sub)]
		if y == sub:
			return 'True'
	return 'False'

print inside('ate','chocolate')

