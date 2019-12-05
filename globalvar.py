dice = ['one','two','three','four','five','six']	#List
namerecallone = 0
namerecalltwo = 0
betonemoney = 2000
bettwomoney = 2000
bm = ' Rubles' 
bm2 = ' Rubles'
class money():					#Class		
	def WinP1(self):
		print('%s Won %s %s \n%s now has %s' % (betonename,betonemoneyspending,bm,betonename,betonemoney))	#Module
	def LossP1(self):
		print('%s Lost %s %s \n%s now has %s' % (betonename,betonemoneyspending,bm,betonename,betonemoney))
	def Winp2(self):
		print('%s Won %s %s \n%s now has %s' % (bettwoname,bettwomoneyspending,bm2,bettwoname,bettwomoney))
	def LossP2(self):
		print('%s Lost %s %s \n%s now has %s' % (bettwoname,bettwomoneyspending,bm2,bettwoname,bettwomoney))

class winners:

	def PlayerOneWins(self):
		file = open('Winners', 'a')
		file.write('%s Has Won.\n' % (betonename))
		file.close()

	def PlayerTwoWins(self):
		file = open('Winners', 'a')
		file.write('%s Has Won.\n' % (bettwoname))
		file.close()

class losers(winners):

	def PlayerOneLoses(self):
		file = open('Losers', 'a')
		file.write('%s Has lost.\n' % (betonename))
		file.close()

	def PlayerTwoLoses(self):
		file = open('Losers', 'a')
		file.write('%s Has lost.\n' % (bettwoname))
		file.close()