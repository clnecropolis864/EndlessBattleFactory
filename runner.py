import battle
import pokedex as dex
import trainer
from pokemon import Pokemon
import copy
import pygame as pg
import sys
from textbox import TextInput

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
	pokemonSelected = 0

	while True:
		#Preliminaries 
		screen.fill((225, 225, 225))
		font = pg.font.SysFont('Roboto', 30)
		events = pg.event.get()

		for event in events:
			if event.type == pg.QUIT:
				# Close window and exit program
				sys.exit()

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
		venuS = pg.image.load("sprites/003.png")
		screen.blit(venuS, (0, 150))
		chariS = pg.image.load("sprites/006.png")
		screen.blit(chariS, (venuS.get_width(), 150))
		blastS = pg.image.load("sprites/009.png")
		screen.blit(blastS, (venuS.get_width() + chariS.get_width(), 150))

		pg.display.update()

		if pokemonSelected > 2:
			break

		clock.tick(60)

def start():
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



