#!/usr/bin/env python
import socket, select, sys

def prompt():
	sys.stdout.write('<You> ')
	sys.stdout.flush()

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print "usage: python client.py hostname port"
	host = sys.argv[1]
	port = sys.argv[2]
	
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)

	try:
		s.connect((host,port))
	except:
		print "unable to connect"
		sys.exit()

	print "connected to server!"
	prompt()

	while 1:
		socket_list = [sys.stdin, s]
		read_socks,write_socks,error_socks = select.select(socket_list,[],[])
		
		for sock in read_socks:
			if sock == s:
				data = sock.recv(1024)
				if not data:
					print "dissconnected from server"
					sys.exit()
				else:
					sys.stdout.write(data)
					prompt()
			else:
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()
