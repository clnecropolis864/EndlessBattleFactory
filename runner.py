import battle
import pokedex as dex
from trainer import Trainer
from pokemon import Pokemon

name = input("What's your name?")

print "Pick 3 Pokemon:"
Charizard = Pokemon(dex.Charizard[0], dex.Charizard[1], dex.CharizardItem[2])
Venusaur = Pokemon(dex.Venusaur[0], dex.Venusaur[1], dex.VenusaurItem[2])
Blastoise = Pokemon(dex.Blastoise[0], dex.Blastoise[1], dex.BlastoiseItem[2])

party = [Charizard, Venusaur, Blastoise]

you = Trainer(name, party)



