#!/usr/bin/env python

import random

y = int(raw_input('Enter a number between 1 and 100: '))

while True:
	x = random.choice(range(1,101))
	print x
	if x == y:
		print 'Correct!'
		break
	elif x < y:
		print 'Incorrect! Higher. Guess again.'
	elif x > y:
		print 'Incorrect! Lower. Guess again.'
