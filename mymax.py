#!/usr/bin/env python

def mymax(a,b):
	if a > b:
		return a
	return b
x=int(raw_input('a = '))
y=int(raw_input('b = '))
print mymax(x,y)
