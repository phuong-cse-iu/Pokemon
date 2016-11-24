import socket 
import threading
clients = set()
clients_lock = threading.Lock()

class ClientThread(threading.Thread):
    def __init__(self, client_socket, addr):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.addr = addr
    def run(self):
        print "Accepted connection from: ", self.addr
        with clients_lock:
            clients.add(self.client_socket)
        try:    
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                else:
                    print data
                    with clients_lock:
                        for c in clients:
                            c.send(data)
        finally:
            with clients_lock:
                clients.remove(self.client_socket)
                self.client_socket.close()

def main():
    host = '127.0.0.1'
    port = 9999
    threads = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(10)
    print "Started on port " + str(port)
    while True:
        client_socket, addr = server_socket.accept()
        thread = ClientThread(client_socket, addr)
        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()
    server_socket.close()   

if __name__ == "__main__":
    main()


