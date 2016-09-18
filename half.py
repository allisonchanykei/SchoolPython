#!/usr/bin/env python

l = 1
h = 100

while True:
	a = (h+l)//2
	print a
	ans = raw_input('Is this correct? (yes/higher/lower): ')
	if ans == 'yes':
		break
	elif ans == 'higher':
		l = a
	elif ans == 'lower':
		h = a
	else:
		print 'invalid input'
