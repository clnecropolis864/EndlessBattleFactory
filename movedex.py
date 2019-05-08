from move import Move, AtkMove, SpMove
from types import *

#AtkMove constructor:
#(self, pp, Type, name, notes = "", effect = "none", power = 0, cth = 1, physical = True, contact = True)
def flamethrower():
	notes = "Offense/RawDamage"
	flamethrower = AtkMove(15, "fire", "Flamethrower", notes, "burn", 95, 1, False, False)
	return flamethrower

def aerialAce():
	aerialAce = AtkMove(15, "flying", "Aerial ace", 60, True, True, "alwaysHit")
	return aerialAce

def sunnyDay():
	sunnyDay = SpMove(5, "fire", "Sunny Day", "sunny")
	return sunnyDay

def solarBeam():
	solarBeam = AtkMove(15, "grass", "Solar Beam", 120, False, "solarBeam")
	return solarBeam

def solarBeamAtk():
	solarBeamatk = AtkMove(15, "grass", "Solar Beam", 120, )

def surf():
	surf = AtkMove(15, "water", "Surf", 90, False, "surf")
	return surf

def iceBeam():
	iceBeam = AtkMove(10, "ice", "Ice Beam", 90, False, "freeze")
	return iceBeam

def rapidSpin():
	rapidSpin = AtkMove(40, "normal", "Rapid Spin", 20, False, "rapidSpin")
	return rapidSpin

def rest():
	rest = SpMove(10, psychic, "Rest", "rest")

def swordsDance():
	swordsDance = SpMove(30, "normal", "Swords Dance", "sharpAttack")

def powerWhip():
	powerWhip = AtkMove(10, "grass", "Power Whip", .85, 120)

def earthquake():
	earthquake = AtkMove(10, "ground", "Earthquake", 100, "doubleDig")

def sleepPowder():
	sleepPowder = AtkMove(15, "grass", "Sleep Powder", .75, 0, False, "slpPowder")
