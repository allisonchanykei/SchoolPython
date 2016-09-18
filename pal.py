#!/usr/bin/env python

a = ''
x = raw_input('Enter a word: ')

for y in range (len(x)):
	z = len(x) - 1 - y
	a = a + x[z]
if a == x:
	print 'This is a palendrone!'
else:
	print 'This is not a palendrone.'	
