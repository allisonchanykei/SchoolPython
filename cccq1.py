#!/usr/bin/python

m=int(raw_input())
d=int(raw_input())

if m==2:
	if d==18:
		print 'special'
	elif d<18:
		print 'before'
	else:
		print 'after'
elif m>2:
	print 'after'
else:
	print 'before'
