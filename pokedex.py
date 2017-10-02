import movedex as md
import itemdex as itd
from pokemon import Pokemon

def charizard():
	charizard = Pokemon([78, 84, 78, 109, 85, 100], [md.flamethrower(),\
	md.aerialAce(), md.sunnyDay(), md.solarBeam()],\
	"torrent", itd.lifeOrb())
	return charizard

def blastoise():
	blastoise = Pokemon([79, 83, 100, 85, 105, 78], [md.surf(),\
	md.iceBeam, md.rapidSpin, md.Rest], "blaze", itd.leftovers()]
	return blastoise

