import random
import calc
#import pygame as pg
import effectdex

class Battlefield(object):
	"""Instance is a battlefield

	INSTANCE ATTRIBUTES:
	you 		[Trainer]
	opp 		[Trainer]
	youPokemon 	[Pokemon]
	oppPokemon	[Pokemon]
	youHazard 	[str]
	oppHazard	[str]
	weather		[str]
	turn 		[int]
	"""

	def __init__(self, you, opp):
		self.__you = you
		self.__opp = opp

		self.__youPokemon = you.getParty(0)
		self.__oppPokemon = you.getParty(0)
		self.__youHazard = "none"
		self.__oppHazard = "none"
		self.__weather = weather
		self.__turn = turn

	def currentlyOut(self, val = 0):
		"""Returns: Pokemon currently out

		Parameter val: The value. 0 for you, 1 for opponent
		Precondition: val is 0 or 1 and of type int
		"""

		if val == 0:
			return self.__youPokemon
		return self.__oppPokemon

	def generateModifier(self, move, user, target):
		"""Returns: modifier used in battle

		Used to fill variables in damage calculation
		equation

		Parameter user: The pokemon using the move

		Parameter target: The target pokemon
		"""

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
		if (user.getStatus() == "burn") and (user.getMove().isPhysical()):
			modifier[5] = 0.5

		#other

		return modifier

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

		for x in range(0, len(user.getMoves())):
			if user.getMoves[x] == move:
				moveID = x
				testboolean = True

		if not testBoolean:
			print ("ERROR")

		modifier = generateModifier()

		if move.getType() == "AtkMove":
			damage = 0

			#modifier = [weather, crit, random, STAB, type, burn, other]

			#DEFINES ATK AND DEF STATES
			attack = 0
			defense = 0
			if move.isPhysical():
				attack = user.getAtk()
				defense = user.getDefense()
			else:
				attack = user.getSpAtk()
				defense = user.getSpDefense()

			#Determines whether move hits
			if move.getEffect.getKey != "alwaysHit":
				if random.random() < move.getAccuracy(): #If move hits
					damage = calc.damageCalc(user.getLevel(), move, attack, defense, modifier)
				else: #If misses
					print ("miss")
					damage = 0

			#Use/Effects
			user.useMove(moveID)
			target.hit(damage)
			self = move.effect(self)

			"""
			LEGACY CODE:
			target.hit(damage)
			target.effect(move.effect())
			user.effect(move.effect())
			"""


		else: #If move is a special move
			target.effect(move.effect())
			user.effect(move.effect())

			if move.effect().getTarget() == "battlefield": #Weather moves
				self.__weather = move.effect().getDetail

	def battleOver(self):
		"""Returns: Whether the battle is over

		Returns a boolean
		"""

		battleOver = True

		if (not allFaint(1)) and (not allFaint()):
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

	def __str__():

		"""
		------------------TURN: 1------------------
		You: Charizard          Opp: Blastoise(BRN)
		HP: 140                              HP: 20
		               WEATHER: clear
		(Blastoise)                      (Venusaur)
		(Venusaur)                      (Charizard)
		Hazards: none                 Hazards: none

		[Surf]               [Ice Beam]
		[Rapid Spin]         [Rest]

		-------------------------------------------
		"""

		line1 = "-" * 18 + "TURN: " + self.__turn + "-" * 18 + "\n"
		line2 = "You: " + self.__youPokemon
		line2 += ("Opp: " + self.__oppPokemon).rjust(43 - len(line2)) + "\n"
		line3 = "HP: " + self.__youPokemon.getHP()
		line3 += ("HP: " + self.__oppPokemon.getHP()).rjust(43 - len(line3)) + "\n"
		line4 = ("WEATHER: " + self.__weather).center(43) + "\n"
		line5 = "(" + self.__you.getParty(1) + ")"
		line5 += ("(" + self.__opp.getParty(1)+ ")").rjust(43 - len(line5)) + "\n"
		line6 = "(" + self.__you.getParty(2) + ")"
		line6 += ("(" + self.__opp.getParty(2)+ ")").rjust(43 - len(line6)) + "\n"
		line7 = "Hazards: " + self.__youHazard
		line7 += ("Hazards " + self.__oppHazard).rjust(43 - len(line7)) + "\n"
		line8 = "\n"
		line9_10 = ""
		for i in range(0, len(self.__youPokemon.getMoves())):
			if (i % 2) == 1:
				line9_10 += ("[" + self.__youPokemon.getMove(i) + "]").rjust(\
					21 - len("[" + self.__youPokemon.getMove(i - 1) + "]")) + "\n"

			line9_10 += "[" + self.__youPokemon.getMove(i - 1) + "]"
		line11 = "-" * 43

		out = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8\
			+ line9_10 + line11



	"""------------------
	GETTER/SETTER METHODS
	-------------------"""
	def getWeather(self):
		return self.__weather
	def setWeather(self, wthr):
		self.__weather = wthr



def run(you, opp):
	"""Returns: None

	Parameter you: you, the trainer
	Precondition: you is of type Trainer

	Parameter opp: the opponent
	Precondition: opp is of type Trainer
	"""
	battleOver = False
	while not battleOver:

		battlefield = Battlefield(you, opp) #Defines battlefield

		selectedMove = pick(battlefield) #Move select
		oppSelectedMove = AIPick(battlefield) #AI picks a move

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

def AIPick(battlefield):
	"""Returns: None

	How the AI picks a move"""

	maxIndex = 0
	maxDamage = 0
	modifier = battlefield.generateModifier()
	for x in range(battlefield.currentlyOut(1).getMoves()):
		#Runs each move through damage calc, sees which one is the biggest
		damage = 0
		attack = 0
		defense = 0

		if battlefield.currentlyOut(1).getMoves()[x].isPhysical():
			attack = user.getAtk()
			defense = user.getDefense()
		else:
			attack = user.getSpAtk()
			defense = user.getSpDefense()

		damage = calc.damageCalc(user.getLevel(), move, attack, defense, modifier)

		if damage > maxDamage:
			maxDamage = damage
			maxIndex = x

	return battlefield.currentlyOut(1).getMoves()[maxIndex]
