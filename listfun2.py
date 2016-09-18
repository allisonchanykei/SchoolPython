#!/usr/bin/python
import random

def contains(n,l):
	for x in range(len(l)):
		if n == l[x]:
			return False
	return True
l=[]
count = 0
x=0

while count<25:
	x=x+1
	n=random.choice(range(100))
#	if n not in l:
	if contains(n,l):
		l.append(n)
		count = count + 1
l.sort()
print x
print l
