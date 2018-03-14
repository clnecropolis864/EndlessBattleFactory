import battle
import pokedex as dex
import trainer
from pokemon import Pokemon
import copy
import pygame as pg
import sys
from textbox import TextInput
from graphicsClasses import *

#Initializers
pg.init()
pg.font.init()

#Screen
size = width, height = 640, 480
screen = pg.display.set_mode(size)

#Misc
pg.display.set_caption("EndlessBattleFactory")
textinput = TextInput()
clock = pg.time.Clock()
name = ""


def menu():
	"""Loads the Main Menu"""
	pokemonSelected = 0

	venuS = Clickable(pg.image.load("sprites/003.png"), PopUp(42, 42, 3))
	chariS = Clickable(pg.image.load("sprites/006.png"), PopUp(42, 42, 3))
	blastS = Clickable(pg.image.load("sprites/009.png"), PopUp(42, 42, 3))

	options = [venuS, chariS, blastS]

	lastClick = (0, 0)

	while pokemonSelected < 3:
		#Preliminaries 
		screen.fill((225, 225, 225))
		font = pg.font.SysFont('Roboto', 30)
		events = pg.event.get()

		# Feed it with events every frame
		textinput.update(events)
		# Blit its surface onto the screen
		screen.blit(textinput.get_surface(), (0, 50))

		#Test Box
		"""
		rect = pg.draw.rect(screen, (100, 100, 100), (50, 50, 50, 50))
		pg.display.flip()
		"""

		#Enter name
		enterName = font.render('Enter your name:', False, (100, 100, 100))
		screen.blit(enterName, (0, 0))

		if textinput.enter():
			print (textinput.get_text())
			name = textinput.get_text()

		#"Pick a pokemon"
		pickPokemon = font.render('Pick a pokemon:', False, (100, 100, 100))
		screen.blit(pickPokemon, (0, 100))

		#Sprites
		r1 = screen.blit(options[0].surface, (0, 150))
		r2 = screen.blit(options[1].surface, (options[0].surface.get_width(), 150))
		r3 = screen.blit(options[2].surface, (options[0].surface.get_width() + options[1].surface.get_width(), 150))

		optionsR = [r1, r2, r3]

		for event in events:
			if event.type == pg.QUIT:
				# Close window and exit program
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				print(event.pos)
				lastClick = event.pos
				for i in range(len(optionsR)):
					if optionsR[i].collidepoint(event.pos):
						print("hi!")
						options[i].stored.draw()
						options[i].active = True
						screen.blit(options[i].stored.surface, event.pos)
					else:
						options[i].active = False

		for pokemon in options:
			if pokemon.active:
				pokemon.stored.draw()
				screen.blit(pokemon.stored.surface, lastClick)

		pg.display.update()


		clock.tick(60)

def start():
	"""Loads the battle"""
	Charizard = dex.charizard()
	Venusaur = dex.venusaur()
	Blastoise = dex.blastoise()

	party = [dex.charizard(), dex.venusaur(), dex.blastoise()]
	you = trainer.Trainer(name, party)

	oppName = "John"
	opp = trainer.AITrainer(oppName)
	oppParty = opp.buildTeam()


	battle.run(you, opp)


menu()
start()



