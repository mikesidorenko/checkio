class Warrior:
	def __init__(self):
		self.health = 50
		self.attack = 5
		self.is_alive = True

class Knight(Warrior):
	def __init__(self):
		super().__init__()   # inherit all __init__ attrs from Warrior class
		self.attack = 7      # reassign attack attr

def fight(unit_1, unit_2):
	while unit_1.is_alive and unit_2.is_alive:             # resume fight condition
		unit_2.health = unit_2.health - unit_1.attack      # unit_1 attacks
		unit_2.is_alive = unit_2.health > 0                #kill when <= 0
		if unit_2.is_alive:                                #check if 2nd alive
			unit_1.health = unit_1.health - unit_2.attack  #unit_2 attacks
			unit_1.is_alive = unit_1.health > 0            #kill when <= 0
		
	return unit_1.is_alive    #true if 1st wins, otherwise false