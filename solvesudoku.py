#!/usr/bin/python

def solve(b,r,c):
	sb=set(b)
	sr=set(r)
	sc=set(c)
	sall=set(range(1,10))
	sol=sall-sb-sr-sc
	return list(sol)
box=[3,6,5]
row=[3,2,1]
col=[6,9]
print solve(box,row,col)
