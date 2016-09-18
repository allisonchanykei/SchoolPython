#!/usr/bin/python
#CLIENT-send tcp
import socket
import sys
#python tcpsend.py ip port
#AF_INET = adress family internet
#SOCK_STREAM = TCP (Transmission Control Protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp sock_stream
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host,port)) #create connection between two computers

line=raw_input('Send:') #blocking, waits for user input
s.send(line)	#sends information through the connection
s.close()		#closes connection and socket

'''
data=s.recv(1024) #1024 number of bytes of chars blocking
print 'Server says: ',data
'''
