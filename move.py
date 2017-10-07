class Move(object):
	"""Instance is move
	    
	INSTANCE ATTRIBUTES:
	pp: pp of move 					[int]
	type: type of move 				[str]
	id: move's unique id			[int]
	name: name of move 				[str]
	"""

	def __init__(self, pp, type, id, name):
		"""Initializer: Creates a Move
        
        Parameter pp: The pp of a move
        Precondition: pp is of type int
        
        Parameter type: The type of the move
        Precondition: type is of type str

        Parameter id: The pokemon's pokedex id
        Precondition: id is of type int

        Parameter name: The current pokemon on the trainer
        Precondition: name is of type str
        """

		self.__pp = pp
		self.__type = type
		self.__id = id
		self.__name = name

	def __str__():
		"""Ret__urns: Name of move"""

		return self.__name

class AtkMove(Move):
	"""Instance is a Move that attacks

	ADDITIONAL INSTANCE ATTRIBUTES:
	cth: chance to hit					[float]
	power: base power of move 			[int]
	physical: if the move is physical 	[bool]
	contact: if move makes contact 		[bool] 
	effect: any secondary effects		[str]
	"""

	def __init__(self, pp, type, id, name, power, cth = 1, physical = True, contact = False, effect = "none"):
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

		Move.__init__(self, pp, type, id, name)
		self.__power = power
		self.__cth = cth
		self.__physical = physical
		self.__contact = contact
		self.__effect = effect

	def getType(self):
		return "AtkMove"

	def getPower(self):
		return self.__power

		

class SpMove(Move):
	"""Instance is a Move that doesn't attack

	ADDITIONAL INSTANCE ATTRIBUTES:
	cth: chance to hit					[float]
	effect: any secondary effects	[str]
	"""


	def __init__(self, pp, type, id, name, cth = 1, effect = "none"):
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

		Move.__init__(self, pp, type, id, name)
		self.__cth = cth
		self.__effect = effect

	def getType(self):
		return "SpMove"



