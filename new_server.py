#!/usr/bin/env python

import socket, sys, threading, time

class Connections(object):
	"""
	The run() method will be started and run in background until the application exits
	"""
	
	def __init__(self,interval=0.1):
		self.interval = interval

		thread = threading.Thread(target=self.run)
		thread.daemon = True
		thread.start()
	
	def user_run(self,conn,addr):
		while True:
			data = conn.recv(buff_size)
			if data:
 	                       print ("<" + str(conn.getpeername()) + "> " + data)
			time.sleep(self.interval)

	def run(self):
		while True:
			print "\nListening for client connections"
			conn, addr = sock.accept()	
			print "Client connected: (%s,%s)" % addr
			client_conn.append([conn,addr[0],addr[1]])
			
			user_thread = threading.Thread(target=self.user_run, args=(conn,addr))
			user_thread.daemon = True
			user_thread.start()
			
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
		pass
	sock.close()
