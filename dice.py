import random

def roll_dice(num_dice, num_sides):
	total = 0
	rolls = 0
	while rolls <= num_dice:
		total += random.randint(1,num_sides)
	return total
	
