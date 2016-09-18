#!/usr/bin/python
import random
l=[]
for x in range (20):
	l.append(random.choice(range(100)))
print l

l.sort()
print l

total = 0
for y in range (20):
	total=total + l[y]
print total

l2 = []
for x in l:
	if x%2==0:
		l2.append(x)
print l2

#won't work:
#for x in l:
#	if x%2 ==1:
#		l.remove(x)
#print l
# *never modify iterable which you are iterating over
