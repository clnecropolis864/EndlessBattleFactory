import copy

class testObject(object):

	def __init__(self, val):
		self.val = val

	def getVal(self):
		return self.val
	def setVal(self, val):
		self.val = val

test = testObject(1)

test2 = test
test3 = copy.copy(test)
test2.setVal(2)

print test.getVal()
print test2.getVal()
print test3.getVal()
