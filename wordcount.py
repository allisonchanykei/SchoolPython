#!/usr/bin/env python

sen = raw_input("Enter a sentence: ")
y = 0
for x in sen:
	if x == " ":
		y = y + 1
print y + 1
