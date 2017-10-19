class Pokemon(object):
	"""Instance is a pokemon
	    
	INSTANCE ATTRIBUTES:
	__hp				[int]
	__attack			[int]
	__defense			[int]
	__special attack	[int]
	__special defense	[int]
	__speed				[int]
	__moves 			[list]
	__item				[str]
	__ability			[str]

	"""

	def __init__(self, stats, moves, ability, item = None):
		"""Initializer: Creates a pokemon
        
        Parameter stats: A pokemon's current stats
        Precondition: stats is of type list with len() = 6
        
        Parameter d: A pokemon's current 4 moves
        Precondition: moves is of type list with len() <= 4

        Parameter ability: A pokemon's ability
        Precondition: ability is of type str

        Parameter item: A pokemon's current held item
        Precondition: item is of type string
        """
		self.__hp = stats[0]
		self.__atk = stats[1]
		self.__defense = stats[2]
		self.__spatk = stats[3]
		self.__spdefense = stats[4]
		self.__spe = stats[5]

		self.__moves = moves

		self.__ability = ability 

		self.__item = item

	def useMove(self, moveno):
		self.__moves[moveno].use()

	def getMoves(self):
		return self.__moves

	def getSpe(self):
		return self.__spe

	def hit(self, damage):
		self.__hp -= damage

	def effect(self, effect):
		pass


	
	
	