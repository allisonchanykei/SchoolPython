#!/usr/bin/env python

import random

x = random.choice(range(1,101))
n = 0

while True:
	y = int(raw_input('Guess a number: '))
	n = n + 1
	if y == x:
		print 'Correct!'
		break
	elif y > 100:
		print 'Invalid input.'
	elif y < x:
		print 'Incorrect! Higher. Guess again.'
	else:
		print 'Incorrect! Lower. Guess again.'
		
print 'It took you',n,'tries to guess the correct number.'
