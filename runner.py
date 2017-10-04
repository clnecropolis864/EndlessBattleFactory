import battle
import pokedex as dex
from trainer import Trainer, AITrainer
from pokemon import Pokemon
import copy

name = raw_input("What's your name?")
print name

print "Pick 3 Pokemon:"
Charizard = dex.charizard()
Venusaur = dex.venusaur()
Blastoise = dex.blastoise()

party = [dex.charizard(), dex.venusaur(), dex.blastoise()]

you = Trainer(name, party)

oppName = "John"
oppParty = copy.copy(party)

opp = AITrainer(oppName, oppParty)

battle.run(you, opp)


