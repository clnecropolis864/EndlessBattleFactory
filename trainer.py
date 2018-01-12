class Trainer(object):
	"""Instance is a trainer (player)
	    
	INSTANCE ATTRIBUTES:
	__name	[str]
	__party	[list]

	"""

	def __init__(self, name, party):
		"""Initializer: Creates a trainer
        
        Parameter name: The trainer (player)'s name
        Precondition: name is of type str
        
        Parameter party: The current pokemon on the trainer
        Precondition: party is of type list
        """
		self.__name = name
		self.__party = party

	def getParty(self, i):
		return self.__party[i]

	def displayParty(self):
		string = "["
		for x in party:
			string += x + " "
			if x.isFaint():
				string += "(FNT) "
			string += "/ "
		string += "]"

		return string
	def test():
		return "test"


class AITrainer(Trainer):
	"""Instance is the AI

	ADDTL. INSTANCE ATTRIBUTES:

	"""

	def __init__(self, name, party):
		"""Initializer: Creates an AI"""

		Trainer.__init__(self, name, party)

	def selectMove():
		pass #Oh dear...this will take some time.

	
def buildTeam():
	"""Builds a team"""
	from pokedex import pk
	import random

	partyStats = [0, 0, 0, 0, 0]

	#First pokemon
	index1 = random.randomint(0, len(pk) - 1)
	self.__party[0] = pk[index1]

	#Inputting pokemon's notes into partyStats
	for i in range(0, len(partyStats)):
		assert len(self.__party[0].getNotes()) == partyStats
		partyStats[i] += self.__party[0].getNotes()[i]

	#Second pokemon
	index2 = 0
	pokemon2 = None

	while True:
		index2 = random.randint(0,len(pk) - 1)

		if index2 != index1:
			pokemon2 = pk[index2]
			if not sharesItem(partyStats, pokemon2.getNotes()):
				break

	#Third pokemon
	index3 = 0
	pokemon3 = None

	while True:
		index2 = random.randint(0,len(pk) - 1)

		if (index3 != index2) and (index3 != index1):
			pokemon3 = pk[index3]
			if not sharesItem(partyStats, pokemon2.getNotes()):
				break
#Helper methods
def highest(li, num = 1):
	"""Returns: the index of <num> greatest items in list li

	Param li: A list
	Precondition: li is of type list and has length > 0

	Param num: The top numbers to be returned
	Precondition: num is of type int and is <= len(li)
	"""

	its = 0
	maxes = []

	while its < num:
		maxes.append(max(li).index())
		li.remove(max(li))
		its += 1

	return maxes

def sharesItem(li1, li2):
	"""Returns: true if any item in li1 is in li2

	Param li1, li2: lists
	Precondition: li1, li2 are of type lists
	"""

	for x in li1:
		if x in li2:
			return True

	return False




	