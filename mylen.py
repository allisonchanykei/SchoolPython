#!/usr/bin/env python

def mylen(s):
	count=0
	for letter in s:
		count = count+1
	return count
	
word=raw_input()

print mylen(word)
