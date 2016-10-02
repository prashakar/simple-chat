#!/usr/bin/env python

import socket, sys, threading, time
from cmd import Cmd

class MyPrompt(Cmd):
	def do_hello(self, args):
	        """Says hello. If you provide a name, it will greet you with it."""
	        if len(args) == 0:
	            name = 'stranger'
	        else:
	            name = args
	        print "Hello, %s" % name
	def do_quit(self,args):
		print "Quitting"
		raise SystemExit
	def do_msg(self,args):
                #print args
                #msg = raw_input("\n<You> ")
                #while msg == "":
                #       print "Please enter a message!"
                #       msg = raw_input("<You> ")
                sock.send(args)
	def emptyline(self):
		pass
	
class Connections(Cmd):
        """
        The run() method will be started and run in background until the application exits
        """

        def __init__(self,interval=0.1):
                self.interval = interval

                thread = threading.Thread(target=self.listen)
                thread.daemon = True
                thread.start()
	def listen(self):
		while True:
	        	data = sock.recv(1024)
			if data:
				#MyPrompt().do_view("<" + str(sock.getpeername()) + "> " + data)
	        		print("<" + str(sock.getpeername()) + "> " + data)

			time.sleep(self.interval)
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
	#print sock.recv(1024)

	print "Creating listening thread"
	list2 = Connections()
	time.sleep(1)	
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop('Starting prompt...')
	
	
