import battle
import pokedex as dex
from trainer import Trainer, AITrainer
from pokemon import Pokemon
import copy
import pygame as pg
import sys

pg.init()
pg.font.init()
size = width, height = 640, 480
screen = pg.display.set_mode(size)
pg.display.set_caption("EndlessBattleFactory")

while True:
	active = False
	nameInput = pg.Rect(100, 100, 140, 32)
	for event in pg.event.get():

		if event.type == pg.QUIT:
			# Close window and exit program
			sys.exit()

	rect = pg.draw.rect(screen, (100, 100, 100), (50, 50, 50, 50))
	pg.display.flip()

	font = pg.font.SysFont('Roboto', 30)
	pickPokemon = font.render('Pick a pokemon:', False, (100, 100, 100))
	screen.blit(pickPokemon, (0, 0))
	pg.display.update()

	Charizard = dex.charizard()
	Venusaur = dex.venusaur()
	Blastoise = dex.blastoise()

	party = [dex.charizard(), dex.venusaur(), dex.blastoise()]

	you = Trainer(name, party)

	oppName = "John"
	oppParty = copy.copy(party)

	opp = AITrainer(oppName, oppParty)

	battle.run(you, opp)


