"""
LEGACY CODE
from effect import Effect
effects = {
	"alwaysHit":Effect("alwaysHit", "self"),
	"sunny":Effect("sunny", "battlefield"),
	"solarBeam":Effect("solarBeam", "one", 1, 2),
	"surf":Effect("surf", "three"),
	"freeze":Effect("freeze", "one", 0.1),
	"rapidSpin":Effect("rapidSpin", "battlefield"),
	"sharpAttack":Effect("sharpAttack", "self"),
	"doubleDig":Effect("doubleDig", "one"),
	"slpPowder":Effect("slpPowder", "one"),
}
"""
bf = None
e = None

from trainer import Trainer
effects = {
	"alwaysHit":alwaysHit(bf),
	"sunny"sunny(bf):,
	"solarBeam":solarBeam(bf),
	"surf":surf(bf),
	"freeze":freeze(bf),
	"rapidSpin"rapidSpin(bf):,
	"sharpAttack":sharpAttack(bf),
	"doubleDig":doubleDig(bf),
	"slpPowder":slpPowder(bf),
	}

def sunny(battlefield):
	battlefield.setWeather("sunny")
	return battlefield

def solarBeam(battlefield):
	pass

