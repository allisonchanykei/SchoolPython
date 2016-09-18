#!/usr/bin/python
#CLIENT-receive tcp
import socket,sys

#a socket is a pipe that connects to a port
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Address Family Internet TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #so we can keep using the same port
#host = 'localhost' #or 0.0.0.0 when using the real network
host=sys.argv[1]
#port=3333
port=int(sys.argv[2])
s.bind((host,port)) #need to bind pot 3333 beacuse we are receiving
s.listen(1) #the server listens for incoming connections
while True:
	print 'before accept'
	conn, addr = s.accept() #blocking (same as raw_input but instead waits for an incoming connection)
	print 'after accept'
	print 'conn = ', conn
	print 'addr = ', addr
	data=conn.recv(1024) #also blocking but now for data from the established connection)
	data=2*data
	print data
	raw_input() #block until ready to send (client is waitng for us)
	conn.sendall(data) #or sendall
	conn.close()
#raw_input() (let's see if the data is sent without closing the connecetion)
