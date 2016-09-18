#!/usr/bin/python

f=open('message.txt')
m=f.read()
f.close()
e=open('encrypt.txt','w')
l=[]
i=0
for x in m:
	x=chr(ord(x)+i)
	l.append(x)
	i=i+1
	if i==129:
		i=0
l=l[::-1]
print ''.join(l)
e.write(''.join(l))
e.close()
