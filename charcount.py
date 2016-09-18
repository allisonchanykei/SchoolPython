#!/usr/bin/env python

def charcount(char,string):
	letter = 0
	for let in string:
		if let == char:
			letter = letter + 1
	return letter
	
s = raw_input('Enter a word: ')
c = raw_input('Enter a character: ')

print charcount(c,s),c+'(s) in',s
