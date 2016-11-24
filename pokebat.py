
import json
import socket, select
import sys

HOST = '127.0.0.1'
PORT = 9999
CONNECTION_LIST = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server_socket:
	print "Connected to the server"
else:
	print "Failed to connect to server"
	sys.exit()
	

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)
CONNECTION_LIST.append(server_socket)

print "Chat server started on port " + str(PORT)

while True:
	read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

	for sock in read_sockets:
		if sock == server_socket:
			sockfd, addr = server_socket.accept()
			CONNECTION_LIST.append()


