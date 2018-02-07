import pygame as pg
import pygame.locals as pl

class Clickable:

	def __init__(self, surface, stored):
		"""Initializer: Creates a Clickable object

		Basically a surface that creates something when clicked.
		Stores that something, then creates/destroys it
		accordingly."""
		self.surface = surface
		self.stored = stored

	def getSurface():
		return self.surface
	def getStored():
		return self.stored

class PopUp:

	def __init__ (self, width, height, numElements = 1):
		self.width = width
		self.height = height
		self.numElements = numElements

		self.surface = pg.Surface((width, height))
		self.surface.set_alpha(0)
		self.x, self.y = pg.mouse.get_pos()

		self.elements = []
		self.labels = []

		i = 0
		while i < numElements:
			e = pg.Surface((width, height/3))
			self.elements.append(e)
			i+=1

	def draw(self):
		#Puts various elements in their place
		for i in range(self.elements):
			self.surface.blit(self.elements[i], (self.x, self.y + 
				(self.height / numElements) * i))

	def update(self, events):
		for event in events:
			if event.type == pg.MOUSEBUTTONDOWN:
				if self.surface.get_rect().collidepoint(event.pos): #If click within boundaries
					return True
				return False

	def setLabel(i, label):
		self.labels[i] = label
