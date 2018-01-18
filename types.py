from move import moveType

normal = moveType("normal", [], ["rock", "steel"], ["ghost"])
fire = moveType("fire", ["grass", "ice", "bug", "steel"], ["fire", "water", "rock", "dragon"])
water = moveType("water")
electric = moveType("electric")
ice = moveType("ice")