class Item(object):
	"""Instance is an item
	    
	INSTANCE ATTRIBUTES:
	name: The name
	"""

	def __init__(self, name):
		"""Initializer: Creates an item
        
        Parameter name: The name
        Precondition: name is of type str
        """

		self.name = name