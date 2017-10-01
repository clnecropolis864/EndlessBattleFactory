class Move(Object):
	"""Instance is move
	    
	INSTANCE ATTRIBUTES:
	pp: pp of move 				[int]
	type: type of move 			[str]
	id: move's unique id			[int]
	name: name of move 			[str]
	cth: chance to hit				[int]
	effect: any secondary effects	[str]
	"""

	def __init__(self, pp, type, id, name, cth = 1, effect):
		"""Initializer: Creates a Move
        
        Parameter pp: The pp of a move
        Precondition: pp is of type int
        
        Parameter type: The type of the move
        Precondition: type is of type str

        Parameter id: The pokemon's pokedex id
        Precondition: id is of type int

        Parameter name: The current pokemon on the trainer
        Precondition: name is of type str

        Parameter cth: The chance to hit (default = 1)
        Precondition: cth is of type float
        Precondition: (cth > 0) & (cth <= 1)

        Parameter effect: Secondary effects of the move
        Precondition: effect is of type str
        """

		self.pp = pp
		self.type = type
		self.id = id
		self.name = name
		self.cth = cth
		self.effect = effect

	def __str__():
		"""Returns: Name of move"""

		return name

class AtkMove(Move):
	"""Instance is a Move that attacks

	ADDITIONAL INSTANCE ATTRIBUTES:
	power: base power of move 		[int]
	contact: if move makes contact [bool] 
	"""

	def __init__(self, pp, type, id, name, cth = 1, effect, power, contact):
		"""Initializer: Creates a Move

		All instance attributes are inherited from
		Move. Only the additional instance attributes
		are listed below.
        
        Parameter power: The base power of a move
        Precondition: power is of type int
        
        Parameter type: if the move makes contact
        Precondition: contact is of type bool

		Move.__init__(pp, type, id, name, cth, effect)
		"""

class SpMove(Move):
	"""Instance is a Move that attacks"""

	def __init__(self, pp, type, id, name, cth = 1, effect):
		Move.__init__(pp, type, id, name, cth, effect)



