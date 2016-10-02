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
	
	def broadcast(self,data):
                for client in  client_conn:
                        print client[0]
			client[0].send(data)
	
	def user_run(self,conn,addr):
		while True:
			data = conn.recv(buff_size)
			if data:
 	                	print ("<" + str(conn.getpeername()) + "> " + data)
				self.broadcast(data)
			time.sleep(self.interval)

	def run(self):
		while True:
			conn, addr = sock.accept()	
			print "Client connected: (%s,%s)" % addr
			client_conn.append([conn,addr[0],addr[1]])
			
			conn.send(welcome_banner)
			user_thread = threading.Thread(target=self.user_run, args=(conn,addr))
			user_thread.daemon = True
			user_thread.start()
			time.sleep(self.interval)
	
if __name__ == "__main__":
	ip = "205.211.159.43"
	port = int(sys.argv[1])
	run_time = float(sys.argv[2])*60
	buff_size = 1024
	client_conn = []
	welcome_banner = "Hi, welcome to the test server!"
	#initialize socket module
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip,port))
	sock.listen(10)
	print "sock %s" % sock

	listen_conn = Connections()
	
	start_time = time.time()
	while 1:
		elapsed_time = time.time() - start_time
		if elapsed_time < run_time:
			print "Remaining time: %s" % (run_time-elapsed_time)
		if (60 < run_time-elapsed_time < 61):
			print "One minute remaining!"
		if (int(elapsed_time) == int(run_time)):
			print "Terminating server session!"
		time.sleep(1)
	sock.close()
