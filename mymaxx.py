#!/usr/bin/env python

def mymax(l):
	big=l[0]
	for x in l:
		if x>big:
			big = x
	return big

l=[3,5,1,8,2]
print mymax(l)
