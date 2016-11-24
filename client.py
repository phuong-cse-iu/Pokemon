import socket, select, string, sys
 

char_list = ["1", "2"]

class Pokemon(object):
    def __init__ (self,id,name,type,base_hp,base_atk,base_def ):
        self.id=id
        self.name=name
        self.type=type
        self.base_hp = base_hp
        self.base_atk=base_atk
        self.base_def=base_def 

def attack1():
    ask = raw_input("Do you want to attack?(Y/N)\n")
    if ask == "Y" :
        p2.base_hp = p2.base_hp - p1.base_atk
    elif ask == "N" :
        print "You didnt attack"

def attack2():
    ask = raw_input("Do you want to attack?(Y/N)\n")
    if ask == "Y" :
        p1.base_hp = p1.base_hp - p2.base_atk   
    elif ask == "N" :
        print "You didnt attack\n"

def welcome(data):
    print "Welcome to the demo\n"
    test = True
    while test:
        
        if data == "1":
            print "Your pokemon descriptions:\n"
            print "ID = %d"% (p1.id)
            print "Name = %s"% (p1.name)
            print "Type = %s"% (p1.type)
            print "Base Hp = %d"%(p1.base_hp)
            print "Base Attack = %d"% (p1.base_atk)
            print "Base Defense = %d"% (p1.base_def)
            
            test = False
        elif data == "2":
            print "Your pokemon descriptions:\n"
            print "ID = %d"% (p2.id)
            print "Name = %s"% (p2.name)
            print "Type = %s"% (p2.type)
            print "Base Hp = %d"%(p2.base_hp)
            print "Base Attack = %d"% (p2.base_atk)
            print "Base Defense = %d"% (p2.base_def)
            
            test = False
        else:
            print "Invalid input.\n"

def prompt() :
    sys.stdout.write('<Me> ')
    sys.stdout.flush()

#main function
if __name__ == "__main__":
     
    # create 2 players
    p1 = Pokemon(1,"Ivysaur","grass",250,60,50 )
    p2 = Pokemon(2,"Chameleon","fire",200,60,45 )

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
    print 'Choose a char first: '
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
                        welcome(data)
                        attack1()
                    elif data == "2":
                        print "Player " + char_list[1]
                        welcome(data)
                        attack2()

                    print data
                    prompt()
             
            #user entered a message
            else :
                msg = raw_input("")
                s.send(msg)
                prompt()
         
        