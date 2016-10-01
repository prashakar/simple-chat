#!/usr/bin/env python

import socket

tcp_ip = "10.160.12.242"
tcp_port = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((tcp_ip,tcp_port))
s.listen(1)

conn, addr = s.accept()
print "Connection address: ", addr
while 1:
	data = conn.recv(buffer_size)
	if not data: break
	print "received data: ", data
	conn.send(data)
conn.close()
