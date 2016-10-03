#!/usr/bin/env python

import socket, sys, threading, time, re

class Connections(object):
	"""
	The run() method will be started and run in background until the application exits
	"""
	
	def __init__(self,interval=0.1):
		self.interval = interval

		thread = threading.Thread(target=self.run)
		thread.daemon = True
		thread.start()
	
	def broadcast(self,data,conn,server_msg=False,backto_client=False,direct_client=False):
                for client in client_conn:
			if server_msg == True:
				print "Broadcasting to all users"
				client[0].send(data)
			if backto_client == True:
				print "Send back to REQUESTER %s" % conn
				if client[0] == conn:
					client[0].send(data)
			if (client[0] == conn) and (direct_client == True):
				print "Direct message to %s" % conn
				client[0].send(data)
			elif client[0] != conn:
				print conn
				print client[0]
				print clients[conn]
				try:
					client[0].send(str(clients[conn]) + " " + data)
				except:
					print "Client %s must have disconnected" % client[0]
					del clients[client[0]]
					client_conn.remove(client)
					print str(clients)
					print client_conn
					client[0].close()
					continue
	def user_run(self,conn,addr):
		while True:
			try:
				data = conn.recv(buff_size)
				if data:
 	                		print ("<" + str(conn.getpeername()) + "> " + data)
					if data[:8] == "USERNAME":
						print "Adding user %s to dict" % data[9:]
						clients[conn] = [data[9:]];
						print "Total client list: %s" % str(clients)
						data = "<%s has joined the server>" % data[9:]
						self.broadcast(data,conn,server_msg=True)
					elif data == "USER_REQUEST":
						print "Show users to client %s" % conn
						data = "<Client List>\n%s" % str(clients[conn])
						self.broadcast(data,conn,backto_client=True)
					elif data[:6] == "DIRECT":
						match = re.search('DIRECT:(.*)MSG:(.*)',data)
						user = match.group(1)
						data = match.group(2)
						print "Direct message to %s" % user
						print "MESSAGE: %s" % data
						for conn, name in clients.items():
							print conn
							print name[0]
							if name[0] == user:
								self.broadcast(data,conn,direct_client=True)
								break
						#self.broadcast(data,conn)
					else:
						self.broadcast(data,conn)
				time.sleep(self.interval)
			except:
				sys.exit(1)
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
	clients = {}
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
