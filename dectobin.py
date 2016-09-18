#!/usr/bin/env python

def dec(d):
	b="1"
	x=0
	while d-2**x>=2**x:
		x=x+1
	d=d-2**x
	while x>0:
		x=x-1
		if d>=2**x:
			d=d-2**x
			b=b+'1'
		else:
			b=b+'0'
	return b
	
d=int(raw_input())
print dec(d)
