#!/usr/bin/env python

import socket, sys, threading, time

class Connections(object):
	"""
	The run() method will be started and run in background until the application exits
	"""
	
	def __init__(self,interval=1):
		self.interval = interval

		thread = threading.Thread(target=self.run)
		thread.daemon = True
		thread.start()

	def run(self):
		while True:
			print "Listening for client connections"
			conn, addr = sock.accept()	
			print "Client connected: (%s,%s)" % addr
			client_conn.append([conn,addr])
			time.sleep(self.interval)
			
if __name__ == "__main__":
	ip = "205.211.159.43"
	port = int(sys.argv[1])
	buff_size = 1024
	client_conn = []

	#initialize socket module
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip,port))
	sock.listen(10)
	print "sock %s" % sock

	listen_conn = Connections()
	
	while 1:
		for client in client_conn:
			print "\nTOTAL Clients connected: %s" % client_conn
			data = client[0].recv(buff_size)
			if data:
				print ("<" + str(client[0].getpeername()) + "> " + data)
	sock.close()
