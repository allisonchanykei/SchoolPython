def shuffle (s1,s2):
	n = ""
	for l in range (len(s1)):
		n = n + s1[l]+s2[l]
	return n
a = '1234'
b = 'abcd'
print shuffle (a,b)
