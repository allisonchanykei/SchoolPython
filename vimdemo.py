#!/usr/bin/python
import random


min=int(raw_input("guess from: "))
max=int(raw_input("guess to: "))
#raw_input returns a string. So need to change it to integer
#aiorenstioeanors
rand=random.randrange(min,max+1)
print rand #cheating
count=0
while True:
	guess=int(raw_input("Take a guess: "))
	count=count + 1
	if (guess==rand):
		break
	if (guess>rand):
		print "Too high"
	else:
	#if (guess<rand): #logically not needed
		print "Too low"
	
print "congrats"
print "it took  you ",count, " guesses to win"
