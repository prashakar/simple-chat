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
	def do_all(self,args):
		sock.send(args)
	def do_msg(self,args):
		args = args.split()
		sock.send("DIRECT:"+args[0]+"MSG:"+args[1])
                #print args
                #msg = raw_input("\n<You> ")
                #while msg == "":
                #       print "Please enter a message!"
                #       msg = raw_input("<You> ")
	def emptyline(self):
		pass
	def do_setuser(self,args):
		username = args
		print "Username set to %s" % username
	def do_list(self,args):
		sock.send("USER_REQUEST")

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
	        		print(data)

			time.sleep(self.interval)
if __name__ == "__main__":
	ip = "205.211.159.43"
	port = int(sys.argv[1])
	buff_size = 1024

	username = str(raw_input("Please enter a username: "))
	print "Thanks! You will now be connected.\n"
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print sock	
	try:
		sock.connect((ip,port))
	except:
		print "Unable to connect!"
		sys.exit()
	
	print "Sucessfully connected to the server!"
	#print sock.recv(1024)

	print "Creating listening thread\n"
	list2 = Connections()
	time.sleep(1)
	print "Sending some data over"
	sock.send("USERNAME:" + username)

	time.sleep(1)	
	prompt = MyPrompt()
	prompt.prompt = '> '
	prompt.cmdloop('Starting prompt...')
	
	
