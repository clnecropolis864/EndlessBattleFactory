#The same as runner, but uses command line window instead of GUI
#Easier to test existing code


import battle
import pokedex as dex
import trainer
from pokemon import Pokemon
import copy

print("WTF")

def start():
    """Loads the battle"""
    Charizard = dex.charizard()
    Venusaur = dex.venusaur()
    Blastoise = dex.blastoise()

    party = [dex.charizard(), dex.venusaur(), dex.blastoise()]
    you = trainer.Trainer(name, party)

    oppName = "John"
    oppParty = [dex.charizard(), dex.venusaur(), dex.blastoise()]
    opp = trainer.AITrainer(oppName)
    #oppParty = opp.buildTeam()


    battle.run(you, opp)

start()

