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

from trainer import Trainer
import random
from runner import Battlefield
bf = Battlefield()
def setBf(battlefield):
	bf = battlefield


def alwaysHit():
	pass
def sunny():
	battlefield.setWeather("sunny")
def solarBeam():
	pass
def surf():
	pass
def freeze():
	if random.random() < 0.1:
		battlefield.currentlyOut(1).setStatus("freeze")

effects = {
	"alwaysHit":alwaysHit(bf),
	"sunny":sunny(bf),
	"solarBeam":solarBeam(bf),
	"surf":surf(bf),
	"freeze":freeze(bf),
	"rapidSpin":rapidSpin(bf),
	"sharpAttack":sharpAttack(bf),
	"doubleDig":doubleDig(bf),
	"slpPowder":slpPowder(bf),
	}
