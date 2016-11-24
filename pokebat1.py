import socket, select
import threading

RECV_BUFFER = 1024
connection_list = []
client_list = []
class ClientThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
    def run(self):
        while True:
            data = self.client_socket.recv(RECV_BUFFER)
            if not data:
                break
            print "Server recieve data: " + data
            for sock in client_list:
                if sock != self.client_socket:
                    sock.send(data)

def main():
    threadList = []
    
    host = "127.0.0.1"
    port = 9999
    recv_buffer = 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(10)

    
    print "Chat server started at port " + str(port)

    while True:
         (client_socket, addr) = server_socket.accept()
         client_list.append(client_socket)
         clientThread = ClientThread(client_socket)
         clientThread.start()
         threadList.append(clientThread)

    for t in threadList:
        t.join()

         
    client_socket.close()
if __name__ == "__main__":
    main()
    
    
