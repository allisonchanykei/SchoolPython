#!/usr/bin/env python

def mymin(l):
	small=l[0]
	for x in l:
		if x<small:
			small = x
	return small

l=[3,5,1,8,2]
print mymin(l)
