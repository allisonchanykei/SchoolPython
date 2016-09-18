#!/usr/bin/python

import sys
f=open(sys.argv[2],'r')
for x in f:
	if sys.argv[1] in x:
		print x,
f.close()
