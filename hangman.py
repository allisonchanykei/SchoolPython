#!/usr/bin/python

import random
wordlist=['hat','ware','love','like','home','act','mops','hop','light','put','living','days','dating','sick','stars','popcorn',
     	 'sited','base','time','take','neat','wear','from','guts','brother','people','pole','fusion','elastic','paparazzi']

word=random.choice(wordlist)
word=[str(x) for x in word]

fill=[]
wrong=[]
for x in range(len(word)):
	fill.append('_')

count = 5
while count>0:
	print ' '.join(fill)
	print 'Guessed:',','.join(wrong)
	print 'You have',count,'chance(s) left.' 
	guess = raw_input('Guess(a-z):')
	i=0
	r=0
	for y in wrong:
		while guess == y:
			print 'You have entered this character before.'
			print ' '.join(fill)
			print 'Guessed:',','.join(wrong)
			print 'You have',count,'chance(s) left.'
			guess = raw_input('Guess(a-z):')
	for x in word:
		if  guess == x:
			fill.pop(i)
			fill.insert(i,guess)
			i=i+1
			r=r+1
			continue
		i=i+1
	if i == len(fill) and r == 0:
		wrong.append(guess)
		count = count - 1
	if fill==word:
		print ' '.join(fill)
		print "You've done it!"
		break
if fill!=word:
	print ' '.join(fill)
	print 'You are dead.'
	print 'The correct word was', ''.join(word)
