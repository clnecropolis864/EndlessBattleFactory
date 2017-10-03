from move import Move, AtkMove, SpMove

def flamethrower():
	flamethrower = AtkMove(15, "fire", 1, "Flamethrower", 95, False, False)
	return flamethrower

def aerialAce():
	aerialAce = AtkMove(15, "flying", 2, "Aerial ace", "alwaysHit", 60, True)
	return aerialAce

def sunnyDay():
	sunnyDay = SpMove(5, "fire", 3, "Sunny Day", "sunny")
	return sunnyDay

def solarBeam():
	solarBeam = AtkMove(15, "grass", 4, "Solar Beam", "solarBeam", 120, False, False)
	return solarBeam

def surf():
	surf = AtkMove(15, "water", 5, "Surf", "surf", 90, False, False)
	return surf

def iceBeam():
	iceBeam = AtkMove(10, "ice", 6, "Ice Beam", "freeze", 90, False, False)
	return iceBeam

def rapidSpin():
	rapidSpin = AtkMove(40, "normal", 7, "Rapid Spin", "rapidSpin", 20, False)
	return rapidSpin

def rest():
	rest = SpMove(10, "psychic", 8, "Rest", "rest")

def swordsDance():
	swordsDance = SpMove(30, "normal", 9, "Swords Dance", "sharpAttack")

def powerWhip():
	powerWhip = AtkMove(10, "grass", 10, "Power Whip", .85, 120, True)

def earthquake():
	earthquake = AtkMove(10, "ground", 11, "Earthquake", "doubleDig", 100, True)

def sleepPowder():
	sleepPowder = AtkMove(15, "grass", 12, "Sleep Powder", "slpPowder", .75, 0, False, False)