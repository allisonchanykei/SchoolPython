#!/usr/bin/python
import sys
f=open(sys.argv[2],'r')
line = int(sys.argv[1])
while line>0:
	print f.readline(),
	line=line-1
f.close()
