#!/usr/bin/python

f=open('encrypt.txt')
d=f.read()
f.close()
d=d[::-1]
l=[]
i=0
for x in d:
	x=chr(ord(x)-i)
	i=i+1
	l.append(x)
	if i==129:
		i=0
print ''.join(l),
