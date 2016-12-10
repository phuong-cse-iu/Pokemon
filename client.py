import socket, select, string, sys
import json

# def iniAttack():
#     if player1[0]['base_speed'] > player2[0]['base_speed']:
#         print "Player 1 will attack first."
#         return   1  
#     elif player1[0]['base_speed'] < player2[0]['base_speed']:       
#         print "Player 2 will attack first."
#         return   2  


# ef showHP():
#     print "Player 1 HP: %s " %(player1[0]['base_hp'])
#     print "Player 2 HP: %s\n "% (player2[0]['base_hp'])         
# def text1():
#     ask = raw_input("Do you want to attack or switch pokemon?(A/S/N)\n")
#     if ask == "Y" :
#         player2[0]['base_hp'] = player1[0]['base_atk'] - player2[0]['base_def']
#         print "You attacked Player 2!"
#     elif ask == "S":
#         switchPokemon1()    
#     elif ask == "N" :
#         print "You didn't do anything"
#     showHP()             
    
# def text2():
#     ask = raw_input("Do you want to attack or switch pokemon?(A/S/N)\n")
#     if ask == "Y" :
#         player1[0]['base_hp'] = player2[0]['base_atk'] - player1[0]['base_def']
#         print "You attacked Player 1!"
#     elif ask == "S":
#         switchPokemon2()    
#     elif ask == "N" :
#         print "You didn't do anything"
#     showHP()         
    
# def endgame():
#     if player1[0]['base_hp'] <= 0:
#         print "Game Over, Player 2 wins.\n"
#     elif player2[0]['base_hp'] <= 0:
#         print "Game Over, Player 1 wins.\n" 
#     print "Final Player 1 hp: %d\n" %(player1[0]['base_hp'])
#     print "Final Player 2 hp: %d\n" %(player2[0]['base_hp'])
# def welcome():
#     print "Welcome to the demo\n"
#     welcome1()
#     welcome2()
# def welcome1(): 
#     for i in range (3):
#         x = input("Player 1 please choose the pokemon number: => ")
#         choosePokemon1(x)   
# def welcome2(): 
#     for i in range (3): 
#         y = input("Player 2 please choose the pokemon number: => ") 
#         choosePokemon2(y)
 
# def summon():
#     x = input("Player 1 please choose the pokemon to summon: => ")
#     x = x -1
#     for i in range (3):
#         if i == x:
#             player1.append(total1[i].copy())
#     print "Pokemon %s" %(total1[x]['name'])+ " has been chosen"
#     y = input("Player 2 please choose the pokemon to summon: => ")
#     y = y -1
#     for i in range (3):
#         if i == y:
#             player2.append(total2[i].copy())
#     print "Pokemon %s" %(total2[y]['name'])+ " has been chosen"
# def choosePokemon1(k):
#     test = True
#     while test:
#         if k <= len(data):
#             k = k-1
#             print "Your pokemon descriptions:\n"
#             print "ID = %d"% (data[k]['id'])
#             print "Name = %s"% (data[k]['name'])
#             print "Type = %s"% (data[k]['type'])
#             print "Speed = %d"% (data[k]['base_speed'])
#             print "Base Hp = %d"%(data[k]['base_hp'])
#             print "Base Attack = %d"% (data[k]['base_atk'])
#             print "Base Defense = %d"% (data[k]['base_def'])
#             test = False
#             total1.append(data[k].copy())       
#             break
#         else:
#             print "Invalid input,please choose anotwer number.\n"
#             welcome1() #testing
            
# def choosePokemon2(k):
#     test = True
#     while test:
#         if k <= len(data):
#             k = k-1
#             print "Your pokemon descriptions:\n"
#             print "ID = %d"% (data[k]['id'])
#             print "Name = %s"% (data[k]['name'])
#             print "Type = %s"% (data[k]['type'])
#             print "Speed = %d"% (data[k]['base_speed'])
#             print "Base Hp = %d"%(data[k]['base_hp'])
#             print "Base Attack = %d"% (data[k]['base_atk'])
#             print "Base Defense = %d"% (data[k]['base_def'])
#             test = False
#             total2.append(data[k].copy())   
#             break
#         else:
#             print "Invalid input,please choose anotwer number.\n"
#             welcome2() #testing
            


# player1 = []
# player2 = []                
# total1 = [] 
# total2 = []
# eV = 0.5 
# with open('pokedex.json' ) as pokedex:
#     data = json.load(pokedex)
# newdata = sorted(enumerate(data), key = lambda x:x[1]['id'])
# welcome()
# summon()
# turn = iniAttack()
# while True :    
#     if turn == 1:
#         print "Its player 1's turn.\n"
#         text1()
#         if player2[0]['base_hp'] <= 0:
#             break
#         else:       
#             turn = 2
#     elif turn == 2:
#         print "Its player 2's turn.\n"
#         text2()
#         if player1[0]['base_hp'] <= 0:
#             break
#         else:   
#             turn = 1    
# endgame()       

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
         
        