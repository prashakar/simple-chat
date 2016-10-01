#!/usr/bin/env python
import socket

tcp_ip = "10.160.12.242"
tcp_port = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip,tcp_port))
while 1:
	message = raw_input("Enter message to send:\n")	
	s.send(message)
	data = s.recv(buffer_size)
s.close()
print "received data: ",data
