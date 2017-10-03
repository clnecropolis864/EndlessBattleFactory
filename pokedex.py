import movedex as md
import itemdex as itd
from pokemon import Pokemon

def charizard():
	charizard = Pokemon([78, 84, 78, 109, 85, 100], [md.flamethrower(),\
	md.aerialAce(), md.sunnyDay(), md.solarBeam()],\
	"blaze", itd.lifeOrb())
	return charizard

def blastoise():
	blastoise = Pokemon([79, 83, 100, 85, 105, 78], [md.surf(),\
	md.iceBeam, md.rapidSpin, md.Rest], "torrent", itd.leftovers())
	return blastoise

def venusaur():
	venusaur = Pokemon([80, 82, 83, 100, 100, 80], [md.swordsDance(),\
		md.powerWhip(), md.earthquake(), md.sleepPowder()],\
		"chlorophyll", itd.leftovers())
	return venusaur