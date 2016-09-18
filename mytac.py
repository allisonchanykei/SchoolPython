#!/usr/bin/python

import sys
f=open(sys.argv[1],'r')
s=f.readlines()
#s=f.read()
#print s[::-1]
f.close()
for x in s[::-1]:
	print x,
