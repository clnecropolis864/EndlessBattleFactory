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
	"""Returns: Damage multiplier based on typing

	Returns the "type" value in modifier

	Param attack: The attacking move
	Precondition: Attack os if type str

	Param defense: The defensive type of the recipient pokemon
	Precondition: defense is of type list, len 2, containing str objects
	"""
	multiplier = 1.0

	for x in defense:

		if attack == "normal":
			if x == "ghost":
				multiplier *= 0
			elif (x == "rock") or (x == "steel"):
				multipler *= 0.5

		elif attack == "fire":
			if (x == "fire") or (x == "water") or ("x == rock") or (x == " dragon"):
				multiplier *= 0.5
			elif (x == "grass") or (x == "ice") or (x == "bug") or (x == "steel"):
				multiplier *= 2

		elif attack =="water":
			if (x == "water") or (x == "grass") or (x == "dragon"):
				multiplier *= 0.5
			elif (x == "fire") or (x == "ground") or (x == "rock"):
				multiplier *= 2

		elif attack == "electric":
			if (x == "ground"):
				multiplier *= 0
			elif (x == "electric") or (x == "grass") or (x == "dragon"):
				multiplier *= 0.5
			elif (x == "water") or (x == "flying"):
				multiplier *= 2

		elif attack == "grass":
			if (x == "fire") or (x == "grass") or (x == "poison") or (x == "flying") or (x == "bug") or (x == "dragon"):
				multiplier *= 0.5
			elif (x == "water") or (x == "ground") or (x == "rock"):
				multiplier *= 2

		elif attack == "ice":
			if (x == "fire") or (x == "water") or (x == "ice") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "grass") or (x == "ground") or (x == "flying") or (x == "dragon"):
				multiplier *= 2

		elif attack == "fighting":
			if (x == "ghost"):
				multiplier *= 0
			elif (x == "poison") or (x == "flying") or (x == "psychic") or (x == "bug"):
				multiplier *= 0.5
			elif (x == "normal") or (x == "ice") or (x == "rock") or (x == "dark") or (x == "steel"):
				multiplier *= 2

		elif attack == "poison":
			if (x == "steel"):
				multiplier *= 0
			elif (x == "poison") or (x == "ground") or (x == "rock") or (x == "ghost"):
				multiplier *= 0.5
			elif (x == "grass"):
				multiplier *= 2

		elif attack == "ground":
			if (x == "flying"):
				multiplier *= 0
			elif (x == "grass") or (x == "bug"):
				multiplier *= 0.5
			elif (x == "fire") or (x == "electric") or (x == "poison") or (x == "rock") or (x == "steel"):
				multiplier *= 2

		elif attack == "flying":
			if (x == "electric") or (x == "rock") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "grass") or (x == "fighting") or (x == "bug"):
				multiplier *= 2

		elif attack == "psychic":
			if (x == "dark"):
				multiplier *= 0
			elif (x == "psychic") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "fighting") or (x == "poison"):
				multiplier *= 2

		elif attack == "bug":
			if (x == "fire") or (x == "fighting") or (x == "poison") or (x == "flying") or (x == "ghost") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "grass") or (x == "psychic") or (x == "dark"):
				multiplier *= 2

		elif attack == "rock":
			if (x == "fighting") or (x == "ground") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "fire") or (x == "ice") or (x == "flying") or (x == "bug"):
				multiplier *= 2

		elif attack == "ghost":
			if (x == "normal"):
				multiplier *= 0
			elif (x == "dark"):
				multiplier *= 0.5
			elif (x == "psychic") or (x == "ghost"):
				multiplier *= 2

		elif attack == "dragon":
			if (x == "steel"):
				multiplier *= 0.5
			elif (x == "dragon"):
				multiplier *= 2

		elif attack == "dark":
			if (x == "fighting") or (x == "dark"):
				multiplier *= 0.5
			elif (x == "psychic") or (x == "ghost"):
				multiplier *= 2

		elif attack == "steel":
			if (x == "fire") or (x == "water") or (x == "electric") or (x == "steel"):
				multiplier *= 0.5
			elif (x == "ice") or (x == "rock"):
				multiplier *= 2


	return multiplier