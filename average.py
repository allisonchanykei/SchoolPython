#!/usr/bin/env python

x = float(raw_input("Enter a number: "))
total = 0
loop = 0
while x != 0:
	total = total + x
	x = float(raw_input("Enter a number: "))
	loop = loop + 1
else:
	average = total / loop
	print "The average is",average
