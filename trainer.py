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


class AITrainer(Trainer):
	"""Instance is the AI

	ADDTL. INSTANCE ATTRIBUTES:

	"""

	def __init__(self, name, party):
		"""Initializer: Creates an AI"""

		Trainer.__init__(self, name, party)

	def selectMove():

		pass #Oh dear...this will take some time.

	