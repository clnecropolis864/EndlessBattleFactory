def damageCalc(level, move, atk, defense, modifier):
	"""Returns: Damage dealt

	Standard damage calculator.

	Param level: level is the level of the pokemon
	Precondition: level is an int from 1-100

	Param move: The move in question
	Precondition: move is of type Move

	Param atk: The attack of the attacking pokemon
	Precondition: atk is an int and is > 0

	Param def: The defense of the defending pokemon
	Precondition: def is of type int and is > 0

	Param modifier: An array of all the multipliers
	of the move (such as type effectivenss). Has
	format [weather, crit, random, STAB, type, burn, other]
	Precondition: modifier is of type list with length 7,
	and all default values are 1
	"""

	power = move.getPower()
	#power = move
	modifierTotal = 1

	for x in modifier:
		modifierTotal *= x

	return int((((2.0 * level / 5 + 2) * power * atk / defense) / 50\
	 + 2) * modifierTotal)

def typeChart(attack, defense):
	multiplier = 1.0

	for x in defense:

		if attack == "normal":
			if x == "ghost":
				multiplier *= 0
			elif (x == "rock") or (x == "steel"):
				multipler /= 2:

		elif attack == "fire":
			if x == "" #finish