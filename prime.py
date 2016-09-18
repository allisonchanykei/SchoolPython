#!usr/env/bin python
 
for x in range (2,101):
	factor = 0
	for y in range (2,x):
		if x % y == 0:
			factor = factor + 1
	if factor == 0:
		print x,


