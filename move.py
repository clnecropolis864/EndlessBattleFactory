import effectdex

class Move(object):
	"""Instance is move

	INSTANCE ATTRIBUTES:
	pp: pp of move 					[int]
	type: type of move 				[list]
	name: name of move 				[str]
	notes: usage of move 			[str]
	"""

	def __init__(self, pp, Type, name, effect = "none", notes = ""):
		"""Initializer: Creates a Move

        Parameter pp: The pp of a move
        Precondition: pp is of type int and is > 0

        Parameter type: The type of the move
        Precondition: type is of type list populated with str
        Precondition: len(type) is between 1 and 2

        Parameter name: The move name
        Precondition: name is of type str

        Parameter effect: The side effects of the move
        Precondition: effect is of object str
        Precindition: effect has the same value as a key in effectdex, to which
        	there is a corresponding effect

        Parameter notes: The details of a move's usage. i.e,
        	swords dance is for support, flamethrower is to
        	attack, etc. Used for random team generation purposes.
        Precondition: notes is of type str
        """

		self._pp = pp
		self._Type = Type
		self._name = name
		self._effect = effect
		self._notes = notes

	def __str__(self):
		"""Returns: Name of move"""
		return self._name

	def getNotes(self):
		return self._notes

	def effect(battlefield):
		"""Returns: changed battlefield

		Takes in a battlefield, modifies it according to the effect
		by using self.__effect as a key for the dict in effectdex.py,
		and returns it.

		Parameter val: The value. 0 for you, 1 for opponent
		Precondition: val is 0 or 1 and of type int
		"""

		effectdex.bf = battlefield
		effectdex.e = self._effect
		battlefield = effectdex.effects[self._effect.getKey()]
		return effectdex.bf



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
        Parameter effect: str will be passed into effectdex dict,
        Which calls a function.
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
		return self._power

	def getAccuracy(self):
		return self._cth

	def isPhysical(self):
		return self._physical

	def use(self, target):
		if target.getAbility() == "pressure":
			self._pp -= 2
		else:
			self._pp -= 1



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
		self._cth = cth

	def getType(self):
		return "SpMove"






"""
LEGACY CODE:
Move/pokemon typing now uses type str
Type effectiveness now calculated in calc.py, using strings
"""
class moveType(object):
	"""Instance is a type of move. Only used in move objects
	Just makes it easier to track type effectiveness
	"""

	def __init__(self, name, strengths, weaknesses, noEffect = ""):
		"""Initializer: Creates an instance of moveType

		Param name: The name of the type
		Precondition: name is of type str

		Param strengths: The things it's (offensively) good against
		Precondition: strengths a list with items of type str

		Param weaknesses: The thing's it's (offensively) bad against
		Precondition: weaknesses is a list with items of type str

		Param noEffect: The thing that it has no effect against
		Precondition: noEffect is of type str
		"""

		self.__name = name
		self.__strengths = strengths
		self.__weaknesses = weaknesses
		self.__noEffect = noEffect

	def getName():
		return self.__name

	def getStrengths():
		return self.__strengths

	def getWeaknesses():
		return self.__weaknesses

	def getNoEffect():
		return self.noEffect





