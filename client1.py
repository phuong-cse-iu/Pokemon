import os
import socket
host = "127.0.0.1" # set to IP address of target computer
port = 9999
addr = (host, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
message = raw_input("Enter message to send or type 'exit': ")

while True:
	message = raw_input("Enter message to send or type 'exit': ")
	if message != 'exit':
		client_socket.send(message)
	
	data = client_socket.recv(1024)
	if not data:
		break
	print data
    
    
client_socket.close()
os._exit(0)
