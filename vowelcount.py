#!/usr/bin/env python

sen = raw_input("Enter a sentence: ")
y = 0
for x in sen:
	if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
		y = y + 1
print y
