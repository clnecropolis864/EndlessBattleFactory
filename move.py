class Move(Object):
	"""Instance is move
	    
	INSTANCE ATTRIBUTES:
	pp: pp of move 					[int]
	type: type of move 				[str]
	id: move's unique id			[int]
	name: name of move 				[str]
	effect: any secondary effects	[str]
	"""

	def __init__(self, pp, type, id, name, effect = "none"):
		"""Initializer: Creates a Move
        
        Parameter pp: The pp of a move
        Precondition: pp is of type int
        
        Parameter type: The type of the move
        Precondition: type is of type str

        Parameter id: The pokemon's pokedex id
        Precondition: id is of type int

        Parameter name: The current pokemon on the trainer
        Precondition: name is of type str

        Parameter effect: Secondary effects of the move
        Precondition: effect is of type str
        """

		self.pp = pp
		self.type = type
		self.id = id
		self.name = name
		self.effect = effect

	def __str__():
		"""Returns: Name of move"""

		return name

class AtkMove(Move):
	"""Instance is a Move that attacks

	ADDITIONAL INSTANCE ATTRIBUTES:
	cth: chance to hit					[float]
	power: base power of move 			[int]
	physical: if the move is physical 	[bool]
	contact: if move makes contact 		[bool] 
	"""

	def __init__(self, pp, type, id, name, effect = "none", cth = 1, power, physical = True, contact):
		"""Initializer: Creates a Move

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
        
        Parameter type: if the move makes contact
        Precondition: contact is of type bool
        """

		Move.__init__(pp, type, id, name, effect)
		self.cth = cth
		self.power = power
		self.physical = physical
		self.contact = contact

		

class SpMove(Move):
	"""Instance is a Move that doesn't attack"""

	def __init__(self, pp, type, id, name, cth = 1, effect = "none"):
		Move.__init__(pp, type, id, name, cth, effect)



