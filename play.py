
import libtcodpy as libtcod
from operator import itemgetter, attrgetter
#from char import *
#from location import *
from namegen import *
from dialogue import *
#import time
from world import *
import shelve

#player = None
#game = None
#world = None

def save_game():
	file = shelve.open('savegame', 'n')
        file['game'] = game

        file['world'] = world
        file['player_party'] = player_party
        #file['game'] = game
        #print player_party
        #print world
        file.close()

def load_game():
	#global player_party, world
	file = shelve.open('savegame', 'r')
	#print file
        game = file['game']

    	world = file['world']
	#print world
    	player_party = file['player_party']
	#print player_party

	file.close()
	#print 'close'
	return game, world, player_party

#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

player_party = []
world = []
playing_game = True

class Game:
	def __init__(self,running,starting):
	        self.running = running
	        self.starting = starting
	 
 
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'CYBERHOBO', False)
libtcod.sys_set_fps(30)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

def play_turn(party,world,playing_game,location):
	location = find_location(player_party,world)
	turn_finished = False
	while turn_finished == False and playing_game == True:
		location = turn(party,world,turn_finished,location)
		turn_finished == True

def startup():
	global player_party
	global world

       	#startup
       	options = []
       	libtcod.console_print(0, 1, 1, "CYBERHOBO")
       	libtcod.console_print(0, 1, 5, "[n]ew game")
	game_found = False
	try:
		game, world, player = load_game()
	        libtcod.console_print(0, 1, 6, "[l]oad game")
		#game_found = True
	except:
		game_found = False
        libtcod.console_print(0, 1, 7, "[q]uit")

       	libtcod.console_flush()
       	key = libtcod.console_check_for_keypress()
       	if key.c == ord('n'):
       	        return 1
	elif key.c == ord('l') and game_found == False:
		return 2
	elif key.c == ord('q'):
		return 3
 

def describe_location(my_location):
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1, location.name)
        libtcod.console_print(0,1,2, location.area)

        item_count = 1
        line_count = 4
        for item in location.items:
		print item.name
                print_line = item_count + line_count
                libtcod.console_print(0,1,print_line, item.name)
                libtcod.console_print(0,15,print_line, item.base_value)
                item_count += 1

        libtcod.console_flush()



def find_area(party,city):
	my_area = party.area
	for area in city.areas:
		if area.name == area:
			my_area = area
	return area

def find_location(party,city):
        my_location = party.location 
        for area in city.areas:
                for location in area.locations:
                        if location.name == my_location and location.items == my_location.items and location.actors == my_location.actors:
				if len(location.rooms) == 0:
                                	my_location = location
				if len(location.rooms) >= 1:
					for room in location.rooms:
						if room == my_location:
							my_location == room
        #print my_location.name
        return my_location

def num_to_letter(num):
	if num == 1:
		letter = 'a'
        elif num == 2:
                letter = 'b'
        elif num == 3:
                letter = 'c'
        elif num == 4:
                letter = 'd'
        elif num == 5:
                letter = 'e'
        elif num == 6:
                letter = 'f'
        elif num == 7:
                letter = 'g'
        elif num == 8:
                letter = 'h'
        elif num == 9:
                letter = 'i'
        elif num == 10:
                letter = 'j'
        elif num == 11:
                letter = 'k'
        elif num == 12:
                letter = 'l'
        elif num == 13:
                letter = 'm'
        elif num == 14:
                letter = 'n'
        elif num == 15:
                letter = 'o'
        elif num == 16:
                letter = 'p'
        elif num == 17:
                letter = 'q'
        elif num == 18:
                letter = 'r'
        elif num == 19:
                letter = 's'
        elif num == 20:
                letter = 't'
        elif num == 21:
                letter = 'u'
        elif num == 22:
                letter = 'v'
        elif num == 23:
                letter = 'w'
        elif num == 24:
                letter = 'x'
        elif num == 25:
                letter = 'y'
        elif num == 26:
                letter = 'z'
        elif num == 27:
                letter = 'A'
        elif num == 28:
                letter = 'B'
        elif num == 29:
                letter = 'C'
        elif num == 30:
                letter = 'D'
        elif num == 31:
                letter = 'E'
        elif num == 32:
                letter = 'F'
        elif num == 33:
                letter = 'G'
        elif num == 34:
                letter = 'H'
        elif num == 35:
                letter = 'I'
        elif num == 36:
                letter = 'J'
        elif num == 37:
                letter = 'K'
        elif num == 38:
                letter = 'L'
        elif num == 39:
                letter = 'M'
        elif num == 40:
                letter = 'N'
        elif num == 41:
                letter = 'O'
        elif num == 42:
                letter = 'P'
        elif num == 43:
                letter = 'Q'
        elif num == 44:
                letter = 'R'
        elif num == 45:
                letter = 'S'
        elif num == 46:
                letter = 'T'
        elif num == 47:
                letter = 'U'
        elif num == 48:
                letter = 'V'
        elif num == 49:
                letter = 'X'
        elif num == 50:
                letter = 'Y'
        elif num == 51:
                letter = 'Z'
        elif num == 52:
                letter = '1'
        elif num == 53:
                letter = '2'
        elif num == 54:
                letter = '3'
        elif num == 55:
                letter = '4'
        elif num == 56:
                letter = '5'
        elif num == 57:
                letter = '6'
	elif num == 58:
		letter = '7'
	elif num == 59:
		letter = '8'
	elif num == 60:
		letter = '9'
	elif num == 61:
		letter = '0'
	elif num == 62:
		letter = '!'
	elif num == 63:
		letter = '@'
	elif num == 64:
		letter = '#'
	elif num == 65:
		letter = '&'
	elif num == 66:
		letter = '('
	elif num == 67:
		letter = ")"
	elif num == 68:
		letter = "&"
	elif num == 69:
		letter = ','
	elif num == 70:
		letter = '.'
	elif num == 71:
		letter = '/'
	elif num == 72:
		letter = ';'
	elif num == 73:
		letter = '"'
	elif num == 74:
		letter = ':'
	elif num == 75:
		letter = '?'
	elif num == 78:
		letter = '>'
	elif num == 79:
		letter = '<'
	elif num == 80:
		letter = ']'
	elif num == 81:
		letter = '['
	elif num == 82:
		letter = '}'
	elif num == 83:
		letter = '{'
	elif num == 84:
		letter = "~"
	elif num == 85:
		letter = '|'
	elif num == 86:
		letter = '-'
	elif num == 87:
		letter = '_'
	elif num == 88:
		letter = '='
	elif num == 89:
		letter = '+'
	elif num == 90:
		letter = '`'



	else:
		letter = 'error'

	return letter

def show_areas(party,world,start):
	libtcod.console_clear(0)
	my_area = find_area(party,world)
	line_count = 1
	libtcod.console_print(0,1,line_count,world.name)
	line_count += 2
	areas = []
	for area in world.areas:
		areas.append(area)
        count = 1
        options = []
        letter = " "
        for area in areas:
                line_count= count + 5
                #print count
                letter = num_to_letter(count)
                option = [letter,area]
                options.append(option)
                #print location.name
                #print my_location.name
                if area.name == my_area.name:
                        string = '[' + letter + '] ' + area.name + "*"
                        width = len(string)
                        libtcod.console_set_default_foreground(0, libtcod.green)
                        libtcod.console_print(0,1,line_count, '[' + letter + '] ' + area.name)
                        libtcod.console_flush()
    
   	                libtcod.console_set_default_foreground(0, libtcod.white)

                else:
                        libtcod.console_print(0,1,line_count, '[' + letter + '] ' + area.name)
                count += 1
        offset_x = 5
        offset_y = 30
        rows = 16
        columns = 16
        row_count = 1
        column_count = 1
        while column_count <= columns:
                while row_count <= rows:
                        libtcod.console_set_char_background(0, column_count + offset_y, row_count + offset_x, libtcod.darkest_grey, flag=libtcod.BKGND_SET)
                        row_count += 1
                row_count = 1
                column_count += 1
	area_count = 1
	areas = []
        for area in world.areas:
		letter = num_to_letter(area_count)
		this_area = [letter,area]
		areas.append(this_area)
		area_count += 1
	for area in areas:
                #print option[1].x
                #print option[1].y
                libtcod.console_print(0,offset_y + area[1].y,offset_x + area[1].x, area[0])
                if party.x == option[1].x and party.y == option[1].y:
                        libtcod.console_set_char_background(0, area[1].y + offset_y, area[1].x + offset_x, libtcod.dark_green, flag=libtcod.BKGND_SET)
                else:
                        libtcod.console_set_char_background(0, area[1].y + offset_y, area[1].x + offset_x, libtcod.dark_grey, flag=libtcod.BKGND_SET)

	libtcod.console_flush()
	finished_area = False
	while finished_area == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('*'):
			return True
		for area in areas:
			if key.c == ord(area[0]):
				party.area = area[1]
				party.x= my_area.x
				party.y = my_area.y
				return True
def faction_attack(party,world,faction,attacker,my_location):
	libtcod.console_clear(0)
	libtcod.console_print(0,1,1,"A group of " + str(len(attacker.members)) + " " + faction.name + " approach you:")
        libtcod.console_print(0,1,2,'Get ready to die!')

        libtcod.console_print(0,1,6,"[f]ight!")
	libtcod.console_flush()
	decision = False
	while decision == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('f'):
	                decision = battle(party,attacker,my_location,world,True)

# t r a v e l
def travel(party,world,start):
	my_location = find_location(party,world)
	if my_location.parent_location != None:
		my_location = my_location.parent_location
	my_area = find_area(party,world)
        libtcod.console_clear(0)

	def show_locations():
	        libtcod.console_print(0,1,1, my_location.area)

		locations = []
		for location in my_area.locations:
			locations.append(location)
		count = 1
		options = []
		letter = " "
		for location in locations:
			line = count + 5
			print count
			letter = num_to_letter(count)
	                option = [letter,location]
			options.append(option)
			print location.name
			print my_location.name
			if location.name == my_location.name and my_location.items == location.items and my_location.actors == location.actors:
				string = '[' + letter + '] ' + location.name + "*"
				width = len(string)
				libtcod.console_set_default_foreground(0, libtcod.green)
				if count <= 40:
					libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
				elif count >= 41 and count <= 61:
					libtcod.console_print(0,30,line-21, '[' + letter + '] ' + location.name)
				elif count >= 62:
					libtcod.console_print(0,60,line-42, '[' + letter + '] ' + location.name)
				libtcod.console_flush()
	                    	libtcod.console_set_default_foreground(0, libtcod.white)
			#elif len(location.rooms) >= 1:
			#	found_room = False
			#	while found_room == False:
			#		for room in location.rooms:
			#			if room.name == 'Your Apartment':
                        #        			libtcod.console_set_default_foreground(0, libtcod.yellow)
                        #        			if count <= 40:
                        #        	        		libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                        #        			elif count >= 41 and count <= 61:
                        #        	        		libtcod.console_print(0,30,line-21, '[' + letter + '] ' + location.name)
                        #        			elif count >= 62:
                        #        	        		libtcod.console_print(0,60,line-42, '[' + letter + '] ' + location.name)
                        #        			libtcod.console_flush()
                        #        			libtcod.console_set_default_foreground(0, libtcod.white)
			#				found_room = True
			#		if found_room == False:
                        #        		if count <= 40:
                        #        		        libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                        #        		elif count >= 41 and count <= 61:
                        #        		        libtcod.console_print(0,30,line-21, '[' + letter + '] ' + location.name)
                        #        		elif count >= 62:
                        #        		        libtcod.console_print(0,60,line-42, '[' + letter + '] ' + location.name)
			else:
				if count <= 40:
					libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
				elif count >= 41 and count <= 61:
					libtcod.console_print(0,30,line-21, '[' + letter + '] ' + location.name)
				elif count >= 62:
                                        libtcod.console_print(0,60,line-42, '[' + letter + '] ' + location.name)

			count += 1
		return options
	options = show_locations()
	def show_map():
		offset_x = 5
		offset_y = 30
		rows = 16
		columns = 16
		row_count = 1
		column_count = 1
		while column_count <= columns:
			while row_count <= rows:
				libtcod.console_set_char_background(0, column_count + offset_y, row_count + offset_x, libtcod.darkest_grey, flag=libtcod.BKGND_SET)
				row_count += 1
			row_count = 1
			column_count += 1
		for option in options:
			#print option[1].x
			#print option[1].y
			libtcod.console_print(0,offset_y + option[1].y,offset_x + option[1].x, option[0])
			if my_location.x == option[1].x and my_location.y == option[1].y:
		                libtcod.console_set_char_background(0, option[1].y + offset_y, option[1].x + offset_x, libtcod.dark_green, flag=libtcod.BKGND_SET)
			else:
				libtcod.console_set_char_background(0, option[1].y + offset_y, option[1].x + offset_x, libtcod.dark_grey, flag=libtcod.BKGND_SET)
		libtcod.console_flush()
	show_map()
        action = False
        while action == False:
                libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
		for option in options:
			#print option[0]
                	if key.c == ord(option[0]):
                        	#print 'option a'
				party.location = option[1]
				action = True
		if key.c == ord('/'):
			finished = False
			while finished == False:
				action = show_areas(party,world,start)
				show_map()
				options = show_locations()
				action = False
				finished = True
				#return action

	#get distance to destination
	if start.x >= party.location.x + 1:
		x_distance = start.x - party.location.x
	elif start.x <= party.location.x:
		x_distance = party.location.x - start.x
        if start.y >= party.location.y + 1:
                y_distance = start.y - party.location.y
        elif start.y <= party.location.y:
                y_distance = party.location.y - start.y
	distance = x_distance + y_distance

	print action
	if action == True:
		#check who cant walk
		cant_walk = []
		for member in party.members:
			if member.health.current_stamina <= 0 and member.combat_status.knocked_down == False:
				member.combat_status.knocked_down = True
				cant_walk.append(member)
			elif member.combat_status.knocked_down == True and member.health.current_stamina >= 1:
				member.combat_status.knocked_down = False
				member.health.current_stamina -= 5
				if member.health.current_stamina <= 0:
					member.health.current_stamina = 0
                        elif member.combat_status.knocked_down == True and member.health.current_stamina <= 0:
				cant_walk.append(member)

		#check who can drag
		can_drag = []
		for member in party.members:
			 if member.combat_status.knocked_down == False:
				can_drag.append(member)
		
		#do we have to drag anyone
		dragging = []
		print len(cant_walk)
		if len(cant_walk) >= 1 and len(can_drag) >= 1:
			for member in cant_walk:
				libtcod.console_clear(0)
				libtcod.console_print(0,1,1, member.fname + ' ' + member.lname + " can't walk.")
				libtcod.console_print(0,1,3, "Who will drag them?")
				line_count = 5
				member_count = 1
				options = []
				for member in can_drag:
					letter = num_to_letter(member_count)
					option = [letter,member]
					options.append(option)
					member_count += 1
				for option in options:
					libtcod.console_print(0,1,line_count, '[' + option[0] + '] ' + option[1].fname + ' ' + option[1].lname)
					line_count += 1
				libtcod.console_flush()
				choice_made = False
				while choice_made == False:
					key = libtcod.console_check_for_keypress()
					for option in options:
						if key.c == ord(option[0]):
							drag = [option[1],member]
							dragging.append(drag)
							choice_made = True
		elif len(cant_walk) >= 1 and len(can_drag) == 0:
                        libtcod.console_clear(0)
                        libtcod.console_print(0,1,1, "You cannot travel.")
                	libtcod.console_print(0,1,3, "[c]ontinue")
                        libtcod.console_flush()
                        choice_made = False
	                while choice_made == False:
				key = libtcod.console_check_for_keypress()
				if key.c == ord('c'):
					break
		
		#check for angry factions
		my_area = find_area(party,world)
		angry_factions = []
		for organization in my_area.organizations:
			if organization.player_reputation <= -20:
				angry_factions.append(organization)

		if len(angry_factions) >= 1:
			roll = random.randint(1,10)
			if roll == 10:
				faction = random.choice(angry_factions)
				attackers = []
				max_attackers = random.randint(3,6)
				attacker_count = 1
				while attacker_count <= max_attackers:
					attacker = random.choice(faction.footsoldiers)
					attackers.append(attacker)
					attacker_count += 1
				attacker_party = NPC(attackers,500,[],50)
				gang_attack_finished = False
				while gang_attack_finished == False:
					gang_attack_finished = faction_attack(party,world,faction,attacker_party,my_location)
					#gang_attack_finished = battle(party,attacker_party,my_location,world,True)



		day = world.time.day
                hour = world.time.hour

		world.time.minute += 1 * distance
		#hour = world.time.hour
		
		world.time.correct()
		if world.time.day <= day + 1:
			my_area.clean_up()
		if world.time.hour >= hour + 1 or world.time.hour == 0 and hour >= world.time.hour:
			for member in party.members:
				member.handle_mind()
				member.hunger += 4
				if member.hunger >= 101:
					member.hunger = 100
				member.thirst += 8
				if member.thirst >= 101:
					member.thirst = 100
				member.sleep -= 3
				if member.sleep <= -1:
					member.sleep = 0 
		for member in party.members:
			if member.health.bleeding_rate >= 1:
				member.bleed()
			chance = random.randint(1,3)
			member.health.current_stamina -= 1
			if len(dragging) >= 1:
				for member in dragging:
					member[1].health.current_stamina -= 1
		#world.time.correct()
		my_location = find_location(party,world)
		#people
                if my_location.is_bar == True and world.time.hour >= my_location.time_open and world.time.hour <= my_location.time_close + 1:
                        #my_location.actors = []
                        try:
                                num_regulars = random.randint(2,4)
                        except:
                                num_regulars = 2
                        if len(my_location.regulars) >= 1:
                                possible_regulars = my_location.regulars
                        else:
                                possible_regulars = []
                        count = 1
                        regulars = []
                        while count <= num_regulars:
                                try:
                                        regular = random.choice(my_location.regulars)
                                        #possible_regulars.remove(regular)
					if regular not in regulars:
                                        	regulars.append(regular)
                                        #possible_regulars.remove(regular)
                                        count += 1
                                except:
					count += 1
                        #my_location.actors = NPC(regulars,0,[],0)
		my_area = find_area(party,world)
		
		#print my_location
		travelling = True
		while travelling == True:
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1, 'Travelling.')
			libtcod.console_flush()
			save_game()
			party.x = my_area.x
			party.y = my_area.y
			travelling = False
		turn_finished = True

		#save_game()
		return my_location, turn_finished

# T U R N

def turn(party,world,turn_finished,location):
	#locate player and describe location
        my_location = find_location(party,world)
	location = my_location
	libtcod.console_clear(0)
	describe_location(my_location)
	#check if safehouse
	if my_location.is_safehouse == True:
		libtcod.console_print(0,1,22, "[p]arty,[r]est,[t]ravel.")
        else:
		libtcod.console_print(0,1,22, "[p]arty,[t]ravel")




        item_count = 1
        line_count = 4
	#libtcod.console_clear(0)
        for item in my_location.items:
		print item.name
                if item_count <= 10:
                        print_line = item_count + line_count
                        libtcod.console_print(0,1,print_line, item.name)
		elif item_count >= 11 and item_count <= 20:
                        print_line = item_count + line_count - 10
                        libtcod.console_print(0,20,print_line, item.name)
                elif item_count >= 21 and item_count <= 32:
                        print_line = item_count + line_count - 20
                        libtcod.console_print(0,40,print_line, item.name)
                item_count += 1

        libtcod.console_flush()



	action = False
	while action == False:
		libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
                if key.c == ord('t'):
			location = travel(party,world,False)
			player_party = Party(True,player,party,location,area,city)
			action = True
	turn_finished = True
	return turn_finished,location

def clear_screen():
	h = 1
	w = 1
	while w <= SCREEN_WIDTH:
		while h <= SCREEN_HEIGHT:
	        	libtcod.console_print(0, w, h, " ")
			libtcod.console_flush()
			h = h + 1
		w = w + 1

def roll_dice(num_dice, num_sides):
        total = 0
        rolls = 1
        while rolls <= num_dice:
                total += random.randint(1,num_sides)
		rolls += 1
        return total

def gen_player_stats(profession):
        strength = roll_dice(3,5)
        dexterity = roll_dice(3,5)
        intelligence = roll_dice(3,5)
        willpower = roll_dice(3,5)
	charisma = roll_dice(3,5)
        if profession == "Hustler":
                intelligence = intelligence + random.randint(1,4)
                charisma = charisma + random.randint(2,4)
        elif profession == "Drug Dealer":
                strength = strength + random.randint(2,4)
                dexterity = dexterity + random.randint(1,2)
        elif profession == "Robber":
                strength = strength + random.randint(4,6)
                dexterity = dexterity + random.randint(2,4)
        elif profession == "Hacker":
                strength = strength - random.randint(4,6)
        elif profession == "Sex Worker":
                dexterity = dexterity + random.randint(1,2)
                intelligence = intelligence 
                willpower = willpower 
                charisma = charisma + random.randint(3,5)

        return strength, dexterity, intelligence, willpower, charisma

def gen_character(profession,gender):
	strength, dexterity, intelligence, willpower, charisma = 0,0,0,0,0
	player_stats = Stats(strength,dexterity,intelligence,willpower,charisma,strength,dexterity,intelligence,willpower,charisma)
	strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
        skills = gen_skills(profession)
        weapon = gen_player_weapons(profession)
        if weapon.name == "Knife" or weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
        	skills.brawl = random.randint(1,3)
        elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
                skills.pistol = random.randint(1,3)
        elif weapon.name == "12g Shotgun": 
                skills.shotgun = random.randint(1,3) 
        elif weapon.name == "AK-47": 
                skills.rifle = random.randint(1,3) 
        outfit = gen_player_outfit(profession, gender)
        age = random.randint(18,45)
        hp = strength + dexterity + willpower
        traits = gen_player_traits()
	if gender == 'Male':
		fname = random.choice(male_fnames)
	elif gender == "Female":
		fname = random.choice(female_fnames)
	lname = random.choice(surnames)
        if profession == "Hipster":
        	money = 500
        else: 
        	money = 100
        return player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname
        #player_stats, skills, weapon, outfit, age, hp, traits, money = gen_character()

def create_world(player):
	libtcod.console_clear(0)
	valid_city = False
	while valid_city == False:
	        libtcod.console_print(0, 1, 1, "Generating world...")
	        libtcod.console_flush()
		world = gen_new_city()
		valid_city = True
	return world
        for area in city:
        	for location in area:
                	print location.name


def create_party(player):
	party_members = []
	party_members.append(player)
	num_members = 3
	count = 1
	while count <= num_members:

        	libtcod.console_clear(0)
		if count == 1:
        		libtcod.console_print(0, 1, 1, "What is your 1st companions gender?")
		elif count == 2:
			libtcod.console_print(0, 1, 1, "What is your 2nd companions gender?")
		elif count == 3:
			libtcod.console_print(0, 1, 1, "What is your 3rd companions gender?")

        	libtcod.console_print(0, 1, 5, "[M]ale")
        	libtcod.console_print(0, 1, 6, "[F]emale")
        	libtcod.console_flush()
		choose_gender = False	
		choose_profession = False
	        while choose_gender == False:
        	        key = libtcod.console_check_for_keypress()
        	        if key.c == ord('m'):
        	                #print 'male'
        	                gender = 'Male'
				fname = random.choice(male_fnames)
				lname = random.choice(surnames)
				choose_gender = True
        	        elif key.c == ord('f'):
        	                print 'female'
        	                gender = 'Female'
				fname = random.choice(female_fnames)
				lname = random.choice(surnames)
        	                choose_gender = True

	        while choose_gender == True and choose_profession == False:
	                libtcod.console_clear(0)
       		        libtcod.console_print(0, 1, 1, "Choose your companion's profession")
       		        libtcod.console_print(0, 1, 5, "(1)HUSTLER")
  			libtcod.console_print(0, 1, 6, "(2)CRIMEPUNK")
               		libtcod.console_print(0, 1, 7, "(3)HIPSTER")
                	libtcod.console_print(0, 1, 8, "(4)SCUMBAG")
                	libtcod.console_print(0, 1, 9, "(5)WASTOID")
                        libtcod.console_print(0, 1, 10, "(6)SCRIPT KIDDIE")
                        libtcod.console_print(0, 1, 11, "(7)SEX WORKER")
                        libtcod.console_print(0, 1, 12, "(8)LOST SOUL")

                	libtcod.console_flush()
                	key = libtcod.console_check_for_keypress()
                	if key.c == ord('1'):
                        	profession = 'Hustler'
                        	choose_profession = True
                	elif key.c == ord('2'):
                	        profession = 'Crimepunk'
                	        choose_profession = True
                	elif key.c == ord('3'):
                        	profession = 'Hipster'
                        	choose_profession = True
                	elif key.c == ord('4'):
				profession = 'Scumbag'
                       		choose_profession = True
                	elif key.c == ord('5'):
                        	profession = 'Wastoid'
                        	choose_profession = True
			elif key.c == ord('6'):
				profession = 'Script Kiddie'
				choose_profession = True
			elif key.c == ord('7'):
				profession = 'Sex Worker'
				choose_profession = True
			elif key.c == ord('8'):
				profession = 'Lost Soul'
				choose_profession = True
		if choose_gender == True and choose_profession == True:
			age = random.randint(18,45)

			#starting money
			if profession == "Hipster":
				money = 500
			else:
				money = 100
			#inventory
			#health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)
			inventory = [bandages,morphine,speed]
			strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
			max_health = strength * 10
			health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100)
			skills = gen_skills(profession)
			skills_xp = skills
			weapon = gen_player_weapons(profession)
			outfit = gen_player_outfit(profession,gender)
			tool = 'None'
			drugs = []
			traits = gen_player_traits()
			affiliation = 'Player Organization'
			combat_status = Combat_Status(False,False,False,False,False)
	                #mind
	                happiness = random.randint(40,100)
	                stress = random.randint(0,25)
	                sanity = random.randint(40,100)
	                horny = random.randint(0,35)
			#addictions
			nicotine_addiction = Addiction('Nicotine',0,0,4,[])
			caffeine_addiction = Addiction('Caffeine',0,0,2,[])
			cocaine_addiction = Addiction('Cocaine',0,0,7,[])
			opiates_addiction = Addiction('Opiates',0,0,10,[])
			speed_addiction = Addiction('Speed',0,0,7,[])


	                addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
			trauma = 0
	                mind = Mind(happiness,stress,sanity,horny,addictions,trauma)

			hunger,thirst,sleep = 0,0,100

			stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
			home = 'None'
			party_member = Char(gender,age, profession,affiliation,health, stats, [], skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'player',combat_status,home,mind,hunger,thirst,sleep)
			party_members.append(party_member)
			count += 1 
	#print player_party.location
	libtcod.console_clear(0)
	#generate world
	world = create_world(player)
	#choose random starting location
	locations = []
	for area in world.areas:
		print area.name
		for location in area.locations:
			#print location.name
			if location.is_safehouse == True:
				locations.append(location)
	location = random.choice(locations)
	area = location.area
	city = location.city
        #finally, create the party and place it in the starting location

	#starting cash and fame
	money = 800
	fame = 0
	for member in party_members:
		money += member.start_money

	#is_player,leader,members,location,area,city,money,inventory,safehouse,fame
        player_party = Party(True,player,party_members,location,area,city,money,inventory,location,fame,1,1)
	my_area = find_area(player_party,world)
	player_party.x = my_area.x
	player_party.y = my_area.y
	return player_party,world
	

def main_menu():
	print 'gooo'
	#ask gender
	gender = ''
	choose_gender = False
	choose_profession = False
	confirm_roll = False
	choice_made = False
	confirm_skills = False
	confirm = False
	game_starting = True

	libtcod.console_clear(0)
        libtcod.console_print(0, 1, 1, "What is your gender?")

        libtcod.console_print(0, 1, 5, "[M]ale")
        libtcod.console_print(0, 1, 6, "[F]emale")
	libtcod.console_flush()
	while choose_gender == False:
		key = libtcod.console_check_for_keypress()
        	if key.c == ord('m'):
			print 'male'
			gender = 'Male'
			choose_gender = True
		elif key.c == ord('f'):
			print 'female'
			gender = 'Female'
			choose_gender = True
	#has_name = False
	##while has_name == False:
        #	if gender == 'Male':
        #        	fname = random.choice(male_fnames)
        #        elif gender == 'Female':
        #                fname = random.choice(female_fnames)
        #        lname = random.choice(surnames)
        #        has_name = True
	while choose_profession == False:
		libtcod.console_clear(0)
        	libtcod.console_print(0, 1, 1, "What is your profession?")
        	libtcod.console_print(0, 1, 5, "(1)HUSTLER")
                libtcod.console_print(0, 1, 6, "(2)CRIMEPUNK")
                libtcod.console_print(0, 1, 7, "(3)HIPSTER")
                libtcod.console_print(0, 1, 8, "(4)SCUMBAG")
                libtcod.console_print(0, 1, 9, "(5)WASTOID")
                libtcod.console_print(0, 1, 10, "(6)SCRIPT KIDDIE")
                libtcod.console_print(0, 1, 11, "(7)SEX WORKER")
                libtcod.console_print(0, 1, 12, "(8)LOST SOUL")	


		libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
                if key.c == ord('1'):
                        profession = 'Hustler'
                        choose_profession = True
                elif key.c == ord('2'):
                        profession = 'Crimepunk'
                        choose_profession = True
                elif key.c == ord('3'):
                        profession = 'Hipster'
                        choose_profession = True
                elif key.c == ord('4'):
                        profession = 'Scumbag'
                        choose_profession = True
                elif key.c == ord('5'):
                        profession = 'Wastoid'
                        choose_profession = True
                elif key.c == ord('6'):
                        profession = 'Script Kiddie'
                        choose_profession = True
                elif key.c == ord('7'):
                        profession = 'Sex Worker'
                        choose_profession = True
                elif key.c == ord('8'):
                        profession = 'Lost Soul'
                        choose_profession = True

	if choose_gender == True and choose_profession == True:
		libtcod.console_clear(0)
		while confirm_roll == False:
	                strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
			player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname = gen_character(profession,gender)
			while choice_made == False:
				libtcod.console_print(0, 1, 1,fname + " " + lname) 
                		libtcod.console_print(0, 1, 2, profession)
 				libtcod.console_print(0, 1, 3, gender)
	          		libtcod.console_print(0, 1, 6, "STR: " + str(strength))
	                	libtcod.console_print(0, 1, 7, "DEX: " + str(dexterity))
	                	libtcod.console_print(0, 1, 8, "INT: " + str(intelligence))
	                	libtcod.console_print(0, 1, 9, "WIL: " + str(willpower))
	                	libtcod.console_print(0, 1, 10, "CHA: " + str(charisma))
        	        	libtcod.console_print(0, 1, 12, "[a]ccept")
                                libtcod.console_print(0, 1, 13, "[r]e-roll")

				libtcod.console_flush()

		                key = libtcod.console_check_for_keypress()
				if key.c == ord("a"):
					libtcod.console_clear(0)
					choice_made, confirm_roll = True, True
				elif key.c == ord("r"): 
					libtcod.console_clear(0)
			                strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
					player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname = gen_character(profession,gender)
	if confirm_roll == True and confirm_skills == False:
		while confirm_skills == False:
			libtcod.console_clear(0)

#			def gen_character():
#				player_stats = Stats(strength,dexterity,intelligence,willpower,charisma,strength,dexterity,intelligence,willpower,charisma)
#				skills = gen_skills(profession)
#				weapon = gen_player_weapons(profession)
#				outfit = gen_player_outfit(profession, gender)
#				age = random.randint(18,45)
#				hp = strength + dexterity + willpower
#				traits = gen_player_traits(profession)
#				if profession == "Hipster":
#					money = 500
#				else: 
#					money = 100
#				return player_stats, skills, weapon, outfit, age, hp, traits, money
#			player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname = gen_character(profession,gender)
			while confirm_skills == False:
	                       	libtcod.console_print(0, 1, 1,fname + " " + lname)
                        	libtcod.console_print(0, 1, 2, profession)
                        	libtcod.console_print(0, 1, 3, gender)
                        	libtcod.console_print(0, 1, 4, "Age: " + str(age))
			
				libtcod.console_print(0, 20, 1, outfit.name)
				libtcod.console_print(0, 20, 2, weapon.name)
				libtcod.console_print(0, 20, 4, "$" + str(money))

				trait_count = 1
				for trait in traits:
					buffer = 6
					line = buffer + trait_count
					libtcod.console_print(0,20,line, str(trait.name))
					trait_count += 1
				

                        
				libtcod.console_print(0, 1, 7, "STR: " + str(strength))
                	        libtcod.console_print(0, 1, 8, "DEX: " + str(dexterity))
                	        libtcod.console_print(0, 1, 9, "INT: " + str(intelligence))
                	        libtcod.console_print(0, 1, 10, "WIL: " + str(willpower))
                	        libtcod.console_print(0, 1, 11, "CHA: " + str(charisma))

				libtcod.console_print(0,1,15, "Brawl:")
				libtcod.console_print(0,1,16, "Computer:")
				libtcod.console_print(0,1,17, "Dodge:")
				libtcod.console_print(0,1,18, "Disguise:")
				libtcod.console_print(0,1,19, "Etiquette:")
				libtcod.console_print(0,1,20, "Explosive:")
				libtcod.console_print(0,1,21, "First Aid:")
				libtcod.console_print(0,1,22, "Investigate:")
				libtcod.console_print(0,1,23, "Leadership")
				libtcod.console_print(0,1,24, "Lie:")
        	                libtcod.console_print(0,1,25, "Negotiate:")

       		                libtcod.console_print(0,20,15, "Persuade:")
                	        libtcod.console_print(0,20,16, "Pickpocket:")
				libtcod.console_print(0,20,17, "Pistol:")
                                libtcod.console_print(0,20,18, "Rifle:")

                                libtcod.console_print(0,20,19, "Security:")
	                        libtcod.console_print(0,20,20, "Seduction:")
        	                libtcod.console_print(0,20,21, "Shotgun:")
                	        libtcod.console_print(0,20,22, "Stealth:")
                	        libtcod.console_print(0,20,23, "Streetwise:")
                	        libtcod.console_print(0,20,24, "Throw:")
                	        libtcod.console_print(0,20,25, "Torture:")

                	        libtcod.console_print(0,15,15, str(skills.brawl))
                	        libtcod.console_print(0,15,16, str(skills.computers))
                	        libtcod.console_print(0,15,17, str(skills.dodge))
                	        libtcod.console_print(0,15,18, str(skills.disguise))
                	        libtcod.console_print(0,15,19, str(skills.etiquette))
                	        libtcod.console_print(0,15,20, str(skills.explosives))
                	        libtcod.console_print(0,15,21, str(skills.first_aid))
                	        libtcod.console_print(0,15,22, str(skills.investigate))
                	        libtcod.console_print(0,15,23,str(skills.leadership))
				libtcod.console_print(0,15,24, str(skills.lying))
                	        libtcod.console_print(0,15,25, str(skills.negotiate))

                        	libtcod.console_print(0,35,16, str(skills.persuasion))
                        	libtcod.console_print(0,35,17, str(skills.pickpocket))
                                libtcod.console_print(0,35,18, str(skills.pistol))
                                libtcod.console_print(0,35,18, str(skills.rifle))

                                libtcod.console_print(0,35,19, str(skills.security))
                        	libtcod.console_print(0,35,20, str(skills.seduction))
                        	libtcod.console_print(0,35,21, str(skills.shotgun))
                        	libtcod.console_print(0,35,22, str(skills.stealth))
                        	libtcod.console_print(0,35,23,str(skills.streetwise))
                        	libtcod.console_print(0,35,24, str(skills.throw))
                        	libtcod.console_print(0,35,25, str(skills.torture))

				libtcod.console_print(0,1,28, "[a]ccept")
                        	libtcod.console_print(0,1,29, "[r]e-roll")

				libtcod.console_flush()
                        	key = libtcod.console_check_for_keypress()
				if key.c == ord('r'):
					libtcod.console_clear(0)
					id = 1
					player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname = gen_character(profession,gender)
					player = id, gender, profession, player_stats,[], skills,weapon,outfit,None,traits,fname,lname,money
				elif key.c == ord('a'):
					libtcod.console_clear(0)
					confirm_skills = True
	if confirm_skills == True and confirm_roll == True:
		
        	#lets go
		libtcod.console_clear(0)
                id = 1

		#health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)
		drugs = []
		#fame = 0

		stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
		max_health = stats.strength * 10
		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100)
		combat_status = Combat_Status(False,False,False,False,False)
                #mind
                happiness = random.randint(40,100)
                stress = random.randint(0,30)
                sanity = random.randint(40,100)
                horny = random.randint(0,40)
		#addictions
		nicotine_addiction = Addiction('Nicotine',0,0,4,[])
		caffeine_addiction = Addiction('Caffeine',0,0,2,[])
		cocaine_addiction = Addiction('Cocaine',0,0,7,[])
		opiates_addiction = Addiction('Opiates',0,0,10,[])
		speed_addiction = Addiction('Speed',0,0,7,[])


                addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
		trauma = 0
                mind = Mind(happiness,stress,sanity,horny,addictions,trauma)

		skills_xp = skills
		home = 'None'
		affiliation = 'Player Organization'

		hunger,thirst,sleep = 0,0,100


                player = Char(gender, age, profession,affiliation,health, stats,[], skills,skills_xp,weapon,outfit,None,traits,drugs,fname,lname,money,'player',combat_status,home,mind,hunger,thirst,sleep)
		#player_party, world = create_party(player)
		return player
	        #play_turn(player_party,world,True)

def take_damage(damage,target):
                target.health.current_health = target.health.current_health - damage
		return target.health.current_health

def enemy_attack(attacker,target,player):

                libtcod.console_print(0,1,line_count,"ENEMY ATTACK:")



def attack(attacker,target,party,controller,my_location,player,world,show_fight):
	attack_finished = False
	libtcod.console_clear(0)
	line_count = 1
	target_chosen = False
	possible_targets = []
	target_name = target.fname + " " + target.lname
	if controller == "enemy":
		libtcod.console_print(0,1,line_count,"ENEMY ATTACK:")
		line_count += 1

	else:
		line_count = 1
	if target.combat_status.knocked_down == False:
		libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " attacks " + target.fname + " " + target.lname + " with a " + attacker.weapon.name + ".")
        elif target.combat_status.knocked_down == True:
                libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " attacks " + target.fname + " " + target.lname + " with a " + attacker.weapon.name + " while they are defenceless.")
	#print target.fname + " " + target.lname
	line_count += 1
	strength_bonus = 0
	attacker.mind.stress += 5
	#get the attacker skill with the weapon & add strength bonus to damage if brawl
	if attacker.weapon.weapon_type == "brawl":
		print attacker.skills
		attacker_skill = attacker.skills.brawl
		strength_bonus = attacker.stats.strength / 5
        elif attacker.weapon.weapon_type == "pistol":
                attacker_skill = attacker.skills.pistol
        elif attacker.weapon.weapon_type == "shotgun":
                attacker_skill = attacker.skills.shotgun
        elif attacker.weapon.weapon_type == "rifle":
                attacker_skill = attacker.skills.rifle
        improve_skill_roll = random.randint(1,30)
        if improve_skill_roll <= attacker.stats.intelligence:
		if attacker.weapon.weapon_type == "brawl":
        	        attacker.skills.brawl += 1
		elif attacker.weapon.weapon_type == "pistol":
		        attacker.skills.pistol += 1
		elif attacker.weapon.weapon_type == "shotgun":
		        attacker.skills.shotgun += 1
		elif attacker.weapon.weapon_type == "rifle":
		        attacker.skills.rifle += 1


	#attack roll
	attack_roll = random.randint(1,10) + attacker_skill
	#defend roll
	defend_roll = random.randint(1,10) + target.skills.dodge
	
	defend_roll = defend_roll / 2
        damage_taken = (attacker.weapon.damage - target.outfit.defense)
        if damage_taken <= -1:
	        damage_taken = 0

	#if attack hits
	if defend_roll <= attack_roll and damage_taken >= 1:
		target.mind.stress += random.randint(5,15)
		target.mind.trauma += random.randint(1,2)
		#print damage_taken
		
		if controller == "player":
			target.damage(damage_taken)
		elif controller == "enemy":
			target.damage(damage_taken)
		#print target.health.current_health
		#libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was hit for " + str(damage_taken) + " damage.")
		#line_count += 1

		#give an injury
		if attacker.weapon.name == "Punch" and damage_taken >= 1:
			injury = random.choice(bruises)
		elif attacker.weapon.name == "Knife" and damage_taken >= 1:
			attack_types = ['major cut','minor cut','stab']
			attack_type = random.choice(attack_types)
			if attack_type == 'major cut':
				injury = random.choice(major_cuts)
			elif attack_type == 'minor cut':
				injury = random.choice(minor_cuts)
			elif attack_type == 'stab':
				injury = random.choice(stab_wounds)
                elif attacker.weapon.name == "Sword" and damage_taken >= 1:
                        attack_types = ['major cut','minor cut','stab','sever']
                        attack_type = random.choice(attack_types)
                        if attack_type == 'major cut':
                                injury = random.choice(major_cuts)
                        elif attack_type == 'minor cut':
                                injury = random.choice(minor_cuts)
                        elif attack_type == 'stab':
                                injury = random.choice(stab_wounds)
                        elif attack_type == 'sever':
				check_exists = False
				while check_exists == False:
					exists = False
                                	injury = random.choice(severed_limbs)
					if len(target.injuries) >= 1:
						for existing_injury in target.injuries:
							if existing_injury.location == injury.location and existing_injury.name == injury.name:
								exists = True
                                                        elif existing_injury.name == "blown off" and existing_injury.location == injury.location:
                                                                exists = True
					if exists == False:
						check_exists = True
					elif exists == True:
						exists = True
	                                limb = Limb(target_name,injury.name,injury.location,'limb',True,100)
        	                        my_location.items.append(limb)



		elif attacker.weapon.name == "Baseball Bat" or attacker.weapon.name == "Crowbar" or attacker.weapon.name == "Shovel" and damage_taken >= 1:
			attack_types = ["bruise","fracture"]
			attack_type = random.choice(attack_types)
			if attack_type == "bruise":
				injury = random.choice(bruises)
			elif attack_type == "fracture":
				injury = random.choice(fractures)
		elif attacker.weapon.name == "9mm Pistol":
			injury = random.choice(shot_9mm)
		elif attacker.weapon.name == "12g Shotgun":
			attack_types = ['shotgun wound', 'blown off']
			attack_type = random.choice(attack_types)
			if attack_type == "shotgun wound":
				injury = random.choice(shot_12g)
			elif attack_type == "blown off":
                                check_exists = False
                                while check_exists == False:
                                        exists = False
                                        injury = random.choice(blown_off_limbs)
                                        if len(target.injuries) >= 1:
                                                for existing_injury in target.injuries:
                                                        if existing_injury.name == injury.name and existing_injury.location == injury.location:
                                                                exists = True
							elif existing_injury.name == "severed" and existing_injury.location == injury.location:
								exists = True
                                        if exists == False:
                                                check_exists = True
                                        elif exists == True:
                                                exists = True
				limb = Limb(target_name,injury.name,injury.location,'limb',True,100)
				my_location.items.append(limb)


		elif attacker.weapon.name == "AK-47" or attacker.weapon.name == 'Uzi' and damage_taken >= 1:
			attack_chance = random.randint(1,4)
			if attack_chance == 4:
				attack_type = 'blown off'
			else:
				attack_type = 'ak47'
                        if attack_type == "ak47":
                                injury = random.choice(shot_ak47)
                        elif attack_type == "blown off":
                                check_exists = False
                                while check_exists == False:
                                        exists = False
                                        injury = random.choice(blown_off_limbs)
                                        if len(target.injuries) >= 1:
                                                for existing_injury in target.injuries:
                                                        if existing_injury.name == injury.name and existing_injury.location == injury.location:
                                                                exists = True
                                                        elif existing_injury.name == "severed" and existing_injury.location == injury.location:
                                                                exists = True
                                        if exists == False:
                                                check_exists = True
                                        elif exists == True:
                                                exists = True
                                limb = Limb(target_name,injury.name,injury.location,'limb',True,100)
                                my_location.items.append(limb)




		min_bonus_damage = injury.damage_bonus / 2
		max_bonus_damage = injury.damage_bonus 
		bonus_damage = random.randint(min_bonus_damage,max_bonus_damage)


		#cause bleeding
		if injury.cause_bleeding >= 1:
			target.health.bleeding_rate += (injury.cause_bleeding / 2)
			target.health.current_blood -= (injury.cause_bleeding / 2) 

		#cause pain
		if injury.cause_pain >= 1:
			target.health.current_pain += (injury.cause_pain / 2)

		#cause stamina loss
                if injury.cause_stamina_loss >= 1:
                        target.health.current_stamina -= (injury.cause_stamina_loss)
		#cause trauma
		if (damage_taken + bonus_damage) >= (target.health.max_health / 4):
			target.mind.trauma += 2

		#check if target knocked down
		just_knocked_down = False
		if (damage_taken + bonus_damage) >=  (target.health.max_health / 4) and target.combat_status.knocked_down == False and target.health.current_stamina >= 1:
			saving_throw = random.randint(1,20)
			if saving_throw >= (target.stats.willpower + 1):
				target.combat_status.knocked_down = True
				just_knocked_down = True
		elif injury.name == 'severed' or injury.name == 'blown off':
			if injury.location == 'right leg' or injury.location == 'left leg':
				knockdown_roll = random.randint(1,8)
				if knockdown_roll != 1:
					target.combat_status.knocked_down = True
					just_knocked_down = True

		else:
			just_knocked_down = False
		passed_pain = False
	        if attacker.health.current_pain >= 1:
        	        resistance = (attacker.stats.willpower) + (attacker.stats.strength) 
        	        resist_roll = random.randint(3,resistance)
        	        pain = attacker.health.current_pain
        	        pain_roll = random.randint(1,pain)
        	        passed_pain = False
        	        if resist_roll >= pain_roll:
        	                passed_pain = True
        	        elif resist_roll <= pain_roll - 1:
        	                passed_pain = False
        	else:
        	        passed_pain = True
		if passed_pain == False:
	                target.combat_status.knocked_down = True
                        just_knocked_down = True


		#did target lose their weapon
                if injury.name == 'severed' or injury.name == 'blown off':
                        if injury.location == 'right arm':
				if target.weapon.name != "Punch":
					my_location.items.append(target.weapon)
					target.weapon == punch
		
		
		target.health.current_health -= bonus_damage
		target.health.max_health -= (bonus_damage) + (damage_taken /2) 
		target.injuries.append(injury)
		#print injury.name
		#libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was hit.")
		#line_count += 1
		total_damage = damage_taken + bonus_damage
		if total_damage >= 1:
                	libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + injury.description + ".")
			line_count += 1
		if total_damage >= 1:
			libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " took " + str(total_damage) + " damage.")
			line_count += 1
                if target.health.bleeding_rate >= 1 and target.health.current_health >= 1:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is bleeding.")
                        line_count += 1
		if target.combat_status.knocked_down == True and target.health.current_health >= 1 and just_knocked_down == True:
			libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was knocked down.")
			line_count += 1
		#is target dead?
		
		for injury in target.injuries:
			if injury.name == "severed" or injury.name == "blown off" and injury.location == "head":
				target.health.current_health = 0
				target.health.max_health = 0
		if target.health.current_health <= 0:
			#print defender_party
			libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is dead.")
			#drop corpse, items and money at location
			my_location.corpses.append(target)
			if target.weapon.name != "Punch":
				my_location.items.append(target.weapon)
				target.weapon = punch
			#my_location.items.append(target.outfit)
			#target.outfit = naked
			player.money += target.start_money
			
			#is the target in a organization
			for area in world.areas:
				for organization in area.organizations:
					if organization.name == target.affiliation:
						organization.player_reputation -= 5
			#are we on anyone's turf
                        for area in world.areas:
                                for organization in area.organizations:
                                        if organization.name == my_location.owned_by:
                                                organization.player_reputation -= 2

			#remove from team
			party.members.remove(target)
			#if len(party.members) == 0:
				#attack_finished = True
				#return attack_finished
			line_count += 1
		

	#if attack missed
	elif defend_roll >= attack_roll: 
		libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " missed.")
	        line_count += 1



	line_count += 2	
	libtcod.console_print(0,1,line_count,"[c]ontinue]")
	libtcod.console_flush()	
	confirmed = False
	while confirmed == False:
	        key = libtcod.console_check_for_keypress()
                if key.c == ord('c'):
                        libtcod.console_clear(0)
			move_finished, attack_finished = True,True
			confirmed = True
	
	return move_finished, attack_finished


def player_battle_attack(attacker,player,enemy,controller,my_location,world,show_fight):
	#move_finished, attack_finished = False, False
	libtcod.console_clear(0)
	#if len(player.members) == 0 or len(enemy.members) == 0:
	#	attack_finished = True
	#	return attack_finished
        libtcod.console_clear(0)
	attack_finished = False
	move_finished = False
        #show player and enemy parties

	#if attacker is knocked down check if they are in too much pain
	if attacker.health.current_pain >= 1:
		resistance = (attacker.stats.willpower) + (attacker.stats.strength) 
		resist_roll = random.randint(3,resistance)
		pain = attacker.health.current_pain
		pain_roll = random.randint(1,pain)
		passed_pain = False
		if resist_roll >= pain_roll:
			passed_pain = True
		elif resist_roll <= pain_roll - 1:
			passed_pain = False
	else:
		passed_pain = True
	if attacker.combat_status.knocked_down == True and attacker.health.current_health >= 1 and attacker.health.current_stamina >= 1 and passed_pain == True:
		if controller == "player":
	                libtcod.console_set_default_foreground(0, libtcod.green)
			libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " got up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)

		elif controller == "enemy":
			libtcod.console_set_default_foreground(0, libtcod.red) 
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " got up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)
		libtcod.console_print(0,1,4, "[c]onfirm")
		libtcod.console_flush()
		attacker.combat_status.knocked_down = False
		confirmed = False
		while confirmed == False:
			key = libtcod.console_check_for_keypress()
			if key.c == ord('c'):
				attack_finished = True
				move_finished = True
				return attack_finished,move_finished
	elif attacker.combat_status.knocked_down == True and attacker.health.current_health >= 1 and attacker.health.current_stamina <= 0 and passed_pain == True:
                if controller == "player":
                        libtcod.console_set_default_foreground(0, libtcod.green)
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " does not have enough stamina to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)

                elif controller == "enemy":
                        libtcod.console_set_default_foreground(0, libtcod.red) 
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " does not have enough stamina to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_print(0,1,4, "[c]onfirm")
                libtcod.console_flush()
                confirmed = False
                while confirmed == False:
                        key = libtcod.console_check_for_keypress()
                        if key.c == ord('c'):
                                attack_finished = True
                                move_finished = True
                                return attack_finished,move_finished
        elif attacker.combat_status.knocked_down == True and attacker.health.current_health >= 1 and attacker.health.current_stamina <= 0 and passed_pain == False:
                if controller == "player":
                        libtcod.console_set_default_foreground(0, libtcod.green)
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " does not have enough stamina and is in too much pain  to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)

                elif controller == "enemy":
                        libtcod.console_set_default_foreground(0, libtcod.red) 
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " does not have enough stamina and is in too much pain to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_print(0,1,4, "[c]onfirm")
                libtcod.console_flush()
                confirmed = False
                while confirmed == False:
                        key = libtcod.console_check_for_keypress()
                        if key.c == ord('c'):
                                attack_finished = True
                                move_finished = True
                                return attack_finished,move_finished
        elif attacker.combat_status.knocked_down == True and attacker.health.current_health >= 1 and attacker.health.current_stamina >= 1 and passed_pain == False:
                if controller == "player":
                        libtcod.console_set_default_foreground(0, libtcod.green)
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is in too much pain to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)

                elif controller == "enemy":
                        libtcod.console_set_default_foreground(0, libtcod.red) 
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is in too much pain to get up.")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_print(0,1,4, "[c]onfirm")
                libtcod.console_flush()
                confirmed = False
                while confirmed == False:
                        key = libtcod.console_check_for_keypress()
                        if key.c == ord('c'):
				libtcod.console_clear(0)
                                attack_finished = True
                                move_finished = True
                                return attack_finished,move_finished





	elif controller == "player" and attack_finished == False and len(enemy.members) != 0 and len(player.members) != 0 and attacker.combat_status.knocked_down == False:
        	line_count = 3
		libtcod.console_set_default_foreground(0, libtcod.green) 
		libtcod.console_print(0,1,1, 'Who will ' + attacker.fname + " " + attacker.lname + " attack?")
                libtcod.console_set_default_foreground(0, libtcod.white)
		options = []
		option_count = 0
		for member in enemy.members:
			option_count += 1
			option = [option_count, member]
			options.append(option)
			line_count += 1
			libtcod.console_print(0,1,line_count,"[" + str(option_count) + "]" + member.fname + " " + member.lname)

		line_count += 2
		libtcod.console_print(0,1,line_count,"[b]ack")
		libtcod.console_flush()
		choice_made = False
		while choice_made == False:
	                key = libtcod.console_check_for_keypress()
			for option in options:
				target_key = str(option[0])
				defender_skills =  option[1].skills
	                        #print defender_skills
				if key.c == ord(target_key):
					attack_finished = attack(attacker,option[1],enemy,"player",my_location,player,world,True)
					#attack uses stamina
					attacker.health.current_stamina -= random.randint(1,4)
					move_finished = True
					choice_made = True
		                elif key.c == ord('b'):
	                        	libtcod.console_clear(0)
	                        	attack_finished = True
					move_finished = True
					choice_made = True
	elif controller == "enemy" and attack_finished == False and len(enemy.members) != 0 and len(player.members) != 0 and attacker.combat_status.knocked_down == False:
		target_chosen = False
		while attack_finished == False:
			#print member.fname + " " + member.lname + "attack"
			while target_chosen == False:
				target = random.choice(player.members)
				target_chosen = True
				#print choice_made
			print target.fname + " " + target.lname
			attack_finished = attack(attacker,target,player,"enemy",my_location,player,world,True)
			move_finished = True
			return attack_finished,move_finished
		#fix bug?
		#for member in player.members:
		#	if member != target:
		#		member.health.current_health += 15
	if len(player.members) >= 1 and len(enemy.members) <= 0:
		for item in my_location.items:
			if item.item_type == "container":
				item.is_visible = True
		
	return attack_finished

def enemy_battle_turn(enemy,player,player_party):
	to_attack = random.choice(player.members)
	#decide what to do
	attacking = True
	while attacking == True:
		target = to_attack
		attacker_skills = enemy.skills
		defender_skills = target.skills
		enemy_turn_finished = attack(enemy,target,player_party,world,True)
		return enemy_turn_finished
	
def player_battle_turn(member,player,enemy,my_location,world,True):
	libtcod.console_clear(0)
	move_finished = False
	attack_finished = False
	if len(player.members) == 0 or len(enemy.members) == 0:
		move_finished = True
	while move_finished == False:
		#check if anyone bled to death
		member.health.current_blood -= member.health.bleeding_rate
		if member.health.current_blood <= 0:
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1,member.fname + " " + member.lname + " bled to death.")
			libtcod.console_print(0,1,3,"[c]ontinue")
                        libtcod.console_flush()
                        my_location.corpses.append(member)
                        my_location.items.append(member.weapon)
			member.weapon = punch
                        my_location.items.append(member.outfit)
			member.outfit = naked
			if member.controlled_by == 'enemy':
                        	player.money += member.start_money
				enemy.members.remove(member)
			elif member.controlled_by == "player":
                        	#remove from team
                        	try:
					player.members.remove(member)
				except:
					print 'error?'

			confirmed = False
			while confirmed == False:
                        	key = libtcod.console_check_for_keypress()
                        	if key.c == ord('c'):
                        	        libtcod.console_clear(0)
                        	        attack_finished = True
                        	        move_finished = True
					return attack_finished


		if member.controlled_by == "player":
			controller = "player"
        		#show attacker
        		line_count = 1
        		libtcod.console_print(0,1,line_count, 'YOUR TURN:')
        		line_count = 2
        		player_count = 1
        		libtcod.console_print(0,1,line_count,member.fname + " " + member.lname)
        		libtcod.console_print(0,24,line_count,member.profession)
        		libtcod.console_print(0,39,line_count,member.outfit.name)
        		libtcod.console_print(0,56,line_count,member.weapon.name)
			libtcod.console_print(0,66,line_count,str(member.skills.brawl))

        		line_count += 2
			if member.combat_status.knocked_down == False:
				libtcod.console_print(0,1,line_count,'[a]ttack')
			elif member.combat_status.knocked_down == True:
				libtcod.console_print(0,1,line_count,'[g]et up!')
			libtcod.console_flush()
	
			key = libtcod.console_check_for_keypress()
        	        if key.c == ord('a') and member.combat_status.knocked_down == False:
				libtcod.console_clear(0)
				attack_finished = False
				move_finished = True
                        elif key.c == ord('g') and member.combat_status.knocked_down == True:
                                libtcod.console_clear(0)
                                attack_finished = False
                                move_finished = True

		elif member.controlled_by == "enemy":
			controller = "enemy"
			move_finished = True
	if member.controlled_by == "player":		
		while move_finished == True and attack_finished == False:                        	
			move_finished = player_battle_attack(member,player,enemy,member.controlled_by,my_location,world,True)
	elif member.controlled_by == "enemy":
		while move_finished == True and attack_finished == False:                               
                        move_finished = player_battle_attack(member,enemy,player,member.controlled_by,my_location,world,True)

                        #print 'fight!'
	return attack_finished
def initiative(player,enemy,my_location,world,show_fight):
	fighters = []
	fighter_id = 1
	turn_finished = False
	for member in player.members:
		member.controlled_by = 'player'
		fighter = (fighter_id, member,'player')
		fighters.append(member)
		fighter_id += 1
	for member in enemy.members:
		fighter = (fighter_id,member,'enemy')
                fighters.append(member)
                fighter_id += 1

        # work through the fighters in order

	while turn_finished == False:
        	for member in sorted(fighters,key=lambda member: member.stats.dexterity,reverse=True):
        	        # if fighter controlled by player
        	        if member.controlled_by == 'player':
				member_turn_finished = False
        	                member_turn_finished = player_battle_turn(member,player,enemy,my_location,world,True)
			elif member.controlled_by == 'enemy':
				member_turn_finished = player_battle_turn(member,enemy,player,my_location,world,True)
		turn_finished = True
	return turn_finished

#main battle function

def battle(player,enemy,location,world,show_fight):
	#check if player party are dead
	fight_finished = False
	num_player = len(player.members)
	#print "player" + " " + str(len(player.members))
        #print "enemy" + " " + str(len(enemy.members))

	libtcod.console_clear(0)
		
        if len(player.members) == 0:
                fight_finished = True
		return fight_finished
        elif len(enemy.members) == 0:
		player.fame += enemy.fame
                fight_finished = True
		return fight_finished
        while fight_finished == False:
        	if len(player.members) == 0:
        	        fight_finished = True
			#print 'fight over'
			return fight_finished
	        elif len(enemy.members) == 0:
			player.fame += enemy.fame
        	        fight_finished = True
			#print 'fight over'
			return fight_finished
		# show player and enemy parties
		line_count = 1
		libtcod.console_print(0,1,line_count, 'YOU:')
		line_count = 2
		option_count = 1
		view_options = []
		for member in player.members:
			letter = num_to_letter(option_count)
			option = [option_count,member]
			view_options.append(option)
			libtcod.console_print(0,1,line_count, "[" + letter + "]" + member.fname + " " + member.lname)
			libtcod.console_print(0,24,line_count,member.profession)
	                libtcod.console_print(0,39,line_count,member.outfit.name)
	                libtcod.console_print(0,56,line_count,member.weapon.name)
			libtcod.console_print(0,70,line_count,str(member.health.current_health) + "/" + str(member.health.max_health))
			line_count += 1
			option_count += 1

		line_count += 2
		libtcod.console_print(0,1,line_count, 'ENEMY:')
		line_count += 1
		for member in enemy.members:
			letter = num_to_letter(option_count)
			option = [option_count,member]
			view_options.append(option)
			libtcod.console_print(0,1,line_count,"[" + letter + "]" + member.fname + " " + member.lname)
			libtcod.console_print(0,24,line_count,member.profession)
			libtcod.console_print(0,39,line_count,member.outfit.name)
			libtcod.console_print(0,56,line_count,member.weapon.name)
			libtcod.console_print(0,70,line_count,str(member.health.current_health) + "/" + str(member.health.max_health))
	                line_count += 1
			option_count += 1

		line_count += 2
		libtcod.console_print(0,1,line_count, '[f]ight!')
		line_count += 1

		libtcod.console_flush()
		# i n i t i a t i v e
		round_finished = False
		if len(player.members) == 0:
			fight_finished,round_finished == True,True
		elif len(enemy.members) == 0:
			fight_finished,round_finished == True,True
		fighters = []
		while round_finished == False:
			key = ' '
			initiative_finished = False
			while initiative_finished == False:
				print view_options
				key = libtcod.console_check_for_keypress()
				if key.c == ord('f'):
                                       	initiative(player,enemy,location,world,True)
                                       	#print 'fight!'
                                       	round_finished,initiative_finished = True,True

def show_container(container,player_party,world):
        my_area = find_area(player_party,world)
	my_location = find_location(player_party,world)
        libtcod.console_clear(0)

	line_count = 1
	libtcod.console_print(0,1,line_count,"CONTAINER:")
	line_count += 3
	item_count = 1
	items_in_container = []
	if container.money >= 1:
                libtcod.console_print(0,1,line_count,"$" + str(container.money))
		line_count += 2

		
	for item in container.items:
		letter = num_to_letter(item_count)
		item_in_container = [letter,item]
		items_in_container.append(item_in_container)
		if item.item_type != "medical":
                	libtcod.console_print(0,1,line_count,"[" + letter + "]" + item.name)
		elif item.item_type == "medical" and item.number >= 2:
                        libtcod.console_print(0,1,line_count,"[" + letter + "]" + item.name+ " (" + str(item.number) + ")")

		line_count += 1
		item_count += 1
	line_count += 3
	if container.money >= 1:
        	libtcod.console_print(0,1,line_count,"[t]ake the money")
	line_count += 1
        libtcod.console_print(0,1,line_count,"[r]eturn")
	line_count += 1
	libtcod.console_flush()
	finished_investigating_container = False	
        while finished_investigating_container == False:
                key = libtcod.console_check_for_keypress()
                if key.c != ord('r'):
			for item in items_in_container:
				if key.c == ord(item[0]):
					player_party.inventory.append(item[1])
					container.items.remove(item[1])
                        		for organization in my_area.organizations:
                                		if organization.name == my_location.owned_by:
                                        		organization.player_reputation -= random.randint(5,15) 
					finished_investigating_container = True
					return finished_investigating_container
		if key.c == ord('r'):
			finished_investigating_container = True
			return finished_investigating_container
		if key.c == ord('t'):
			money_taken = container.money
			player_party.money += container.money
			container.money = 0
                        finished_investigating_container = True
			#anger faction
			for organization in my_area.organizations:
				if organization.name == my_location.owned_by:
					organization.player_reputation -= (money_taken / 500) 
                        return finished_investigating_container





def investigate(my_location,world,party):
        my_area = find_area(party,world)
	count = 1
	corpses_to_investigate = []
	people_to_investigate = []
	containers_to_investigate = []
	#people
	for corpse in my_location.corpses:
		letter = num_to_letter(count)
		thing_to_investigate = [letter, corpse]
		corpses_to_investigate.append(thing_to_investigate)
		count += 1

	for actor in my_location.actors.members:
		letter = num_to_letter(count)
		thing_to_investigate = [letter, actor]
                people_to_investigate.append(thing_to_investigate)
                count += 1

	for item in my_location.items:
		if item.item_type == 'container' and item.is_visible == True:
			letter = num_to_letter(count)
			container_to_investigate = [letter,item]
			containers_to_investigate.append(container_to_investigate)
			count += 1

	libtcod.console_clear(0)
	libtcod.console_print(0,1,1, "INVESTIGATE:")
	line_count = 4
	for corpse in corpses_to_investigate:
		libtcod.console_print(0,1,line_count, "[" + corpse[0] + "]" + corpse[1].fname + " " + corpse[1].lname + " (" + corpse[1].profession +  ")'s corpse.")
		line_count += 1
        for person in people_to_investigate:
                libtcod.console_print(0,1,line_count, "[" + person[0] + "]" + person[1].fname + " " + person[1].lname + " (" + person[1].profession +  ")")
                line_count += 1
        for container in containers_to_investigate:
                libtcod.console_print(0,1,line_count, "[" + container[0] + "]" + container[1].name + ".")
                line_count += 1


	line_count += 2
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	finished_investigating = False
	

	while finished_investigating == False:
	        key = libtcod.console_check_for_keypress()
	
		if key.c != ord('r'):
			#print key.c
			for corpse in corpses_to_investigate:
                                if key.c == ord(corpse[0]):
					my_location = find_location(party,world)
                                        finished_investigating = show_character(corpse[1],world,True,my_location)
					finished_investigating = True
					return finished_investigating
                        for person in people_to_investigate:
                                if key.c == ord(person[0]):
					my_location = find_location(party,world)
                                        finished_investigating = show_character(person[1],world,False,my_location)
                                        finished_investigating = True
                                        return finished_investigating
                        for container in containers_to_investigate:
                                if key.c == ord(container[0]):
                                        my_location = find_location(party,world)
                                        finished_investigating = show_container(container[1],party,world)
                                        finished_investigating = True
                                        return finished_investigating



		elif key.c == ord('r'):
		        finished_viewing = True
	                finished_investigating = True
			return finished_investigating
	return finished_investigating

def show_options(my_location,line_count):
	#check if safehouse
	#if my_location.is_safehouse == False:
	#	libtcod.console_print(0,1,20, '[p]arty, [t]ravel')
	#elif my_location.is_safehouse == True:
	#	libtcod.console_print(0,1,20, '[p]arty, [r]est, [t]ravel')


	libtcod.console_print(0,1,line_count, "ACTIONS:")
	line_count += 1

	#check if we can loot
	can_loot = False
	for item in my_location.items:
		print item.item_type
		if item.item_type == 'junk' and item.can_loot == True:
			can_loot = True
		elif item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'medical' or item.item_type == 'limb':
			can_loot = True
	#check for NPCs
	actors_here = False
	if len(my_location.actors.members) == 0:
		actors_here = False
	elif len(my_location.actors.members) >= 1:
		print my_location.actors.members
		actors_here = True

	#check for options
	options = []
	#attack
	if actors_here == True:
		options.append('[a]ttack')
	#barter
	if my_location.is_store == True and world.time.hour >= my_location.time_open and world.time.hour <= my_location.time_close:
		options.append('[b]usiness')
	#
	#investigate
	containers_here = False
	for items in my_location.items:
		if item.item_type == 'container':
			containers_here = True
	if len(my_location.corpses) >= 1 or len(my_location.actors.members) >= 1 or containers_here == True:
		options.append('[i]nvestigate')
	
	#loot
	if can_loot == True:
		options.append('[l]oot')
	#party
	options.append('[p]arty')
	#rest
	if my_location.is_safehouse == True:
		options.append('[r]est')
        #speak
        if actors_here == True:
                options.append('[s]peak')
	#travel
	options.append('[t]ravel')
	#wait
	options.append('[w]ait')

	if len(options) <= 5:
		option_string = ', '.join(options)
		libtcod.console_print(0,1,line_count, option_string)
	elif len(options) >= 6:
		num_options = len(options)
		option_count = 1
		first_options = []
		second_options = []
		while option_count <= 5:
			for option in options:
				first_options.append(option)
				options.remove(option)
				option_count += 1
		while option_count >= 6 and option_count <= num_options:
			for option in options:
				second_options.append(option)
				option_count += 1
		option_string1 = ', '.join(first_options)
		option_string2 = ', '.join(second_options)
                libtcod.console_print(0,1,line_count, option_string1)
		line_count += 1
                libtcod.console_print(0,1,line_count, option_string2)



	libtcod.console_flush()


def handle_party_drugs(party,world):
	for member in party.members:
		member.handle_drugs()

def handle_party_mind(party):
	for member in party.members:
		member.handle_mind()

def handle_npcs(party,world):
	regulars = []	
	my_location = find_location(party,world)
	#who lives here and are they home
	#for area in world.areas:
	#	for location in area.locations:
	#		for npc in location.actors.members:
	#			if npc.home == my_location:
	#				regulars.append(npc)
	#			if len(location.rooms) >= 2:
	#				for room in location.rooms:
	#					for npc in room.actors.members:
	#						if npc.home == my_location:
	#							regulars.append(npc)
	#							if npc in area.randos:
	#								area.randos.remove(npc)
	#	print area.randos
	#	for rando in area.randos:
	#		if rando == None:
	#			area.randos.remove(rando)
	#		elif rando.home == my_location:
	#			chance_home = random.randint(1,2)
	#			if rando not in my_location.actors.members:
	#				regulars.append(rando)
	#				area.randos.remove(rando)
	#add actors
	my_area = find_area(party,world)

	#check for chars in this location who live here
        for actor in my_location.actors.members:
		if actor == None:
			my_location.actors.members.remove(actor)
		elif actor.home == my_location:
			chance = 1
			if chance == 1:
                		regulars.append(actor)
				my_location.actors.members.remove(actor)
        for actor in my_location.actors.members:
		my_area.randos.append(actor)
		my_location.actors.members.remove(actor)




	my_area = find_area(party,world)
	#is this a bar 
	try:
		if my_location.is_bar == True and world.time.hour >= my_location.time_open and world.time.hour <= my_location.time_close:
        		my_location.actors = []
        	        try:
        	        	num_regulars = random.randint(2,3)
        	        except:
        	        	num_regulars = 3
			if my_location.is_hq == True:
				num_regulars = random.randint(5,8)
        	        if len(my_location.regulars) >= 1:
        	                possible_regulars = my_location.regulars
        	        else:
        	                possible_regulars = []
        	        count = 1
        	        regulars = []
        	        while count <= num_regulars:
        	        	try:
        	                	regular = random.choice(my_location.regulars)
        	                        possible_regulars.remove(regular)
        	                        regulars.append(regular)
        	                        possible_regulars.remove(regular)
        	                        count += 1
        	                except:
        	                        count +=1

			my_location.actors = NPC(regulars,0,[],0)
	except:
		my_location.actors = NPC([],0,[],0)
	if my_location.is_bar == True:
		num_randos = random.randint(1,7)
	else:
		num_randos = random.randint(0,5)
	#what random people are here

	randos = []
	rando_count = random.randint(1,6)
	print len(my_area.randos)
	#standard location
	if my_location.is_hq == False and my_location.is_apt == False:
		while rando_count <= num_randos:
		#	#print my_area.randos
		        regular = random.choice(my_area.randos)
        	        regulars.append(regular)
        	        rando_count += 1
	#apt
	#if my_location.is_hq == False and my_location.is_apt == True:
	#	rando_chance = random.randint(1,6)
	#	if rando_chance == 1:
	#		rando_count = 1
	#		num_rando = random.randint(1,3)
	#		while rando_count <= num_rando:
	#			regular = random.choice(my_area.randos)
	#			regulars.append(regular)
	#			rando_count += 1
	#if len(my_location.actors.members) >= 1:
	#	for npc in my_location.actors.members:
	#		regulars.append(npc)

        my_location.actors = NPC(regulars,0,[],0)



#rest
def rest(party,world,hours,guard):
	messages = []
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	count = 1
	interrupted = False
	while count <= hours and interrupted == False:
		owned = False
		#do we own this location
		for location in world.player_organization.locations_owned:
			if location == my_location:
				owned = True
		drugs_value = party.money
		for item in party.inventory:
			drugs_value += item.base_value
                #chance to be robbed
                if my_location.owned_by != 'No one':
	                chance = random.randint(1,40)
                        if chance == 1:
        	                for organization in my_area.organizations:
                	                if organization.name == my_location.owned_by and organization.player_reputation <= 24:
                        	                robbery(party,world,True)
                                                interrupted = True
                                                return interrupted
                elif drugs_value >= 2000 and my_location.owned_by == 'No one':
                	chance = drugs_value / 1000
                        chance_robbery = random.randint(1,500)
                        if chance_robbery <= chance:
                        	robbery(party,world,False)
                               	interrupted = True
                               	return interrupted

		#did anyone steal from us
		steal_chance = random.randint(1,50)
		if steal_chance == 1 and owned == False and guard == 'No one':
			items_to_steal = []
			for item in party.inventory:
				items_to_steal.append(item)
			for member in party.members:
				if member.weapon != 'Punch':
					items_to_steal.append(member.weapon)
				if member.outfit != 'Naked':
					items_to_steal.append(member.outfit)
			stolen_item = random.choice(items_to_steal)
			try:
				item_found = False
				while item_found == False:
					for item in party.inventory:
						if item == stolen_item:
							party.inventory.remove(item)
							item_found = True
			except:
				for member in party.members:
					if stolen_item == member.weapon:
						member.weapon = punch
					elif stolen_item == member.outfit:
						member.outfit = naked
			message = stolen_item.name + " was stolen!"
			show_stolen = True
                        libtcod.console_clear(0)

			while show_stolen == True:
		                libtcod.console_print(0,1,1, message)
		                libtcod.console_print(0,1,2, '[c]ontinue')
				libtcod.console_flush()
	                        key = libtcod.console_check_for_keypress()
				if key.c == ord('c'):
					show_stolen = False


		messages = []
		#beds? cats?
		beds = []
		cats = []
		for item in my_location.items:
			if item.name == "Sleeping bag" or item.name == "Bed" or item.name == "Couch":
				beds.append(item)
			if item.name == 'Cat':
				cats.append(cat)
                for item in party.inventory:
                        if item.name == "Sleeping bag":
                                beds.append(item)

		#handle drugs
		handle_party_drugs(party,world)
		#handle npcs
		handle_npcs(party,world)
		#handle health
		for member in party.members:
			member.health.current_health += 1
			if member.mind.stress >= 40:
				member.mind.stress -= random.randint(1,2)
			if member.mind.happiness <= 40:
				member.mind.happiness = random.randint(1,3)
		
			if member.health.bleeding_rate  >= 1:
				member.bleed()
			if member == guard:
				member.health.current_stamina -= 5
				if member.health.current_stamina <= 0:
					member.health.current_stamina = 0
		#handle time
		day = world.time.day
                world.time.hour += 1
		world.time.correct()
		if day != world.time.day:
                	my_area.clean_up() 

		count += 1
		#handle cats
		if len(cats) >= 1:
			if len(cats) >= 2:
				cat_bonus = 4
			else:
				cat_bonus = 2
			for member in party.members:
				member.mind.happiness += cat_bonus
		#handle minds
		handle_party_mind(party)
		for member in party.members:
			if member.mind.trauma >= 1 and member != guard:
				member.mind.trauma -= 1
		#hunger & thirst
		for member in party.members:
			member.hunger += 3
			member.thirst += 5
		#handle npcs
		handle_npcs(party,world)
		#sleeping
		messages = []
		for member in party.members:
                        if member != guard and member.sleep <= 70:
                                if len(beds) >= 1:

                                        bed_used = random.choice(beds)
                                        message = member.fname + " " + member.lname + " slept. (" + bed_used.name + ")"
                                        messages.append(message)
                                        beds.remove(bed_used)
                        		if member.health.current_health  <= (member.health.max_health - 1):
                                        	member.health.current_health += random.randint(2,4)
                                        member.sleep += 15
					member.health.current_stamina += 15
                                else:
                                        member.health.current_health += 1
					member.sleep += random.randint(1,13)
					message = member.fname + " " +  member.lname + " slept."
					messages.append(message)
					member.health.current_stamina += 10
                        elif member != guard and member.sleep >= 71:
				print 'relax'
                        	if member.health.current_health  <= (member.health.max_health - 1):
					member.health.current_health += 4
				message = member.fname + " " + member.lname + " relaxed."
				member.health.current_stamina += 10
				messages.append(message)

			elif member == guard:
				member.sleep -= 5
				if member.sleep <= 0:
					member.sleep = 0
				message = guard.fname + " " + guard.lname + " stood guard."
				messages.append(message)

		show_actions = True
                libtcod.console_clear(0)

                while show_actions == True:
			line_count = 1
			for message in messages:
                               	libtcod.console_print(0,1,line_count, message)
				line_count += 1
                        libtcod.console_print(0,1,line_count + 2, '[c]ontinue')
                        libtcod.console_flush()
                        key = libtcod.console_check_for_keypress()
                        if key.c == ord('c'):
                        	show_actions = False
				return messages
		save_game()
		return messages
def robbery(player_party,world,faction):
	libtcod.console_clear(0)
	being_robbed = True
	my_location = find_location(player_party,world)
	my_area = find_area(player_party,world)
	num_robbers = random.randint(2,6)
	robber_count = 1
	robbers = []
	if faction == False:
		while robber_count <= num_robbers:
			robber = random.choice(my_area.randos)
			robbers.append(robber)
			robber_count += 1
		robbers_party = NPC(robbers,100 * num_robbers,[],3 * num_robbers)
	elif faction == True:
		for organization in my_area.organizations:
			if my_location.owned_by == organization.name:
				faction_here = organization.name
				while robber_count <= num_robbers:
					robber = random.choice(organization.footsoldiers)
					robbers.append(robber)
					robber_count += 1
		robbers_party = NPC(robbers,100 * num_robbers,[],3 * num_robbers)

	choice_made = False
	while choice_made == False:
		line_count = 1
		if faction == False:
        		libtcod.console_print(0,1,line_count, str(num_robbers) + " robbers approach you and demand all your stuff!")
                elif faction == True:
                        libtcod.console_print(0,1,line_count, str(num_robbers) + " " + faction_here + " approach you and demand all your stuff:")
			line_count += 2
                        libtcod.console_print(0,1,line_count, "This is our motherfuckin' turf...")

		line_count+= 2
                libtcod.console_print(0,1,line_count, "[f]ight!")
		line_count += 1
                libtcod.console_print(0,1,line_count, "[s]urrender")
		libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
		if key.c == ord('f'):
			for member in robbers_party.members:
				if faction == False:
					try:
						my_area.randos.remove(member)
					except:
						continue
				if faction == True:
					for organization in my_area.organizations:
						if faction_here == organization.name:
							try:
								organization.footsoldiers.remove(member)
							except:
								continue
			battle(player_party,robbers_party,my_location,world,True)
			choice_made = True
		elif key.c == ord('s'):
			for member in player_party.members:
				member.outfit = naked
				member.weapon = punch
			player_party.inventory = []
			player_party.money = 0
			choice_made = True
	return True
def deal_drugs(party,world,length_time):
	finished_dealing = False

        libtcod.console_clear(0)
	drugs_in_inventory = []
        line_count = 1


        drugs_in_inventory = []
	options= []
	drug_count = 1
        for item in party.inventory:
	        if item.name == "Crack" or item.name == "Weed" or item.name == "Cocaine" or item.name == "Morphine" or item.name == "Speed" or item.name == "Heroin":
			letter = num_to_letter(drug_count)
			option = [letter, item]
        	        options.append(option)
			drug_count += 1
	drug_chosen = False

	if len(options) <= 0:
		libtcod.console_print(0,1,line_count,"You have no drugs")
		libtcod.console_print(0,1,line_count + 2,"[b]ack")
		libtcod.console_flush()
		confirm = False
		while confirm == False:
			key = libtcod.console_check_for_keypress()
			if key.c == ord('b'):
				finished_dealing = True
				return finished_dealing
	elif len(options) >= 1:
		libtcod.console_clear(0)
		libtcod.console_print(0,1,line_count,"SELL WHICH DRUGS:")
		line_count += 1
		for option in options:
			libtcod.console_print(0,1,line_count,"[" + option[0] + "]" + option[1].name + "(" + str(option[1].number) + ")")
			line_count += 1
		libtcod.console_flush()
		while drug_chosen == False:
			key = libtcod.console_check_for_keypress()
			for option in options:
				print key.c
				if key.c == ord(option[0]):
					drug_to_sell = option[1]
					drug_chosen = True

		libtcod.console_clear(0)
		hour_count = 0
		my_location = find_location(party,world)
		my_area = find_area(party,world)
		total_streetwise = 0
		total_disguise = 0
		total_negotiate = 0
		for member in party.members:
			total_streetwise += member.skills.streetwise
			total_disguise += member.skills.disguise
			total_negotiate += member.skills.negotiate
		hour_count = 1
		interrupted = False
		while hour_count <= length_time and interrupted == False:
			roll = random.randint(1,20)
			drugs_value = player_party.money
			for item in party.inventory:
				if item.item_type == 'medical':
					drugs_value += item.base_value * item.number
			#chance to be robbed
			if my_location.owned_by != 'No one':
				chance = random.randint(1,20)
				if chance == 1:
					for organization in my_area.organizations:
						if organization.name == my_location.owned_by:
							robbery(party,world,True)
							interrupted = True
							return interrupted
			elif drugs_value >= 1000 and my_location.owned_by == 'No one':
				chance = drugs_value / 1000
				chance_robbery = random.randint(1,250)
				if chance_robbery <= chance:
					robbery(party,world,False)
					interrupted = True
					return interrupted
			if roll <= total_streetwise + 1:
				found_item = False
				while found_item == False:
					for item in party.inventory:
						if item.name == drug_to_sell.name and item.number == drug_to_sell.number:
							if item.number >= 2:
								num_sold = random.randint(1,item.number)
							else:
								num_sold = 1
							if item.number == 1:
								party.inventory.remove(drug_to_sell)
							elif item.number >= 2 and item.number >= num_sold:
								item.number -= num_sold
                                                        elif item.number <= num_sold or item.number == 0:
                                                                party.inventory.remove(drug_to_sell)

							if item.base_value <= 99:
								profit = (total_negotiate * (item.base_value / 45 ) * num_sold)
                                                        elif item.base_value >= 100:
                                                                profit = (total_negotiate * (item.base_value / 100 ) * num_sold)
							if item.number >= 1:
								total_money = profit + (item.base_value * num_sold)
								party.money += total_money
								libtcod.console_print(0, 1, line_count,"You sold " + str(num_sold) + " " + drug_to_sell.name + " for $" + str(total_money) +  ".")
								line_count += 1
							elif item.number == 0:
                                                                party.inventory.remove(drug_to_sell)

							disguise_roll = random.randint(1,20)
							if disguise_roll >= total_disguise: 
								for organization in my_area.organizations:
									if organization.name == my_location.owned_by:
										organization.player_reputation -= 1
										party.fame += 1
							for member in party.members:
								member.health.current_stamina -= random.randint(2,8)
								skill_chance = random.randint(1,80)
								if skill_chance == 1:
									member.skills.streetwise += 1
	                                                        	libtcod.console_print(0,1,line_count,member.fname + " " + member.lname + "'s Streetwise is now " + str(member.skills.streetwise) + "." )
									line_count += 1
								elif skill_chance == 2:
									member.skills.negotiate += 1
									libtcod.console_print(0,1,line_count,member.fname + " " + member.lname + "'s Negotiate is now " + str(member.skills.negotiate) + ".")
									line_count += 1
							line_count += 1
							hour_count += 1
							found_item = True
					if found_item == False:
						libtcod.console_print(0,1,line_count,"You have no drugs left.")
						line_count += 1
						hour_count += 1
						found_item = True
			elif roll >= total_streetwise:
			        libtcod.console_print(0, 1, line_count,"You found no customers.")
                	        line_count += 1
				hour_count += 1
		hour = world.time.hour
		world.time.hour += length_time
                world.time.correct()
                if world.time.hour >= hour + 1 or world.time.hour == 0 and hour >= world.time.hour:
                        for member in party.members:
                                member.handle_mind()
                                member.hunger += 5 * length_time
                                if member.hunger >= 101:
                                        member.hunger = 100
                                member.thirst += 7 * length_time
                                if member.thirst >= 101:
                                        member.thirst = 100
                                member.sleep -= 4 * length_time
                                if member.sleep <= -1:
                                        member.sleep = 0 
                for member in party.members:
                        if member.health.bleeding_rate >= 1:
				bleed_count = 1
				while bleed_count <= length_time:
                                	member.bleed()
					bleed_count += 1
                        chance = random.randint(1,3)
                        member.health.current_stamina -= 1 * length_time
                #world.time.correct()
                my_location = find_location(party,world)

		line_count += 1
	        libtcod.console_print(0, 1, line_count,"[b]ack")
		libtcod.console_flush()
		while finished_dealing == False:
			key = libtcod.console_check_for_keypress()
	                if key.c == ord('b'):
	                        print 'b'
	                        finished_dealing = True
	                        return finished_dealing


			

def deal(party,world):
        finished_dealing = False
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"How long will you deal drugs?")
	libtcod.console_print(0,1,2,"[1] hour, [2] hours, [4] hours")
	libtcod.console_flush()
        while finished_dealing == False:
		key = libtcod.console_check_for_keypress()
         	if key.c == ord('1'):
		        deal_drugs(party,world,1)
       			finished_dealing = True
       			return finished_dealing
                elif key.c == ord('2'):
                        deal_drugs(party,world,2)
                        finished_dealing = True
                        return finished_dealing
                elif key.c == ord('4'):
                        deal_drugs(party,world,4)
                        finished_dealing = True
                        return finished_dealing





def make_safehouse(party,world):
	finished_safehouse = False
	libtcod.console_clear(0)
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	vacant_apt = False
	#print location.name
	if party.location.name == "Vacant Apartment":
		vacant_apt = True
		libtcod.console_print(0,1,1,"It will close $2000/month and a $2000 deposit to rent this apartment.")
		libtcod.console_print(0,1,3,"[r]ent, [b]ack")
	else:
		libtcod.console_print(0,1,1, "This isn't a apartment you can rent.")
		libtcod.console_print(0,1,3, "[b]ack")
	libtcod.console_flush()
	while finished_safehouse == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('b'):
			finished_safehouse = True
			return finished_safehouse
		if key.c == ord('r') and party.location.name == "Vacant Apartment" and party.money >= 4000:
			party.money -= 4000
			party.location.is_safehouse = True
			party.location.items.append(bed)
			party.location.owned_by = 'Player'
			party.location.name = 'Your Apartment'
			world.player_organization.locations_owned.append(party.location)
			world.player_organization.rent_paid = "True"
			world.player_organization.month = world.time.month
			finished_safehouse = True
			return finished_safehouse
def furnish_safehouse(party,world):
	my_apartment = False
	libtcod.console_clear(0)
	line_count = 1
	if party.location.name == "Your Apartment":
		libtcod.console_print(0,1,line_count,"FURNISH APARTMENT:")
		my_apartment = True
		line_count += 1
	elif party.location.name != "Your Apartment":
		libtcod.console_print(0,1,line_count,"This is not your apartment.")
		line_count += 1

	if party.location.name == "Your Apartment":
		options = []
		item_count = 1
		for item in furniture:
			letter = num_to_letter(item_count)
			option = [letter,item]
			options.append(option)
			item_count += 1
		for option in options:
			libtcod.console_print(0,1,line_count,"[" + option[0] + "]" + option[1].name)
			libtcod.console_print(0,24,line_count,"$" + str(option[1].base_value))
			line_count += 1
	line_count += 1
	libtcod.console_print(0,1,line_count,'[r]eturn')
	libtcod.console_flush()
	finished_furnish = False
	while finished_furnish == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('r'):
			finished_furnish = True
			return True
		if my_apartment == True:
			for option in options:
				if key.c == ord(option[0]):
					if party.money >= option[1].base_value:
						party.location.items.append(option[1])
						party.money -= option[1].base_value
						finished_furnish = True
						return True
def show_actions(party,world):
	finished_action = False
        line_count = 1
        libtcod.console_print(0, 1, line_count,"ACTIONS")
	line_count += 2
        libtcod.console_print(0, 1, line_count,"[a] deal drugs")
	line_count += 1
	libtcod.console_print(0,1,line_count,"[b] rent apartment")
	line_count += 1
	libtcod.console_print(0,1,line_count, "[c] furnish apartment")
	line_count += 2
	libtcod.console_print(0, 1, line_count,"[r]eturn")
	libtcod.console_flush()

	while finished_action == False:
		key = libtcod.console_check_for_keypress()
                if key.c == ord('r'):
                        #print 'b'
                        finished_action = True
                        return finished_action
		elif key.c == ord('a'):
			deal_drugs(party,world,1)
			finished_action = True
			return finished_action
		elif key.c == ord('b'):
			make_safehouse(party,world)
			finished_action = True
			return finished_action
		elif key.c == ord('c'):
			furnish_safehouse(party,world)
			finished_action = True
			return finished_action



def show_rest(party,world):
	finished_resting = False
	libtcod.console_clear(0)
	line_count = 1
        libtcod.console_print(0, 1, line_count,"Who will guard?")
	line_count += 2
	possible_guards = []
	member_count = 1
	for member in party.members:
		letter = num_to_letter(member_count)
		possible_guard = [letter,member]
		possible_guards.append(possible_guard)
		member_count += 1
	for possible_guard in possible_guards:
	        libtcod.console_print(0, 1, line_count, "[" + possible_guard[0] + "] " + possible_guard[1].fname + " " + possible_guard[1].lname)
		line_count += 1
	line_count += 1
        libtcod.console_print(0, 1, line_count,"[n]o one")

	line_count += 2
	libtcod.console_print(0, 1, line_count,"[r]eturn")
	libtcod.console_flush()
	finished_resting = False
        while finished_resting == False:
                key = libtcod.console_check_for_keypress()
                if key.c == ord('r'):
                        #print 'b'
                        finished_resting = True
                        return finished_resting
		elif key.c== ord('n'):
			rest(party,world,1,'No one')
			finished_resting = True
			return finished_resting
                elif key.c != ord('b') or key.c != ord('n'):
			for possible_guard in possible_guards:
				if key.c == ord(possible_guard[0]):
                        		rest(party,world,1,possible_guard[1])
                        		finished_resting = True
                        		return finished_resting

def wait(party,world,hours):
        my_area = find_area(party,world)
        count = 1
        while count <= hours:


                #handle drugs
                handle_party_drugs(party,world)
		handle_party_mind(party)
		handle_npcs(party,world)
                #handle health
                for member in party.members:
                        #if member.health.current_health  <= (member.health.max_health - 1):
                        #        member.health.current_health += 1
                        if member.health.bleeding_rate  >= 1:
                                member.bleed()
                        if member.health.current_stamina <= 100:
                                member.health.current_stamina -= random.randint(5,10)
				if member.health.current_stamina <= 0:
					member.health.current_stamina = 0
			if member.mind.happiness >= 20:
				member.mind.happiness -= random.randint(1,2)
			member.hunger += 6
                #handle time
                day = world.time.day
                world.time.hour += 1
                world.time.correct()
                if day != world.time.day:
                        my_area.clean_up() 

                count += 1
		
                waiting = True
                while waiting == True:
                        libtcod.console_clear(0)
                        libtcod.console_print(0,1,1, 'Waiting.')
                        libtcod.console_flush()
                        save_game()
                        waiting = False


def show_wait(party,world):
        finished_resting = False
        libtcod.console_clear(0)
        line_count = 1
        libtcod.console_print(0, 1, line_count,"Wait for how long?")
        line_count += 2
        libtcod.console_print(0, 1, line_count,"[1] hour, [2] hours, [4] hours, [8] hours")
        line_count += 2
        libtcod.console_print(0, 1, line_count,"[b]ack")
        libtcod.console_flush()
        finished_resting = False
        while finished_resting == False:
                key = libtcod.console_check_for_keypress()
                if key.c == ord('b'):
                        #print 'b'
                        finished_resting = True
                        return finished_resting
                elif key.c== ord('1'):
                        wait(party,world,1)
                        finished_resting = True
                        return finished_resting
                elif key.c== ord('2'):
                        wait(party,world,2)
                        finished_resting = True
                        return finished_resting

                elif key.c== ord('4'):
                        wait(party,world,4)
                        finished_resting = True
                        return finished_resting
                elif key.c== ord('8'):
                        wait(party,world,8)
                        finished_resting = True
                        return finished_resting

def show_character(target,world,corpse,my_location):
	libtcod.console_clear(0)
        libtcod.console_print(0, 1, 1,target.fname + " " + target.lname)
        libtcod.console_print(0, 1, 2, target.profession)
        libtcod.console_print(0, 1, 3, target.gender)
        libtcod.console_print(0, 1, 4, "Age: " + str(target.age))
        libtcod.console_print(0, 25, 1, target.outfit.name)
        libtcod.console_print(0, 25, 2, target.weapon.name)

	drug_count = 1
	for drug in set(target.drugs):
		libtcod.console_print(0,40,drug_count,drug.name)
		drug_count += 1


        libtcod.console_print(0, 1, 7, "STR: " + str(target.stats.strength))
        libtcod.console_print(0, 1, 8, "DEX: " + str(target.stats.dexterity))
        libtcod.console_print(0, 1, 9, "INT: " + str(target.stats.intelligence))
        libtcod.console_print(0, 1, 10, "WIL: " + str(target.stats.willpower))
        libtcod.console_print(0, 1, 11, "CHA: " + str(target.stats.charisma))

        trait_count = 1
        for trait in target.traits:
		if trait_count <= 5:
                	libtcod.console_print(0,10,trait_count + 6, str(trait.name))
                	trait_count += 1
		elif trait_count >= 6 and trait_count <= 10:
                        libtcod.console_print(0,30,trait_count + 1, str(trait.name))
                        trait_count += 1
		elif trait_count >= 11 and trait_count <= 15:
                        libtcod.console_print(0,50,trait_count - 4, str(trait.name))
			trait_count += 1

	if corpse == False:
		libtcod.console_print(0, 1, 13, "Health:")
		libtcod.console_print(0, 9, 13, str(target.health.current_health) + " / " + str(target.health.max_health))
		libtcod.console_print(0, 20, 13, "Max Health:")
		libtcod.console_print(0, 33, 13, str(target.health.base_max) + "")


        	libtcod.console_print(0, 1, 14, "Blood:")
        	libtcod.console_print(0, 9, 14, str(target.health.current_blood))
        	libtcod.console_print(0, 20, 14, "Rate bleed:")
        	libtcod.console_print(0, 35, 14, str(target.health.bleeding_rate))

        	libtcod.console_print(0, 1, 15, "Stamina:")
        	libtcod.console_print(0, 9, 15, str(target.health.current_stamina))
        	libtcod.console_print(0, 20, 15, "Pain:")
        	libtcod.console_print(0, 35, 15, str(target.health.current_pain))

                libtcod.console_print(0, 1, 17, "Hunger:")
                libtcod.console_print(0, 12, 17, str(target.hunger))
                libtcod.console_print(0, 1, 18, "Thirst:")
                libtcod.console_print(0, 12, 18, str(target.thirst))
                libtcod.console_print(0, 20, 17, "Sleep:")
                libtcod.console_print(0, 32, 17, str(target.sleep))




                libtcod.console_print(0, 1, 20, "MOOD:")
                libtcod.console_print(0, 1, 21, "Happiness:")
                libtcod.console_print(0, 12, 21, str(target.mind.happiness))
                libtcod.console_print(0, 1, 22, "Stress:")
                libtcod.console_print(0, 12, 22, str(target.mind.stress))
                libtcod.console_print(0, 1, 23, "Sanity:")
                libtcod.console_print(0, 12, 23, str(target.mind.sanity))
                libtcod.console_print(0, 1, 24, "Horny:")
                libtcod.console_print(0, 12, 24, str(target.mind.horny))
                libtcod.console_print(0, 1, 25, "Trauma:")
                libtcod.console_print(0, 12, 25, str(target.mind.trauma))
	#	if addiction.addiction_level >= 1:
	#		has_addiction = True
	#		print addiction.name
		

        	libtcod.console_print(0, 20, 20, 'ADDICTIONS:')
        	libtcod.console_print(0, 20, 21, 'Amphetamines:')
                libtcod.console_print(0, 35, 21, str(target.mind.addictions.speed.addiction_level))
        	libtcod.console_print(0, 20, 22, 'Caffeine:')
                libtcod.console_print(0, 35, 22, str(target.mind.addictions.caffeine.addiction_level))
        	libtcod.console_print(0, 20, 23, 'Cocaine:')
                libtcod.console_print(0, 35, 23, str(target.mind.addictions.cocaine.addiction_level))
        	libtcod.console_print(0, 20, 24, 'Nicotine:')
                libtcod.console_print(0, 35, 24, str(target.mind.addictions.nicotine.addiction_level))
        	libtcod.console_print(0, 20, 25, 'Opioids:')
                libtcod.console_print(0, 35, 25, str(target.mind.addictions.opiates.addiction_level))

	elif corpse == True:
        	libtcod.console_set_default_foreground(0, libtcod.red) 
                libtcod.console_print(0,1,20, "DEAD")
                libtcod.console_set_default_foreground(0, libtcod.white)

	if len(target.injuries) == 0:
		libtcod.console_print(0,1,27,"No injuries.")
        elif len(target.injuries) >= 1:
                libtcod.console_print(0,1,27,"INJURIES.")
	injury_count = 1
        for injury in target.injuries:
                if injury_count <= 5:
                        libtcod.console_print(0, 1, injury_count + 27, injury.name + "(" + injury.location + ")")
                        injury_count += 1 
                elif trait_count >= 6 and trait_count <= 10:
                        libtcod.console_print(0, 30, injury_count + 22, injury.name + "(" + injury.location + ")")
                        injury_count += 1



	libtcod.console_print(0,1,35, "SKILLS:")
        libtcod.console_print(0,1,36, "Brawl:")
        libtcod.console_print(0,1,37, "Computer:")
        libtcod.console_print(0,1,38, "Dodge:")
        libtcod.console_print(0,1,39, "Disguise:")
        libtcod.console_print(0,1,40, "Etiquette:")
        libtcod.console_print(0,1,41, "Explosive:")
        libtcod.console_print(0,1,42, "First Aid:")
        libtcod.console_print(0,1,43, "Investigate:")
        libtcod.console_print(0,1,44, "Leadership")
        libtcod.console_print(0,1,45, "Lie:")
        libtcod.console_print(0,1,46, "Negotiate:")

        libtcod.console_print(0,20,36, "Persuade:")
        libtcod.console_print(0,20,37, "Pickpocket:")
        libtcod.console_print(0,20,38, "Pistol:")
        libtcod.console_print(0,20,39, "Rifle:")
        libtcod.console_print(0,20,40, "Security:")
        libtcod.console_print(0,20,41, "Seduction:")
        libtcod.console_print(0,20,42, "Shotgun:")
        libtcod.console_print(0,20,43, "Stealth:")
        libtcod.console_print(0,20,44, "Streetwise:")
        libtcod.console_print(0,20,45, "Throw:")
        libtcod.console_print(0,20,46, "Torture:")

        libtcod.console_print(0,15,36, str(target.skills.brawl))
        libtcod.console_print(0,15,37, str(target.skills.computers))
        libtcod.console_print(0,15,38, str(target.skills.dodge))
        libtcod.console_print(0,15,39, str(target.skills.disguise))
        libtcod.console_print(0,15,40, str(target.skills.etiquette))
        libtcod.console_print(0,15,41, str(target.skills.explosives))
        libtcod.console_print(0,15,42, str(target.skills.first_aid))
        libtcod.console_print(0,15,43, str(target.skills.investigate))
        libtcod.console_print(0,15,44,str(target.skills.leadership))
        libtcod.console_print(0,15,45, str(target.skills.lying))
        libtcod.console_print(0,15,46, str(target.skills.negotiate))

        libtcod.console_print(0,35,36, str(target.skills.persuasion))
        libtcod.console_print(0,35,37, str(target.skills.pickpocket))
        libtcod.console_print(0,35,38, str(target.skills.pistol))
        libtcod.console_print(0,35,39, str(target.skills.rifle))
        libtcod.console_print(0,35,40, str(target.skills.security))
        libtcod.console_print(0,35,41, str(target.skills.seduction))
        libtcod.console_print(0,35,42, str(target.skills.shotgun))
        libtcod.console_print(0,35,43, str(target.skills.stealth))
        libtcod.console_print(0,35,44,str(target.skills.streetwise))
        libtcod.console_print(0,35,45, str(target.skills.throw))
        libtcod.console_print(0,35,46, str(target.skills.torture))


	libtcod.console_print(0,1,48, "[b]ack")
	if corpse == True and target.outfit.name != 'Naked':
		libtcod.console_print(0,20,48, "[s]trip")

	libtcod.console_flush()

	finished_viewing = False
	while finished_viewing == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('b'):
			#print 'b'
			finished_viewing = True
			return finished_viewing
		elif key.c == ord('s') and corpse == True and target.outfit.name != 'Naked':
			my_location.items.append(target.outfit)
			target.outfit = naked
			finished_viewing = True
			return finished_viewing
			
def show_outfits(target,world):
        finished_outfits = False
        count = 1
        options_list = []
        options_list2 = []
        libtcod.console_clear(0)
        while finished_outfits == False:
                for member in target.members:
                        option = [count, member]
                        options_list.append(option)
                        libtcod.console_print(0,1,count,"[" + str(count) + "] " + member.fname + " " + member.lname)
                        libtcod.console_print(0,24,count,member.outfit.name)
                        count += 1
                for item in target.inventory:
                        if item.item_type == 'outfit':
                                letter = num_to_letter(count)
                                option = [letter, item]
                                options_list2.append(option)
                                libtcod.console_print(0,1,count + 3,"[" + letter + "] " + item.name)
                                count += 1
		libtcod.console_print(0,1,count + 3,"[r]eturn")
                libtcod.console_flush()
                finished_outfit = False
                while finished_outfit == False:
                        libtcod.console_flush()
                        key = libtcod.console_check_for_keypress()
			if key.c == ord('r'):
				finished_outfit = True
				return finished_outfit
                        for option in options_list:
                                item_key = str(option[0])
                                if key.c == ord(item_key):
                                        if option[1].outfit.name != "Naked":
                                                target.inventory.append(option[1].outfit)
                                        option[1].outfit = naked
                                        finished_outfit = True
                                        return finished_outfit
                        for option in options_list2:
                                item_key = str(option[0])
                                if key.c == ord(item_key):
                                        my_outfit = option[1]
                                        outfit_assigned = False
                                        count += 1
                                        libtcod.console_print(0,1,count + 3,"Use the number keys to assign the outfit to someone.")
                                        count += 2
                                        libtcod.console_print(0,1,count + 3,"[r]eturn")
                                        libtcod.console_flush()

                                        while outfit_assigned == False:
                                                key = libtcod.console_check_for_keypress()
                                                for option in options_list:
                                                        item_key = str(option[0])
                                                        if key.c == ord(item_key):
                                                                if option[1].outfit.name == 'Naked':
                                                                        option[1].outfit = my_outfit
									target.inventory.remove(my_outfit)
                                                                        finished_outfit = True
                                                                        return finished_outfit
                                                                elif option[1].outfit.name != 'Naked':
                                                                        target.inventory.append(option[1].outfit)
                                                                        target.inventory.remove(my_outfit)
                                                                        option[1].outfit = my_outfit
                                                                        finished_outfit = True
                                                                        return finished_outfit
							elif key.c == ord("r"):
								finished_outfit = True
								return finished_outfit

def show_weapons(target,world):
	finished_weapons = False
	count = 1
	options_list = []
	options_list2 = []
	libtcod.console_clear(0)
	while finished_weapons == False:
		libtcod.console_print(0,1,1,"WEAPONS:")
		for member in target.members:
			option = [count, member]
			options_list.append(option)
			libtcod.console_print(0,1,count+1,"[" + str(count) + "] " + member.fname + " " + member.lname)
			libtcod.console_print(0,24,count+1,member.weapon.name)
			count += 1
		for item in target.inventory:
			if item.item_type == 'weapon':
				letter = num_to_letter(count)
				option = [letter, item]
				options_list2.append(option)
				libtcod.console_print(0,1,count + 4,"[" + letter + "] " + item.name)
				count += 1
		libtcod.console_print(0,1,count + 4,"[r]eturn")
		libtcod.console_flush()
		choose_weapon = False
		while choose_weapon == False:
	                libtcod.console_flush()
			key = libtcod.console_check_for_keypress()
			if key.c == ord('r'):
				finished_weapons = True
				return finished_weapons
			for option in options_list:
				item_key = str(option[0])
				if key.c == ord(item_key):
					if option[1].weapon.name != "Punch":
						target.inventory.append(option[1].weapon)
					option[1].weapon = punch
					finished_weapons = True
					return finished_weapons
			for option in options_list2:
				item_key = str(option[0])
				if key.c == ord(item_key):
					my_weapon = option[1]
					weapon_assigned = False
					count += 1
                                        libtcod.console_print(0,1,count + 3,"Use the number keys to assign the weapon to someone.")
                                        count += 2
                                        libtcod.console_print(0,1,count + 3,"[r]eturn")
					libtcod.console_flush()

					while weapon_assigned == False:
			                        key = libtcod.console_check_for_keypress()
			                        for option in options_list:
                		        	        item_key = str(option[0])
                        			        if key.c == ord(item_key):
								if option[1].weapon.name == 'Punch':
                                			        	option[1].weapon = my_weapon
									target.inventory.remove(my_weapon)
                                        				choose_weapon,finished_weapons = True,True
                                        				return finished_weapons
                                                                elif option[1].weapon.name != 'Punch':
                                                                        target.inventory.append(option[1].weapon)
									target.inventory.remove(my_weapon)
                                                                        option[1].weapon = my_weapon
                                                                        choose_weapon,finished_weapons = True,True
                                                                        return finished_weapons
							elif key.c == ord('r'):
								finished_weapons = True
								return finished_weapons	

def check_addiction(target,drug_used):
	print target.fname + " " + target.lname
	if drug_used.name == 'Cocaine' or drug_used.name == 'Crack':
		drug_type = 'Cocaine'
        elif drug_used.name == 'Heroin' or drug_used.name == 'Morphine':
                drug_type = 'Opiates'
        elif drug_used.name == 'Speed' or drug_used.name == 'Meth':
                drug_type = 'Speed'
	print drug_type

	#for addiction in target.mind.addictions:
	#	if addiction.name == drug_type:
        #		addiction.times_used += 1
        #		roll = random.randint(1,10)
        #		roll += target.stats.willpower
        #		if roll <= addiction.addictiveness + addiction.times_used:
        #			addiction.addiction_level += 1
	return target

def use_item(target,world,player_party):

	finished_using = False
        count = 1
        while finished_using == False:
                option = count
                libtcod.console_clear(0)
                libtcod.console_print(0,1,1, "Use what?" )
        
                count = 1
                items = []
                line = 0
                for item in target.inventory:
			if item.item_type == 'medical' or item.item_type == 'food' or item.item_type == 'drink':
                        	letter = num_to_letter(count)
                        	item_to_add = [letter, item]
                        	items.append(item_to_add)
                        	line = count + 3
                                libtcod.console_print(0,1,line, '[' + letter + '] ' + item.name + "(" + str(item.number) + ")" )
                        count += 1
                line += 3       
                libtcod.console_print(0,1,line, '[*] go back.' )
                libtcod.console_flush()
		drugs_used = []
		choose_item = False

		while choose_item == False:

                        key = libtcod.console_check_for_keypress()
			
                        if key.c == ord('*'):
                        	finished_using = True
                                return finished_using 
			
			item_to_use = None

			for item in items:
				#print item
				item_key = str(item[0])
				if key.c == ord(item_key):
					item_to_use = item[1]
					#print item_to_use
                			count = 1
                			people = []
                			line = 0
					libtcod.console_clear(0)
					#libtcod.console_clear(0)
					libtcod.console_print(0,1,1, 'Who will use ' + item_to_use.name + '?')
					for member in target.members:
                               			letter = num_to_letter(count)
						print member
                               			person_to_add = [letter, member]
                               			people.append(person_to_add)
                               			line = count + 3
                               			libtcod.console_print(0,1,line, '[' + letter + '] ' + member.fname + " " + member.lname )
						count += 1
					line += 2
					libtcod.console_print(0,1,line, '[r]eturn')
					libtcod.console_flush()
					choose_person = False
					while choose_person == False:
		                        	key = libtcod.console_check_for_keypress()
						if key.c == ord('r'):
							finished_using = True
							return finished_using
						for member in people:
							item_key = member[0]
							if key.c == ord(item_key):
								#print 'goooo!!! motherfucker!!!'
								if item_to_use.name == 'Morphine' or item_to_use.name == "Heroin":	
									if item_to_use.name == "Morphine":
										member[1].drugs.append(morphine)
										drug_used = [member[1], morphine]
										drugs_used.append(drug_used)
										#print member[1].drugs
										if item_to_use.number >= 2:
											item_to_use.number -= 1
										elif item_to_use.number == 1:
											target.inventory.remove(item_to_use)
									
                                                                	if item_to_use.name == "Heroin":
                                                                	        member[1].drugs.append(heroin)
                                                                                drug_used = [member[1], heroin]
                                                                                drugs_used.append(drug_used)
                                                                	        #print member[1].drugs
                                                                	        if item_to_use.number >= 2:
                                                                	                item_to_use.number -= 1
                                                                	        elif item_to_use.number == 1:
                                                                	                target.inventory.remove(heroin)

									roll = random.randint(1,10)
									roll += member[1].stats.willpower
									if roll <= member[1].mind.addictions.opiates.addictiveness + member[1].mind.addictions.opiates.times_used:
										member[1].mind.addictions.opiates.addiction_level += 1
										member[1].mind.addictions.opiates.times_used += 1
										trait_chosen = False
										while trait_chosen == False:
											negative_trait = random.choice(addiction_traits)
											if negative_trait not in member[1].traits:
												member[1].traits.append(negative_trait)
												member[1].mind.addictions.opiates.traits.append(negative_trait)
												trait_chosen = True
										choose_person = True
										finished_using = True
                                                                elif item_to_use.name == "Cocaine":
                                                                        member[1].drugs.append(cocaine)
                                                                        #print member[1].drugs
                                                                        drug_used = [member[1],cocaine]
                                                                        drugs_used.append(drug_used)
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
                                                                                target.inventory.remove(item_to_use)
                                                                        roll = random.randint(1,10)
                                                                        roll += member[1].stats.willpower
                                                                        if roll <= member[1].mind.addictions.cocaine.addictiveness + member[1].mind.addictions.cocaine.times_used:
                                                                        	member[1].mind.addictions.opiates.addiction_level += 1
                                                                                member[1].mind.addictions.opiates.times_used += 1
                                                                                trait_chosen = False
                                                                                while trait_chosen == False:
                                                                                        negative_trait = random.choice(addiction_traits)
                                                                                        if negative_trait not in member[1].traits:
                                                                                                member[1].traits.append(negative_trait)
												member[1].mind.addictions.cocaine.traits.append(negative_trait)
                                                                                                trait_chosen = True

                                                                                choose_person = True
                                                                                finished_using = True
                                                                elif item_to_use.item_type == "food":
									member[1].hunger -= item_to_use.nutrition
									if member[1].hunger <= 0:
										member[1].hunger = 0
                                                                        #print member[1].drugs
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
                                                                                target.inventory.remove(item_to_use)
                                                                elif item_to_use.name == "Speed":
                                                                        member[1].drugs.append(speed)
                                                                        drug_used = [member[1],morphine]
                                                                        drugs_used.append(drug_used)
                                                                        #print member[1].drugs
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
                                                                                target.inventory.remove(item_to_use)
                                                                        member[1].mind.addictions.speed.times_used += 1
                                                                        roll = random.randint(1,10)
                                                                        roll += member[1].stats.willpower
                                                                        if roll <= member[1].mind.addictions.speed.addictiveness + member[1].mind.addictions.speed.times_used:
                                                                        	member[1].mind.addictions.speed.addiction_level += 1
                                                                                trait_chosen = False
                                                                                while trait_chosen == False:
                                                                                        negative_trait = random.choice(addiction_traits)
                                                                                        if negative_trait not in member[1].traits:
                                                                                                member[1].traits.append(negative_trait)
												member[1].mind.addictions.speed.traits.append(negative_trait)

                                                                                                trait_chosen = True

										choose_person = True
										finished_using = True

                                                                elif item_to_use.name == "Crack":
                                                                        member[1].drugs.append(crack)
									drug_used = [member[1], crack]
									drugs_used.append(drug_used)
                                                                        #print member[1].drugs
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
										try:
                                                                                	target.inventory.remove(crack)
										except:
											for item in target.inventory:
												if item.name == item_to_use.name:
													target.inventory.remove(item_to_use)
                                                                        member[1].mind.addictions.cocaine.times_used += 1
                                                                        roll = random.randint(1,10)
                                                                        roll += member[1].stats.willpower
                                                                        if roll <= member[1].mind.addictions.cocaine.addictiveness + member[1].mind.addictions.cocaine.times_used:
                                                                        	member[1].mind.addictions.cocaine.addiction_level += 1
                                                                                trait_chosen = False
                                                                                while trait_chosen == False:
                                                                                        negative_trait = random.choice(addiction_traits)
											print negative_trait.name
                                                                                        if negative_trait not in member[1].traits:
                                                                                                member[1].traits.append(negative_trait)
												member[1].mind.addictions.cocaine.traits.append(negative_trait)

                                                                                                trait_chosen = True

										choose_person = True
										finished_using = True

                                                                elif item_to_use.item_type == "drink":
                                                                        member[1].thirst -= item_to_use.nutrition
									if member[1].thirst <= 0:
										member[1].thirst = 0
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
                                                                                target.inventory.remove(item_to_use)


                                                                elif item_to_use.name == "Bandages":
                                                                        member[1].health.bleeding_rate = 0
                                                                        if item_to_use.number >= 2:
                                                                                item_to_use.number -= 1
                                                                        elif item_to_use.number == 1:
                                                                                target.inventory.remove(bandages)
								
								#finished_using = True
								#print drugs_used	
								return drugs_used


def drop_item(target,world):
	finished_dropping = False
	count = 1
	while finished_dropping == False:
		option = count
		libtcod.console_clear(0)
	        libtcod.console_print(0,1,1, "Drop what?" )
	
		count = 1
		items = []
		line = 0
		for item in target.inventory:
			letter = num_to_letter(count)
			item_to_add = [letter, item]
			items.append(item_to_add)
			line = count + 3
			if item.item_type != "medical":
				libtcod.console_print(0,1,line, '[' + letter + '] ' + item.name )
                        elif item.item_type == "medical":
                                libtcod.console_print(0,1,line, '[' + letter + '] ' + item.name + "(" + str(item.number) + ")" )
			count += 1
		line += 3	
		libtcod.console_print(0,1,line, '[r]eturn' )
		libtcod.console_flush()
		#drop item
                key = libtcod.console_check_for_keypress()
		num_items = len(items)
		keys = []
		key_count = 1
		while key_count <= num_items:
			item_key = num_to_letter(key_count)
			keys.append(item_key)
			key_count += 1
		def fetch_item(items,key):
			for item in items:
				if item[0] == str(key):
					print 'found item'
					return item
		#print keys
		if key.c == ord('r'):
			libtcod.console_clear(0)
			finished_dropping = True
		elif key.c == ord('a') or key.c == ord('b') or key.c == ord('c') or key.c == ord('d') or key.c == ord('e') or key.c == ord('f'):
			print items
			for item in items:
				print item[0] + " " + item[1].name
				if ord(item[0]) == key.c:
					my_location = find_location(target,world)
					item = item[1]
					print item.name
					target.inventory.remove(item)
					my_location.items.append(item)
					libtcod.console_clear(0)
					finished_dropping = True
					return finished_dropping
def show_reputation(player,world):
	my_location = find_location(player,world)
	libtcod.console_clear(0)
	libtcod.console_print(0,1,1,"REPUTATION:")
	finished_reputation = False
	count = 3
	for area in world.areas:
		for organization in area.organizations:
			print organization.name
			libtcod.console_print(0,1,count,organization.name)
			libtcod.console_print(0,26,count,str(organization.player_reputation))
			count += 1
	libtcod.console_print(0,1,count + 2,'[r]eturn')
	libtcod.console_flush()
	while finished_reputation == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('r'):
			finished_reputation = True
def show_dismiss(player,world):
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"Dismiss who?")
	options = []
	member_count = 1
	for member in player.members:
		letter = num_to_letter(member_count)
		option = [letter, member]
		options.append(option)
	        libtcod.console_print(0,1,3 + member_count,'[' + option[0] + '] ' + option[1].fname + ' ' + option[1].lname)
		member_count += 1
        libtcod.console_print(0,1,6 + member_count,'[*] go back')
	libtcod.console_flush()
	choice_made = False	
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('*'):
			choice_made = True
		elif key.c != ord('*'):
			for option in options:
				if key.c == ord(option[0]):
					#my_location.actors.members.append(option[0])
					world.player_organization.footsoldiers.append(option[1])
					find_home = False
					while find_home == False:
						if len(world.player_organization.locations_owned) >= 1:
							location = random.choice(world.player_organization.locations_owned)
							option[1].home = location
							location.actors.members.append(option[1])
							find_home = True
						else:
							my_area = find_area(player,world)
							my_area.append(option[1])
							find_home = True
					player.members.remove(option[1])
					choice_made = True
					


def show_manage(player,world):
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"MANAGE PARTY:")
        libtcod.console_print(0,1,3,"[a]ssign leader, [d]ismiss member")
        libtcod.console_print(0,1,4,"[b]ack")

	libtcod.console_flush()
        finished_manage = False
	while finished_manage == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('b'):
			finished_manage = True
		elif key.c == ord('d'):
			show_dismiss(player,world)
			finished_manage = True

def show_party(target,world):
	finished_party = False
	finished_showing = False
	options = []
	def show():
      		libtcod.console_clear(0)

		count = 1
		print target.members
		libtcod.console_flush()	
		count = 1
		item_count = 0
		libtcod.console_print(0,1,1, "TEAM:")
		#options = []
		party_count = 1
		for member in target.members:
			libtcod.console_print(0,1,count+1, "[" +str(count) + "]")
			libtcod.console_print(0,5,count+1, member.fname)
			spacing = len(member.fname) + 6
			libtcod.console_print(0,spacing,count+1, member.lname)
			libtcod.console_print(0,28,count+1, member.profession)
			libtcod.console_print(0,40,count+1, member.outfit.name)
        	        libtcod.console_print(0,56,count+1, member.weapon.name)
			libtcod.console_flush()
			#party.append(member)
			option = [party_count,member]
			options.append(option)
			party_count += 1
			count += 1
		count += 3
		libtcod.console_print(0,1,count, "MONEY:")
		libtcod.console_print(0,40,count, "FAME: " + str(target.fame))
		count += 1
        	libtcod.console_print(0,1,count, "$" + str(target.money))
                count += 2



		#stack medical,food,drink items
		medical = []
		food = []
		drink = []

		for item in target.inventory:
			if item.item_type == 'medical':
				target.inventory.remove(item)
				for other_item in target.inventory:
					if item.name == other_item.name:
						item.number = item.number + other_item.number
						target.inventory.remove(other_item)
				target.inventory.append(item)

		print_line = count + 2
                libtcod.console_print(0,1,print_line, "INVENTORY:")
		item_count = 1
		# types of items
		for item in target.inventory:
			print item.name
                	if item.item_type == 'junk' or item.item_type == 'food' or item.item_type == 'drink':
				if item_count <= 12:
                	        	libtcod.console_print(0,1,print_line + item_count, item.name)
              		        	item_count += 1
                                elif item_count >= 13 and item_count >= 24 :
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1
			elif item.item_type == 'medical':
				if item_count <= 12:
					libtcod.console_print(0,1,print_line + item_count, item.name + "(" + str(item.number) + ")")
					item_count += 1
                                if item_count >= 13 and item_count <= 24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name + "(" + str(item.number) + ")")
                                        item_count += 1

	                elif item.item_type == 'outfit':
				if item_count <= 12:
	                        	libtcod.console_print(0,1,print_line + item_count, item.name)
	                        	item_count += 1
                                if item_count >= 12 and item_count <= 24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1

	                elif item.item_type == 'weapon':
				if item_count <= 12:
	                        	libtcod.console_print(0,1,print_line + item_count, item.name)
	                        	item_count += 1
                                if item_count >= 13 and item_count <=24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1
                        elif item.item_type == 'limb':
				if item_count <= 12:
					string = item.name + "'s " + item.location
                                	libtcod.console_print(0,1,print_line + item_count, string)
                                	item_count += 1
                                if item_count >= 13 and item_count <= 24:
                                        string = item.name + "'s " + item.location
                                        libtcod.console_print(0,24,print_line + item_count - 12, string)
                                        item_count += 1
		print_line += 12
		return print_line
	while finished_showing == False:
		print_line = show()
		libtcod.console_print(0,1,print_line + 3, "OPTIONS:")
		libtcod.console_print(0,1,print_line + 4, "[a]ctions, [c]lothing, [d]rop item, [m]anage, [o]rganization, [r]eputation")
		libtcod.console_print(0,1,print_line + 5, "[u]se item, [w]eapons")
                libtcod.console_print(0,1,print_line + 7, '[b]ack')

		libtcod.console_flush()
		decision = False
		while decision == False:
	                key = libtcod.console_check_for_keypress()
			#go back
			if key.c == ord('b'):
				#print 'true'
				finished_party = True
				return finished_party
                        #actions
                        elif key.c == ord('a'):
                                #print 'true'
                                finished_action = False
                                while finished_action == False:
                                        libtcod.console_clear(0)
                                        finished_action = show_actions(player_party,world)
                                        decision = True

			#drop item
	                elif key.c == ord('d'):
	                        #print 'true'
	                        finished_dropping = False
				while finished_dropping == False:
					libtcod.console_clear(0)
					finished_dropping = drop_item(player_party,world)
					decision = True
					#pturn(player_party,world)
			#weapons
	                elif key.c == ord('w'):
	                        #print 'true'
	                        finished_weapons = False
	                        while finished_weapons == False:
	                                libtcod.console_clear(0)
	                                finished_weapons = show_weapons(player_party,world)
	                                decision  = True
	                #clothing
	                elif key.c == ord('c'):
	                        #print 'true'
	                        finished_outfits = False
	                        while finished_outfits == False:
	                                libtcod.console_clear(0)
	                                finished_outfits = show_outfits(player_party,world)
	                                decision = True
                        #manage party
                        elif key.c == ord('m'):
                                finished_manage = False
                                while finished_manage == False:
                                        libtcod.console_clear(0)
                                        show_manage(player_party,world)
					finished_manage = True
                                        decision = True

                        #reputation
                        elif key.c == ord('r'):
                                finished_reputation = False
                                while finished_reputation == False:
                                        libtcod.console_clear(0)
                                        finished_reputation = show_reputation(player_party,world)
                                        decision = True

			#use item
			elif key.c == ord('u'):
				finished_using = False
				while finished_using == False:
					libtcod.console_clear(0)
					use_item(player_party,world,player_party)
					#print drugs
					#for drug_used in drugs:
						#print drug_used[0].fname + " " + drug_used[0].lname
					#	drug_target = drug_used[0]
						#drug_target.use_drug(drug_used[1])
					#	print drug_used[1]
						#drug_used = drug_used[1]
					        #print drug_target.fname + " " + drug_target.lname
					        #if drug_used.name == 'Cocaine' or drug_used.name == 'Crack':
                				#	drug_type = 'Cocaine'
        					#elif drug_used.name == 'Heroin' or drug_used.name == 'Morphine':
     						#        drug_type = 'Opiates'
        					#elif drug_used.name == 'Speed' or drug_used.name == 'Meth':
                				#	drug_type = 'Speed'
        					#print drug_type     

        				#for addiction in drug_target.mind.addictions:
						#print addiction.name + " " + drug_type
        				#	if addiction.name == drug_type:
	                                #                print addiction.name + " " + drug_type
        				#        	addiction.times_used += 1
                			#	       	roll = random.randint(1,10)
                			#	       	roll += drug_target.stats.willpower
                             		#		addiction.addiction_level += 1
					#		print drug_target.fname + " " + drug_target.lname + " got addicted to " + drug_type
					finished_using = True
				decision = True
			#organization
			elif key.c == ord('o'):
				finished_organization = False
				while finished_organization == False:
					libtcod.console_clear(0)
					finished_organization = show_organization(player_party,world)
					decision = True

			#party members
			for option in options:
				char_key = str(option[0])
				if key.c == ord(char_key):
					finished_viewing = False
					while finished_viewing == False:
						my_location = find_location(player_party,world)
						finished_viewing = show_character(option[1], world,False,my_location)
						decision = True
						return finished_viewing
#	party_turn(player_party,world)
	return finished_party
#buy
def buy(player,location):
        libtcod.console_clear(0)
        line_count = 1
        libtcod.console_print(0,1,line_count, "BUY:")
        line_count += 2
        item_count = 1
        items_to_buy = []	
	for item in location.sold_here:
		letter = num_to_letter(item_count)
		item_to_buy = [letter, item]
		items_to_buy.append(item_to_buy)
		if item.item_type == "medical":
			if item.number == 1:
				libtcod.console_print(0,1,line_count, "[" + letter + "]" + item.name)
				libtcod.console_print(0,22,line_count, "($" + str(item.base_value) + ")")
			elif item.number >= 2:
				value = item.number * item.base_value
				libtcod.console_print(0,1,line_count, "[" + letter + "]" + item.name + "[" +  str(item.number) + "]")
				libtcod.console_print(0,22,line_count, "($" + str(value) + ")")
		else:
                	libtcod.console_print(0,1,line_count, "[" + letter + "]" + item.name)
                        libtcod.console_print(0,22,line_count, "($" + str(item.base_value) + ")")


		item_count += 1
		line_count += 1
	line_count += 1
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	finished_buying = False
	while finished_buying == False:
                key = libtcod.console_check_for_keypress()
                for item_to_buy in items_to_buy:
                        item_key = item_to_buy[0]
                        if key.c == ord(item_key):
				if item_to_buy[1].item_type == 'medical':
					value = item_to_buy[1].base_value * item_to_buy[1].number
				else:
					value = item_to_buy[1].base_value
				if player.money >= value: 
                                	player.money -= value 
					if item_to_buy[1].item_type != 'medical':
                                		player.inventory.append(item_to_buy[1])
					elif item_to_buy[1].item_type == 'medical':
						#see if item already in inventory
						found = False
						while found == False:
							for item in player.inventory:
								if item.item_type == item_to_buy[1].item_type and item.name == item_to_buy[1].name:
									item.number += item_to_buy[1].number
									found = True
							if found == False:
								player.inventory.append(item_to_buy[1])
								found = True
					if location.owned_by != 'No one':
						for area in world.areas:
							for organization in area.organizations:
								if location.owned_by == organization.name:
									if item_to_buy[1].base_value >= 1000:
										organization.player_reputation += item_to_buy[1].base_value / 1000
                                	finished_buying = True
                                	return finished_buying
				else:
					libtcod.console_clear(0)
					libtcod.console_print(0,1,1, "You cannot afford that.")
					libtcod.console_print(0,1,3, "[c]ontinue")
					libtcod.console_flush()
					finished_being_broke = False
					while finished_being_broke == False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('c'):
							finished_buying = True
							return finished_buying
                if key.c == ord('r'):
                        #choice_made = True
                        finished_buying = True
                        return finished_buying	

#sell
def sell(player,location):
        libtcod.console_clear(0)
        line_count = 1
        libtcod.console_print(0,1,line_count, "SELL:")
	line_count += 2
	item_count = 1
	items_to_sell = []
	for item in player.inventory:
		letter = num_to_letter(item_count)
		item_to_sell = [letter, item]
		items_to_sell.append(item_to_sell)
		libtcod.console_print(0,1,line_count,"[" + letter + "]" + item.name)
		value = item.base_value / 4 
		libtcod.console_print(0,22,line_count,"$" + str(value))
		item_count += 1
		line_count += 1
	line_count += 1
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	finished_selling = False
	while finished_selling == False:
                key = libtcod.console_check_for_keypress()
		for item_to_sell in items_to_sell:
			item_key = item_to_sell[0]
			if key.c == ord(item_key):
				player.money += (item_to_sell[1].base_value / 4)
				player.inventory.remove(item_to_sell[1])
				finished_selling = True
				return finished_selling
                if key.c == ord('r'):
                        #choice_made = True
                        finished_selling = True
                        return finished_selling			

def heal_injuries(player,world):
        libtcod.console_clear
        libtcod.console_print(0,1,1, "HEAL INJURIES:")
	line_count = 3
	member_count = 1
	options = []
	for member in player.members:
		letter = num_to_letter(member_count)
		member_cost = 0
		for injury in member.injuries:
			member_cost += injury.cost_to_heal
		option = [letter, member, member_cost]
		options.append(option)
		libtcod.console_print(0,1,line_count, "[" + letter + "]" + member.fname + " " + member.lname)
		libtcod.console_print(0,26,line_count, "$" + str(member_cost))
		line_count += 1
		member_count += 1
	line_count += 2
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	choice_made = False
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
               	for option in options:
			my_key = option[0]
			print my_key
               	        if key.c == ord(my_key) and player.money >= option[2]:
				player.money -= option[2]
				option[1].injuries = []
				option[1].health.current_health = option[1].health.base_max
				option[1].health.max_health = option[1].health.base_max
				option[1].health.current_blood = 100
				option[1].health.bleeding_rate = 0
				option[1].health.current_pain = 0
				#player.money -= option[2]
				choice_made = True
				finished_services = True
				return finished_services
				#choice_made = True
                if key.c == ord('r'):
                        choice_made = True
                        finished_services = True
                        return finished_services
	finished_services = True
	return finished_services


def restore_health(player,world):
        libtcod.console_clear
        libtcod.console_print(0,1,1, "RESTORE HEALTH:")
        line_count = 3
        member_count = 1
        options = []
        for member in player.members:
                letter = num_to_letter(member_count)
		#member.injuries = []
		health_missing = member.health.base_max - member.health.current_health
                member_cost = health_missing * 15 
                option = [letter, member, member_cost]
                options.append(option)
                libtcod.console_print(0,1,line_count, "[" + letter + "]" + member.fname + " " + member.lname)
                libtcod.console_print(0,26,line_count, "$" + str(member_cost))
                line_count += 1
                member_count += 1
        line_count += 2
        libtcod.console_print(0,1,line_count, "[r]eturn")
        libtcod.console_flush()
        choice_made = False
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
                for option in options:
                        if key.c == ord(option[0]) and player.money >= option[2]:
                                member.injuries = []
                                member.health.current_health = member.health.max_health
                                player.money -= option[2]
                                finished_services = True
                                return finished_services
                	elif key.c == ord('r'):
                        	#choice_made = True
                	        finished_services = True
                	        return finished_services

	
def services(player,location):
	libtcod.console_clear
	libtcod.console_print(0,1,1, "SERVICES:")
	line_count = 3
	available_services = []
	service_count = 1
	for service in location.services_here:
		letter = num_to_letter(service_count)
		available_service = [letter, service]
		libtcod.console_print(0,1,line_count, "[" + letter + "]" + service.name)
		available_services.append(available_service)
		service_count += 1
		line_count += 1
	line_count += 1
	#libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	choice_made = False
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
		for available_service in available_services:
			if key.c == ord(available_service[0]):
				if available_service[1].name == "heal injuries":
					healing_injuries = False
					while healing_injuries == False:
						healing_injuries = heal_injuries(player,location)
					finished_services = True
					return finished_services
                if key.c == ord('r'):
                        #choice_made = True
                        finished_services = True
                        return finished_services


#barter
def show_barter(player,location):
	libtcod.console_clear(0)
	line_count = 1
	libtcod.console_print(0,1,1, location.name)
	options = []
	if location.can_sell == True:
		options.append("[p]awn")
	if location.services == True:
		options.append("[s]ervices")
	if location.is_store == True:
		options.append("[b]uy") 
	line_count = 3
	for option in options:
		libtcod.console_print(0,1,line_count,option)
		line_count += 1

        libtcod.console_print(0,1,line_count + 2, "[*] go back")

	libtcod.console_flush()
	choice_made = False
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('*'):
			#choice_made = True
			finished_bartering = True
			return finished_bartering
                if key.c == ord('p') and location.can_sell == True:
                        finished_selling = False
			while finished_selling == False:
				finished_selling = sell(player,location)
                        finished_bartering = True
                        return finished_bartering
                if key.c == ord('b'):
                        finished_buying = False
                        while finished_buying == False:
                                finished_buying = buy(player,location)
                        finished_bartering = True
                        return finished_bartering
                if key.c == ord('s') and location.services == True:
                        finished_services = False
                        while finished_services == False:
                                finished_services = services(player,location)
                        finished_services = True
                        return finished_services

#speak

def rob_npc(char,target,world,player,location):
	my_location = find_location(player,world)
        line_count = 1
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " tells " + target.fname + " " + target.lname + " to hand over all his money.")
        line_count += 2
	#check if people are around
	if len(my_location.actors) >= 2:
		libtcod.console_print(0,1,line_count, target.fname + " " + target.lname + " yells for help.")
        #libtcod.console_print(0,1,line_count, "[a] make small talk.")
#	else:

def recruit(char,target,world,player,location):
	#choice_made = False
        line_count = 1
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " attempts to recruit " + target.fname + " " + target.lname + ".")
	line_count += 1
	libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " succeeded!")
	line_count += 2
	libtcod.console_print(0,1,line_count, "[b]ack")
        libtcod.console_flush()
        key = libtcod.console_check_for_keypress()
	#choice_made = False
        if key.c == ord('b'):
                libtcod.console_clear(0)
		print 'ok'
		#world.organization.footsoldiers.append(target)
		#for area in world.areas:
		#	for organization in area.organizations:
		#		if organization.name == char.affiliation:
		#			organization.player_reputation -= 4
		target.controlled_by = 'player'
                player.members.append(target)
		for member in player.members:
			member.controlled_by = 'player'
                location.actors.members.remove(target)
	        choice_made = True
		return choice_made
def conversation(char,target,player,world,location):
	line_count = 1
	libtcod.console_clear(0)
	libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " is talking to " + target.fname + " " + target.lname + ".")
	line_count += 2
	libtcod.console_print(0,1,line_count, "[a] make small talk.")
	line_count += 1
	libtcod.console_print(0,1,line_count, "[b] rob them.")
        line_count += 1
        libtcod.console_print(0,1,line_count, "[c] recruit them.")

	line_count += 2
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	choice_made = False
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('r'):
			finished_speaking = True
			return finished_speaking
                elif key.c == ord('c') and len(player.members) <= 8:
			
		        libtcod.console_clear(0)
		        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " attempts to recruit " + target.fname + " " + target.lname + ".")
		        line_count += 1
      			libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " succeeded!")
       			line_count += 2
        		libtcod.console_print(0,1,line_count, "[r]eturn")
        		libtcod.console_flush()
        		#key = libtcod.console_check_for_keypress()
			finished_speaking = False
        		#choice_made = True
			#return finished_speaking
			while finished_speaking == False:
				key = libtcod.console_check_for_keypress()
	        		if key.c == ord('r'):
	        		        libtcod.console_clear(0)
	        		        print 'ok'
	        		        #world.organization.footsoldiers.append(target)
	        		        player.members.append(target)
	        		        location.actors.members.remove(target)
					for area in world.areas:
						for organization in area.organizations:
							if organization.name == target.affiliation:
								organization.player_reputation -= 4
					#choice_made = recruit(char,target,world ,player,location)
					finished_speaking = True
					choice_made = True
	        		 	return finished_speaking

		elif key.c == ord('a'):
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1, target.fname + " " + target.lname + " says:")
			dialogue = random.choice(standard_npc_responses)
			libtcod.console_print(0,1,2, dialogue + ".")
		
			libtcod.console_print(0,1,4, "[r]eturn")
			libtcod.console_flush()
			confirm = False
			while confirm == False:
				key = libtcod.console_check_for_keypress()
        	       		if key.c == ord('r'):
                	       		finished_speaking = True
					choice_made = True
                	       		return finished_speaking

def speak_to_who(player,world,target,location,finished_speaking):

        #finished_speaking = False
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1, "Who will talk to " + target.fname + " " + target.lname + "?")
        member_count = 1
        line_count = 3
        possible_options = []
        for member in player.members:
        	letter = num_to_letter(member_count)
                option = [letter,member]
                possible_options.append(option)
                libtcod.console_print(0,1,line_count, "[" + letter + "]" + member.fname + " " + member.lname)
                libtcod.console_print(0,24,line_count, "(" + member.profession + ")")
                line_count += 1
                member_count += 1
        line_count += 1
        libtcod.console_print(0,1,line_count, "[r]eturn")
        libtcod.console_flush()
        while finished_speaking == False:
                key = libtcod.console_check_for_keypress()
                if key.c == ord('r'):
                        finished_speaking = True
                        return finished_speaking
                elif key.c  != ord('r'):
                        for option in possible_options:
				if key.c == ord(option[0]):
                               	        finished_speaking = conversation(option[1], target,player, world,location)
                               	        finished_speaking = True
                               	        return finished_speaking

def speak(player,world,location):
	my_location = find_location(player,world)
        libtcod.console_clear(0)
        line_count = 1
        libtcod.console_print(0,1,line_count, "Speak to who?")
	line_count += 2
	person_count = 1
	options = []
	for actor in my_location.actors.members:
		letter = num_to_letter(person_count)
		option = [letter,actor]
		options.append(option)
		libtcod.console_print(0,1,line_count, "[" + letter + "]" + actor.fname + " " + actor.lname)
		libtcod.console_print(0,24,line_count, "(" + actor.profession + ")")
		person_count += 1
		line_count += 1
	line_count += 1
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	npc_chosen = False
	
	while npc_chosen == False:
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				target = option[1]
				#npc_chosen = True
				finished_speaking = False
				finish = False
				while finished_speaking == False:
					finished_speaking = speak_to_who(player,world,target,location,finish)
		if key.c == ord('r'):
			finished_speaking = True
			return finished_speaking



#loot
def loot(party,world):
	finished_loot = False
	my_location = find_location(party,world)
	items_to_loot = []
	for item in my_location.items:
		if item.item_type == 'junk' and item.can_loot == True:
			items_to_loot.append(item)
		elif item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'medical' or item.item_type == 'limb':
			items_to_loot.append(item)
		
	libtcod.console_clear(0)
	libtcod.console_print(0,1,1, 'LOOT:')
	print_line = 2
	count = 1
	options = []
	for item in items_to_loot:
		letter = num_to_letter(count)
		option = [letter,item]
		options.append(option)
		count += 1
	option_count = 1
	for option in options:
		if option[1].item_type != 'medical' and option[1].item_type != 'limb':
			libtcod.console_print(0,1, print_line + option_count, "[" + option[0] + "]" + option[1].name)
			option_count += 1
		elif option[1].item_type == 'medical':
			libtcod.console_print(0,1, print_line + option_count, "[" + option[0] + "]" + str(option[1].number) + " " + option[1].name)
			option_count += 1
		elif option[1].item_type == 'limb':
			libtcod.console_print(0,1, print_line + option_count, "[" + option[0] + "]" + option[1].name + "'s " + option[1].location)
			option_count += 1

	#option_count += 1
	libtcod.console_print(0,1, print_line + option_count, "[r]eturn")
	libtcod.console_flush()
	choice_made = False
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		#choice_made = True
		for option in options:
	               	if key.c == ord("r"):
	                       	finished_loot,choice_made == True
	                       	libtcod.console_clear(0)
	                       	return finished_loot,finished_loot
			elif key.c == ord(option[0]):
				print option[1].name
				#item = item[1]
				party.inventory.append(option[1])
				my_location.items.remove(option[1])
				libtcod.console_clear(0)
				return finished_loot,finished_loot

def show_rooms(party,world,my_location):
	libtcod.console_clear(0)
	libtcod.console_print(0, 1, 1, 'ROOMS:')
	finished = False
	if len(my_location.rooms) <= 0:
		if my_location.parent_location != None:
			my_location.rooms = my_location.parent_location.rooms
	while finished == False:
		room_count = 1
		options = []
		for room in my_location.rooms:
			letter = num_to_letter(room_count)
			option = [letter, room]
			options.append(option)
			libtcod.console_print(0,1,room_count + 1, '[' + option[0] + ']' + option[1].name)
			room_count += 1
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				party.location = option[1]
				finished = True
				return finished
		if key.c == ord('*'):
			finished = True
			return finished
		libtcod.console_flush()

def check_rent(player_party,world):
	if world.time.day == 1 and world.player_organization.rent_checked == False:
		if len(world.player_organization.locations_owned) >= 1:
			for location in world.player_organization.locations_owned:
				world.player_organization.rent_due.append(location)
			world.player_organization.rent_paid = False
			world.player_organization.rent_checked = True
			return world.player_organization.rent_checked 
			#print 'checked rent'
def show_organization(party,world):
	libtcod.console_clear(0)
	finished_organization = False
	line_count = 1
	my_location = find_location(party,world)
	if len(world.player_organization.hq) >= 1:
                libtcod.console_print(0,1,line_count,'HEADQUARTERS:')
		line_count += 1
		for hq in world.player_organization.hq:
                        libtcod.console_print(0,1,line_count,hq.name)
			line_count = 1
	elif len(world.player_organization.hq) <= 0 and len(world.player_organization.locations_owned) >= 1:
	        libtcod.console_print(0,1,line_count,'No headquarters. [a]ssign')
		line_count += 2


	if len(world.player_organization.locations_owned) >= 1:
		for location in world.player_organization.locations_owned:
                        libtcod.console_print(0,1,line_count,'LOCATIONS:')
			line_count += 2
			libtcod.console_print(0,1,line_count,location.name)
			libtcod.console_print(0,20,line_count, "$2000/month")
			line_count += 1
			if world.player_organization.rent_paid == False:
				line_count += 1
				libtcod.console_print(0,1,line_count,"Rent is due!")
				line_count += 1
	else:
		libtcod.console_print(0,1,line_count,"You own no locations")
		line_count += 1
	line_count += 2
	if world.player_organization.rent_paid == False and len(world.player_organization.locations_owned) >= 1:
		libtcod.console_print(0,1,line_count,"[p]ay rent")
		line_count += 1
	if len(world.player_organization.footsoldiers) >= 1:
                libtcod.console_print(0,1,line_count,"FOOTSOLDIERS:")
		line_count += 2
		my_footsoldiers = []
		footsoldier_count = 1
		for footsoldier in world.player_organization.footsoldiers:
			letter = num_to_letter(footsoldier_count)
			option = [letter,footsoldier]
                	libtcod.console_print(0,1,line_count,'[' + letter + '] ' + footsoldier.fname + ' ' + footsoldier.lname)
                        libtcod.console_print(0,30,line_count,footsoldier.profession)
	                libtcod.console_print(0,45,line_count,footsoldier.outfit.name)
                        libtcod.console_print(0,60,line_count,footsoldier.weapon.name)
			my_footsoldiers.append(option)
			line_count += 1
			footsoldier_count += 1

        elif len(world.player_organization.footsoldiers) <= 0:
                libtcod.console_print(0,1,line_count,"You have no footsoldiers.")
		my_footsoldiers = []
                line_count += 1
	line_count += 2
        libtcod.console_print(0,1,line_count,"[*] go back")

	libtcod.console_flush()
	while finished_organization == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('*'):
			finished_organization == True
			return True
		elif key.c == ord('p') and world.player_organization.rent_paid == False:
			rent = 2000 * len(world.player_organization.locations_owned)
			if party.money >= rent:
				party.money -= rent
				world.player_organization.rent_paid = True
				return True
		elif key.c != ord('*') and key.c != ord('p'):
			for option in my_footsoldiers:
				#print option[0] + ' ' + option[1].fname + ' ' + option[1].lname
				if key.c == ord(option[0]):
					show_character(option[1],world,False,my_location)
					finished_organization = True
					return True
def check_evicted(party,world):
	if world.time.day >= 5 and world.player_organization.rent_paid == False:
		for location in world.player_organization.locations_owned:
			location.name = "Vacant Apartment"
			for item in location.items:
				location.items.remove(item)
			world.player_organization.locations_owned.remove(location) 
			return world.player_organization.locations_owned

	
def show_messages(messages):
	libtcod.console_clear(0)
	finished_messages = False
	line_count = 1
        libtcod.console_print(0,1,1, 'MESSAGES:')
	line_count += 2
	for message in messages:
               	libtcod.console_print(0,1,line_count, message)
		line_count += 1
	line_count += 2
        libtcod.console_print(0,1,line_count, '[b]ack')
	libtcod.console_flush()
	while finished_messages == False:
	        key = libtcod.console_check_for_keypress()

		if key.c == ord('b'):
			finished_messages = True
			return finished_messages


def party_turn(player_party,world):

	world.player_organization.check_rent = check_rent(player_party,world)
	check_evicted(player_party,world)
#describe the location
	turn_finished = False
	described = False
	while described == False:
		#check_rent(player_party,world)
		#find the player party
		my_location = find_location(player_party,world)
		my_location_items = my_location.items
		#print my_location.name
		#describe area
	        libtcod.console_clear(0)
		libtcod.console_print(0,1,1, 'LOCATION:')
	        libtcod.console_print(0,1,2, my_location.name)
	        libtcod.console_print(0,1,3, my_location.area)
 		#check if safehouse
		#if my_location.is_safehouse == True:
	        #        libtcod.console_print(0,1,4, 'Safehouse')
		#check if store
        	if my_location.is_store == True and world.time.hour >= my_location.time_open and world.time.hour <= my_location.time_close:
			libtcod.console_print(0,1,4, 'OPEN')
		#else:
                #        libtcod.console_print(0,1,4, 'CLOSED')

		#time
		world.time.correct()
		hour = world.time.get_hour()
		month = world.time.get_month()
		am_pm = world.time.get_am_or_pm()
		libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))
		if world.time.minute <= 9:
			minute = '0' + str(world.time.minute)
		else:
			minute = world.time.minute
		libtcod.console_print(0,40,2, str(hour) + ':' + str(minute) + ' ' + am_pm)
		libtcod.console_print(0,40,3, "$" + str(player_party.money))
		#is this location owned
		if my_location.owned_by != "No one":
                        libtcod.console_print(0,1,5, "LOCATION OWNER:")
			libtcod.console_print(0,18,5, my_location.owned_by)
		#rooms
		if my_location.parent_location != None:
			my_location.rooms = my_location.parent_location.rooms
		if len(my_location.rooms) >= 1:
			libtcod.console_print(0,40,4, str(len(my_location.rooms)) + ' rooms[*]')
		#check if anyone died
		messages = []
		for member in player_party.members:
			if member.health.current_blood <= 0:
				message = member.fname + " " + member.lname + " bled to death."
				messages.append(message)
				my_location.corpses.append(member)
				my_location.items.append(member.weapon)
				member.weapon = punch
				#my_location_items.append(member.outfit)
				#member.outfit = naked
				player_party.members.remove(member)
                        #check stamina
                        if member.health.current_stamina <= 40 and member.health.current_stamina >= 20:
                                message = member.fname + ' ' + member.lname + " is tired."
                                messages.append(message)
                        elif member.health.current_stamina <= 19 and member.health.current_stamina >= 1:
                                message = member.fname + ' ' + member.lname + " is exhausted."
                                messages.append(message)
                        elif member.health.current_stamina <= 0 and member.combat_status.knocked_down == False:
                                message = member.fname + ' ' + member.lname + " collapsed on the ground."
				member.combat_status.knocked_down = True
                                messages.append(message)
			if member.combat_status.knocked_down == True:
                                message = member.fname + ' ' + member.lname + " is on the ground."
                                messages.append(message)
			#check hungry
			def eat(target,inventory):
				finished = False
				while finished == False:
					for item in inventory:
						if item.item_type == 'food' and target.hunger >= 30:
							target.hunger -= item.nutrition
							if target.hunger <= 0:
								target.hunger = 0
							inventory.remove(item)
                                			message = member.fname + ' ' + member.lname + " ate " + item.name + "."
                                			messages.append(message)
							finished = True
					finished = True
						
                        if member.hunger >= 30 and member.hunger <= 49:
                                message = member.fname + ' ' + member.lname + " is hungry."
				messages.append(message)
                                eat(member,player_party.inventory)

			elif member.hunger >= 60:
				message = member.fname + ' ' + member.lname + " very hungry."
                                messages.append(message)
				eat(member,player_party.inventory)
                        #check thirsty
                        def drink(target,inventory):
                                finished = False
                                while finished == False:
                                        for item in inventory:
                                                if item.item_type == 'drink' and target.thirst >= 50:
                                                        target.thirst -= item.nutrition
							if target.thirst <= 0:
								target.thirst = 0
                                                        inventory.remove(item)
                                                        message = member.fname + ' ' + member.lname + " drank " + item.name + "."
                                                        messages.append(message)
                                                        finished = True
                                        finished = True
                        if member.thirst >= 50 and member.thirst <= 74:
                                message = member.fname + ' ' + member.lname + " is thirsty."
                                messages.append(message)
                                drink(member,player_party.inventory)

                        elif member.thirst >= 75:
                                message = member.fname + ' ' + member.lname + " is very thirsty."
                                messages.append(message)
                        	drink(member,player_party.inventory)

			#check if anyone unhappy
			if member.mind.happiness <= 20 and member.mind.happiness >= -19:
				message = member.fname + ' ' + member.lname + " is unhappy."
				messages.append(message)
                        elif member.mind.happiness <= -20:
                                message = member.fname + ' ' + member.lname + " is miserable."
                                messages.append(message)

			#check if anyone bleeding
			if member.health.bleeding_rate >= 1 and member.health.bleeding_rate <= 4:
                                message = member.fname + ' ' + member.lname + " is bleeding."
				messages.append(message)
                        elif member.health.bleeding_rate >= 5:
                                message = member.fname + ' ' + member.lname + " is bleeding badly."
                                messages.append(message)

	                #check if anyone in pain


                        if member.health.current_pain >= 5 and member.health.current_pain <= 20:
                                message = member.fname + ' ' + member.lname + " is in pain."
				messages.append(message)
                        elif member.health.current_pain >= 21:
                                message = member.fname + ' ' + member.lname + " is in horrible pain."
                                messages.append(message)

	                #check if anyone stressed
                        if member.mind.stress >= 30 and member.mind.stress <= 59:
                                message = member.fname + ' ' + member.lname + " is stressed."
                                messages.append(message)
                        elif member.mind.stress >= 60:
                                message = member.fname + ' ' + member.lname + " is very stressed."
                                messages.append(message)
                        #check if anyone stressed
                        #if member.mind.sanity <= 20 and member.mind.sanity >= -19:
                        #        message = member.fname + ' ' + member.lname + " is feeling weird."
                        #        messages.append(message)
                        #elif member.mind.sanity <= -20:
                        #        message = member.fname + ' ' + member.lname + " is acting crazy."
                        #        messages.append(message)

			#check if anyone knocked down
			if member.combat_status.knocked_down == True:

				#message = member.fname + " " + member.lname + " is on the ground."
				#messages.append(message)
                		resistance = (member.stats.willpower) + (member.stats.strength) 
                		resist_roll = random.randint(3,resistance)
                		pain = member.health.current_pain
				if pain >= 1:
                			pain_roll = random.randint(1,pain)
                			passed_pain = False
                			if resist_roll >= pain_roll:
                        			passed_pain = True
                			elif resist_roll <= pain_roll - 1:
                        			passed_pain = False
        				else:
                				passed_pain = True
				else:
					passed_pain = True
				if passed_pain == True and member.health.current_stamina >= 1:
					message = member.fname + " " + member.lname + " got up."
					messages.append(message)
					member.combat_status.knocked_down = False
				else:
					if passed_pain == False:
                                        	message = member.fname + " " + member.lname + " is in too much pain to get up."
                                        	messages.append(message)
					if member.health.current_stamina <= 0:
                                                message = member.fname + " " + member.lname + " has no Stamina to get up."
                                                messages.append(message)


	        item_count = 1
	        line_count = 8
		#described = True
#items
		libtcod.console_print(0,1,line_count,"ITEMS HERE:")
		line_count += 1
		item_count = 1
		#print location.items
        	for item in my_location.items:
			#print item.name
			if item_count <= 6:	
				#line_count = 9
				#line_count = item_count + line_count
				if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
					libtcod.console_print(0,1,line_count, item.name)
					item_count += 1
					line_count += 1
				elif item.item_type == 'medical':
					libtcod.console_print(0,1,line_count, item.name + "(" + str(item.number) + ")")
					item_count += 1
					line_count += 1
				elif item.item_type == 'container' and item.is_visible == True:
					libtcod.console_print(0,1,line_count, item.name)
					item_count += 1
					line_count += 1
                                elif item.item_type == 'limb':
                                        libtcod.console_print(0,1,line_count, item.location)
                                        item_count += 1
                                        line_count += 1

                        elif item_count >= 7 and item_count <=12:
				#line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        libtcod.console_print(0,20,line_count-6, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'medical':
                                        libtcod.console_print(0,20,line_count-6, item.name + "(" + str(item.number) + ")")
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'container' and item.is_visible == True:
                                        libtcod.console_print(0,20,line_count-6, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'limb':
                                        libtcod.console_print(0,20,line_count-6, item.location)
                                        item_count += 1
                                        line_count += 1
	

                        elif item_count >= 13 and item_count <=18:
                                #line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        libtcod.console_print(0,40,line_count-12, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'medical':
                                        libtcod.console_print(0,40,line_count-12, item.name + "(" + str(item.number) + ")")
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'container' and item.is_visible == True:
                                        libtcod.console_print(0,40,line_count-12, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'limb':
                                        libtcod.console_print(0,40,line_count-12, item.location)
                                        item_count += 1
                                        line_count += 1


                        elif item_count >= 19 and item_count <=24:
                                #line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        libtcod.console_print(0,60,line_count-18, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'medical':
                                        libtcod.console_print(0,60,line_count-18, item.name + "(" + str(item.number) + ")")
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'container' and item.is_visible == True:
                                        libtcod.console_print(0,60,line_count-18, item.name)
                                        item_count += 1
                                        line_count += 1
                                elif item.item_type == 'limb':
                                        libtcod.console_print(0,60,line_count-18, item.location)
                                        item_count += 1
                                        line_count += 1

			else:
				possible_regulars = []
			count = 1
		line_count = 16
		if len(my_location.actors.members) >= 1 or len(my_location.corpses) >= 1:
			libtcod.console_print(0,1,line_count, 'PEOPLE HERE:')
			count = 1
			for actor in my_location.actors.members:
				if actor == None:
					my_location.actors.members.remove(actor)
			for actor in my_location.actors.members:
				line_count += 1
				#print line_count
				#print actor.fname
				try:
					libtcod.console_print(0,1,line_count, actor.fname + " " + actor.lname)
                                	libtcod.console_print(0,25,line_count, "(" + actor.profession + ")")
					count += 1
				except:
					count = count
					line_count -= 1
                        for corpse in my_location.corpses:
                                line_count += 1
                                #print line_count
                                #print actor.members
                                libtcod.console_print(0,1,line_count, corpse.profession + " corpse")
		line_count += 2
		#show if anyone bled to death

		#messages	
		if len(messages) >= 1:
			libtcod.console_print(0,1,line_count,"MESSAGES:")
			line_count += 1
			message_count = 1
			for message in messages:
				if message_count <= 10:
					libtcod.console_print(0,1,line_count,message)
					line_count += 1
                                elif message_count >= 11 and message_count <= 20:
                                        libtcod.console_print(0,35,line_count - 10,message)
                                        line_count += 1				
				message_count += 1
			if len(messages) >= 21:
				line_count += 1
				libtcod.console_print(0,1,line_count - 8,'[m]ore messages.')
		described = True
	
        libtcod.console_flush() 
	

#options
	describe_options = False
	line_count += 2
	while describe_options == False:
		#show options
		show_options(my_location,line_count)
		describe_options = True
	action  = False
        while action == False:
		#get a decision
                libtcod.console_flush()
                key = libtcod.console_check_for_keypress()


                #attack
                if key.c == ord('a'):
                        finished_fighting = False
			while finished_fighting == False:
				finished_fighting = battle(player_party,my_location.actors,my_location,world,True)
                        action = True


		#barter
		if key.c == ord('b'):
			finished_bartering = False
			while finished_bartering == False:
				finished_bartering = show_barter(player_party,my_location)
			action = True


		#loot
		looting = False
		if key.c == ord('l'):
			finished_loot = False
			looting = False
			for item in my_location.items:
				if item.can_loot == True:
					looting = True

			if looting == True:
				while finished_loot ==  False:
					finished_loot = loot(player_party,world)
				looting = False
			action = True

		#
		#investigate
                if key.c == ord('i'):
			finished_viewing = False
			while finished_viewing == False:
                        	investigate(my_location,world,player_party)
				finished_viewing = True

                        action = True  		
		
		#
		#travel
                if key.c == ord('t'):
                        my_location, turn_finished = travel(player_party,world,my_location)
                        #handle drugs, injuries, etc
                        handle_party_drugs(player_party,world)
			handle_party_mind
			handle_npcs(player_party,world)
                        action = True		

		#messages
		if key.c == ord('m'):
			finished_messages = False
			while finished_messages == False:
				finished_messages = show_messages(messages)
				action = True
		#party		
		if key.c == ord('p'):
			finished_party = False
			while finished_party == False:
				finished_party = show_party(player_party,world)

				action = True
                #rest
                if key.c == ord('r'):
                        finished_rest = False
                        while finished_rest == False:
                                finished_rest = show_rest(player_party,world)

                                action = True

		#speak
                if key.c == ord('s'):
                        finished_speaking = False
                        while finished_speaking == False:
                                finished_speaking = speak(player_party,world,my_location)

                                action = True
		#wait
                if key.c == ord('w'):
                        finished_wait = False
                        while finished_wait == False:
                                finished_wait = show_wait(player_party,world)

                                action = True
		#[*]go to other room
		if key.c == ord('*'):
			finished_move = False
			while finished_move == False:
				finished_move = show_rooms(player_party,world,my_location)
				action = True




			#finished_turn = True
			#if finished_showing == True:
			#	described = False
		

#start the game
game = Game(True, True)
messages = []
def run():
	global game
	while not libtcod.console_is_window_closed():
		while game.running == True and game.starting == True:
			start = startup()
			libtcod.console_flush()
			begin = 0
			if start == 2:
				try:
	                	        libtcod.console_clear(0)
	                	        libtcod.console_print(0,1,1, 'Loading.')
	                	        libtcod.console_flush()
					game, world, player_party = load_game()
	
					begin = 2
				except:
					begin = 1
			elif start == 1:
				begin = 1
			elif start == 3:
				return True
			if begin == 1:
				player = main_menu()
	        		player_party, world = create_party(player)
				location = player_party.location
				world.player_organization.locations_owned = []
				game.starting = False
			elif begin == 2:
				game_starting = False
			elif begin == 3:
				#game.running = False
				return True
	    	while game.running == True and game.starting == False and len(player_party.members) >= 1:
			turn_finished = False
			new_messages = []
			#if len(messages) >= 1:
			#	for message in messages:
			#		new_messages.append(message)
			while turn_finished == False:
				#save_game()
				#world,player_party = load_game()
				my_location = find_location(player_party,world)
				turn_finished = party_turn(player_party,world)
		confirm = False
		libtcod.console_clear(0)
		while game.running == True and game.starting == False and len(player_party.members) <= 0 and confirm == False:
			while confirm == False:
		                libtcod.console_print(0,1,1, 'GAME OVER.')
        	                libtcod.console_print(0,1,3, '[c]ontinue')
	
        	                libtcod.console_flush()
				key = libtcod.console_check_for_keypress()
				if key.c == ord('c'):
					libtcod.console_clear(0)
					game.running,game.starting,confirm = True,True,True

run()
