#!/usr/bin/env python

def palindrome(s):
	s = s.upper() 
	a = ''
	for x in s:
		a = x + a
		if a == s:
			return 'true'
	return 'false'

print palindrome('Bob')
