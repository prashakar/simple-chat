#!/usr/bin/env python
import socket

tcp_ip = "127.0.0.1"
tcp_port = 5005
buffer_size = 1024
message = "hello this is a test!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip,tcp_port))
s.send(message)
data = s.recv(buffer_size)
s.close()
print "received data: ",data
