import json
 
class Pokemon(object):
	def __init__ (self,id,name,type,base_hp,base_atk,base_def ):
  		self.id=id
		self.name=name
		self.type=type
		self.base_hp = base_hp
		self.base_atk=base_atk
		self.base_def=base_def 

def welcome():
	print "Welcome to the demo\n"
	test = True
	while test:
		x = raw_input("Please choose the pokemon number:\n")
		if x == "1":
			print "Your pokemon descriptions:\n"
			print "ID = %d"% (p1.id)
			print "Name = %s"% (p1.name)
			print "Type = %s"% (p1.type)
			print "Base Hp = %d"%(p1.base_hp)
			print "Base Attack = %d"% (p1.base_atk)
			print "Base Defense = %d"% (p1.base_def)
			print_out_pokemon()
			test = False
		elif x == "2":
			print "Your pokemon descriptions:\n"
			print "ID = %d"% (p2.id)
			print "Name = %s"% (p2.name)
			print "Type = %s"% (p2.type)
			print "Base Hp = %d"%(p2.base_hp)
			print "Base Attack = %d"% (p2.base_atk)
			print "Base Defense = %d"% (p2.base_def)
			print_out_pokemon()
			test = False
		else:
				print "Invalid input.\n" 	

def print_out_pokemon():
	print "You chose your first pokemon.\n"
	print "The other player will play the remaining pokemon.\n"
	print "Player 1 will attack first\n."

def text1():
	ask = raw_input("Do you want to attack?(Y/N)\n")
	if ask == "Y" :
		p2.base_hp = p2.base_hp - p1.base_atk
	elif ask == "N" :
	 	print "You didnt attack"
			
def text2():
	ask = raw_input("Do you want to attack?(Y/N)\n")
	if ask == "Y" :
		p1.base_hp = p1.base_hp - p2.base_atk	
	elif ask == "N" :
		print "You didnt attack\n"
	 	 	
def endgame():
	if p1.base_hp == 0 | p1.base_hp <0:
		print "Game Over, Player 2 wins.\n"
	elif p2.base_hp == 0 | p2.base_hp <0:
		print "Game Over, Player 1 wins.\n"	
	print "Player 1 hp: %d\n" %(p1.base_hp)
	print "Player 2 hp: %d\n"%(p2.base_hp)	


p1 = Pokemon(1,"Ivysaur","grass",250,60,50 )
p2 = Pokemon(2,"Chameleon","fire",200,60,45 )	 

welcome()
 
turn = 1
while p1.base_hp > 0 | p2.base_hp >0:

	if turn == 1:
		print "Its player 1's turn.\n"
		text1()
		turn = 2

	if turn == 2:
		print "Its player 2's turn.\n"
		text2()
		turn = 1	
endgame()		