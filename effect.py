class Effect(object):
	"""Instance is the effect of a move

	INSTANCE ATTRIBUTES:
	detail	[str]
	target 	[str]
	chance	[float]
	value	[float]
	"""

	def __init__(self, detail, target, chance = 1, value = 0):
		self.__detail = detail
		self.__target = target
		self.__chance = chance
		self.__value = value