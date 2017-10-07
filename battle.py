import random
import calc

class Battlefield(object):
	"""Instance is a battlefield

	INSTANCE ATTRIBUTES:
	youPokemon 	[Pokemon]
	oppPokemon	[Pokemon]
	hazard 		[str]
	weather		[str]
	"""

	def __init__(self, youPokemon, oppPokemon, hazard, weather):
		self.__youPokemon = youPokemon
		self.__oppPokemon = oppPokemon
		self.__hazard = hazard
		self.__weather = weather

	def currentlyOut(self, val):
		if val == 0:
			return self.__oppPokemon
		return self.__youPokemon

	def useMove(move, user, target):
		if move.getType() == "AtkMove":
			damage = calc.damageCalc()




def run(you, opp):
	while isRunning:
		"""Returns: None

		RUNS THE BATTLE. LINK TO HTML
		AS MUCH AS POSSIBLE.

		Parameter you: you, the trainer
		Precondition: you is of type Trainer

		Parameter opp: the opponent
		Precondition: opp is of type Trainer
		"""

		battlefield = Battlefield(you.getParty(0), opp.getParty(0))

		selectedMove = pick(battlefield)
		oppSelectedMove = opp.selectMove()

		if (battlefield.currentlyOut().getSpe()) > (battlefield.currentlyOut(0).getSpe()):
			battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(0))
			battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(0), battlefield.currentlyOut())
		elif (battlefield.currentlyOut().getSpe()) < (battlefield.currentlyOut(0).getSpe()):
			battlefield.useMove(oppSelectedMove, battlefield.currentlyOut(0), battlefield.currentlyOut())
			battlefield.useMove(selectedMove, battlefield.currentlyOut(), battlefield.currentlyOut(0))
		else:
			rand = #GENERATE RAND NUM FROM 0-1



	pass

def pick(battlefield):
	x = raw_input("FIGHT/PKMN")
	moves = []

	if x == "FIGHT":
		print "Select a move:"
		for m in battlefield.currentlyOut().getMoves():
			moves.append(m)
			print(str(m))

		x = raw_input("")
		if x.lower() == str(moves[0]).lower():
			return = moves[0]
		elif x.lower() == str(moves[1]).lower():
			return = moves[1]
		elif x.lower() == str(moves[2]).lower():
			return = moves[2]
		elif x.lower() == str(moves[3]).lower():
			return = moves[3]

