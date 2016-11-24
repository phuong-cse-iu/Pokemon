import socket, select, string, sys
 

char_list = ["1", "2"]

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()




 
#main function
if __name__ == "__main__":
     
    

    host = '127.0.0.1'
    port = 9999
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    print 'Choose char to play: '


    prompt()


     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    if data == "1":
                        print "Player " + char_list[0]
                    elif data == "2":
                        print "Player " + char_list[1]

                    print data
                    prompt()
             
            #user entered a message
            else :
                msg = raw_input("")
                s.send(msg)
                prompt()