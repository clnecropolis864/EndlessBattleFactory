class Battlefield(object):
	"""Instance is a battlefield

	INSTANCE ATTRIBUTES:
	youPokemon 	[Pokemon]
	oppPokemon	[Pokemon]
	"""

	def __init__(self, youPokemon, oppPokemon):
		self.__youPokemon = youPokemon
		self.__oppPokemon = oppPokemon

	def currentlyOut(self):
		return self.__youPokemon

def run(you, opp):
	"""Returns: None

	RUNS THE BATTLE. LINK TO HTML
	AS MUCH AS POSSIBLE.

	Parameter you: you, the trainer
	Precondition: you is of type Trainer

	Parameter opp: the opponent
	Precondition: opp is of type Trainer
	"""

	battlefield = Battlefield(you.getParty(0), opp.getParty(0))

	pick(battlefield)

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
			moves[0].use()
		elif x.lower() == str(moves[1]).lower():
			moves[1].use()
		elif x.lower() == str(moves[2]).lower():
			moves[2].use()
		elif x.lower() == str(moves[3]).lower():
			moves[3].use()

