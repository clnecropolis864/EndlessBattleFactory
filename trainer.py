class Trainer(object):
	"""Instance is a trainer (player)
	    
	INSTANCE ATTRIBUTES:
	name	[str]
	party	[list]

	"""

	def __init__(self, name, party):
		"""Initializer: Creates a trainer
        
        Parameter name: The trainer (player)'s name
        Precondition: name is of type str
        
        Parameter party: The current pokemon on the trainer
        Precondition: party is of type list
        """
		self.name = name
		self.party = party