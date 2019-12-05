"""This is the dice game project but has
a betting system and some other things."""

import random						#Importing Variables from another file
from globalvar import *
class money():					#Class, Displays how many rubles were lost or won and how much the now have 		
	def WinP1(self):
		print('%s Won %s %s \n%s now has %s' % (betonename,betonemoneyspending,bm,betonename,betonemoney))	
	def LossP1(self):
		print('%s Lost %s %s \n%s now has %s' % (betonename,betonemoneyspending,bm,betonename,betonemoney))
	def Winp2(self):
		print('%s Won %s %s \n%s now has %s' % (bettwoname,bettwomoneyspending,bm2,bettwoname,bettwomoney))
	def LossP2(self):
		print('%s Lost %s %s \n%s now has %s' % (bettwoname,bettwomoneyspending,bm2,bettwoname,bettwomoney))

class winners:												#Makes a new file that displays winners for one, losers for another
	def PlayerOneWins(self):
		file = open('Winners', 'a')
		file.write('%s Has Won.\n' % (betonename))
		file.close()

	def PlayerTwoWins(self):
		file = open('Winners', 'a')
		file.write('%s Has Won.\n' % (bettwoname))
		file.close()

class losers(winners):							#inheritance
	def PlayerOneLoses(self):
		file = open('Losers', 'a')
		file.write('%s Has lost.\n' % (betonename))
		file.close()

	def PlayerTwoLoses(self):
		file = open('Losers', 'a')
		file.write('%s Has lost.\n' % (bettwoname))
		file.close()

a = money()
g = losers()
		
print('\nEveryone starts with 2,000 Rubles\nMinimum bet is 200 Rubles.\nIf you have less than 200 Rubles remaining,\nyou must bet all of your remaining money.\n')
while True:																									#starts the game/ Boolean / loop
	Play = input('Player 1 would You Like to Play? ')														#Checks if they want to play/ local Variable

	if Play.lower().startswith('y'):
		Play = input('Player 2 would You Like to Play? ')

		if Play.lower().startswith('y'):
			if namerecallone == 0:																			#Asks for their name and how much they want to bet
				betonename = input('Enter Your Name Player 1? ')			
			betonemoneyspending = int(input('How Much are you Betting %s? (Numerical Form.) '% (betonename)))

			if betonemoneyspending >= 200 or betonemoney <= 200 and betonemoneyspending == betonemoney:				#Allows bet if the bet is above or = 200 unless they have less than that 
																													#than it makes them do max bet
				if betonemoneyspending <= betonemoney:																#Checks if they have enough money.
					betonebet = 0
					namerecallone = 1
					print()


					if namerecalltwo == 0:
						bettwoname = input('Enter Your Name Player 2? ')
						namerecalltwo = 1
					bettwomoneyspending = int(input('How Much are you Betting %s? (Numerical Form.) ' % bettwoname))
					
					if bettwomoneyspending >= 200 or bettowmoney <= 200 and bettwomoneyspending == bettwomoney:		#Allows bet if the bet is above or = 200 unless they have less than that 
																													#than it makes them do max bet
						if bettwomoneyspending <= bettwomoney:														#Checks if they have enough money.
							bettwobet = 0
							print()

							for i in range(0,5): 
								dice1, dice2 = random.randint(0,5), random.randint(0,5) 										#gives variables a random Number 1-6 
								if dice1 > dice2: betonebet +=  1 ; print('%s Wins %s > %s' %(betonename,dice[dice1],dice[dice2]))	#Prints who wins and how. the dice[dice1] thing makes
								elif dice2 > dice1: bettwobet += 1 ; print('%s Wins %s < %s' %(bettwoname,dice[dice1],dice[dice2]))	#the intergers words
								else: print('Tie %s = %s'%(dice1, dice2))

							if betonebet > bettwobet: 																			#Finds the Overall Winner and says if 
								betonemoney += betonemoneyspending																#Calls class and def to print the outcome
								bettwomoney -= bettwomoneyspending
								a.WinP1()
								a.LossP2()
								print()																							#they won or lost and how much they won or lost
							elif bettwobet > betonebet:																			#Calls class and def to print the outcome
								betonemoney -= betonemoneyspending
								bettwomoney += bettwomoneyspending
								a.Winp2()
								a.LossP1()
							else:
								print('House Wins!!!!')																			#Calls class and def to print the outcome
								betonemoney -= betonemoneyspending		
								bettwomoney -= bettwomoneyspending
								a.LossP1()
								a.LossP2()
							print()


							if betonemoney == 0 and bettwomoney == 0:										#Checks for a winner/ Logical operator
								g.PlayerOneLoses()															#Calls class/ inheritance and outputs a file
								g.PlayerTwoLoses()
								break 

							elif betonemoney == 0:
								g.PlayerOneLoses()
								g.PlayerTwoWins()
								break

							elif bettwomoney == 0:
								g.PlayerOneWins()
								g.PlayerTwoLoses()
								break

							while True:
								endPlay = input('Would You Like To Play Again? ')										#Asks if they want to play again
								if endPlay.lower().startswith('y'): 
									print('\n')
									break
								elif endPlay.lower().startswith('n'): break 
								else: print('Try Again. (Only Yes or No Accepted)\n')
							if endPlay.lower().startswith('n'):
								break


						else: print('Canceled\n%s Does not have enough money\n' % (bettwoname)) 									#outputs different error messages
					else: print('Canceled\nMinimum bet is 200 Rubles or \nif you have less than 200 Rubles you must go all in\n')
				else: print('Canceled\n%s Does not have enough money\n' % (betonename)) 
			else: print('Canceled\nMinimum bet is 200 Rublesor\nif you have less than 200 Rubles you must go all in\n')

		elif Play.lower().startswith('n'): 
			break
		else:
			 print('Try Again. (Only Yes or No Accepted)'), print()
	elif Play.lower().startswith('n'): 
		break
	else:
		 print('Try Again. (Only Yes or No Accepted)'), print()

print('Goodbye')