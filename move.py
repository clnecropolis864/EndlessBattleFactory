import effectdex

class Move(object):
	"""Instance is move
	    
	INSTANCE ATTRIBUTES:
	pp: pp of move 					[int]
	type: type of move 				[str]
	id: move's unique id			[int]
	name: name of move 				[str]
	"""

	def __init__(self, pp, Type, ID, name, effect = "none", notes = ""):
		"""Initializer: Creates a Move
        
        Parameter pp: The pp of a move
        Precondition: pp is of type int
        
        Parameter type: The type of the move
        Precondition: type is of type str

        Parameter id: The pokemon's pokedex id
        Precondition: id is of type int

        Parameter name: The current pokemon on the trainer
        Precondition: name is of type str

        Parameter effect: The side effects of the move
        Precondition: effect is of type str

        Parameter notes: The details of a move's usage. i.e, 
        	swords dance is for support, flamethrower is to
        	attack, etc.
        Precondition: notes is of type str
        """

		self.__pp = pp
		self.__Type = Type
		self.__ID = ID
		self.__name = name
		self.__effect = effect
		self.__notes = notes

	def __str__(self):
		"""Returns: Name of move"""
		return self.__name

	def getNotes(self):
		return self.__notes

	def effect(self, effect):
		return effectdex.effects[effect]


class AtkMove(Move):
	"""Instance is a Move that attacks

	ADDITIONAL INSTANCE ATTRIBUTES:
	cth: chance to hit					[float]
	power: base power of move 			[int]
	physical: if the move is physical 	[bool]
	contact: if move makes contact 		[bool] 
	effect: any secondary effects		[str]
	"""

	def __init__(self, pp, Type, id, name, effect = "none", notes = "", power = 0, cth = 1, physical = True, contact = False):
		"""Initializer: Creates an attacking move

		All instance attributes are inherited from
		Move. Only the additional instance attributes
		are listed below.

		Parameter cth: The chance to hit (default = 1)
		Precondition: cth is of type float
		Precondition: (cth > 0) & (cth <= 1)
        
        Parameter power: The base power of a move
        Precondition: power is of type int

        Parameter physical: if the move is physical
        Precondition: physical is type bool
        
        Parameter contact: if the move makes contact
        Precondition: contact is of type bool

        Parameter effect: The side effect of the move
        Precondition: effect is of type str
        """

		Move.__init__(self, pp, Type, id, name, effect, notes)
		self.__power = power
		self.__cth = cth
		self.__physical = physical
		self.__contact = contact
		self.__effect = effect

	def getType(self):
		return "AtkMove"

	def getPower(self):
		return self.__power

	def getAccuracy(self):
		return self.__cth

	def isPhysical(self):
		return self.__physical

	def use(self, target):
		if target.getAbility() == "pressure":
			self.__pp -= 2
		else:
			self.__pp -= 1


		


		

class SpMove(Move):
	"""Instance is a Move that doesn't attack

	ADDITIONAL INSTANCE ATTRIBUTES:
	cth: chance to hit				[float]
	effect: any secondary effects	[str]
	"""


	def __init__(self, pp, Type, id, name, effect = "none", notes = "", cth = 1):
		"""Initializer: Creates an attacking move

		All instance attributes are inherited from
		Move. Only the additional instance attributes
		are listed below.

		Parameter cth: The chance to hit (default = 1)
		Precondition: cth is of type float
		Precondition: (cth > 0) & (cth <= 1)

		Parameter effect: The side effect of the move
		Precondition: effect is of type str
		"""

		Move.__init__(self, pp, Type, id, name, effect, notes)
		self.__cth = cth

	def getType(self):
		return "SpMove"



