class Pokemon(object):
	"""Instance is a pokemon

	INSTANCE ATTRIBUTES:
	name 				[str]
	hp					[int]
	attack				[int]
	defense				[int]
	special attack		[int]
	special defense		[int]
	speed				[int]
	moves 				[list]
	ability				[str]
	type				[list]
	item				[str]
	level				[int]
	notes				[list]

	isFaint				[bool]
	status				[str]
	"""

	def __init__(self, name, stats, moves, ability, typing, notes = [], item = None, level = 100):
		"""Initializer: Creates a pokemon

		Parameter stats: A pokemon's current stats
			[hp, attack, defense, special attack, special defense, speed]
		Precondition: stats is of type list with len() = 6

		Parameter moves: A pokemon's current 4 moves
		Precondition: moves is of type list with len() <= 4

		Parameter ability: A pokemon's ability
		Precondition: ability is of type str

		Parameter typing: A pokemon's typing
		Precondition: typing is of type list of length between 1 and 2
		Precondition: list items are of type str

		Parameter notes: The details on a pokemon's use
		Precondition: notes is of type list with length 5 (for now)

		Parameter item: A pokemon's current held item
		Precondition: item is of type string

		Parameter level: A pokemon's level
		Precondition: level is of type int
		"""

		self.__name = name

		#Stats
		self.__hp = stats[0]
		self.__atk = stats[1]
		self.__defense = stats[2]
		self.__spatk = stats[3]
		self.__spdefense = stats[4]
		self.__spe = stats[5]

		self.__moves = moves
		self.__ability = ability
		self.__typing = typing

		#With default values
		self.__item = item
		self.__level = level
		self.__notes = notes

		#Not a parameter
		self.__isFaint = False
		self.__status = ""

	#GETTER METHODS
	def getHP(self):
		return self.__hp
	def getAtk(self):
		return self.__atk
	def getDefense(self):
		return self.__defense
	def getSpAtk(self):
		return self.__spatk
	def getSpDef(self):
		return self.__spdefense
	def getSpe(self):
		return self.__spe
	def getMoves(self):
		return self.__moves
	def getAbility(self):
		return self.__ability
	def getTyping(self):
		return self.__typing
	def getLevel(self):
		return self.__level
	def getNotes(self):
		return self.__notes
	def getStatus(self):
		return self.__status

	def setStatus(self, status):
		self.status = status

	def useMove(self, moveno, target):
		"""Uses the move

		Param moveno: index of the move 	[int]
		Param target: target				[Pokemon]
		"""
		self.__moves[moveno].use(target)


	def hit(self, damage):
		"""Gets hit

		Subtracts damage from hp
		If hp is less than 0, the pokemon
		is fainted

		Parameter damage: the damage dealt
		Precondition: damage is an int
		"""
		self.__hp -= damage

		if hp <= 0:
			self.__isFaint = True
			hp = 0

	def effect(self, effect):
		pass


	def setStatus(self, status):
		self.__status = status

	#FAINTED METHODS

	def isFaint(self):
		return self.__isFaint

	def __str__(self):
		if(isFaint):
			return self.__name + "(FNT)"
		return self.__name + self.__status

"""Legend:
[Physical attack, Special attack, Physical Defense, Special Defense, Support]
"""
build = {
"SpecialAttacker": [0, 5, 2, 0, 1],
"Utility": [1,1,1,1,5],
"SwordsDance": [4, 0, 0, 0, 4]
}




