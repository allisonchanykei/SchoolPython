#!/usr/bin/env/ python

total = 0
newinfect = 1
day = 1
while True:
	total = total + newinfect
	if total > 7e9:
		break
	day = day + 1
	newinfect = newinfect*2
print day
