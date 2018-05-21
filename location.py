import libtcod
def describe_location(my_location):
	libtcod.console_clear(0)
        libtcod.console_print(0,1,1, location.name)
	libtcod.console_print(0,1,1, location.area)

	item_count = 1
	line_count = 4
	for item in location.items:
		while item_count >= 10:
			print_line = item_count + line_count
			libtcod.console_print(0,1,print_line, item.name)
			libtcod.console_print(0,15,print_line, item.base_value)
			item_count += 1

	libtcod.console_flush()

def find_location(party,district):
	my_location = party.location
	for area in district.areas:
		for location in area.locations:
			if location.name == my_location:
				my_location = location
	#print my_location.name
	return my_location

def turn(party,world):
	my_location = find_location(party,world)
	describe_location(my_location)
