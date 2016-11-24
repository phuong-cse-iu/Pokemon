import json
import socket, select

player = ["1", "2"]
 
def choose_pokemon(pokemon):
    list_of_active_pokemon = []
    for one_pokemon in pokemon:
        list_of_active_pokemon.append(one_pokemon)
    return list_of_active_pokemon

def fight_pokemon(pokemon):
    return pokemon

#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)
 
if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    PLAYER_LIST = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 9999
    COUNT = 0
    # open pokedex.json file
    with open("player.json", "r") as jsonFile:
	    data = json.load(jsonFile)
    print (data)

   
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

   
 
    print "Chat server started on port " + str(PORT)

    for p in player:
        print p
 
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                client_socket, (ip, port) = server_socket.accept()
                CONNECTION_LIST.append(client_socket)
                print "Client (%s, %s) connected" % (ip, port)
                 
                broadcast_data(client_socket, "[%s:%s] entered room\n" % (ip, port))
             
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)

                    if data == "1" or data == "2":
                        if not data in player:
                            sock.send("Choose another char!")
                        else:
                            player.remove(data)
                            sock.send(data)

                                        
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)           
                    

                    for p in player:
                        print p


                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % (ip, port))
                    print "Client (%s, %s) is offline" % (ip, port)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

     
    server_socket.close()