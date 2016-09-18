#!/usr/bin/python

import sys
f=open(sys.argv[2],'r')
line = int(sys.argv[1])
s=f.readlines()
f.close()
#for x in s[len(s)-line:]:
#	print x,
for x in range(len(s)-line,len(s)):
	print s[x],
