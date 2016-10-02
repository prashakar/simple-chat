#!/usr/bin/env python
import socket, select

def broadcast(sock,message):
	for socket in connection_list:
		if socket != s and socket != sock :
			try:
				socket.send(message)
			except:
				socket.close()
				connection_list.remove(socket)

<<<<<<< HEAD
if __name__ == "__main__":
	tcp_ip = "127.0.0.1"
	tcp_port = 5005
	buffer_size = 1024
	#keep track of sockets
	connection_list=[]
		
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((tcp_ip,tcp_port))
	connection_list.append(s)
	s.listen(10)
	print "Server started on port %s" % tcp_port
	
	while 1:
		read_socks,write_socks,error_socks = select.select(connection_list,[],[])
	
		for sock in read_socks:
			if sock == s:
				conn, addr = s.accept()
				connection_list.append(conn)
				print "Client connected: %s" % addr
				
			else:
				try:
					data = conn.recv(buffer_size)
					if data:
						broadcast(sock,"\r"+'<'+str(sock.getpeername())+'>'+data)
				except:
					broadcast(sock,"client at %s is offline" % addr)
					print "Client at %s is offline" % addr
					sock.close()
					connection_list.remove(sock)
					continue
		s.close()
=======
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
>>>>>>> 88f64167e592acdd087acc8381790122c0fd0622
