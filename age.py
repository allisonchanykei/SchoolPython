#!/usr/bin/env python
citizen=raw_input("Are you a citizen?(y/n): ")
if citizen=="n":
	print "You must be a citizen in order to vote!"
elif citizen=="y":
	age=int(raw_input("Enter your age: "))
	if age>120:
		print "You can't vote because you are DEAD!"
	elif age>=18:
		print "You can vote!"
	elif age<0:
		print "You can't vote because you were not born yet!"
	else:
		print "Sorry, you can only vote when you are 18 or older!"
else:
	print "Invalid input!"
