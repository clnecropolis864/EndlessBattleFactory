class Pokemon(Object):
	"""Instance is a pokemon
	    
	INSTANCE ATTRIBUTES:
	hp				[int]
	attack			[int]
	defense			[int]
	special attack	[int]
	special defense	[int]
	speed			[int]

	"""

	def __init__(self, stats, moves, item = None):
		"""Initializer: Creates a pokemon
        
        Parameter stats: A pokemon's current stats
        Precondition: stats is of type list with len() = 6
        
        Parameter d: A pokemon's current 4 moves
        Precondition: moves is of type list with len() <= 4

        Parameter item: A pokemon's current held item
        Precondition: item is of type string
        """
		self.hp = stats[0]
		self.atk = stats[1]
		self.defense = stats[2]
		self.spatk = stats[3]
		self.spdefense = stats[4]
		self.spe = stats[5]

		self.moves = moves

		self.item = item

	def useMove(self, moveno):
		self.moves[moveno].use()


	
	
	