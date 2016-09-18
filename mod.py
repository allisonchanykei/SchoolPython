#!/usr/bin/env python

def foo(x):
	'''This is the foo function doc string 
It describes the function. '''
	print 'this function prints',x
	
#print 'the name of this program is',__name__
#if the built in __name__ variable is __main__ then run the if statement below
if __name__ == '__main__':
	print 'this is being run in mod'
	foo(5)
	print foo.__doc__	#prints the doc string of the foo function
