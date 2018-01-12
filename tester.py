import calc
import trainer
import pokedex as dex
modifier = [1, 1, 1, 1.5, 2, 1, 1]

#print calc.damageCalc(30, 150, 71, 45, modifier)

party = [dex.charizard(), dex.venusaur(), dex.blastoise()]
you = trainer.Trainer("Chuck", party)
print(type(you))