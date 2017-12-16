import random
import calc
import pygame as pg

class Battlefield(object):
	"""Instance is a battlefield

	INSTANCE ATTRIBUTES:
	youPokemon 	[Pokemon]
	oppPokemon	[Pokemon]
	hazard 		[str]
	weather		[str]
	"""

	def __init__(self, youPokemon, oppPokemon, hazard="none", weather="none"):
		self.__youPokemon = youPokemon
		self.__oppPokemon = oppPokemon
		self.__hazard = hazard
		self.__weather = weather

	def currentlyOut(self, val = 0):
		"""Returns: Pokemon currently out

		Parameter val: The value. 0 for you, 1 for opponent
		Precondition: val is 0 or 1 and of type int
		"""

		if val == 0:
			return self.__youPokemon
		return self.__oppPokemon

	def useMove(self, move, user, target):
		"""Returns: None

		Parameter move: The move. Is of type Move
		Parameter user: The user. Is of type Pokemon
		Parameter target: The target. Is of type Pokemon
		"""

		#Gives ID of move slected (ID of array)
		moveID = 0
		testBoolean = False 
		"""Will set to true if user.getMoves[x] never
		equals move"""

		for x in range(1, len(user.getMoves())):
			if user.getMoves[x] == move:
				moveID = x
				testboolean = True

		if not testBoolean:
			print ("ERROR")




		if move.getType() == "AtkMove":
			damage = 0

			#modifier = [weather, crit, random, STAB, type, burn, other]
			modifier = [1, 1, 1, 1, 1, 1, 1]

			#DEFINES MODIFIER VALUES
			#Weather
			if self.__weather == "sunny":
				if move.getType() == "fire":
					modifier[0] = 1.5
				elif move.getType() == "water":
					modifier[0] = 0.5
			elif self.__weather == "rainy":
				if move.getType() == "fire":
					modifier[0] = 0.5
				elif move.getType() == "water":
					modifier[0] = 1.5

			#crit
			crit = 0 #filler, calculates crit chance
			modifier[1] = crit

			#random
			randModifier = int(random.random() * 16 + 85)
			randModifier /= 100.0
			modifier[2]

			#STAB
			if move.getType() in user.getTyping():
				modifier[3] = 1.5

			#type
			modifier[4] = calc.typeChart(move.getType(), target.getTyping())

			#burn
			if user.getStatus() == "burn":
				modifier[5] = 0.5

			#other

			#DEFINES ATK AND DEF STATES
			attack = 0
			defense = 0
			if move.isPhysical():
				attack = user.getAtk()
				defense = user.getDefense()
			else:
				attack = user.getSpAtk()
				defense = user.getSpDefense()



			if random.random() < move.getAccuracy(): #If move hits
				damage = calc.damageCalc(user.getLevel(), move, attack, defense, modifier)
			else: #If misses
				print ("miss")

			user.useMove(moveID)

			"""
			LEGACY CODE:	
			target.hit(damage)
			target.effect(move.effect())
			user.effect(move.effect())
			"""


		else: #If move is a special move
			target.effect(move.effect())
			user.effect(move.effect())

	def battleOver(self):
		"""Returns: Whether the battle is over

		Returns a boolean
		"""

		battleOver = True

		if (not allFaint(0)) and (not allFaint()):
			battleOver = False

		return battleOver

	def allFaint(self, val = 0):
		"""Returns: Whether the battle is over

		Parameter val: The value. 0 for you, 1 for opponent
		Precondition: val is 0 or 1 and of type int
		"""
		allFaint = True

		if val == 0:
			for x in youPokemon:
				if not x.isFaint():
					allFaint = False
			return allFaint

		for x in oppPokemon:
			if not x.isFaint():
				allFaint = False
		return allFaint

	def getWeather():
		return self.__weather



def run(you, opp):
	"""Returns: None

	RUNS THE BATTLE. LINK TO HTML
	AS MUCH AS POSSIBLE.

	Parameter you: you, the trainer
	Precondition: you is of type Trainer

	Parameter opp: the opponent
	Precondition: opp is of type Trainer
	"""
	battleOver = False
	while not battleOver:

		battlefield = Battlefield(you.getParty(0), opp.getParty(0)) #Defines battlefield

		selectedMove = pick(battlefield) #Move select
		oppSelectedMove = opp.selectMove() #AI picks a move

		#Checks speed, executes moves accordingly
		if (battlefield.currentlyOut().getSpe()) > (battlefield.currentlyOut(1).getSpe()):
			battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(1))
			battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(1), battlefield.currentlyOut())
		elif (battlefield.currentlyOut().getSpe()) < (battlefield.currentlyOut(1).getSpe()):
			battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(1), battlefield.currentlyOut())
			battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(1))
		else: #If speed is equal
			rand = random.random()
			if rand < 50:
				battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(1))
				battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(1), battlefield.currentlyOut())
			else:
				battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(1), battlefield.currentlyOut())
				battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(1))

		#Checks if battle is over
		battleOver = battlefield.battleOver()		

	

def pick(battlefield):
	"""Returns: None

	The process of picking to fight or to switch

	Parameter battlefield: the battlefield
	Precondition: battlefield is of type Battlefield
	"""

	moves = [] #Represents the 4 moves you can choose from


	print ("Select a move:")
	for m in battlefield.currentlyOut().getMoves():
		moves.append(m)
		print (str(m))

	x = input("")
	if x.lower() == str(moves[0]).lower():
		return moves[0]
	elif x.lower() == str(moves[1]).lower():
		return moves[1]
	elif x.lower() == str(moves[2]).lower():
		return moves[2]
	elif x.lower() == str(moves[3]).lower():
		return moves[3]

