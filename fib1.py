#!/usr/bin/env/ python

c = 0
a = 0
b = 1
print a,b,
while True:
	c = a + b
	if c < 50:
		print c,
		a = b
		b = c

