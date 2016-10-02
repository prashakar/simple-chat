#!/usr/bin/env python

import socket, sys

def prompt(msg=""):
	sys.stdout.write("<You> " + msg)
	sys.stdout.flush()
if __name__ == "__main__":
	ip = "205.211.159.43"
	port = int(sys.argv[1])
	buff_size = 1024

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print sock	
	try:
		sock.connect((ip,port))
	except:
		print "Unable to connect!"
		sys.exit()
	
	print "Connected to server!"
	print sock.recv(1024)

	while 1:
		msg = raw_input("<You> ")
		while msg == "":
			print "Please enter a message!"
			msg = raw_input("<You> ")
		sock.send(msg)
		try:
			data = sock.recv(1024)
			print data
		except:
			pass	
	
