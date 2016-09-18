#!/usr/bin/env python

def bin(b):
	d=0
	b=b[::-1]
	for x in range (len(b)):
		d=d+int(b[x])*(2**x)
#		i=b[len(b)-1-x]
#		d=d+int(i)*(2**x)
	return d
n=raw_input()
print bin(n)
