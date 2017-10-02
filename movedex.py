from move import Move, AtkMove, SpMove

def flamethrower():
	flamethrower = AtkMove(15, "fire", 1, "Flamethrower", 95, False)
	return flamethrower

def aerialAce():
	aerialAce = AtkMove(15, "flying", 2, "Aerial ace", "alwaysHit", 60, True)
	return aerialAce

def sunnyDay():
	sunnyDay = SpMove(5, "fire", 3, "Sunny Day", "sunny")
	return sunnyDay

def solarBeam():
	solarBeam = AtkMove(15, "grass", 4, "Solar Beam", "solarBeam", 120, False)
	return solarBeam