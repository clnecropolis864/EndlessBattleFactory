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
		return party[i]

class AITrainer(Trainer):
	"""Instance is the AI

	ADDTL. INSTANCE ATTRIBUTES:

	"""

	def __init__(self, name, party):
		"""Initializer: Creates an AI"""

		Trainer.__init__(self, name, party)

	