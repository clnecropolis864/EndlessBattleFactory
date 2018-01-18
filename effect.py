class Effect(object):
	"""Instance is the effect of a move

	INSTANCE ATTRIBUTES:
	key		[str]
	target 	[list] (str)
	chance	[float]
	value	[float]
	"""

	def __init__(self, key, target, chance = 1, value = 0):
		self.__key = detail
		self.__target = target
		self.__chance = chance
		self.__value = value

	def getTarget(self):
		return target

	def getKey(self):
		return self.__key