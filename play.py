
import libtcodpy as libtcod
from operator import itemgetter, attrgetter
from namegen import *
from dialogue import *
from world import *
import shelve
import time
def save_game():
	file = shelve.open('savegame', 'n')
        file['game'] = game

        file['world'] = world
        file['player_party'] = player_party
        file['game'] = game
	file['party_actions'] = party_actions
        print player_party
        print world
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
        party_actions = file['party_actions']

	file.close()
	#print 'close'
	return game, world, player_party,party_actions

#actual size of the window
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 70

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
		game, world, player, party_actions = load_game()
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



def find_area(party,world):
	my_area = party.area
	for area in world.areas:
		if area.name == my_area:
			my_area = area
	return my_area

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
		letter = '$'
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
		letter = '"'
	elif num == 72:
		letter = ':'
	elif num == 73:
		letter = '?'
	elif num == 74:
		letter = '>'
	elif num == 75:
		letter = '<'
	elif num == 76:
		letter = ']'
	elif num == 77:
		letter = '['
	elif num == 78:
		letter = '}'
	elif num == 79:
		letter = '{'
	elif num == 80:
		letter = "~"
	elif num == 81:
		letter = '|'
	elif num == 82:
		letter = '-'
	elif num == 83:
		letter = '_'
	elif num == 84:
		letter = '='
	elif num == 85:
		letter = '+'
	elif num == 86:
		letter = '`'



	else:
		letter = 'error'

	return letter

def show_areas(party,world,start):
	libtcod.console_clear(0)
	my_area = start
	my_location = find_location(party,world)
	line_count = 1
	libtcod.console_print(0,1,line_count,world.name)
	line_count += 2
	areas = []
	for area in world.areas:
		areas.append(area)
	print my_area.name
        count = 1
        options = []
        letter = " "
        for area in world.areas:
                line_count= count + 5
                #print count
                letter = num_to_letter(count)
                option = [letter,area]
                options.append(option)
                #print location.name
                #print my_location.name
                if area.name == my_location.area:
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
        rows = 56
        columns = 56
        row_count = 1
        column_count = 1

        while column_count <= columns:
                while row_count <= rows:
                        libtcod.console_set_char_background(0, column_count + offset_y, row_count + offset_x, libtcod.darkest_grey, flag=libtcod.BKGND_SET)
                        row_count += 1
                row_count = 1
                column_count += 1
	area_count = 1
	options = []
        for area in world.areas:
		letter = num_to_letter(area_count)
		this_area = [letter,area]
		options.append(this_area)
		area_count += 1
	for option in options:
                #print option[1].x
                #print option[1].y
                libtcod.console_print(0,offset_y + option[1].y,offset_x + option[1].x, option[0])
                if party.area_x == option[1].x and party.area_y == option[1].y:
                        libtcod.console_set_char_background(0, option[1].y + offset_y, option[1].x + offset_x, libtcod.dark_green, flag=libtcod.BKGND_SET)
                else:
                        libtcod.console_set_char_background(0, option[1].y + offset_y, option[1].x + offset_x, libtcod.dark_grey, flag=libtcod.BKGND_SET)

	libtcod.console_flush()
	finished_area = False
	while finished_area == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('*'):
			return True
		for option in options:
			if key.c == ord(option[0]):
				party.area = option[1].name
				#print party.area.name
				
				party.area_x= option[1].x
				party.area_y = option[1].y
				my_location = find_location(party,world)
				my_location.area = option[1].name
				my_area = option[1]
				return my_location,my_area
def faction_attack(party,world,faction,attacker,my_location):
	libtcod.console_clear(0)
	if faction.name == party.area:
        	libtcod.console_print(0,1,1,"A group of " + str(len(attacker.members)) + " " + faction.name + " residents approach you:")
	else:
		libtcod.console_print(0,1,1,"A group of " + str(len(attacker.members)) + " " + faction.name + " approach you:")
        libtcod.console_print(0,1,2,'Get ready to die!')

        libtcod.console_print(0,1,6,"[f]ight!")
	libtcod.console_flush()
	decision = False
	while decision == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('f'):
	                decision = battle(party,attacker,my_location,world,True,party_actions)



# t r a v e l


def set_up_tents(party,world,party_actions,campsite,my_location):
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"TENTS:")
	tent_count = 1
	tents = []
	for item in party.inventory:
		if item.item_type == 'tent':
			tents.append(item)
	if len(tents) <= 0:
	        libtcod.console_print(0,1,2,"You have no tents.")
	option_count = 1
	options = []
	if len(tents) >= 1:
		for tent in tents:
			letter = num_to_letter(tent_count)
			new_option = [letter,tent]
			options.append(new_option)
			tent_count += 1
		for option in options:
                	libtcod.console_print(0,1,1+option_count,"[" + option[0] + "] " + tent.name)
			option_count += 1

        libtcod.console_print(0,1,10,"[ESC]")
	libtcod.console_flush()
	finished = False
	while finished == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        libtcod.console_clear(0)
                        return campsite
		else:
			if len(options) >= 1:
				for option in options:
					if key.c == ord(str(option[0])):
						campsite.tents_set_up.append(option[1])
						my_location.items.append(tent)
						party.inventory.remove(option[1])
						libtcod.console_clear(0)
						return campsite



def build_fire(party,world,party_actions,campsite,my_location):
        libtcod.console_clear(0)
	#find wood
	campsite.has_fire = True
	my_location.items.append(fire)
        libtcod.console_print(0,1,1,"You build a fire here.")

        libtcod.console_print(0,1,3,"[ESC]")
	libtcod.console_flush()
	finished = False
	while finished == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			libtcod.console_clear(0)
			finished = True


def show_travel_msg(messages):
	libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"MESSAGES:")

	if len(messages) >= 1:
        	msg_count = 1
                for message in messages:
                	libtcod.console_set_default_foreground(0, libtcod.white)
                	if msg_count <= 20:
                        	libtcod.console_set_default_foreground(0, message.color)
                                libtcod.console_print(0,1,3 + msg_count, message.message)
                                libtcod.console_set_default_foreground(0, libtcod.white)

                        elif msg_count >= 21 and msg_count <= 40:
                                libtcod.console_set_default_foreground(0, message.color)
                                libtcod.console_print(0,35,3+msg_count-20, message.message)
                                libtcod.console_set_default_foreground(0, libtcod.white)

                        elif msg_count >= 41 and msg_count <= 60:
                                libtcod.console_set_default_foreground(0, message.color)
                                libtcod.console_print(0,70,3+msg_count-40, message.message)
                                libtcod.console_set_default_foreground(0, libtcod.white)
                        msg_count += 1
	elif len(messages) <= 0:
		msg_count = 1
		libtcod.console_print(0,1,1,"No messages.")
	libtcod.console_print(0,1,25,"[ESC]")
	libtcod.console_flush()
	finished = False
	while finished == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			return True

def travel_msg(party,world,party_actions,hour):
	messages = []
	#check stamina
	for member in party.members:
	        if member.health.current_stamina <= 40 and member.health.current_stamina >= 20:
        	        new_message = member.fname + ' ' + member.lname + " is tired."
			message = Message(new_message,world.time,libtcod.white)
                        messages.append(message)
                elif member.health.current_stamina <= 19 and member.health.current_stamina >= 1:
                        new_message = member.fname + ' ' + member.lname + " is exhausted."
                        message = Message(new_message,world.time,libtcod.grey)

                        messages.append(message)
                elif member.health.current_stamina <= 0 and member.combat_status.knocked_down == False:
                        new_message = member.fname + ' ' + member.lname + " collapsed on the ground."
                        member.combat_status.knocked_down = True
                        message = Message(new_message,world.time,libtcod.yellow)

                        messages.append(message)
                if member.combat_status.knocked_down == True:
                        new_message = member.fname + ' ' + member.lname + " is on the ground."
                        message = Message(new_message,world.time,libtcod.dark_grey)

                        messages.append(message)
	#check cold
                if member.health.body_temp <= 10 and member.health.body_temp >= -25:
                	new_message = member.fname + ' ' + member.lname + " is cold."
			message = Message(new_message,world.time,libtcod.blue)
                        messages.append(message)
                elif member.health.body_temp <= -26:
                        new_message = member.fname + ' ' + member.lname + " is freezing!"
			message = Message(new_message,world.time,libtcod.light_blue)
                        messages.append(message)
                elif member.health.body_temp >= 70 and member.health.body_temp <= 99:
                        new_message = member.fname + ' ' + member.lname + " is hot"
			message = Message(new_message,world.time,libtcod.yellow)
                        messages.append(message)
                elif member.health.body_temp >= 100:
                	new_message = member.fname + ' ' + member.lname + " is very hot!"
			message = Message(new_message,world.time,libtcod.orange)
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
        	                                new_message = member.fname + ' ' + member.lname + " ate " + item.name + "."
						message = Message(new_message,world.time,libtcod.white)
        	                                messages.append(message)
        	                                finished = True
        	                finished = True
	        if member.hunger >= 30 and member.hunger <= 49:
	        	new_message = member.fname + ' ' + member.lname + " is hungry."
			message = Message(new_message,world.time,libtcod.white)
	                messages.append(message)
	                eat(member,player_party.inventory)
	        elif member.hunger >= 60:
		        new_message = member.fname + ' ' + member.lname + " very hungry."
			message = Message(new_message,world.time,libtcod.orange)
	                messages.append(message)
	        	eat(member,player_party.inventory)
	        #check thirst
	        def drink(target,inventory):
	                finished = False
	                while finished == False:
	        	        for item in inventory:
	                	        if item.item_type == 'drink' and target.thirst >= 50:
	                        	        target.thirst -= item.nutrition
	                                        if target.thirst <= 0:
	                                	        target.thirst = 0
	                                        inventory.remove(item)
	                                        new_message = member.fname + ' ' + member.lname + " drank " + item.name + "."
						message = Message(new_message,world.time,libtcod.white)
                                        finished = True
                if member.thirst >= 50 and member.thirst <= 74:
                	new_message = member.fname + ' ' + member.lname + " is thirsty."
			message = Message(new_message,world.time,libtcod.white)
                        messages.append(message)
                        drink(member,player_party.inventory)

                elif member.thirst >= 75:
                        new_message = member.fname + ' ' + member.lname + " is very thirsty."
			message = Message(new_message,world.time,libtcod.orange)
                        messages.append(message)
                        drink(member,player_party.inventory)
        	#check if anyone unhappy
        	if member.mind.happiness <= 20 and member.mind.happiness >= -19:
        		new_message = member.fname + ' ' + member.lname + " is unhappy."
			message = Message(new_message,world.time,libtcod.white)
        	        messages.append(message)
        	elif member.mind.happiness <= -20:
        	        new_message = member.fname + ' ' + member.lname + " is miserable."
			message = Message(new_message,world.time,libtcod.orange)
        	        messages.append(message)
        	#check if anyone bleeding
        	if member.health.bleeding_rate >= 1 and member.health.bleeding_rate <= 4:
		        new_message = member.fname + ' ' + member.lname + " is bleeding."
			message = Message(new_message,world.time,libtcod.red)
        	        messages.append(message)
        	elif member.health.bleeding_rate >= 5:
                	new_message = member.fname + ' ' + member.lname + " is bleeding badly."
			message = Message(new_message,world.time,libtcod.dark_red)
                	messages.append(message)
                #check if anyone in pain

                if member.health.current_pain >= 5 and member.health.current_pain <= 20:
                	new_message = member.fname + ' ' + member.lname + " is in pain."
			message = Message(new_message,world.time,libtcod.white)
                        messages.append(message)
                elif member.health.current_pain >= 21:
                        new_message = member.fname + ' ' + member.lname + " is in horrible pain."
			message = Message(new_message,world.time,libtcod.yellow)
                        messages.append(message)
                #check if anyone stressed
                if member.mind.stress >= 30 and member.mind.stress <= 59:
                     	new_message = member.fname + ' ' + member.lname + " is stressed."
			message = Message(new_message,world.time,libtcod.white)
                        messages.append(message)
                elif member.mind.stress >= 60:
                        new_message = member.fname + ' ' + member.lname + " is very stressed."
			message = Message(new_message,world.time,libtcod.yellow)
                        messages.append(message)
                #check if anyone stressed
                if member.mind.sanity <= 20 and member.mind.sanity >= 0:
                        new_message = member.fname + ' ' + member.lname + " is acing strangely."
			message = Message(new_message,world.time,libtcod.white)
                        messages.append(message)
                elif member.mind.sanity <= -1:
                        new_message = member.fname + ' ' + member.lname + " is acting crazy."
			message = Message(new_message,world.time,libtcod.pink)
                        messages.append(message)



	#finally return all the messages
	return messages

def make_camp(party,world,party_actions,campsite,my_location):
	libtcod.console_clear(0)
	finished_camp = False
	while finished_camp == False:
		made_choice = False
	        libtcod.console_print(0,1,1, 'CAMPSITE:')
		if campsite.has_fire == False:
		        libtcod.console_print(0,1,2, 'Campsite has no fire.')
                elif campsite.has_fire == True:
                        libtcod.console_print(0,1,2, 'Campsite has fire.')

		if len(campsite.tents_set_up) == 0:
			libtcod.console_print(0,1,3, 'No tents set up.')
		elif len(campsite.tents_set_up) >= 1:
                        libtcod.console_print(0,1,3, str(len(campsite.tents_set_up)) + ' tents set up.')

		libtcod.console_print(0,1,6, 'OPTIONS:')
                libtcod.console_print(0,1,7, '[a] set up tent')
                libtcod.console_print(0,1,8, '[b] build a fire')

                libtcod.console_print(0,1,10, '[ESC]')
		libtcod.console_flush()
		while made_choice == False:
			key = libtcod.console_check_for_keypress()
			if key.vk == libtcod.KEY_ESCAPE:
				libtcod.console_clear(0)
				return campsite
                        elif key.c == ord('a'):
                                set_up_tents(party,world,party_actions,campsite,my_location)
                                libtcod.console_clear(0)
                                made_choice = True

			elif key.c == ord('b'):
				build_fire(party,world,party_actions,campsite,my_location)
				libtcod.console_clear(0)
				made_choice = True


def travel_stop(party,world,party_actions):
	libtcod.console_clear(0)
	my_location = gen_wasteland(0,0)
	has_fire = False
	tents_set_up = []
	if stream in my_location.items:
		has_water = True
	else:
		has_water = False
	campsite = Campsite(my_location,has_fire,tents_set_up,has_water)
	print my_location.name
	finished_stop  = False
	while finished_stop == False:
                libtcod.console_print(0,1,1, my_location.name)
                world.time.correct(party_actions)
                hour = world.time.get_hour()
                month = world.time.get_month()
                am_pm = world.time.get_am_or_pm()
                libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))
                if world.time.minute <= 9:
                        minute = '0' + str(world.time.minute)
                else:
                        minute = world.time.minute
                libtcod.console_print(0,40,2, str(hour) + ':' + str(minute) + ' ' + am_pm)

                libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))

		if world.weather.temperature >= 1 and world.weather.temperature <= 19:
                        libtcod.console_set_default_foreground(0, libtcod.yellow)
                elif world.weather.temperature >= 20:
                        libtcod.console_set_default_foreground(0, libtcod.orange)
                elif world.weather.temperature <= 0 and world.weather.temperature >= -19:
                        libtcod.console_set_default_foreground(0, libtcod.blue)
                elif world.weather.temperature <= -20:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                libtcod.console_print(0,40,4, str(world.weather.temperature) + "C")

                libtcod.console_set_default_foreground(0, libtcod.white)
                if world.weather.clouds == 'Sunny':
                        libtcod.console_set_default_foreground(0, libtcod.yellow)
                elif world.weather.clouds == 'Overcast':
                        libtcod.console_set_default_foreground(0, libtcod.gray)
                elif world.weather.clouds == 'Dark clouds':
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                elif world.weather.clouds == 'Light rain':
                        libtcod.console_set_default_foreground(0, libtcod.light_blue)
                elif world.weather.clouds == 'Heavy rain' or world.weather.clouds == "Heavy freezing rain":
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                elif world.weather.clouds == 'Light snow' or world.weather.clouds == "Light freezing rain" or world.weather.clouds == "Heavy snow":
                        libtcod.console_set_default_foreground(0, libtcod.blue)

                libtcod.console_print(0,40,3, str(world.weather.clouds))
                if world.weather.precipitation == True:
                        libtcod.console_print(0,40,5, str(world.weather.precipitation_type))
                libtcod.console_set_default_foreground(0, libtcod.white)
		print my_location.items
                libtcod.console_print(0,1,7, "THINGS HERE:")
		item_count = 1
		for item in my_location.items:
			if item == None:
				my_location.items.remove(item)

			else:
	                        if item.name == "Fire":
        	                        libtcod.console_set_default_foreground(0, libtcod.orange)
        	                elif item.item_type == "tent":
        	                        libtcod.console_set_default_foreground(0, libtcod.light_green)

				if item_count <= 4:
					libtcod.console_print(0,1,item_count+8, item.name)
				elif item_count >= 5 and item_count <= 8:
                                        libtcod.console_print(0,15,item_count+4, item.name)
                                elif item_count >= 9 and item_count <= 12:
                                        libtcod.console_print(0,30,item_count, item.name)
                                elif item_count >= 13 and item_count <= 16:
                                        libtcod.console_print(0,45,item_count-4, item.name)
                                elif item_count >= 17 and item_count <= 20:
                                        libtcod.console_print(0,60,item_count-8, item.name)
                                elif item_count >= 21 and item_count <= 25:
                                        libtcod.console_print(0,75,item_count-12, item.name)
                        libtcod.console_set_default_foreground(0, libtcod.white)


			item_count += 1

		libtcod.console_print(0,1,14, "MESSAGES:")
		messages = travel_msg(party,world,party_actions,world.time.hour)
                if len(messages) >= 1:
	                msg_count = 1
                        for message in messages:
        	                libtcod.console_set_default_foreground(0, libtcod.white)
                                if msg_count <= 10:
                	                libtcod.console_set_default_foreground(0, message.color)
                                        libtcod.console_print(0,1,14+msg_count, message.message)
                                        libtcod.console_set_default_foreground(0, libtcod.white)

        	                elif msg_count >= 11 and msg_count <= 20:
        	                        libtcod.console_set_default_foreground(0, message.color)
                	                libtcod.console_print(0,35,4+msg_count, message.message)
                                        libtcod.console_set_default_foreground(0, libtcod.white)

                	        elif msg_count >= 21:
	        	                libtcod.console_set_default_foreground(0, message.color)
                	                libtcod.console_print(0,35,22, "[m]ore")
                                        libtcod.console_set_default_foreground(0, libtcod.white)
                                msg_count += 1

		libtcod.console_print(0,1,50, '[c]ontinue, [s]et up camp, [p]arty, [r]est')
		libtcod.console_flush()
		key = libtcod.console_check_for_keypress()
		if key.c == ord('c'):
			finished_stop = True
		elif key.c == ord('r'):
			show_rest(party,world)
			libtcod.console_clear(0)
			finished_stop = False
		elif key.c == ord('p'):
			show_party(party,world,party_actions)
			libtcod.console_clear(0)
			finished_stop = False
		elif key.c == ord('s'):
			campsite = make_camp(party,world,party_actions,campsite,my_location)
			libtcod.console_clear(0)
			finished_stop = False
                elif key.c == ord('m'):
                        show_travel_msg(messages)
                        libtcod.console_clear(0)
                        finished_stop = False

def travel(party,world,start,my_area,party_actions):
	starting_area = my_area
	orig_area = my_area
	orig_area_x = orig_area.x
	orig_area_y = orig_area.y
	start_location = find_location(party,world)
	messages = []
	first_time = True
	def show_locations():
		#libtcod.console_clear(0)
	        libtcod.console_print(0,1,1, my_location.area)
                libtcod.console_print(0,43,1, '[ESC]')
                libtcod.console_print(0,1,3, '[/] world map.')

		locations = []
		for location in my_area.locations:
			locations.append(location)
		count = 1
		options = []
		letter = " "
		for location in locations:
			line = count + 5
			#print count
			letter = num_to_letter(count)
	                option = [letter,location]
			options.append(option)
			#print location.name
			#print my_location.name
			if location.name == my_location.name and my_location.items == location.items and my_location.actors == location.actors:
				string = '[' + letter + '] ' + location.name + "*"
				width = len(string)
				libtcod.console_set_default_foreground(0, libtcod.green)
				if count <= 60:
					#libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                                        if type(location.owned_by) == str:
	                                        libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                                                libtcod.console_set_default_foreground(0, libtcod.gray)
                                                libtcod.console_print(0,30,line, " (" + location.owned_by + ")")
                                                libtcod.console_set_default_foreground(0, libtcod.white) 
                                        else:
                                                libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                                                libtcod.console_set_default_foreground(0, libtcod.gray)
                                                libtcod.console_print(0,30,line, " (" + location.owned_by.name + ")")
                                                libtcod.console_set_default_foreground(0, libtcod.white) 

				elif count >= 61:
                                        if type(location.owned_by) == str:
                                                libtcod.console_print(0,50,line, '[' + letter + '] ' + location.name)
                                                libtcod.console_set_default_foreground(0, libtcod.gray)
                                                libtcod.console_print(0,75,line, " (" + location.owned_by + ")")
                                                libtcod.console_set_default_foreground(0, libtcod.white) 
                                        else:
                                                libtcod.console_print(0,50,line, '[' + letter + '] ' + location.name)
                                                libtcod.console_set_default_foreground(0, libtcod.gray)
                                                libtcod.console_print(0,75,line, " (" + location.owned_by.name + ")")
                                                libtcod.console_set_default_foreground(0, libtcod.white) 
					#libtcod.console_print(0,60,line-42, '[' + letter + '] ' + location.name)
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
				if location.owned_by != None:
					if count <= 60:
						if type(location.owned_by) == str:
	                                                libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
							libtcod.console_set_default_foreground(0, libtcod.gray)
                                                        libtcod.console_print(0,30,line, " (" + location.owned_by + ")")
                                                        libtcod.console_set_default_foreground(0, libtcod.white) 

						else:
							libtcod.console_print(0,1,line, '[' + letter + '] ' + location.name)
                                                        libtcod.console_set_default_foreground(0, libtcod.gray) 
							if location.owned_by.name == None:
                                                        	libtcod.console_print(0,30,line, " (" + location.owned_by.fname + " " + lname + ")")
                                                        	libtcod.console_set_default_foreground(0, libtcod.white) 
                                                        elif location.owned_by.name != None:
                                                                libtcod.console_print(0,30,line, " (" + location.owned_by.name + ")")
                                                                libtcod.console_set_default_foreground(0, libtcod.white)
							else:
                                                                libtcod.console_set_default_foreground(0, libtcod.white) 
 

					elif count >= 61:
						if type(location.owned_by) == str:
                                                        libtcod.console_print(0,50,line-21, '[' + letter + '] ' + location.name)
                                                        libtcod.console_set_default_foreground(0, libtcod.gray) 
                                                        libtcod.console_print(0,75,line-21, " (" + location.owned_by + ")")
                                                        libtcod.console_set_default_foreground(0, libtcod.white) 


                                                elif type(location.owned_by) != str:
                                                        libtcod.console_print(0,50,line-21, '[' + letter + '] ' + location.name)
                                                        libtcod.console_set_default_foreground(0, libtcod.gray)
							if location.owned_by != None: 
                                                        	if type(location.owned_by.name) != str:
                                                        	        libtcod.console_print(0,75,line-21, " (" + location.owned_by.fname + " " + lname + ")")
                                                        	        libtcod.console_set_default_foreground(0, libtcod.white) 
                                                        	elif location.owned_by.name != None:
                                                        	        libtcod.console_print(0,75,line-21, " (" + location.owned_by.name + ")")
                                                        	        libtcod.console_set_default_foreground(0, libtcod.white) 

								else:
 	                                                	        libtcod.console_set_default_foreground(0, libtcod.white) 

			count += 1
		return options,my_area
	def show_map(options):
		#libtcod.console_clear(0)
		offset_x = 5
		offset_y = 50
		rows = 32
		columns = 32
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
        def main_menu(my_area,party,world,my_location,start):
        #finished = False
                my_location = find_location(party,world)
                if my_location.parent_location != None:
                        my_location = my_location.parent_location
                #my_area = find_area(party,world)
                start_area = my_area
                start_area_x = party.area_x
                start_area_y = party.area_y
                libtcod.console_clear(0)
                options,my_area = show_locations()
		new_area = my_area
                show_map(options)
		return options,start_area,start_area_x,start_area_y,new_area
	def travel_menu(my_location,my_area,party,world,start_area,start):
		my_location = find_location(party,world)
		options,start_area,start_area_x,start_area_y,new_area = main_menu(my_area,party,world,my_location,start)
        	finished_action = False
		new_area =find_area(party,world)
		new_area = my_area
        	while finished_action == False:
			#libtcod.console_clear(0)
			#show_map()
			#options, my_area = show_locations()
        	        libtcod.console_flush()
               		key = libtcod.console_check_for_keypress()
			for option in options:
				#print option[0]
                		if key.c == ord(option[0]):
                	        	#print 'option a'
					party.location = option[1]
					my_area = find_area(party,world)
					
					my_location = party.location
					new_location = option[1]
					#action = True
					finished_action = True
					print my_location.name
					print my_area.name
                       		        return my_location,my_area,False,start_area,start_area_x,start_area_y,my_area,new_location,True

                        	elif key.vk == libtcod.KEY_ESCAPE:
                        	        my_area = find_area(party,world)
					new_location = start
	                	        return my_location,orig_area,True,orig_area,orig_area_x,orig_area_y,orig_area,new_location,True

				elif key.c== ord('/'):
					libtcod.console_clear(0)
					my_location,my_area = show_areas(party,world,start_area)
					new_location = my_location
					#party.location = my_location2
					#party.area = my_area2.name
					#my_area = find_area(party,world)
					finished_action = False
                                        return my_location,my_area,False,start_area,start_area_x,start_area_y,my_area,new_location,False

					#while finished == False:
                                	#	options2,start_area2,start_area_x,start_area_y,new_area = main_menu(my_area,party,world,my_location)
					#	start_area = start_area2
					#	libtcod.console_flush()
					#	finished2 = False
					#	while finished2 == False:
                				#	#libtcod.console_flush()
                			#		key2 = libtcod.console_check_for_keypress()
						
                			#		for option2 in options2:
                        		#			if key2.c == ord(option2[0]):
				         #                               #print 'option a'
                                        #				party.location = option2[1]
                                        #				my_area = find_area(party,world)

                                        #				my_location = party.location
                                        #				new_location = option2[1]
                                        				#action = True
                                        #				finished_action = True
                                        #				print my_location.name
                                        #				print my_area.name
                                        #				return my_location,my_area,False,start_area,start_area_x,start_area_y,my_area,new_location

					#			elif key2.vk == libtcod.KEY_ESCAPE:
					#				my_area = starting_area
					#				new_location = party.location
					#				my_location = new_location
					#				#party.area = my_area
					#		                return my_location,starting_area,True,start_area,start_area_x,start_area_y,start_area,new_location
	my_location = party.location
	finished_selection = False
	while finished_selection == False:
		my_location,my_area,exit,start_area,start_area_x,start_area_y,new_area,new_location,finished_selection = travel_menu(my_location,my_area,party,world,starting_area,start)
	if exit == True:
		return my_location,True,my_area
	else:
		action = True
	start = start_location
	party.location = new_location
	#get distance to destination
	if start.x >= party.location.x + 1:
		x_distance = start.x - party.location.x
	elif start.x <= party.location.x:
		x_distance = party.location.x - start.x
        if start.y >= party.location.y + 1:
                y_distance = start.y - party.location.y
        elif start.y <= party.location.y:
                y_distance = party.location.y - start.y
	map_distance = x_distance + y_distance
	
	#will we travel to another area
	area_distance = 0
        print 'FROM: ' + starting_area.name
	print 'TO: ' + new_area.name
	if starting_area != new_area:
		if starting_area.x >= new_area.x + 1:
			area_x_distance = starting_area.x - new_area.x
                elif starting_area.x <= new_area.x:
                        area_x_distance = new_area.x - starting_area.x
                if starting_area.y >= new_area.y + 1:
                        area_y_distance = starting_area.y - new_area.y
                elif starting_area.y <= new_area.y:
                        area_y_distance = new_area.y - starting_area.y
		area_distance = area_x_distance + area_y_distance
	else:
		area_x_distance = 0
		area_y_distance = 0
	#
	speed = 1.0
	print 'area distance:'
	print str(area_distance)
	if area_distance >= 1:
		distance = map_distance + ((area_distance - 1) * 32)
	else:
		distance = map_distance
	print distance
	#print action
	new_location_x = 0
	new_location_y = 0
        directions = ['x','y']

	my_x = starting_area.x
	my_y = starting_area.y

	if action == True:
		amount_travelled = 0
		#speed = 1.0
		x_travelled = 0
		y_travelled = 0
		areas_travelled = 0

		#travel east
		possible_directions = []
		if starting_area.x >= new_area.x:
			possible_directions.append("east")
                elif starting_area.x <= new_area.x - 1:
                        possible_directions.append("west")

                if starting_area.y >= new_area.y:
                        possible_directions.append("south")
                elif starting_area.y <= new_area.y - 1:
                        possible_directions.append("north")

		#travel west

		while amount_travelled <= distance:
			#print 'b'
                        #which direction to travel
        	        #find_direction = False
                        #while find_direction == False:
			#	if len(possible_directions) >= 1:
                        #        	direction = random.choice(possible_directions)
			#	elif len(possible_directions) <= 0:
			#		direction = None
                        #        if direction == 'east':
                        # 	       if x_travelled <= x_distance:
                         #       	       x_travelled += 1
                          #                     find_direction = True
                           #     elif direction == 'west':
                            #           if x_travelled >= x_distance - 1:
                             #                  x_travelled += 1
                              #                 find_direction = True

                               # elif direction == 'south':
                                #	if y_travelled <= y_distance:
                                 #       	y_travelled += 1
                                  #              find_direction = True
                                #elif direction == 'north':
                                 #       if y_travelled >= y_distance - 1:
                                  #              y_travelled += 1
                                   #             find_direction = True
				#else:
				#	find_direction = True

				
			#check who cant walk
			cant_walk = []
			for member in party.members:
				if member.health.current_stamina <= 0 and member.combat_status.knocked_down == False:
					member.combat_status.knocked_down = True
					cant_walk.append(member)
				elif member.combat_status.knocked_down == True and member.health.current_stamina >= 1:
					member.combat_status.knocked_down = False
					#member.health.current_stamina -= 1
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
					line_count += 1
					libtcod.console_print(0,1,line_count, "[s]top here.")
					libtcod.console_flush()
					choice_made = False
					while choice_made == False:
						key = libtcod.console_check_for_keypress()
						for option in options:
							if key.c == ord(option[0]):
								drag = [option[1],member]
								dragging.append(drag)
								first_time = True #restart messages
								choice_made = True
							elif key.c == ord('s'):
								travel_stop(party,world,party_actions)
								first_time = True
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
						travel_stop(party,world,party_actions)
						turn_finished = True
				                return my_location, turn_finished, my_area

						#break
		
			#check for angry factions
			#my_area = find_area(party,world)
			angry_factions = []
			for organization in my_area.organizations:
				if organization.player_reputation <= -20:
					angry_factions.append(organization)

			if len(angry_factions) >= 1:
				roll = random.randint(1,100)
				if roll == 10:
					faction = random.choice(angry_factions)
					attackers = []
					max_attackers = random.randint(3,6)
					attacker_count = 1
					while attacker_count <= max_attackers:
						if faction.name == party.area:
							attacker = random.choice(my_area.randos)
						else:
							attacker = random.choice(faction.footsoldiers)
							attacker = attacker[0]
						attackers.append(attacker)
						attacker_count += 1
					attacker_party = NPC(attackers,500,[],50)
					gang_attack_finished = False
					while gang_attack_finished == False:
						gang_attack_finished = faction_attack(party,world,faction,attacker_party,my_location)
						#gang_attack_finished = battle(party,attacker_party,my_location,world,True)
			
			#robbers
			
			
			#chance_robbers = ran
			party_value = party.party_value()
			print "items value: " + str(party_value)

			if party_value <= 2000:
				chance = random.randint(1,500)
			elif party_value >= 2001 and party_value <= 4000:
				chance = random.randint(1,450)
			elif party_value >= 4001 and party_value <= 6000:
				chance = random.randint(1,400)
			elif party_value >= 6001 and party_value <= 8000:
				chance = random.randint(1,350)
			elif party_value >= 8001 and party_value <= 10000:
				chance = random.randint(1,300)
			elif party_value >= 10001 and party_value <= 12000:
				chance = random.randint(1,250)
			elif party_value >= 12001 or party_value <= 14000:
				chance = random.randint(1,200)
			elif party_value >= 14001 or party_value <= 16000:
				chance = random.randint(1,150)
			elif party_value >= 16001 and party_value <= 18000:
				chance = random.randint(1,100)
			elif party_value >= 18001:
				chance = random.randint(1,50)

			if chance == 1:
				factions = []
				for area in world.areas:
					for faction in area.organizations:
						factions.append(faction)

				attacker = random.choice(factions)
				robbery(party,world,True,party_actions,attacker)
			day = world.time.day
                	hour = world.time.hour

			world.time.minute += 1 
			#hour = world.time.hour
		
			world.time.correct(party_actions)
			#daily maitenance
			if world.time.day <= day + 1:
				#clean up corpses, etc
				my_area.clean_up()
				#reduce alarm levels
				for area in world.areas:
					for location in area.locations:
						if location.alarm_level >= 1:
							location.alarm_level -= 1
						if location.rooms != None and len(location.rooms) >= 1:
							for room in location.rooms:
								if room.alarm_level >= 1:
									room.alarm_level -= 1
                        messages = travel_msg(party,world,party_actions,world.time.hour)

			#handle hour changes
			if world.time.hour >= hour + 1 or world.time.hour == 0:
				#messages = travel_msg(party,world,party_actions,world.time.hour)
				for member in party.members:
					member.handle_mind()
					member.hunger += random.randint(2,3)
					if member.hunger >= 101:
						member.hunger = 100 
					member.thirst += random.randint(4,6)
					if member.thirst >= 101:
						member.thirst = 100
					member.sleep -= random.randint(2,4)
					if member.sleep <= -1:
						member.sleep = 0 
					member.health.current_stamina -= random.randint(4,8)
					if member.health.current_stamina <= -1:
						member.health.current_stamina = 0
				for member in party.members:
					if member.health.bleeding_rate >= 1:
						member.bleed()
					chance = random.randint(1,3)
					#member.health.current_stamina -= 1
					if len(dragging) >= 1:
						for member in dragging:
							member[1].health.current_stamina -= 1
				world.weather = get_weather(world.time)
				party.handle_cold(world,my_location)
			elif first_time == True:
				messages = travel_msg(party,world,party_actions,world.time.hour)
				first_time = False
			else:
                                messages = travel_msg(party,world,party_actions,world.time.hour)
				first_time = False
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
        	                #if my_location.broker != None:
	        		#        regulars.append(my_location.broker)

                        	#my_location.actors = NPC(regulars,0,[],0)
			#my_area = find_area(party,world)
			#amount_travelled += 1
		#print my_location
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1, 'Travelling.')
                        libtcod.console_print(0,1,2, str(amount_travelled) + " / " + str(distance))
	                world.time.correct(party_actions)
	                hour = world.time.get_hour()
	                month = world.time.get_month()
       		        am_pm = world.time.get_am_or_pm()
                	libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))
                	if world.time.minute <= 9:
                	        minute = '0' + str(world.time.minute)
                	else:
                	        minute = world.time.minute
                	libtcod.console_print(0,40,2, str(hour) + ':' + str(minute) + ' ' + am_pm)

                	libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))
			if amount_travelled <= map_distance:
	                        libtcod.console_print(0,1,3, starting_area.name)
			elif amount_travelled >= map_distance + 1 and amount_travelled <= distance - 32:
                                libtcod.console_print(0,1,3, "Wasteland")
                        elif amount_travelled >= map_distance + 1 and amount_travelled >= distance - 32 + 1:
                                libtcod.console_print(0,1,3, new_area.name)
			if world.weather.temperature >= 1 and world.weather.temperature <= 19:
                	        libtcod.console_set_default_foreground(0, libtcod.yellow)
                	elif world.weather.temperature >= 20:
                	        libtcod.console_set_default_foreground(0, libtcod.orange)
                	elif world.weather.temperature <= 0 and world.weather.temperature >= -19:
                	        libtcod.console_set_default_foreground(0, libtcod.blue)
                	elif world.weather.temperature <= -20:
                	        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                	libtcod.console_print(0,40,4, str(world.weather.temperature) + "C")
	                libtcod.console_set_default_foreground(0, libtcod.white)
	                if world.weather.clouds == 'Sunny':
	                        libtcod.console_set_default_foreground(0, libtcod.yellow)
       			elif world.weather.clouds == 'Overcast':
                        	libtcod.console_set_default_foreground(0, libtcod.gray)
                	elif world.weather.clouds == 'Dark clouds':
                	        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                	elif world.weather.clouds == 'Light rain':
                	        libtcod.console_set_default_foreground(0, libtcod.light_blue)
                	elif world.weather.clouds == 'Heavy rain' or world.weather.clouds == "Heavy freezing rain":
                	        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                	elif world.weather.clouds == 'Light snow' or world.weather.clouds == "Light freezing rain" or world.weather.clouds == "Heavy snow":
                	        libtcod.console_set_default_foreground(0, libtcod.blue)

                	libtcod.console_print(0,40,3, str(world.weather.clouds))
                	if world.weather.precipitation == True:
                	        libtcod.console_print(0,40,5, str(world.weather.precipitation_type))
			#messages
                        libtcod.console_set_default_foreground(0, libtcod.white)

			libtcod.console_print(0,1,9, "MESSAGES:")
			if len(messages) >= 1:
				msg_count = 1
				for message in messages:
					libtcod.console_set_default_foreground(0, libtcod.white)
					if msg_count <= 10:
						libtcod.console_set_default_foreground(0, message.color)
			                        libtcod.console_print(0,1,10+msg_count, message.message)
					elif msg_count >= 11 and msg_count <= 20:
						libtcod.console_set_default_foreground(0, message.color)
                       	                        libtcod.console_print(0,35,0+msg_count, message.message)
                                        elif msg_count >= 21:
                                                libtcod.console_print(0,35,22, "[m]ore")
					libtcod.console_set_default_foreground(0, libtcod.white)
					msg_count += 1

                	libtcod.console_set_default_foreground(0, libtcod.white)
                        libtcod.console_print(0,1,50, '[s]top here')
                        libtcod.console_print(0,1,51, '# keys adjust speed')
			key = libtcod.console_check_for_keypress()
			if key.c == ord('s'):
				travel_stop(party,world,party_actions)
			elif key.c == ord('1'):
				speed = 1.0
       	                elif key.c == ord('2'):
               	                speed = 0.8
               	        elif key.c == ord('3'):
               	                speed = 0.4
               	        elif key.c == ord('4'):
               	                speed = 0.2
               	        elif key.c == ord('5'):
               	                speed = 0.1
               	        elif key.c == ord('6'):
               	                speed = 0.08
               	        elif key.c == ord('7'):
               	                speed = 0.06
               	        elif key.c == ord('8'):
               	                speed = 0.04
               	        elif key.c == ord('9'):
               	                speed = 0.02
               	        elif key.c == ord('0'):
               	                speed = 0.008
	                elif key.c == ord('m'):
        	                show_travel_msg(messages)
        	                libtcod.console_clear(0)
        	                finished_stop = False


			libtcod.console_flush()
			#save_game()
			party.x = my_area.x
			party.y = my_area.y
			#travelling = False
			print amount_travelled
			print distance
			amount_travelled += 1
			time.sleep(speed)
		turn_finished = True
		#print my_area.name
		print my_location.name
		print start_location.name
		save_game()
		libtcod.console_clear(0)
	        print start_area.name
        	print my_area.name

		return my_location, turn_finished, my_area

# T U R N

def turn(party,world,turn_finished,location,party_actions):
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
			if item.name == "Blood":
				libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_orange)

			print_line = item_count + line_count
                        libtcod.console_print(0,1,print_line, item.name)
                        if item.name == "Blood":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)

		elif item_count >= 11 and item_count <= 20:
                        if item.name == "Blood":
                                libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_orange)


                        print_line = item_count + line_count - 10
                        libtcod.console_print(0,20,print_line, item.name)
                        if item.name == "Blood":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)

                elif item_count >= 21 and item_count <= 32:
                        if item.name == "Blood":
                                libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_orange)

                        print_line = item_count + line_count - 20
                        libtcod.console_print(0,40,print_line, item.name)
                        if item.name == "Blood":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)
                        if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater":
                                libtcod.console_set_default_foreground(0, libtcod.dark_white)

                item_count += 1

        libtcod.console_flush()



	action = False
	while action == False:
		libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
                if key.c == ord('t'):
			location, finished, my_area = travel(party,world,False,my_area,party_actions)
			#my_area = find_area(party,world)
			player_party = Party(True,player,party,location,area,city,my_area.x,my_area.y)
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
	if weapon.name == 'Punch' or weapon.name == "Brass knuckles":
		skills.brawl = random.randint(1,3)
        elif weapon.name == "Knife" or weapon.name == 'Sword' or weapon.name == 'Machete':
		skills.blade = random.randint(1,3) 
	elif weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
        	skills.blunt = random.randint(1,3)
        elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
                skills.pistol = random.randint(1,3)
        elif weapon.name == "12g Shotgun": 
                skills.shotgun = random.randint(1,3) 
        elif weapon.name == "AK-47": 
                skills.rifle = random.randint(1,3) 
        outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_player_outfit(profession, gender)
        age = random.randint(18,45)
        hp = strength + dexterity + willpower
        traits = gen_player_traits(gender)
	if gender == 'Male':
		fname = random.choice(male_fnames)
	elif gender == "Female":
		fname = random.choice(female_fnames)
	lname = random.choice(surnames)
        if profession == "Hipster":
        	money = 500
        else: 
        	money = 100
        return player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor
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
#        for area in city:
 #       	for location in area:
  #              	print location.name


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
			health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
			skills = gen_skills(profession)
			skills_xp = skills
			weapon = gen_player_weapons(profession)
			possible_outerwear = [leather_jacket,sports_jacket,trenchcoat]
			outerwear = random.choice(possible_outerwear)
			armor = no_armor
			outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_player_outfit(profession,gender)
			tool = 'None'
			drugs = []
			traits = gen_player_traits(gender)
			affiliation = 'Player Organization'
			combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)
	                #mind
	                happiness = random.randint(40,100)
	                stress = random.randint(0,25)
	                sanity = random.randint(40,100)
	                horny = random.randint(0,35)
			morale = random.randint(1,60)
			#addictions
	                nicotine_addiction = Addiction('Nicotine',0,0,4,[])

        	        for trait in traits:
        	                if trait.name == 'Smoker':
        	                        nicotine_addiction = Addiction('Nicotine',0,random.randint(1,4),4,[])

        	        caffeine_addiction = Addiction('Caffeine',0,0,2,[])
        	        cocaine_addiction = Addiction('Cocaine',0,0,7,[])
        	        opiates_addiction = Addiction('Opiates',0,0,10,[])
        	        speed_addiction = Addiction('Speed',0,0,7,[])
        	        for trait in traits:
        	                if trait.name == 'Loves drugs':
        	                        possible_drugs = [speed_addiction,opiates_addiction,cocaine_addiction]
        	                        drug = random.choice(possible_drugs)
        	                        drug.addiction_level = random.randint(2,5)


	                addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
			trauma = 0
	                mind = Mind(happiness,stress,sanity,horny,addictions,trauma,morale)

			hunger,thirst,sleep = 0,0,100

			stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
			home = 'None'
			party_member = Char(gender,age, profession,affiliation,health, stats, [], skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'player',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
			party_members.append(party_member)
			count += 1 
	#print player_party.location
	libtcod.console_clear(0)
	#generate world
	world = create_world(player)
	#choose random starting location
	locations = []
	for area in world.areas:
		if area.name == 'Cliff Heights':
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
        player_party = Party(True,player,party_members,location,area,city,money,inventory,location,fame,1,1,None,None)
	my_area = find_area(player_party,world)
	player_party.area_x = my_area.x
	player_party.area_y = my_area.y
	party_actions = Party_Actions(0,0,0,0,0,0,0,0,0,0)
	return player_party,world,party_actions

def gen_mind(traits):
	#mind
        happiness = random.randint(40,100)
        stress = random.randint(0,30)
        sanity = random.randint(40,100)
        horny = random.randint(0,40)
	morale = random.randint(1,60)
        #addictions
        nicotine_addiction = Addiction('Nicotine',0,0,4,[])

        for trait in traits:
        	if trait.name == 'Smoker':
                	nicotine_addiction = Addiction('Nicotine',0,random.randint(1,4),4,[])

        caffeine_addiction = Addiction('Caffeine',0,0,2,[])
        cocaine_addiction = Addiction('Cocaine',0,0,7,[])
        opiates_addiction = Addiction('Opiates',0,0,10,[])
        speed_addiction = Addiction('Speed',0,0,7,[])
        for trait in traits:
        	if trait.name == 'Loves drugs':
                	possible_drugs = [speed_addiction,opiates_addiction,cocaine_addiction]
                        drug = random.choice(possible_drugs)
                        drug.addiction_level = random.randint(2,5)


	addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
        trauma = 0
        mind = Mind(happiness,stress,sanity,horny,addictions,trauma,morale)
        return mind
	

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
        	libtcod.console_print(0, 1, 5, "[a]HUSTLER")
                libtcod.console_print(0, 1, 6, "[b]CRIMEPUNK")
                libtcod.console_print(0, 1, 7, "[c]HIPSTER")
                libtcod.console_print(0, 1, 8, "[d]SCUMBAG")
                libtcod.console_print(0, 1, 9, "[e]WASTOID")
                libtcod.console_print(0, 1, 10, "[f]SCRIPT KIDDIE")
                libtcod.console_print(0, 1, 11, "[g]SEX WORKER")
                libtcod.console_print(0, 1, 12, "[h]LOST SOUL")	
                libtcod.console_print(0, 1, 13, "[i]MEATBALL") 
                libtcod.console_print(0, 1, 14, "[j]SUVIVALIST") 
                libtcod.console_print(0, 1, 15, "[k]DRUG DEALER") 
                libtcod.console_print(0, 1, 16, "[l]HOBO") 


		libtcod.console_flush()
                key = libtcod.console_check_for_keypress()
                if key.c == ord('a'):
                        profession = 'Hustler'
                        choose_profession = True
                elif key.c == ord('b'):
                        profession = 'Crimepunk'
                        choose_profession = True
                elif key.c == ord('c'):
                        profession = 'Hipster'
                        choose_profession = True
                elif key.c == ord('d'):
                        profession = 'Scumbag'
                        choose_profession = True
                elif key.c == ord('e'):
                        profession = 'Wastoid'
                        choose_profession = True
                elif key.c == ord('f'):
                        profession = 'Script Kiddie'
                        choose_profession = True
                elif key.c == ord('g'):
                        profession = 'Sex Worker'
                        choose_profession = True
                elif key.c == ord('h'):
                        profession = 'Lost Soul'
                        choose_profession = True
		elif key.c == ord('i'):
			profession = 'Meatball'
			choose_profession = True
                elif key.c == ord('j'):
                        profession = 'Survivalist'
                        choose_profession = True
                elif key.c == ord('k'):
                        profession = 'Drug Dealer'
                        choose_profession = True
                elif key.c == ord('l'):
                        profession = 'Hobo'
                        choose_profession = True


	if choose_gender == True and choose_profession == True:
		libtcod.console_clear(0)
		while confirm_roll == False:
                	strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
                        stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
                        max_health = stats.strength * 10
                        health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
                        combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)

			player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_character(profession,gender)
			affiliation = "Player Organization"
			skills_xp = skills
			drugs = []
			home = None
			#hunger,thirst,sleep= 0,0,100
                                #player = Char(gender, age, profession,affiliation,health, stats,[], skills,skills_xp,weapon,outfit,None,traits,drugs,fname,lname,money,
 	                        #       'player',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)


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
			finished = False
			while finished == False:
	                	key = libtcod.console_check_for_keypress()
				if key.c == ord("a"):
					print 'confirm'
					libtcod.console_clear(0)
					finished, confirm_roll = True, True
					#return True
					#finished = 
				elif key.c == ord("r"): 
					libtcod.console_clear(0)
		        	        strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
					#player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname = gen_character(profession,gender)
               				stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
               				#max_health = stats.strength * 10
               				health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
               				combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)
					player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_character(profession,gender)
	                                #mind = gen_mind(traits)
		                                #player = Char(gender, age, profession,affiliation,health, stats,[], skills,skills_xp,weapon,outfit,None,traits,drugs,fname,lname,money,
	                                        #'player',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
                                        finished, confirm_roll = True, True

			#confirm_roll = True
	if confirm_roll == True:
		
        	#lets go
		libtcod.console_clear(0)
                id = 1

		#health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)
		drugs = []
		#fame = 0

#		stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
#		max_health = stats.strength * 10
#		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100)
#		combat_status = Cobat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False)
                player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_character(profession,gender)
                #max_health = stats.strength * 10
                health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
		mind = gen_mind(traits)
		stats = Stats(strength, dexterity, intelligence, willpower, charisma, strength, dexterity, intelligence,willpower,charisma)
		skills_xp = skills
		home = 'None'
		affiliation = 'Player Organization'

		hunger,thirst,sleep = 0,0,100
		possible_outerwear = [trenchcoat,leather_jacket,cheap_suit,sports_jacket]
		outerwear = random.choice(possible_outerwear)
		armor = no_armor
                player = Char(gender, age, profession,affiliation,health, stats,[], skills,skills_xp,weapon,outfit,None,traits,drugs,fname,lname,money,
			'player',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
		target = player
		finished = False
		first_time = True
		while finished == False:
			libtcod.console_clear(0)
			confirmed = show_character(target,None,False,None,None,True)
			if first_time == True:
				first_time == False
			if confirmed == True:
				finished = True
			elif confirmed == False:
				libtcod.console_clear(0)
				#roll_stats()
				strength, dexterity, intelligence, willpower, charisma = gen_player_stats(profession)
                        	player_stats, skills, weapon, outfit, age, hp, traits, money,fname,lname,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_character(profession,gender)
				mind = gen_mind(traits)
				skills_xp = skills
                		player = Char(gender, age, profession,affiliation,health, stats,[], skills,skills_xp,weapon,outfit,None,traits,drugs,fname,lname,money,
                        		'player',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
				
                		target = player
				finished= False
	                        #confirmed = show_character(target,None,False,None,None,True)

		#player_party, world = create_party(player)
	
		return player
	        #play_turn(player_party,world,True)

def take_damage(damage,target):
                target.health.current_health = target.health.current_health - damage
		return target.health.current_health

def enemy_attack(attacker,target,player):

                libtcod.console_print(0,1,line_count,"ENEMY ATTACK:")



def attack(attacker,target,party,controller,my_location,player,world,show_fight,party_actions):
	#my_area = find_area(party,world)
	attack_finished = False
	libtcod.console_clear(0)
	line_count = 1
	just_set_on_fire = False
	got_concussion = False
	target_chosen = False
	possible_targets = []
	target_name = target.fname + " " + target.lname
	if controller == "enemy":
		libtcod.console_print(0,1,line_count,"ENEMY ATTACK:")
		line_count += 1

	else:
		line_count = 1

	#do we need ammo
	no_ammo = False
	if attacker.weapon.needs_ammo == True and attacker.weapon.ammo != None:
		#do we have ammo
		if attacker.weapon.ammo.current_rounds != None:
			if attacker.weapon.ammo.current_rounds >= 1:
				attacker.weapon.ammo.current_rounds -= 1
			elif attacker.weapon.ammo.current_rounds <= 0:
				my_weapon = attacker.weapon
				party.inventory.append(my_weapon)
				attacker.weapon = attacker.weapon.melee
				no_ammo = True
	elif attacker.weapon.needs_ammo != None:
		if attacker.weapon.needs_ammo == True and attacker.weapon.ammo == None:
				my_weapon = attacker.weapon
				party.inventory.append(my_weapon)
				attacker.weapon = attacker.weapon.melee
				no_ammo = True
	if target.combat_status.knocked_down == False:
		libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " attacks " + target.fname + " " + target.lname + " with a " + attacker.weapon.name + ".")
        elif target.combat_status.knocked_down == True:
		if my_location.is_indoors == False:
                	libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " attacks " + target.fname + " " + target.lname + " with a " + attacker.weapon.name + " while they are on the ground.")
                elif my_location.is_indoors == True:
                        libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " attacks " + target.fname + " " + target.lname + " with a " + attacker.weapon.name + " while they are on the floor.")


	#print target.fname + " " + target.lname
	line_count += 1
	strength_bonus = 0
	attacker.mind.stress += 5
	#get the attacker skill with the weapon & add strength bonus to damage if brawl
	if attacker.weapon.weapon_type == "brawl":
		print attacker.skills
		attacker_skill = attacker.skills.brawl
		strength_bonus = attacker.stats.strength / 5
        elif attacker.weapon.weapon_type == "blade":
                #print attacker.skills
                attacker_skill = attacker.skills.blade
                strength_bonus = attacker.stats.strength / 8
        elif attacker.weapon.weapon_type == "blunt":
                #print attacker.skills
                attacker_skill = attacker.skills.blunt
                strength_bonus = attacker.stats.strength / 5

        elif attacker.weapon.weapon_type == "pistol" or attacker.weapon.name == "Bear mace":
                attacker_skill = attacker.skills.pistol
        elif attacker.weapon.weapon_type == "shotgun":
                attacker_skill = attacker.skills.shotgun
        elif attacker.weapon.weapon_type == "rifle":
                attacker_skill = attacker.skills.rifle
        elif attacker.weapon.weapon_type == "throw":
                attacker_skill = attacker.skills.throw

	#chance to improve skill
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
		elif attacker.weapon.weapon_type == 'throw':
			attacker.skills.throw += 1

	#do we have a fire mode
	fire_mode = 'single'
	if attacker.weapon.has_fire_modes == True:
		fire_mode = attacker.weapon.current_fire_mode
	#attack roll
	attack_roll = random.randint(1,10) + attacker_skill
	#defend roll
	defend_roll = random.randint(1,10) + target.skills.dodge
	#check if attacker or target are blind
	if attacker.combat_status.blind == True:
		attack_roll = attack_roll / 5
        if target.combat_status.blind == True:
                defend_roll = attack_roll / 5
	#check for concussions
        if attacker.combat_status.concussion == True:
                attack_roll = attack_roll / 2
        if target.combat_status.concussion == True:
                defend_roll = attack_roll / 2



	defense = target.outfit.defense + target.headwear.defense + target.facewear.defense + target.handwear.defense + target.legwear.defense + target.footwear.defense + target.outerwear.defense + target.armor.defense
	defend_roll = defend_roll / 2
	defense_min = defense / 2
	actual_defense = random.randint(defense_min,defense)
        damage_taken = attacker.weapon.damage - actual_defense
        if damage_taken <= -1:
	        damage_taken = 0

	#damage clothing
	#def damage_clothing(attacker,target,injury):
		
	#if attack hits
	if defend_roll <=attack_roll and damage_taken <= 0:
		if attacker.weapon.name == "Bear mace":
	                libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was blinded!")
                        target.combat_status.blind = True
			target.combat_status.max_blind = random.randint(40,60)
			found = False
			for injury in target.injuries.injury:
				if injury.name == "blind":
					found = True
			if found == False:
				target.injuries.append(bear_maced)
		else:
                	libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was unharmed.")
                line_count += 1

	elif defend_roll <= attack_roll and damage_taken >= 1:
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

		elif attacker.weapon.name == 'Brass knuckles' or attacker.weapon.name == '9mm Pistol(Melee)' or attacker.weapon.name == '12g Shotgun(Melee)' or attacker.weapon.name == 'Uzi(Melee)' or attacker.weapon.name == 'AK47(Melee)':
			injury_types = ['bruise','fracture']
			injury_type = random.choice(injury_types)
			if injury_type == 'bruise':
				injury = random.choice(bruises)
			elif injury_type == 'fracture':
				injury = random.choice(fractures)
                        if injury.location == "head" or injury.location == 'face':
                                if damage_taken >= 10 and damage_taken <= 19:
                                        found = False
                                        for injury in target.injuries:
                                                if injury.name == "mild concussion":
                                                        found = True
                                        if found == False:
                                                target.injuries.append(mild_concussion)
                                        target.combat_status.concussion = True
                                        target.combat_status.max_concussion += 120
                                elif damage_taken >= 20:
                                        found = False
                                        for injury in target.injuries:
                                                if injury.name == "minor concussion":
                                                        target.injuries.remove(injury)
                                                        target.injuries.append(severe_concussion)
                                                        found = True
                                                elif injury.name == "severe concussion":
                                                        found = True
                                        if found == False:
                                                got_concussion = True
                                                target.injuries.append(severe_concussion)
                                        target.combat_status.concussion = True
                                        target.combat_status.max_concussion += 240
		elif attacker.weapon.name == "Knife" and damage_taken >= 1:
			attack_types = ['major cut','minor cut','stab','slash']
			attack_type = random.choice(attack_types)
			if attack_type == 'major cut':
				injury = random.choice(major_cuts)
			elif attack_type == 'minor cut':
				injury = random.choice(minor_cuts)
			elif attack_type == 'stab':
				injury = random.choice(stab_wounds)
			elif attack_type == 'slash':
				injury = random.choice(slashes)
                elif attacker.weapon.name == "Sword" or attacker.weapon.name == 'Machete' and damage_taken >= 1:
                        attack_types = ['major cut','minor cut','stab','sever','slash']
                        attack_type = random.choice(attack_types)
                        if attack_type == 'major cut':
                                injury = random.choice(major_cuts)
                        elif attack_type == 'minor cut':
                                injury = random.choice(minor_cuts)
                        elif attack_type == 'stab':
                                injury = random.choice(stab_wounds)
                        elif attack_type == 'slash':
                                injury = random.choice(slashes)
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
			#got_concussion = False
			attack_types = ["bruise","fracture",'maimed']
			attack_type = random.choice(attack_types)
			if attack_type == "bruise":
				injury = random.choice(bruises)
			elif attack_type == "fracture":
				injury = random.choice(fractures)
			elif attack_type == 'mangled':
				injury = random.choice(manglings)
			elif attack_type == 'maimed':
				injury = random.choice(maimings)
			if injury.location == "head" or injury.location == 'face':
				if damage_taken >= 10 and damage_taken <= 19:
					found = False
					for injury in target.injuries:
						if injury.name == "mild concussion":
							found = True
					if found == False:
						target.injuries.append(mild_concussion)
					target.combat_status.concussion = True
					target.combat_status.max_concussion += 120
                        	elif damage_taken >= 20:
					found = False
					for injury in target.injuries:
						if injury.name == "minor concussion":
							target.injuries.remove(injury)
							target.injuries.append(severe_concussion)
							found = True
						elif injury.name == "severe concussion":
							found = True
					if found == False:
						got_concussion = True
                                		target.injuries.append(severe_concussion)
					target.combat_status.concussion = True
					target.combat_status.max_concussion += 240
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
					my_location.items.append(blood)
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
					my_location.items.append(blood)
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
		elif attacker.weapon.name == 'Molotov' and damage_taken >= 1:
			injury = random.choice(burns)
			chance_set_on_fire = random.randint(1,2)
			if chance_set_on_fire == 1 and target.combat_status.on_fire == False:
				just_set_on_fire = True
				target.combat_status.on_fire = True
                elif attacker.weapon.name == 'Shuriken' and damage_taken >= 1:
			if damage_taken <= 30:
                        	injury = random.choice(minor_cuts)
			elif damage_taken >= 31:
				injury = random.choice(major_cuts)

	        #if attacker.weapon.name == "Bear mace":
	        #        my_location.items.append(attacker.weapon)
        	#        attacker.weapon = punch

		#damage clothing
		if injury.location == 'head' or injury.location == 'neck' or injury.location == 'jaw' or injury.location == 'face':
			if target.headwear != None:
				if target.headwear.name!= 'No headwear':
					target.headwear.damage += random.randint(1,3)
					if injury.cause_bleeding >= 1:
						target.headwear.blood += injury.cause_bleeding / 2
					chance_splatter  = random.randint(1,2)
					if chance_splatter == 1:
						target.outfit.blood += injury.cause_bleeding
						
                elif injury.location == 'right arm' or injury.location == 'left arm' or injury.location == 'ribs' or injury.location == 'right collarbone' or injury.location =='left collarbone':
			
                        if target.outerwear != None:
                                if target.outerwear.name!= 'No outerwear':
                                        target.outerwear.damage += random.randint(1,3)
                                        if injury.cause_bleeding >= 1:
                                                target.outerwear.blood += injury.cause_bleeding / 2
						target.outfit.blood += injury.cause_bleeding / 2
			elif outerwear == None or outerwear.name== 'No outerwear':
				if target.outfit != None:
					if target.outfit.name != 'No outfit':
						target.outfit.damage += random.randint(1,3)
                                        	if injury.cause_bleeding >= 1:
                                                	target.outfit.blood += injury.cause_bleeding / 2

		elif injury.location == 'torso':
			if target.armor != None:
				if target.armor.name != 'No armor':
					target.armor.damage += 2
                                        if injury.cause_bleeding >= 1:
                                                target.armor.blood += injury.cause_bleeding / 2
                                                target.outerwear.blood += injury.cause_bleeding / 2
                                                target.outfit.blood += injury.cause_bleeding / 2

			elif target.armor == None or target.armor.name == 'No armor':
                                if target.outerwear != None:
                                	if target.outerwear.name!= 'No outerwear':
                                        	target.outerwear.damage += random.randint(1,3)
                                        	if injury.cause_bleeding >= 1:
                                        	        target.outerwear.blood += injury.cause_bleeding / 2
							#if target.outfit != None and target.outfit != 'No outfit':
							target.outfit.blood += injury.cause_bleeding /2

                                        elif outerwear == None or outerwear.name== 'No outerwear':
                                                if target.outfit != None:
                                                        if target.outfit.name != 'No outfit':
                                                                target.outfit.damage += random.randint(1,3)
                                        			if injury.cause_bleeding >= 1:
                                                			target.outfit.blood += injury.cause_bleeding / 2

                if injury.location == 'left leg' or injury.location == 'right leg' or injury.location == 'groin':
                        if target.legwear != None:
                                if target.legwear.name!= 'No headwear':
					target.legwear.damage += random.randint(1,3)
                                        if injury.cause_bleeding >= 1:
                                                target.legwear.blood += injury.cause_bleeding / 2
		#blood splatter
		chance_clothes = random.randint(1,2)
		if chance_clothes == 1:
                        possible_clothes = [target.headwear,target.facewear,target.outfit,target.outerwear,target.armor,target.handwear,target.legwear,target.footwear]
			found_clothing = False
			while found_clothing == False:
				random_clothing = random.choice(possible_clothes)
				if random_clothing != None:
					if random_clothing.name != 'No headwear' and random_clothing.name != 'No facewear' and random_clothing.name != 'Naked' and random_clothing.name != 'No handwear':
						if random_clothing.name != "No armor" and random_clothing.name != "No outerwear" and random_clothing != "No legwear" and random_clothing != "No footwear":
							random_clothing.blood += 1
							found_clothing = True
					else:
						found_clothing = True
				else:
					found_clothing = True
		#chance_blood = random.randint(1,2)
		#if chance_blood == 1:
		my_location.items.append(blood)
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
			target.mind.trauma += random.randint(5,20)

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
					#if no_ammo == True:
						
					my_location.items.append(target.weapon)
					target.weapon == punch
		                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " lost their weapon.")
		                        line_count += 1

		
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
		elif total_damage <= 0:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is unharmed.")
                        line_count += 1

                if target.health.bleeding_rate >= 1 and target.health.current_health >= 1:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is bleeding.")
                        line_count += 1
		if target.combat_status.knocked_down == True and target.health.current_health >= 1 and just_knocked_down == True:
			libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " was knocked down.")
			line_count += 1
		if target.combat_status.on_fire == True:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is on fire.")
                        line_count += 1
                if target.combat_status.blind == True:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is blind.")
                        line_count += 1
                if target.combat_status.concussion == True:
                        libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " has a concussion.")
                        line_count += 1


		#is target dead?
		
		for injury in target.injuries:
			if injury.name == "severed" or injury.name == "blown off" and injury.location == "head":
				target.health.current_health = 0
				target.health.max_health = 0
		if target.health.current_health <= 0:
			#print defender_party
			
			libtcod.console_print(0,1,line_count,target.fname + " " + target.lname + " is dead.")
			party_actions.kills += 1
			player.fame += random.randint(2,4)
			#drop corpse, items and money at location
			my_location.corpses.append(target)
			if target.weapon.name != "Punch":
				my_location.items.append(target.weapon)
				target.weapon = punch
			#my_location.items.append(target.outfit)
			#target.outfit = naked
			player.money += target.start_money
			
			#is the target in a organization
			org_found = False
			for area in world.areas:
				for organization in area.organizations:
					if organization.name == target.affiliation:
						organization.members_killed += 1
						#residents like it when you kill gang members
						#for area in world.areas:
						#	for organization in area.organizations:
						#		if organization.name == player.area:
						#			organization.members_killed += 1
						#org_found = True
				for corporation in world.corporations:
					if corporation.name == target.affiliation:
						corporation.members_killed += 1
						#org_found = True
					elif corporation.name == my_location.owned_by:
						organization.killed_on_turf += 1

			if org_found == False:
				for area in world.areas:
					for organization in area.organizations:
						if organization.name == player.area:
							organization.members_killed += 1
			#are we on anyone's turf
                        for area in world.areas:
                                for organization in area.organizations:
                                        if organization.name == my_location.owned_by:
                                                organization.killed_on_turf += 1
			for corporation in world.corporations:
				if corporation.name == my_location.owned_by:
					corporation.killed_on_turf += 1
			#is target a mission npc
		        for job in world.missions:
                		if job.type == "Assassination":
					if job.mission.target.fname == target.fname and job.mission.target.lname == target.lname:
						mission.target = target
		                                job.mission.is_complete = True
                        #check if target is in location regulars
			if target in my_location.regulars:
				my_location.regulars.remove(target)
			#cause trauma?
			
                        #else:

			#remove from team
			party.members.remove(target)
			#if len(party.members) == 0:
				#attack_finished = True
				#return attack_finished
			line_count += 1
		#skill increase?
		roll = random.randint(1,2)
                chance_increase = random.randint(1,8)
                if chance_increase == 1 and controller == 'player':
                        libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + "'s " + attacker.weapon.weapon_type + " increased.")
                        line_count += 1
		if no_ammo == True:
			attacker.weapon = my_weapon
		

	#if attack missed
	elif defend_roll >= attack_roll: 
		libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + " missed.")
	        line_count += 1
		to_increase = 8 + target.skills.dodge
		chance_increase = random.randint(1,to_increase)
		if chance_increase == 1 and controller == 'enemy':
			target.skills.dodge += 1
                	libtcod.console_print(0,1,line_count,attacker.fname + " " + attacker.lname + "'s dodge skill is now "+ str(target.skills.dodge) + ".")
			line_count += 1

        if attacker.weapon.name == "Bear mace":
                my_location.items.append(attacker.weapon)
                attacker.weapon = punch
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


def player_battle_attack(attacker,player,enemy,controller,my_location,world,show_fight,party_actions,target):
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
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " does not have enough stamina and is in too much pain to get up.")
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

        elif attacker.combat_status.knocked_down == False  and attacker.health.current_health >= 1 and attacker.health.current_stamina >= 1 and attacker.combat_status.on_fire == True:
		chance_put_out_flames = random.randint(1,2)
		if chance_put_out_flames == 1:
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is no longer on fire")
			attacker.on_fire = False
		else:
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is still on fire!")
        elif attacker.combat_status.knocked_down == True  and attacker.health.current_health >= 1 and attacker.health.current_stamina >= 1 and attacker.combat_status.on_fire == True:
                chance_put_out_flames = random.randint(1,2)
                if chance_put_out_flames == 1:
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is no longer on fire")
                        attacker.on_fire = False
                else:
                        libtcod.console_print(0,1,1, attacker.fname + " " + attacker.lname + " is still on fire!")




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
			libtcod.console_print(0,1,line_count,"[" + str(option_count) + "] " + member.fname + " " + member.lname)
			libtcod.console_print(0,25,line_count,member.outfit.name)
			libtcod.console_print(0,40,line_count, member.weapon.name)
			libtcod.console_print(0,55,line_count, str(member.health.current_health) + "/" + str(member.health.max_health))

		line_count += 2
		#libtcod.console_print(0,1,line_count,"[b]ack")
		libtcod.console_flush()
		choice_made = False
		while choice_made == False:
	                key = libtcod.console_check_for_keypress()
			for option in options:
				target_key = str(option[0])
				defender_skills =  option[1].skills
	                        #print defender_skills
				if key.c == ord(target_key):
					attack_finished = attack(attacker,option[1],enemy,"player",my_location,player,world,True,party_actions)
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
			attack_finished = attack(attacker,target,player,"enemy",my_location,player,world,True,party_actions)
			move_finished = True
			return attack_finished,move_finished
		#fix bug?
		#for member in player.members:
		#	if member != target:
		#		member.health.current_health += 15

	#make stashes visible
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
	
def player_battle_turn(member,player,enemy,my_location,world,True,party_actions):
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
                        #my_location.items.append(member.outfit)
			#member.outfit = naked
			if member.controlled_by == 'enemy':
                        	player.money += member.start_money
				enemy.members.remove(member)
				party_actions.kills += 1
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
                #check if anyone burned to death
		if member.combat_status.on_fire == True:
			damage = random.randint(5,15)
			member.health.current_health -= damage
			injury = random.choice(burns)
			member.injuries.append(injury)
                if member.health.current_health <= 0:
			if member.combat_status.on_fire == True:
                        	libtcod.console_clear(0)
                        	libtcod.console_set_default_foreground(0, libtcod.orange) 
                        	libtcod.console_print(0,1,1,member.fname + " " + member.lname + " burned to death.")
                        	libtcod.console_set_default_foreground(0, libtcod.white) 

                        	libtcod.console_print(0,1,3,"[c]ontinue")
                        	libtcod.console_flush()
                        	my_location.corpses.append(member)
                        	my_location.items.append(member.weapon)
                        	member.weapon = punch
                        #my_location.items.append(member.outfit)
                        #member.outfit = naked
                        if member.controlled_by == 'enemy':
                                player.money += member.start_money
				if enemy in enemy.members:
                                	enemy.members.remove(member)
                                party_actions.kills += 1
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
			libtcod.console_print(0,66,line_count,str(member.health.current_health) + "/" + str(member.health.max_health))
			#libtcod.console_print(0,66,line_count,str(member.skills.brawl))
			if member.combat_status.on_fire == True:
				line_count += 2
                        	libtcod.console_set_default_foreground(0, libtcod.orange) 
                                libtcod.console_print(0,1,line_count,'ON FIRE')
                                libtcod.console_set_default_foreground(0, libtcod.white)
                        if member.combat_status.blind == True:
                                line_count += 2
                                libtcod.console_set_default_foreground(0, libtcod.blue) 
                                libtcod.console_print(0,1,line_count,'BLIND')
                                libtcod.console_set_default_foreground(0, libtcod.white)  
                        if member.combat_status.concussion == True:
                                line_count += 2
                                libtcod.console_set_default_foreground(0, libtcod.yellow) 
                                libtcod.console_print(0,1,line_count,'CONCUSSION')
                                libtcod.console_set_default_foreground(0, libtcod.white)  


				
        		line_count += 2
			if member.combat_status.knocked_down == False and member.combat_status.on_fire == False:
				libtcod.console_print(0,1,line_count,'[a]ttack')
                                #libtcod.console_print(0,30,line_count,'[t]argeted attack')

				line_count +=1
			elif member.combat_status.knocked_down == True:
				libtcod.console_print(0,1,line_count,'[g]et up!')
				line_count += 1
			elif member.combat_status.knocked_down == False and member.combat_status.on_fire == True:
				libtcod.console_print(0,1,line_count,'[p]ut out the flames!')
				line_count += 1
			line_count += 1
                        libtcod.console_print(0,1,line_count,'[s]kip turn')
			line_count += 1
		

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
			elif key.c == ord('p') and member.combat_status.knocked_down == False and member.combat_status.on_fire == True:
                                libtcod.console_clear(0)
                                attack_finished = False
                                move_finished = True
			elif key.c == ord('s'):
				libtcod.console_clear(0)
				attack_finished = True
				move_finished = True

		elif member.controlled_by == "enemy":
			controller = "enemy"
			move_finished = True
	if member.controlled_by == "player":		
		while move_finished == True and attack_finished == False:                        	
			move_finished = player_battle_attack(member,player,enemy,member.controlled_by,my_location,world,True,party_actions,None)
	elif member.controlled_by == "enemy":
		while move_finished == True and attack_finished == False:                               
                        move_finished = player_battle_attack(member,enemy,player,member.controlled_by,my_location,world,True,party_actions,None)

                        #print 'fight!'
	return attack_finished
def initiative(player,enemy,my_location,world,show_fight,party_actions):
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
        	                member_turn_finished = player_battle_turn(member,player,enemy,my_location,world,True,party_actions)
			elif member.controlled_by == 'enemy':
				member_turn_finished = player_battle_turn(member,enemy,player,my_location,world,True,party_actions)
		world.time.minute += 1
		world.time.correct(party_actions)
		turn_finished = True
	return turn_finished

#main battle function

def battle(player,enemy,location,world,show_fight,party_actions):
	#check if player party are dead
	fight_finished = False
	#for member in player.members:
		
	num_player = len(player.members)
	#print "player" + " " + str(len(player.members))
        #print "enemy" + " " + str(len(enemy.members))

	libtcod.console_clear(0)
		
        if len(player.members) == 0:
                fight_finished = True
		return fight_finished
        elif len(enemy.members) == 0:
		player.fame += enemy.fame
		for member in player.members:
			if member == player.leader:
				if player.leader.skills.leadership >= 1:
					chance == 10 * player.leader.skills.leadership
			else:
				chance = 10
		roll = random.randint(1,chance)
		if roll == 1:
			player.leader.skills.leadership += 1
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
		def show():
			libtcod.console_flush()
			line_count = 1
			libtcod.console_print(0,1,line_count, 'YOU:')
			line_count = 2
			option_count = 1
			view_options = []
			for member in player.members:
				letter = num_to_letter(option_count)
				option = [letter,member]
				view_options.append(option)
				libtcod.console_print(0,1,line_count, "[" + letter + "]" + member.fname + " " + member.lname)
                                libtcod.console_print(0,24,line_count,member.profession)
                                if member.armor.name != "No armor" and member.armor.name != "None":
                                        libtcod.console_print(0,39,line_count,member.armor.name)
                                else:
                                        if member.outerwear.name != "No outerwear" and member.outerwear.name != "None":
                                                libtcod.console_print(0,39,line_count,member.outerwear.name)
                                        else:
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
				option = [letter,member]
				view_options.append(option)
				libtcod.console_print(0,1,line_count,"[" + letter + "]" + member.fname + " " + member.lname)
				libtcod.console_print(0,24,line_count,member.profession)
                                if member.armor.name != "No armor" and member.armor.name != "None":
                                        libtcod.console_print(0,39,line_count,member.armor.name)
				else:
					if member.outerwear.name != "No outerwear" and member.outerwear.name != "None":
	                                        libtcod.console_print(0,39,line_count,member.outerwear.name)
					else:
						libtcod.console_print(0,39,line_count,member.outfit.name)
				libtcod.console_print(0,56,line_count,member.weapon.name)
				libtcod.console_print(0,70,line_count,str(member.health.current_health) + "/" + str(member.health.max_health))
		                line_count += 1
				option_count += 1

			line_count += 2
			libtcod.console_print(0,1,line_count, '[ENTER]')
			line_count += 1

			libtcod.console_flush()
			return view_options
		view_options = show()
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
				#print view_options
				my_location = find_location(player,world)
				key = libtcod.console_check_for_keypress()
				for option in view_options:
					if key.c == ord(option[0]):
						option[1] = show_character(option[1],world,False,my_location,player,False)
						libtcod.console_clear(0)
						view_options = show()
				if key.vk == libtcod.KEY_ENTER:
                                       	initiative(player,enemy,location,world,True,party_actions)
                                       	#print 'fight!'
                                       	round_finished,initiative_finished = True,True

#talk to patrol

#dress code
def check_dress_code(player_party,my_location):
	if my_location.security_level >= 1:
#		if dress_code.name == 'none' or dress_code == None:

		if my_location.dress_code.name != None:
			passed_check = True
			num_violations = 0
			#hats and headwear
			if len(my_location.dress_code.headwear) == 0:
				for member in player_party.members:
					if member.headwear != no_headwear:
						passed_check = False
						num_violations += 1
			elif len(my_location.dress_code.headwear) >= 1:
				if member.headwear not in my_location.dress_code.headwear:
					passed_check = False
					num_violations += 1
			elif my_location.dress_code.headwear == None:
				num_violations = num_violations
                        #shirts
                        if len(my_location.dress_code.outfit) == 0:
        	                for member in player_party.members:
                	                if member.outfit != naked:
                        	                passed_check = False
						num_violations += 1

                        elif len(my_location.dress_code.outfit) >= 1:
                        	if member.outfit not in my_location.dress_code.outfit:
                                	passed_check = False
					num_violations += 1
			elif my_location.dress_code.outfit == None:
				num_violations = num_violations
                        #outerwear
                        if len(my_location.dress_code.outerwear) == 0:
                                for member in player_party.members:
                                        if member.outerwear != no_outerwear:
                        	                passed_check = False
						num_violations += 1

                        elif len(my_location.dress_code.outerwear) >= 1:
                                if member.outerwear not in my_location.dress_code.outerwear:
                                        passed_check = False
					num_violations += 1
			elif my_location.dress_code.outerwear == None:
				num_violations = num_violations
                        #legwear
                        if len(my_location.dress_code.legwear) == 0:
                                for member in player_party.members:
                                        if member.legwear != no_legwear:
                        	                passed_check = False
						num_violations += 1

                        elif len(my_location.dress_code.legwear) >= 1:
                                if member.legwear not in my_location.dress_code.legwear:
                                        passed_check = False
					num_violations += 1
                        elif my_location.dress_code.legwear == None:
                                num_violations = num_violations

                        #footwear
                        if len(my_location.dress_code.footwear) == 0:
                                for member in player_party.members:
                                        if member.footwear != no_footwear:
                          	        	passed_check = False
						num_violations += 1

                        elif len(my_location.dress_code.footwear) >= 1:
                                if member.footwear not in my_location.dress_code.footwear:
                                        passed_check = False
					num_violations += 1
                        elif my_location.dress_code.footwear == None:
                                num_violations = num_violations

			#bloody clothes
			for member in player_party.members:
				if member.headwear != no_headwear and member.headwear != None:
					if member.headwear.blood >= 1:
						num_violations += 1
                                if member.facewear != no_facewear and member.facewear != None:
                                        if member.facewear.blood >= 1:
                                                num_violations += 1
                                if member.outfit != naked and member.outfit != None:
                                        if member.outfit.blood >= 1:
                                                num_violations += 1
                                if member.outerwear != no_outerwear and member.outerwear != None:
                                        if member.outerwear.blood >= 1:
                                                num_violations += 1
                                if member.legwear != no_legwear and member.legwear != None:
                                        if member.legwear.blood >= 1:
                                                num_violations += 1
                                if member.footwear != no_footwear and member.footwear != None:
                                        if member.footwear.blood >= 1:
                                                num_violations += 1
                                if member.armor != no_armor and member.armor != None:
                                        if member.armor.blood >= 1:
                                                num_violations += 1
                        #damaged clothes
                        for member in player_party.members:
                                if member.headwear != no_headwear and member.headwear != None:
                                        if member.headwear.damage >= 1:
                                                num_violations += 1
                                if member.facewear != no_facewear and member.facewear != None:
                                        if member.facewear.damage >= 1:
                                                num_violations += 1
                                if member.outfit != naked and member.outfit != None:
                                        if member.outfit.damage >= 1:
                                                num_violations += 1
                                if member.outerwear != no_outerwear and member.outerwear != None:
                                        if member.outerwear.damage >= 1:
                                                num_violations += 1
                                if member.legwear != no_legwear and member.legwear != None:
                                        if member.legwear.damage >= 1:
                                                num_violations += 1
                                if member.footwear != no_footwear and member.footwear != None:
                                        if member.footwear.damage >= 1:
                                                num_violations += 1
                                if member.armor != no_armor and member.armor != None:
                                        if member.armor.damage >= 1:
                                                num_violations += 1

			print 'dress code: ' + str(passed_check)
			print str(num_violations) + ' violations.'
			#is there anyone here to notice we aren't wearing the right clothes
			violations_noticed = 0
			if len(my_location.actors.members) >= 1:
				
				for member in my_location.actors.members:
					disguise_roll = random.randint(1,10)						
					notice_roll = random.randint(1,10)
					if disguise_roll <= member.skills.disguise:
						notice_roll += random.randint(1,3)
					etiquette_roll = random.randint(1,10)
					if etiquette_roll <= member.skills.etiquette:
						notice_roll += random.randint(1,3)
					if my_location.alarm_level >= 1:
						notice_roll -= my_location.alarm_level
					if notice_roll <= my_location.security_level:
						violations_noticed += 1
						my_location.alarm_level += 1

                                        #increase_disguise = 1 + member.skills.disguise * 10
                                        #chance_disguise_increase = random.randint(1,increase_disguise)
					#if chance_disguise_increase == 1:
						#member = random.choice(player_party.members)
					#	member.skills.disguise += 1
                                        #increase_etiquette = member.skills.etiquette * 15
                                        #chance_etiquette_increase = random.randint(1,increase_etiquette)
					#if chance_etiquette_increase == 1:
					#	member.skills.etiquette += 1








				print str(violations_noticed) + ' violations noticed.'
				if violations_noticed <= 4:
					chance_call_security = 5
				elif violations_noticed >= 5:
					chance_call_security = 7
				call_security_count = 0
				alarm_count = 0
				while violations_noticed <= call_security_count:
					chance = random.randint(1,10)
					if chance <= chance_call_security:
						alarm_count += 1
					call_security_count += 1
				print str(my_location.alarm_level) + ' suspicion.'
				if my_location.parent_location == None:
					for room in my_location.rooms:
						room.alarm_level = my_location.alarm_level
				else:
					for room in my_location.parent_location.rooms:
						room.alarm_level = my_location.alarm_level
				#fight?
				fight = False
				fight_chance = my_location.alarm_level + violations_noticed

				if fight_chance >= my_location.security_level:
					libtcod.console_clear(0)
					line_count = 1
					libtcod.console_print(0,1,line_count,"The patrol approaches you.")
					line_count += 2
					libtcod.console_print(0,1,line_count,"[t]alk")
					line_count += 1
					libtcod.console_print(0,1,line_count,"[f]ight")
					libtcod.console_flush()
					choice_made = False
					while choice_made == False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('f'):
							print 'fight!'
							return True
						elif key.c == ord('t'):
							finished_talking = False
							libtcod.console_clear(0)
							line_count = 1
		                                        libtcod.console_print(0,1,line_count,"Who will do the talking?")
                                                        libtcod.console_print(0,35,line_count,"e")
                                                        libtcod.console_print(0,40,line_count,"l")
                                                        libtcod.console_print(0,45,line_count,"p")


							line_count += 2
							options = []
							member_count = 1
							for member in player_party.members:
								letter = num_to_letter(member_count)
								option = [letter, member]
								libtcod.console_print(0,1,line_count,"[" + option[0] + "] " + option[1].fname + " " + option[1].lname)
	                                                        libtcod.console_print(0,35,line_count,str(option[1].skills.etiquette))
                                                                libtcod.console_print(0,40,line_count,str(option[1].skills.lying))
                                                                libtcod.console_print(0,45,line_count,str(option[1].skills.persuasion))

								options.append(option)
								member_count += 1
								line_count += 1
							libtcod.console_flush()

							while finished_talking == False:
								key = libtcod.console_check_for_keypress()
								for option in options:
									if key.c == ord(option[0]):
										passed_check = False
										libtcod.console_clear(0)
										line_count = 0
										libtcod.console_print(0,1,line_count,"What will " + option[1].fname + " " + option[1].lname + " do?")
										line_count += 2
										libtcod.console_print(0,1,line_count,"[e]tiquette       (" + str(option[1].skills.etiquette) + ")" )
										line_count += 1
										libtcod.console_print(0,1,line_count,"[l]ie             (" + str(option[1].skills.lying) + ")")
										line_count += 1
										libtcod.console_print(0,1,line_count,"[p]ersuasion      (" + str(option[1].skills.persuasion) + ")")
										line_count += 1
										libtcod.console_flush()
										finished_choosing = False
										while finished_choosing == False:
											key = libtcod.console_check_for_keypress()
											if key.c == ord('e'):
												libtcod.console_clear(0)
												roll = random.randint(1,15)
												if roll <= option[1].skills.etiquette:
													passed_check = True
												increase_chance = 1 + option[1].skills.etiquette * 10
												increase_roll = random.randint(1,increase_chance)
												if increase_roll == 1:
													option[1].skills.etiquette += 1
												finished_choosing = True
                                                                                        if key.c == ord('l'):
                                                                                                libtcod.console_clear(0)
                                                                                                roll = random.randint(1,15)
                                                                                                if roll <= option[1].skills.lying:
                                                                                                        passed_check = True
                                                                                                increase_chance = 1 + option[1].skills.lying * 10
                                                                                                increase_roll = random.randint(1,increase_chance)
                                                                                                if increase_roll == 1:
                                                                                                        option[1].skills.lying += 1

                                                                                                finished_choosing = True
                                                                                        if key.c == ord('p'):
                                                                                                libtcod.console_clear(0)
                                                                                                roll = random.randint(1,15)
                                                                                                if roll <= option[1].skills.persuasion:
                                                                                                        passed_check = True
                                                                                                increase_chance = 1 + option[1].skills.persuasion * 10
                                                                                                increase_roll = random.randint(1,increase_chance)
                                                                                                if increase_roll == 1:
                                                                                                        option[1].skills.persuasion += 1

                                                                                                finished_choosing = True
										if passed_check == True:
											return False
										else:
											return True

				else:
					return False
		#print my_location .name

def show_container(container,player_party,world,party_actions):
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
	if my_location.owned_by == 'Player':
		libtcod.console_print(0,1,line_count,"[p]ut money in the container")
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
		if key.c == ord('p') and my_location.owned_by == 'Player':
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1,"How much?")
	
			libtcod.console_print(0,1,3,"[a] $50")
                        libtcod.console_print(0,1,4,"[b] $100")
                        libtcod.console_print(0,1,5,"[c] $250")
                        libtcod.console_print(0,1,6,"[d] $500")
                        libtcod.console_print(0,1,7,"[e] $1000")
                        libtcod.console_print(0,1,8,"[f] $5000")
			
                        libtcod.console_print(0,1,10,"[ESC]")

			libtcod.console_flush()
			finished_money = False
			while finished_money == False:
				key = libtcod.console_check_for_keypress()
				if key.vk == libtcod.KEY_ESCAPE:
					finished_money = True
				elif key.c == ord('a'):
					if player_party.money >= 50:
						player_party.money -= 50
						container.money += 50
						finished_money = True
                                elif key.c == ord('b'):
                                        if player_party.money >= 100:
                                                player_party.money -= 100
                                                container.money += 100
						finished_money = True
                               	elif key.c == ord('c'):
                                        if player_party.money >= 250:
                                                player_party.money -= 250
                                                container.money += 250
                                                finished_money = True
                                elif key.c == ord('d'):
                                        if player_party.money >= 500:
                                                player_party.money -= 500
                                                container.money += 500
                                                finished_money = True
                               	elif key.c == ord('e'):
                                        if player_party.money >= 1000:
                                                player_party.money -= 1000
                                                container.money += 1000
                                                finished_money = True
                                elif key.c == ord('f'):
                                        if player_party.money >= 5000:
                                                player_party.money -= 5000
                                                container.money += 5000
                                                finished_money = True
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





def investigate(my_location,world,party,party_actions):
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
        libtcod.console_print(0,1,line_count, "[ENTER] search for hidden items")
	line_count += 2
	libtcod.console_print(0,1,line_count, "[ESC]")
	libtcod.console_flush()
	finished_investigating = False
	

	while finished_investigating == False:
	        key = libtcod.console_check_for_keypress()
		can_search = True
		if len(my_location.actors.members) >= 1:
			for member in my_location.actors.members:
				if member.affiliation != None and member.affiliation != 'none' and member.affiliation == my_location.owned_by:
					can_search = False
		if key.vk != libtcod.KEY_ESCAPE and key.vk!= libtcod.KEY_ENTER:
			#print key.c
			for corpse in corpses_to_investigate:
                                if key.c == ord(corpse[0]):
					my_location = find_location(party,world)
                                        finished_investigating = show_character(corpse[1],world,True,my_location,party,False)
					finished_investigating = True
					return finished_investigating
                        for person in people_to_investigate:
                                if key.c == ord(person[0]):
					my_location = find_location(party,world)
                                        finished_investigating = show_character(person[1],world,False,my_location,party,False)
                                        finished_investigating = True
                                        return finished_investigating
                        for container in containers_to_investigate:
                                if key.c == ord(container[0]):
                                        my_location = find_location(party,world)
                                        finished_investigating = show_container(container[1],party,world,party)
                                        finished_investigating = True
                                        return finished_investigating
		
		elif key.vk == libtcod.KEY_ENTER and can_search == True:
			libtcod.console_clear(0)
			total_investigate = 2
			for member in party.members:
				total_investigate += member.skills.investigate
			roll = random.randint(1,12)
			if roll <= total_investigate and len(my_location.hidden_items) >= 1:
				libtcod.console_clear(0)
				line_count = 1
				libtcod.console_print(0,1,line_count, "You found:")
				line_count += 1
				for item in my_location.hidden_items:
					party.inventory.append(item)
        	                        libtcod.console_print(0,1,line_count, item.name)
					line_count += 1
					my_location.hidden_items.remove(item)
			else:
				libtcod.console_clear(0)
				line_count = 1
                                libtcod.console_print(0,1,line_count, "You found nothing.")
				line_count += 1
			line_count += 1
			libtcod.console_print(0,1,line_count, '[ESC]')
			libtcod.console_flush()
			confirm = False
			while confirm == False:
				key = libtcod.console_check_for_keypress()
				if key.vk == libtcod.KEY_ESCAPE:
					finished_viewing = True
					finished_investigating = True
					return finished_investigating
			world.time.minute += 5
			world.time.correct(party_actions)
		elif key.vk == libtcod.KEY_ENTER and can_search == False:
			libtcod.console_clear(0)
			libtcod.console_print(0,1,1, "You cannot search here.")
			libtcod.console_print(0,1,3, "[c]ontinue")
			libtcod.console_flush()
			confirm = False
                        while confirm == False:
                                key = libtcod.console_check_for_keypress()
                                if key.c == ord('c'):
                                        finished_viewing = True
                                        finished_investigating = True
                                        return finished_investigating

		elif key.vk == libtcod.KEY_ESCAPE:
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
		if item.name == 'None':
			my_location.items.remove(item)
		elif item.name != 'None':
			if item.item_type == 'container':
				if item.is_visible == True:
					can_loot = True
				elif item.is_visible == False:
					can_loot = False
			else:
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
	#if len(my_location.corpses) >= 1 or len(my_location.actors.members) >= 1 or containers_here == True:
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
def handle_footsoldiers(party,world,party_actions):
	for member in world.player_organization.footsoldiers:
                print member.npc.fname + " " + member.npc.lname
		#check if hungry/thirsty
		if member.npc.hunger >= 50:
			types_food = [chocolate_bar,candy,chips,peanuts,beef_jerky,corn_dog]
			food_eaten = random.choice(types_food)
			if party.money >= food_eaten.base_value:
				party.money -= food_eaten.base_value
				member.npc.hunger += food_eaten.nutrition
				print 'ate ' + food_eaten.name
		if member.npc.thirst >= 50:
			drink = cola
			if party.money >= cola.base_value:
				party.money -= cola.base_value
				member.npc.thirst += cola.nutrition
				print 'drank ' + cola.name
		#get the time
		current_time = world.time.hour
		#sleep between midnight and 7am
		if world.time.hour >= 0 and world.time.hour <= 8:
                        member.npc.hunger += 3
                        member.npc.thirst += 6
			member.npc.health.current_stamina += 15
			member.npc.sleep += 15
			if member.npc.hunger >= 100:
				member.npc.hunger = 100
                        elif member.npc.thirst >= 100:
                                member.npc.thirst = 100
                        elif member.npc.health.current_stamina >= 100:
                                member.npc.health.current_stamina = 100
                        elif member.npc.sleep >= 100:
                                member.npc.sleep = 100

			print 'sleep'
		#work from 9am to 5pm
		elif world.time.hour >= 9 and world.time.hour <= 17:
			if member.orders == 'Sell drugs':
				footsoldier_sell_drugs(member,party,world,party_actions)
			elif member.orders == 'Beg for money':
				footsoldier_beg(member,party,world,party_actions)
			elif member.orders == "Pickpocket":
                	        footsoldier_pickpocket(member,party,world,party_actions)
			print member.orders
                        member.npc.hunger += 3
                        member.npc.thirst += 6
                        member.npc.health.current_stamina -= 8
                        member.npc.sleep -= 8
                        if member.npc.hunger >= 100:
                                member.npc.hunger = 100
                        elif member.npc.thirst >= 100:
                                member.npc.thirst = 100
                        elif member.npc.health.current_stamina >= 100:
                                member.npc.health.current_stamina = 100
                        elif member.npc.sleep <= 0:
                                member.npc.sleep = 0
		#leisure from 6pm to 11pm
                elif world.time.hour >= 18 and world.time.hour <= 23:
                        member.npc.hunger += 3
                        member.npc.thirst += 6
                        member.npc.health.current_stamina -= 8
                        member.npc.sleep -= 8
                        if member.npc.hunger >= 100:
                                member.npc.hunger = 100
                        elif member.npc.thirst >= 100:
                                member.npc.thirst = 100
                        elif member.npc.health.current_stamina >= 100:
                                member.npc.health.current_stamina = 100
                        elif member.npc.sleep <= 0:
                                member.npc.sleep = 0
			print 'leisure'

def handle_party_drugs(party,world):
	for member in party.members:
		member.handle_drugs()

def handle_party_mind(party):
	for member in party.members:
		member.handle_mind()

def handle_missions(party,world,party_actions):
	for job in world.missions:
		if job.type == "Assassination":
                        #check if target is alive
			#print job.mission.target.fname + " " + job.mission.target.lname
			#print str(job.mission.target.health.current_health)
                        if job.mission.target.health.current_health <= 0:
                                job.mission.is_complete = True
                        #else:
                        #        job.mission.is_complete = False
			#deadline
			if job.mission.deadline.day >= world.time.day:
				job.mission = job.mission
			elif job.mission.deadline.day <= world.time.day - 1 :
				world.missions.remove(job)
				job.broker.broker.player_reputation -= random.randint(13,20)
				#return True
        for job in world.missions:
                if job.type == "Delivery":
                        #check if target is alive
                        #print job.mission.target.fname + " " + job.mission.target.lname
                        #else:
                        #        job.mission.is_complete = False
                        #deadline
                        if job.mission.deadline.day >= world.time.day:
                                job.mission = job.mission
                        elif job.mission.deadline.day <= world.time.day - 1 :
                                world.missions.remove(job)
                                job.broker.broker.player_reputation -= 25
					
                                #return True

def handle_jobs(party,world):
	for area in world.areas:
		for location in area.locations:
			if location.has_broker == True and location.broker != None:
				if len(location.broker.broker.jobs) <= 0:
					print 'generating new jobs'
					num_jobs = random.randint(2,4)
					job_count = 1
					new_jobs = []
					while job_count <= num_jobs:
						print 'creating job'
						mission_types = ['Assassination','Delivery']
						mission_type = random.choice(mission_types)
						if mission_type == 'Assassination':
							name = mission_type
							print name
							type = mission_type
							#choose target
							found_target = False
							print 'finding target'
							while found_target == False:
								offices = []
								found_office = False
								for area in world.areas:
									for new_location in area.locations:
										for corp in world.corporations:
											if new_location.owned_by == corp.name:
												offices.append(new_location)
										#found_office = True
								office = random.choice(offices)
								if office.rooms != None and len(office.rooms) >= 2:
									target_location = random.choice(office.rooms)
								else:
									target_location = office
								
								#print target_location.name
								if len(target_location.regulars) >= 2:
									target = random.choice(target_location.regulars)
									if target != None:
		                                                        	print "target: " + target.fname + " " + target.lname
										found_target = True
									else:
										found_target = False
								elif len(target_location.regulars) == 1:
									for new_target in target_location.regulars:
										target = new_target
										found_target = True
								else:
									found_target = False
							#print "target: " + target.fname + " " + target.lname
							deadline = world.time
							deadline.day += random.randint(2,5)
							if len(location.broker.broker.factions) >= 1:
								employer = random.choice(location.broker.broker.factions)
							else: 
								employer = random.choice(tech_corps)
							print employer.name
							new_mission = Assassination(target,deadline,False,target_location)
							reward = random.randint(4000,16000)
							new_job = Job('name',type,employer,new_mission,reward,location.broker.broker,location)
							location.broker.broker.jobs.append(new_job)
							print 'job created'
							print location.broker.broker.jobs
							job_count += 1
                                                elif mission_type == 'Delivery':
                                                        name = mission_type
                                                        print name
                                                        type = mission_type
                                                        #choose target
                                                        found_target = False
                                                        print 'finding target'


							items = [cocaine_1000g,crack_1000g,heroin_1000g,speed_1000g,weed_1000g]
							item = random.choice(items)
							if item.number != None:
								num_required = item.number
							else:
								num_required = 0
							item.is_quest = True
                                                        while found_target == False:
                                                                offices = []
                                                                found_office = False
                                                                for area in world.areas:
                                                                        for new_location in area.locations:
                                                                                for faction in area.organizations:
                                                                                        if new_location.is_hq == True:
                                                                                                offices.append(new_location)
                                                                                #found_office = True
                                                                office = random.choice(offices)
                                                                if office.rooms != None and len(office.rooms) >= 2:
                                                                        target_location = random.choice(office.rooms)
                                                                else:
                                                                        target_location = office

                                                                #print target_location.name
                                                                if len(target_location.regulars) >= 2:
                                                                        target = random.choice(target_location.regulars)
                                                                        if target != None:
                                                                                print "target: " + target.fname + " " + target.lname
                                                                                found_target = True
                                                                        else:
                                                                                found_target = False
                                                                elif len(target_location.regulars) == 1:
                                                                        for new_target in target_location.regulars:
                                                                                target = new_target
                                                                                found_target = True
                                                                else:
                                                                        found_target = False
                                                        #print "target: " + target.fname + " " + target.lname
                                                        deadline = world.time
                                                        deadline.day += random.randint(2,5)
                                                        if len(location.broker.broker.factions) >= 1:
                                                                employer = random.choice(location.broker.broker.factions)
                                                        else: 
                                                                employer = random.choice(tech_corps)
                                                        print employer.name
                                                        new_mission = Delivery(item,deadline,target,target_location,False,num_required)
                                                        reward = random.randint(500,2000)
                                                        new_job = Job('name',type,employer,new_mission,reward,location.broker.broker,location)
                                                        location.broker.broker.jobs.append(new_job)
							#party.inventory.append(item)
                                                        print 'job created'
                                                        print location.broker.broker.jobs
							job_count += 1
				#elif len(location.broker.broker.jobs) >= 1:
					#print str(len(location.broker.broker.jobs)) + " jobs here"
	return world				
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
	#check for footsoliders who live here
	for footsoldier in world.player_organization.footsoldiers:
		chance = 1
		if footsoldier.home is str:
			print ignore
		elif footsoldier.home is not str:
			if footsoldier.home == my_location.name:
				print footsoldier.npc.fname + " " + footsoldier.npc.lname
				regulars.append(footsoldier.npc)
        my_area = find_area(party,world)

	#who owns this location
	if my_location.owned_by != 'No one':
		for organization in my_area.organizations:
			for location in organization.locations_owned:
				if location == my_location:
					#chance = random.randint(1,3)
					chance = 1
					if chance == 1:
						num_here = random.randint(1,3)
						owners_added = 1
						while owners_added <= num_here:
							if len(organization.footsoldiers) >= 1:
								footsoldier = random.choice(organization.footsoldiers)
								regulars.append(footsoldier[0])
							owners_added += 1


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
#                        if my_location.has_broker == True:
#				print 'broker is here'
#				print my_location.broker.fname + " " + my_location.broker.lname
 #                               regulars.append(my_location.broker)


			my_location.actors = NPC(regulars,0,[],0)
	except:
		my_location.actors = NPC([],0,[],0)
	if my_location.is_bar == True:
		num_randos = random.randint(1,4)
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
			try:
		        	regular = random.choice(my_area.randos)
        	        	regulars.append(regular)
        	        	rando_count += 1
			except:
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
	regulars = set(regulars)
	regulars = list(regulars)
        my_location.actors = NPC(regulars,0,[],0)



#rest
def rest(party,world,hours,guard):
	messages = []
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	count = 1
	interrupted = False
	can_rest = False
	if my_location.owned_by == None and my_location.owned_by == 'Player':
		can_rest = True
	else:
		can_rest = False
	if can_rest == False:
		message = 'You cannot rest here.'
		messages.append(message)
	print can_rest
	while count <= hours and interrupted == False:
		owned = False
		#do we own this location
		for location in world.player_organization.locations_owned:
			if location == my_location and location.name != "Your Squat":
				drugs_value = party.money
				for item in party.inventory:
					drugs_value += item.base_value
                drugs_value = party.money
	        for item in party.inventory:
        		drugs_value += item.base_value

                #chance to be robbed
                if my_location.owned_by != 'No one':

	                chance = random.randint(1,40)
			if my_location.name == 'My Squat':
				chance = random.randint(1,55)
                        if chance == 1:
        	                for organization in my_area.organizations:
                	                if organization.name == my_location.owned_by and organization.player_reputation <= 24:
                        	                robbery(party,world,True,party_actions,False)
                                                interrupted = True
                                                return interrupted
                elif drugs_value >= 2000 and my_location.owned_by == 'No one':
                	chance = drugs_value / 1000
                        chance_robbery = random.randint(1,500)
                        if chance_robbery <= chance:
                        	robbery(party,world,False,party_actions)
                               	interrupted = True
                               	return interrupted

		#did anyone steal from us
		steal_chance = random.randint(1,50)
		if steal_chance == 1 and owned == False and guard == 'No one' and my_location.name != 'Your Squat':
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
		relax = []
		for item in my_location.items:
			if item.name == "Sleeping bag" or item.name == "Bed" or item.name == "Couch":
				beds.append(item)
			if item.name == 'Cat':
				cats.append(cat)
			if item.name == 'Chair' or item.name == "Couch":
				relax.append(item)
                for item in party.inventory:
                        if item.name == "Sleeping bag":
                                beds.append(item)

		#handle drugs
		handle_party_drugs(party,world)
		#handle npcs
		handle_npcs(party,world)
		world = handle_jobs(party,world)
		#handle missions
		handle_missions(party,world,party_actions)
		#handle_jobs(party,world)
		#handle health
		for member in party.members:
			#member.health.current_health += 1
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
		world.weather = get_weather(world.time)
		world.time.correct(party_actions)
		if day != world.time.day:
                	my_area.clean_up() 

		count += 1
		#handle footsoldiers orders
		handle_footsoldiers(party,world,party_actions)
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
			member.thirst += 6
		#handle npcs
		handle_npcs(party,world)
		#handle missions
		world= handle_jobs(party,world)
		handle_missions(party,world,party_actions)
		#handle cold
		party.handle_cold(world,my_location)
		#sleeping
		messages = []
		for member in party.members:
                        if member != guard and member.sleep <= 30:
                                if len(beds) >= 1:

                                        bed_used = random.choice(beds)
                                        message = member.fname + " " + member.lname + " slept. (" + bed_used.name + ")"
                                        messages.append(message)
                                        beds.remove(bed_used)
                        		if member.health.current_health  <= (member.health.max_health - 1):
                                        	member.health.current_health += random.randint(2,4)
                                        member.sleep += 15
					member.health.current_stamina += 15
					if member.health.current_stamina >= 101:
						member.health.current_stamina = 100
                                else:
                                        member.health.current_health += 1
					member.sleep += random.randint(1,13)
					message = member.fname + " " +  member.lname + " slept."
					messages.append(message)
					member.health.current_stamina += 10
                                        if member.health.current_stamina >= 101:
                                                member.health.current_stamina = 100
                        elif member != guard and member.sleep >= 31:
				#print 'relax'
				if len(relax) >= 1:
					relax_used= random.choice(relax)
	                                message = member.fname + " " + member.lname + " relaxed. (" + relax_used.name + ")"
					messages.append(message) 
	
        	                	if member.health.current_health  <= (member.health.max_health - 1):
						member.health.current_health += 4
					#message = member.fname + " " + member.lname + " relaxed."
					member.health.current_stamina += 10
					relax.remove(relax_used)
				else:
                                        message = member.fname + " " + member.lname + " relaxed." 
                                        messages.append(message) 
        
                                        if member.health.current_health  <= (member.health.max_health - 1):
                                                member.health.current_health += 3
                                        #message = member.fname + " " + member.lname + " relaxed."
                                        member.health.current_stamina += 8
                                if member.health.current_stamina >= 101:
                                	member.health.current_stamina = 100
				#messages.append(message)

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
		#save_game()
		return messages
def robbery(player_party,world,faction,party_actions,attacker_faction):
	libtcod.console_clear(0)
	being_robbed = True
	my_location = find_location(player_party,world)
	my_area = find_area(player_party,world)
	num_robbers = random.randint(2,6)
	robber_count = 1
	robbers = []
	if faction == False and attacker_faction == None:
		while robber_count <= num_robbers:
			robber = random.choice(my_area.randos)
			robbers.append(robber)
			robber_count += 1
		robbers_party = NPC(robbers,100 * num_robbers,[],3 * num_robbers)
	elif faction == True and attacker_faction == None:
		for organization in my_area.organizations:
			if my_location.owned_by == organization.name:
				faction_here = organization.name
				while robber_count <= num_robbers:
					robber = random.choice(organization.footsoldiers)
					robber = robber[0]
					robbers.append(robber)
					robber_count += 1
		robbers_party = NPC(robbers,100 * num_robbers,[],3 * num_robbers)
	elif attacker_faction != None and faction == True:
		faction_here = attacker_faction.name
		while robber_count <= num_robbers and robber_count <= len(attacker_faction.footsoldiers):
			if attacker_faction.footsoldiers >= 1:
	                	robber = random.choice(attacker_faction.footsoldiers)
                        	robber = robber[0]
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
			#line_count += 2
                        #libtcod.console_print(0,1,line_count, "This is our motherfuckin' turf...")

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
			battle(player_party,robbers_party,my_location,world,True,party_actions)
			choice_made = True
		elif key.c == ord('s'):
			for member in player_party.members:
				member.outfit = naked
				member.weapon = punch
			player_party.inventory = []
			player_party.money = 0
			choice_made = True
	return True
def footsoldier_pickpocket(member,party,world,party_actions):
	chance_get_caught = random.randint(3,18)
        bonus = (member.npc.skills.stealth / 2) + (member.npc.skills.security / 2)
        total = member.npc.skills.pickpocket + bonus
        roll = random.randint(3,18)
        roll += total
	if roll >= chance_get_caught:
		party.money += random.randint(5,200)
		party_actions.stealing += 1

def footsoldier_beg(member,party,world,party_actions):
	bonus = (member.npc.skills.etiquette / 2) + (member.npc.skills.streetwise / 2) + (member.npc.stats.charisma / 4)
        total = member.npc.skills.persuasion + bonus
        roll = random.randint(3,18)
        roll += total
        difficulty = random.randint(4,24)
       	if roll >= difficulty + 1:
               	money_earned = random.randint(bonus,bonus*2) * random.randint(1,2)
                party.money += money_earned

def footsoldier_sell_drugs(footsoldier,party,world,party_actions):
	options= []
        drug_count = 1
	my_location = footsoldier.home
	print my_location
	
	#print my_location.name
	if my_location == 'No home':
		print 'no home'
	elif my_location != 'No home':
		if my_location.items is not str:
       			for item in my_location.items:
				print item.name
    			        if item.name == "Crack" or item.name == "Weed" or item.name == "Cocaine" or item.name == "Morphine" or item.name == "Speed" or item.name == "Heroin":
					options.append(item)
	if len(options) <= 0:
		print 'no drugs here to sell'
		return True
	item_to_sell = random.choice(options)
	print 'sell ' + item_to_sell.name
	hour_count = 0
        #my_location = find_location(party,world)
        #my_area = find_area(party,world)
        total_streetwise = 0
        total_disguise = 0
        total_negotiate = 0
        total_streetwise += footsoldier.npc.skills.streetwise
        total_disguise += footsoldier.npc.skills.disguise
        total_negotiate += footsoldier.npc.skills.negotiate
        hour_count = 1
        interrupted = False
        roll = random.randint(1,20)
        drugs_value = 500
        if roll <= total_streetwise + 1:
		print 'passed roll'
       	        if item_to_sell.number >= 2:
			max_sell = footsoldier.npc.skills.negotiate + footsoldier.npc.skills.streetwise
			if max_sell >= item_to_sell.number + 1:
				max_sell = item_to_sell.number
               	        num_sold = random.randint(1,max_sell)
			if num_sold <= item_to_sell.number - 1:
				item_to_sell.number -= num_sold
               	else:
               		num_sold = 1
                        profit = (total_negotiate+ total_streetwise * 2 * (item_to_sell.base_value / 100 ))
                        #party.money += profit + (item_to_sell.base_value * num_sold)
			my_location.items.remove(item_to_sell)
               	if item_to_sell.base_value <= 99:
               		profit = (total_negotiate+ total_streetwise * 4 * (item_to_sell.base_value / 60 ))
               	        #party.money += profit + (item_to_sell.base_value * num_sold)
               	        #found_item = True+ drug_to_sell.base_value

               	elif item_to_sell.base_value >= 100:
               		profit = (total_negotiate + total_streetwise * 8 * (item_to_sell.base_value / 20 ))  
			#party.money += profit + (item_to_sell.base_value * num_sold)
#			found_item = True
		party.money += profit + (item_to_sell.base_value * num_sold)
		party_actions.drug_dealing += num_sold
		fame_increase = random.randint(1,3) * num_sold
		party.fame += fame_increase
		print str(profit + item_to_sell.base_value)
	else:
		print 'failed roll'
        skills = ['streetwise', 'disguise', 'negotiate']
	skill = random.choice(skills)

	if skill == 'negotiate':
		amount = 20*total_negotiate
		#skill_chance = random.randint(1,amount)
        elif skill == 'disguise':
                amount = 20*total_disguise

                #skill_chance = random.randint(1,amount)
        elif skill == 'streetwise':
                amount = 20*total_streetwise

	if amount <= 1:
		amount = 10
        skill_chance = random.randint(1,amount)
	if skill_chance <= 1:
		skill_chance = 10
	roll = random.randint(1,skill_chance)
	if roll == 1:
		if skill == 'negotiate':
			footsoldier.npc.skills.negotiate += 1
                if skill == 'disguise':
                        footsoldier.npc.skills.disguise += 1
                if skill == 'streewise':
                        footsoldier.npc.skills.streetwise += 1
	for member in party.members:
		if member == party.leader:
			if party.leader.skills.leadership >= 1:
				chance = 100 * party.leader.skills.leadership
			else:
				chance = 50
			roll = random.randint(1,chance)
			if roll == 1:
				party.leader.skills.leadership += roll

def deal_drugs(party,world,length_time,party_actions):
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
					#party_actions.drug_dealing += option[1].number
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
					robbery(party,world,True,party_actions,None)
					interrupted = True
					return interrupted
	elif drugs_value >= 1000 and my_location.owned_by == 'No one':
		chance = random.randint(1,50)
		chance_robbery = random.randint(1,250)
		if chance_robbery <= chance:
			robbery(party,world,False,party_actions,None)
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
						profit = (total_negotiate * 2 * (item.base_value / 45 ) * num_sold)
                                        elif item.base_value >= 100:
                                                profit = (total_negotiate * 8 * (item.base_value / 100 ) * num_sold)
					if item.number >= 1:
						total_money = profit + (item.base_value * num_sold)
						party.money += total_money
						party_actions.drug_dealing += num_sold
						libtcod.console_print(0, 1, line_count,"You sold " + str(num_sold) + " " + drug_to_sell.name + " for $" + str(total_money) +  ".")
						line_count += 1
					elif item.number == 0:
               	                                party.inventory.remove(drug_to_sell)

					#disguise_roll = random.randint(1,20)
					#if disguise_roll >= total_disguise: 
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
        world.time.correct(party_actions)
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
	for member in party.members:
		if member == party.leader:
			chance = party.leader.skills.leadership + 1 * 50
			roll = random.randint(1,chance)
			if roll == 1:
				party.leader.skills.leadership += 1

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

def beg(party,world,party_actions):
	libtcod.console_clear(0)
	line_count = 1
	location = find_location(party,world)
	area = find_area(party,world)
        if len(location.actors.members) <= 0:
                return True
        libtcod.console_print(0,1,line_count,"Who will beg?")
        line_count += 2
        count = 1
        options = []
        for member in party.members:
                letter = num_to_letter(count)
                libtcod.console_print(0,1,line_count,"["+ letter + "]" + member.fname + " " + member.lname) 
                libtcod.console_print(0,35,line_count,str(member.skills.persuasion))
                option =[letter,member]
                options.append(option)
                line_count += 1
                count += 1
        choice_made = False
        libtcod.console_flush()
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
                for member in options:
                        if key.c == ord(member[0]):
                                libtcod.console_clear(0)
                                bonus = (member[1].skills.etiquette / 2) + (member[1].skills.streetwise / 2) + (member[1].stats.charisma / 4)
                                total = member[1].skills.persuasion + bonus
                                roll = random.randint(3,18)
                                roll += total
				difficulty = random.randint(4,24)
				if roll >= difficulty + 1:
					money_earned = random.randint(bonus,bonus*2) * random.randint(1,2)
					party.money += money_earned
					line_count = 1
				        libtcod.console_print(0,1,line_count,member[1].fname + ' ' + member[1].lname + ' earned $' + str(money_earned) + '.')
					line_count += 2
				elif roll <= difficulty:
                                        line_count = 1
                                        libtcod.console_print(0,1,line_count,member[1].fname + ' ' + member[1].lname + ' earned nothing.')
                                        line_count += 2

				world.time.hour += 1
				world.time.correct(party_actions)
				libtcod.console_print(0,1,line_count,"[c]ontinue")
				libtcod.console_flush()
				#handle drugs
                		handle_party_drugs(party,world)
                		handle_party_mind(party)
                		handle_npcs(party,world)
				handle_missions(party,world,party_actions)
				world = handle_jobs(party,world)
		                handle_footsoldiers(party,world,party_actions)

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
                        			member.hunger += 3
				if location.owned_by != 'No one':
					for area in world.areas:
						for organization in area.organizations:
							if organization.name == location.owned_by:
								organization.player_reputation -= 1
				confirm = False
				while confirm == False:
					key = libtcod.console_check_for_keypress()
					if key.c == ord('c'):
						confirm = True
						return True
def pickpocket(party,world,party_actions):
	libtcod.console_clear(0)
	line_count = 1
	location= find_location(party,world)
	if len(location.actors.members) <= 0:
		return True
        libtcod.console_print(0,1,line_count,"Who will pickpocket?")
	line_count += 2
	count = 1
	options = []
	for member in party.members:
		letter = num_to_letter(count)
		libtcod.console_print(0,1,line_count,"["+ letter + "]" + member.fname + " " + member.lname) 
	        libtcod.console_print(0,35,line_count,str(member.skills.pickpocket))
                libtcod.console_print(0,45,line_count,str(member.skills.stealth))
                libtcod.console_print(0,35,line_count,str(member.skills.security))
		option =[letter,member]
		options.append(option)
		line_count += 1
		count += 1
	choice_made = False
	libtcod.console_flush()
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				libtcod.console_clear(0)
				chance_get_caught = random.randint(3,18)
				bonus = (member.skills.stealth / 2) + (member.skills.security / 2)
				total = member.skills.pickpocket + bonus
				roll = random.randint(3,18)
				roll += total
				if chance_get_caught >= roll:
			                libtcod.console_print(0,1,1,option[1].fname + " " + option[1].lname + " was caught pickpocketing.")
                                        libtcod.console_print(0,1,3,"[c]ontinue") 

					libtcod.console_flush()
					continued = False
					while continued == False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('c'):
							location = find_location(party,world)
							enemy = location.actors
							battle(party,enemy,location,world,True,party_actions)
							return True
				elif chance_get_caught <= roll - 1:
					amount_stolen = random.randint(5,100)
					line_count = 1
					libtcod.console_print(0,1,line_count,option[1].fname + " " + option[1].lname + " stole  $" + str(amount_stolen) + ".")
					line_count += 1
					skill_chance = random.randint(1,8)
					party.money += amount_stolen
					if skill_chance == 1:
						option[1].skills.pickpocket += 1
						libtcod.console_print(0,1,line_count,option[1].fname + " " + option[1].lname + "'s  Pickpocket is now " + str(option[1].skills.pickpocket) + ".")
						line_count += 1
					libtcod.console_print(0,1,3,"[c]ontinue")
					libtcod.console_flush()
					continued = False
					while continued == False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('c'):
							return True
def make_safehouse(party,world):
	finished_safehouse = False
	libtcod.console_clear(0)
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	price= my_area.price
	vacant_apt = False
	#print location.name
	if party.location.name == "Vacant Apartment":
		vacant_apt = True
		libtcod.console_print(0,1,1,"It will cost $" + str(price) + " and a $" + str(price) + " deposit to rent this apartment.")
		libtcod.console_print(0,1,3,"[r]ent, [b]ack")
        elif party.location.name == "Abandoned Apartment":
                vacant_apt = True
                libtcod.console_print(0,1,1,"Do you want to squat here?.")
                libtcod.console_print(0,1,3,"[y]es, [n]o")
	else:
		libtcod.console_print(0,1,1, "This isn't a apartment you can rent or squat.")
		libtcod.console_print(0,1,3, "[b]ack")
	libtcod.console_flush()
	while finished_safehouse == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('b'):
			finished_safehouse = True
			return finished_safehouse
		if key.c == ord('r') and party.location.name == "Vacant Apartment" and party.money >= (price * 2):
			party.money -= (price * 2)
			party.location.is_safehouse = True
			party.location.items.append(bed)
			party.location.owned_by = 'Player'
			party.location.name = 'Your Apartment'
			world.player_organization.locations_owned.append(party.location)
			world.player_organization.rent_paid = "True"
			world.player_organization.rent_amount += price
			world.player_organization.month = world.time.month
			finished_safehouse = True
			return finished_safehouse
		elif key.c == ord('y') and party.location.name == "Abandoned Apartment":
			for area in world.areas:
				for location in area.locations:
					if location == party.location:
						target = location
                        party.location.is_safehouse = True
                        party.location.owned_by = 'Player'
                        party.location.name = 'Your Squat'
			target = party.location
                        world.player_organization.locations_owned.append(party.location)
                        #world.player_organization.rent_paid = "True"
                        world.player_organization.month = world.time.month
                        world.player_organization.rent_paid = "True"

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
def show_actions(party,world,party_actions):
	finished_action = False
        line_count = 1
        libtcod.console_print(0, 1, line_count,"ACTIONS")
	line_count += 2
        libtcod.console_print(0, 1, line_count,"[a] deal drugs")
	line_count += 1
	libtcod.console_print(0,1,line_count,"[b] rent apartment")
	line_count += 1
	libtcod.console_print(0,1,line_count, "[c] furnish apartment")
        line_count += 1
        libtcod.console_print(0,1,line_count, "[d] pickpocket")
        line_count += 1
        libtcod.console_print(0,1,line_count, "[e] beg")
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
			deal_drugs(party,world,1,party_actions)
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
                elif key.c == ord('d'):
			pickpocket(party,world,party_actions)
                        finished_action = True
                        return finished_action
		elif key.c == ord('e'):
			beg(party,world,party_actions)
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
	my_location = find_location(party,world)
        #make sure thee isn't a corpse and a living person
        for corpse in my_location.corpses:
                for member in my_location.actors.members:
                        if corpse.fname == member.fname and corpse.lname == member.lname: 
				print corpse.fname + " " + corpse.lname
                                my_location.actors.members.remove(member) 
				if member in my_location.regulars:
					my_location.regulars.remove(member)
                        elif corpse == member: 
                                print corpse.fname + " " + corpse.lname
                                my_location.actors.members.remove(member) 


        my_area = find_area(party,world)
        count = 1
        while count <= hours:

                #handle drugs
                handle_party_drugs(party,world)
		handle_party_mind(party)
		handle_npcs(party,world)
		world = handle_jobs(party,world)
                handle_footsoldiers(party,world,party_actions)
		handle_missions(party,world,party_actions)

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
			member.hunger += 3
                #handle time
                day = world.time.day
                world.time.hour += 1
                world.time.correct(party_actions)
		world.weather = get_weather(world.time)
                if day != world.time.day:
                        my_area.clean_up() 
		handle_npcs(party,world)
                count += 1
		
                waiting = True
                while waiting == True:
                        libtcod.console_clear(0)
                        libtcod.console_print(0,1,1, 'Waiting.')
                        libtcod.console_flush()
                        #save_game()
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
def show_homes(footsoldier,world):
        libtcod.console_clear(0)
	options = []
	my_location = 'No home'
	if len(world.player_organization.locations_owned) <= 0:
		libtcod.console_print(0, 1, 1,"You own no locations.")
	elif len(world.player_organization.locations_owned) >= 1:
        	libtcod.console_print(0, 1, 1,"HOMES:")
		options = []
		count = 1
		for location in world.player_organization.locations_owned:
			letter = num_to_letter(count)
			option = [letter,location]
			options.append(option)
	                libtcod.console_print(0, 1,count+1,"[" + letter + "] " + location.name)
			count += 1
        libtcod.console_print(0, 1, 8,"[ESC]")

        libtcod.console_flush()

        finished_viewing = False
        while finished_viewing == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        #print 'b'
                        finished_viewing = True
                        return finished_viewing,my_location
		for option in options:
			if key.c == ord(option[0]):
				my_location = option[1]
				option[1].is_apt = True
				footsoldier[2] = location
				footsoldier[0].home = location
				
		finished_viewing = True
	return finished_viewing,my_location

def show_missions(player,world,party_actions):
        libtcod.console_clear(0)
	line_count = 1
        libtcod.console_print(0, 1, 1,"MISSIONS:")
	line_count += 2
	missions_here = []
        print str(len(world.missions))
        if len(world.missions) >= 1:
                job_count = 1
                for job in world.missions:
                        letter = num_to_letter(job_count)
                        libtcod.console_print(0,1,line_count, "[" + letter + "]" + job.type)
                        libtcod.console_print(0,25,line_count, job.employer.name)
                        libtcod.console_print(0,50,line_count, "$" + str(job.reward))
                        this_mission = [letter,job]
                        missions_here.append(this_mission)
                        job_count += 1
                        line_count += 1
        line_count += 1
        libtcod.console_print(0,1,line_count, "[ESC]")
        libtcod.console_flush()
	location = find_location(player,world)
        finished_showing = False
        while finished_showing == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        finished_showing = True
                else:
			
                        for job in missions_here:
                                if key.c == ord(job[0]) and job[1].type == "Assassination":
                                        finished_showing = show_assassination(job[1],party_actions,False,world,location)
					return finished_showing
                                elif key.c == ord(job[0]) and job[1].type == "Delivery":
                                        finished_showing = show_delivery(job[1],party_actions,False,world,location,player)
                                        return finished_showing

        libtcod.console_flush()
def show_journal(player,world,party_actions):
        libtcod.console_clear(0)
        libtcod.console_print(0, 1, 1,"JOURNAL:")

        libtcod.console_print(0, 1, 3,"[m]issions")

        libtcod.console_print(0, 1, 5,"[ESC]")

        libtcod.console_flush()

        finished_viewing = False
        while finished_viewing == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        #print 'b'
                        finished_viewing = True
                        return finished_viewing
		elif key.c == ord("m"):
			finished_viewing = show_missions(player,world,party_actions)
			return finished_viewing



def show_orders(footsoldier,world,party):
	#target = footsoldier
	#orders = footsoldier[1]
	#home = footsoldier[2]
	my_location = find_location(party,world)
	libtcod.console_clear(0)
        libtcod.console_print(0, 1, 1,"ORDERS:")
        libtcod.console_print(0, 1, 3,"[a] assign home")
        libtcod.console_print(0, 1, 4,"[b] beg for money")
        libtcod.console_print(0, 1, 5,"[c] pickpocket")
        libtcod.console_print(0, 1, 6,"[d] deal drugs")
        libtcod.console_print(0, 1, 8,"[ESC]")

	libtcod.console_flush()

        finished_viewing = False
        while finished_viewing == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        #print 'b'
                        finished_viewing = True
                        return finished_viewing
		elif key.c == ord('a'):
			print 'show homes'
			footsoldier.home = my_location
			#finished_homes = False
			#while finished_homes == False:
			#	finished_homes,footsoldier.home = show_homes(footsoldier,world)
			finished_viewing = True
                elif key.c == ord('b'):
                        footsoldier.orders = 'Beg for money'
                        finished_viewing = True
                elif key.c == ord('c'):
                        footsoldier.orders = 'Pickpocket'
                        finished_viewing = True
                elif key.c == ord('d'):
			footsoldier.orders = 'Sell drugs'
			finished_viewing = True
	footsoldier = Footsoldier(footsoldier.npc,footsoldier.orders,footsoldier.home)
	#print footsoldier[2]
	#return True
def show_character(target,world,corpse,my_location,player_party,creation):
	libtcod.console_clear(0)
        libtcod.console_print(0, 1, 1,target.fname + " " + target.lname)
        libtcod.console_print(0, 1, 2, target.profession)
        libtcod.console_print(0, 1, 3, target.gender)
        libtcod.console_print(0, 1, 5, "Age: " + str(target.age))
	if target.headwear.name != 'None':
	        libtcod.console_print(0, 25, 1, target.headwear.name)
		if target.headwear.damage >= 3:
                	libtcod.console_set_default_foreground(0, libtcod.dark_gray)
	                libtcod.console_print(0, 42, 1, 'd')
	                libtcod.console_set_default_foreground(0, libtcod.white)
                if target.headwear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 43, 1, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.headwear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 44, 1, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.headwear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 45, 1, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)


        elif target.headwear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 25, 1, 'No headwear')
                libtcod.console_set_default_foreground(0, libtcod.white)

	if target.outfit != None:
        	libtcod.console_print(0, 25, 2, target.outfit.name)
                if target.outfit.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 42, 2, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outfit.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 43, 2, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outfit.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 44, 2, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outfit.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 45, 2, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)
        if target.legwear.name != 'None':
                libtcod.console_print(0, 25, 3, target.legwear.name)
                if target.legwear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 42, 3, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.legwear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 43, 3, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.legwear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 44, 3, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.legwear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 45, 3, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)
        elif target.legwear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 25, 3, 'No bottoms')
                libtcod.console_set_default_foreground(0, libtcod.white)
        if target.footwear.name != 'None':
                libtcod.console_print(0, 25, 4, target.footwear.name)
                if target.footwear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 42, 4, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.footwear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 43, 4, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.footwear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 44, 4, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.footwear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 45, 4, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

        elif target.footwear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 25, 4, 'No footwear')
                libtcod.console_set_default_foreground(0, libtcod.white)
        if target.outerwear.name != 'None':
                libtcod.console_print(0, 25, 5, target.outerwear.name)
                if target.outerwear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 42, 5, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outerwear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 43, 5, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outerwear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 44, 5, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.outerwear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 45, 5, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

        elif target.outerwear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 25, 5, 'No outerwear')
                libtcod.console_set_default_foreground(0, libtcod.white)

        libtcod.console_print(0, 50, 1, target.weapon.name)
        if target.facewear.name != 'None':
                libtcod.console_print(0, 50, 2, target.facewear.name)
                if target.facewear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 67, 2, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.facewear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 68, 2, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.facewear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 69, 2, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.facewear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 70, 2, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

	elif target.facewear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 50, 2, 'No facewear')
                libtcod.console_set_default_foreground(0, libtcod.white)
	
        if target.eyewear.name != 'None':
                libtcod.console_print(0, 50, 3, target.eyewear.name)
                if target.eyewear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 67, 3, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.eyewear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 68, 3, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.eyewear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 69, 3, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.eyewear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 70, 3, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

        elif target.eyewear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 50, 3, 'No eyewear')
                libtcod.console_set_default_foreground(0, libtcod.white)
        if target.handwear.name != 'None':
                libtcod.console_print(0, 50, 4, target.handwear.name)
                if target.handwear.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 67, 4, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.handwear.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 68, 4, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.handwear.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 69, 4, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.handwear.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 70, 4, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

        elif target.handwear.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 50, 4, 'No handwear')
                libtcod.console_set_default_foreground(0, libtcod.white)
        if target.armor.name != 'None':
                libtcod.console_print(0, 50, 5, target.armor.name)
                if target.armor.damage >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                        libtcod.console_print(0, 67, 5, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.armor.blood >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)
                        libtcod.console_print(0, 68, 5, 'b')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.armor.dirty >= 3:
                        libtcod.console_set_default_foreground(0, libtcod.dark_brown)
                        libtcod.console_print(0, 69, 5, 'd')
                        libtcod.console_set_default_foreground(0, libtcod.white)
                if target.armor.wet >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                        libtcod.console_print(0, 70, 5, 'w')
                        libtcod.console_set_default_foreground(0, libtcod.white)

        elif target.armor.name == 'None':
                libtcod.console_set_default_foreground(0, libtcod.gray)
                libtcod.console_print(0, 50, 5, 'No armor')
                libtcod.console_set_default_foreground(0, libtcod.white)

	#if target.weapon.needs_ammo == False:
        #        libtcod.console_set_default_foreground(0, libtcod.gray)
        #        libtcod.console_print(0, 75, 1, 'N/A')
        #        libtcod.console_set_default_foreground(0, libtcod.white)
	if target.weapon.needs_ammo == True and target.weapon.ammo != None:
		if target.weapon.ammo.current_rounds >= 1:
			libtcod.console_print(0, 75, 1, '(' +  str(target.weapon.ammo.current_rounds) + ' / ' + str(target.weapon.ammo.max_rounds) + ')')
		else:
	                libtcod.console_set_default_foreground(0, libtcod.red)
			libtcod.console_print(0, 75, 1, 'Out of ammo!')
	                libtcod.console_set_default_foreground(0, libtcod.gray)


	if creation == False and player_party.leader == target:
	        libtcod.console_set_default_foreground(0, libtcod.green)
        	libtcod.console_print(0, 10, 5, 'Leader')
                libtcod.console_set_default_foreground(0, libtcod.white)

	#drug_count = 1
	#for drug in set(target.drugs):
	#	libtcod.console_print(0,40,drug_count,drug.name)
	#	drug_count += 1


        libtcod.console_print(0, 1, 7, "STR: " + str(target.stats.strength))
        libtcod.console_print(0, 1, 8, "DEX: " + str(target.stats.dexterity))
        libtcod.console_print(0, 1, 9, "INT: " + str(target.stats.intelligence))
        libtcod.console_print(0, 1, 10, "WIL: " + str(target.stats.willpower))
        libtcod.console_print(0, 1, 11, "CHA: " + str(target.stats.charisma))

        trait_count = 1
    #    if target.affiliation != None and target.affiliation != 'No one' and target.affiliation != 'none' and target.affiliation != 'Player Organization':
   #             libtcod.console_set_default_foreground(0, libtcod.light_blue)
  #              libtcod.console_print(0, 10, trait_count + 6, target.affiliation)
 #               libtcod.console_set_default_foreground(0, libtcod.white)
#		trait_count += 1

        for trait in target.traits:
		if trait.name == 'Evil' or trait.name == 'Sadist' or trait.name == 'Pyromaniac' or trait.name == 'Crazy' or trait.name == 'Tremors':
			libtcod.console_set_default_foreground(0, libtcod.dark_red)
                if trait.name == 'Angelic' or trait.name == 'Demonic':
                        libtcod.console_set_default_foreground(0, libtcod.dark_orange)
                
                #if trait.name == 'Generous' or trait.name == 'Emotional' or trait.name == 'Focused' or trait.name == 'Imaginative' or trait.name == 'Decisive' or trait.name == 'Adventurous' or trait.name == 'Goofy' or trait.name == 'Empathic' or trait.name == 'Alert' or trait.name == 'Calm' or trait.name == 'Benevolent':
                #        libtcod.console_set_default_foreground(0, libtcod.dark_green)
		if trait_count <= 5:
                	libtcod.console_print(0,10,trait_count + 6, str(trait.name))
                	trait_count += 1
		elif trait_count >= 6 and trait_count <= 10:
                        libtcod.console_print(0,30,trait_count + 1, str(trait.name))
                        trait_count += 1
		elif trait_count >= 11 and trait_count <= 15:
                        libtcod.console_print(0,50,trait_count - 4, str(trait.name))
			trait_count += 1
		libtcod.console_set_default_foreground(0, libtcod.white)
        if target.affiliation != None and target.affiliation != 'No one' and target.affiliation != 'none' and target.affiliation != 'Player Organization':
                libtcod.console_set_default_foreground(0, libtcod.light_blue)
		if trait_count <= 5:
	                libtcod.console_print(0, 10, trait_count + 6, target.affiliation)
                elif trait_count >= 6 and trait_count <= 10:
                        libtcod.console_print(0, 30, trait_count + 1, target.affiliation)
                elif trait_count >= 1 and trait_count <= 15:
                        libtcod.console_print(0, 50, trait_count - 4, target.affiliation)
		trait_count += 1
                libtcod.console_set_default_foreground(0, libtcod.white)

	if corpse == False:
		libtcod.console_print(0, 1, 13, "Health:")
		libtcod.console_print(0, 10, 13, str(target.health.current_health) + " / " + str(target.health.max_health))
		libtcod.console_print(0, 20, 13, "Max health:")
		libtcod.console_print(0, 32, 13, str(target.health.base_max) + "")
                libtcod.console_print(0, 40, 13, "Body temp:")
                libtcod.console_print(0, 60, 13, str(target.health.body_temp))

                libtcod.console_print(0, 40, 14, "Outfit warmth:")
		outfit_warmth = target.check_clothing_warmth()
                libtcod.console_print(0, 60, 14, str(outfit_warmth))

		print "cold_rating: " + str(target.health.cold_rating)
		if target.health.cold_rating >= 20:
			libtcod.console_set_default_foreground(0, libtcod.light_red)
		        libtcod.console_print(0, 40, 15, "Very warm")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                elif target.health.cold_rating >= 10 and target.health.cold_rating <= 19:
                        libtcod.console_set_default_foreground(0, libtcod.orange)
                        libtcod.console_print(0, 40, 15, "Warm")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                elif target.health.cold_rating <= 9 and target.health.cold_rating >= 5:
                        libtcod.console_set_default_foreground(0, libtcod.green)
                        libtcod.console_print(0, 40, 15, "Comfortable")
                        libtcod.console_set_default_foreground(0, libtcod.white)

                elif target.health.cold_rating <= 4 and target.health.cold_rating >= -10:
                        libtcod.console_set_default_foreground(0, libtcod.blue)
                        libtcod.console_print(0, 40, 15, "Cold")
                        libtcod.console_set_default_foreground(0, libtcod.white)
                elif target.health.cold_rating <= -11:
                        libtcod.console_set_default_foreground(0, libtcod.light_blue)
                        libtcod.console_print(0, 40, 15, "Freezing")
                        libtcod.console_set_default_foreground(0, libtcod.white)




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

	if len(target.injuries) == 0 and len(target.drugs) == 0:
                #libtcod.console_set_default_foreground(0, libtcod.dark_green)
		libtcod.console_print(0,1,27,"No injuries.")
                libtcod.console_set_default_foreground(0, libtcod.white)

        #elif len(target.injuries) >= 1:
              #  libtcod.console_print(0,1,27,"INJURIES:")
	injury_count = 1

	#	injury_count += 1
#	if target.affiliation != None and target.affiliation != 'No one':
#                libtcod.console_set_default_foreground(0, libtcod.light_blue)
#                libtcod.console_print(0, 1, injury_count + 27, target.affiliation)
#                libtcod.console_set_default_foreground(0, libtcod.white)

        for injury in target.injuries:
                libtcod.console_set_default_foreground(0, injury.color)

                if injury_count <= 5:
                        libtcod.console_print(0, 1, injury_count + 27, injury.name + "(" + injury.location + ")")
                        injury_count += 1 
                elif injury_count >= 6 and injury_count <= 10:
                        libtcod.console_print(0, 30, injury_count + 22, injury.name + "(" + injury.location + ")")
                        injury_count += 1
                elif injury_count >= 11 and injury_count <= 15:
                        libtcod.console_print(0, 60, injury_count + 17, injury.name + "(" + injury.location + ")")
                        injury_count += 1
                elif injury_count >= 16 and injury_count <= 20:
                        libtcod.console_print(0, 90, injury_count + 12, injury.name + "(" + injury.location + ")")
                        injury_count += 1

                libtcod.console_set_default_foreground(0, libtcod.white)

	for drug in target.drugs:
		if drug.name == 'Cocaine'or drug.name== 'Crack' or drug.name == 'Speed' or drug.name =='Heroin'or drug.name == 'Speed' or drug.name == 'Morphine':
	                libtcod.console_set_default_foreground(0, libtcod.green)
                elif drug.name == 'Cocaine withdrawl'or drug.name== 'Crack withdrawl' or drug.name == 'Speed withdrawl' or drug.name =='Heroin withdrawl'or drug.name == 'Opiate withdrawl':
                        libtcod.console_set_default_foreground(0, libtcod.red)  

                if injury_count <= 5:
                        libtcod.console_print(0, 1, injury_count + 27, drug.name)
                        injury_count += 1 
                elif injury_count >= 6 and injury_count <= 10:
                        libtcod.console_print(0, 30, injury_count + 22, drug.name)
                        injury_count += 1 
                elif injury_count >= 11 and injury_count <= 15:
                        libtcod.console_print(0, 60, injury_count + 17, drug.name)
                        injury_count += 1
                libtcod.console_set_default_foreground(0, libtcod.white)



	libtcod.console_print(0,1,34, "SKILLS:")

        libtcod.console_print(0,1,35, "Blade:")
        libtcod.console_print(0,1,36, "Blunt:")
        libtcod.console_print(0,1,37, "Brawl:")
        libtcod.console_print(0,1,38, "Computer:")
        libtcod.console_print(0,1,39, "Dodge:")
        libtcod.console_print(0,1,40, "Disguise:")
        libtcod.console_print(0,1,41, "Driving:")
        libtcod.console_print(0,1,42, "Etiquette:")
        libtcod.console_print(0,1,43, "Explosive:")

        libtcod.console_print(0,20,35, "First Aid:")
        libtcod.console_print(0,20,36, "Investigate:")
        libtcod.console_print(0,20,37, "Leadership")
        libtcod.console_print(0,20,38, "Lie:")
        libtcod.console_print(0,20,39, "Negotiate:")
        libtcod.console_print(0,20,40, "Persuade:")
        libtcod.console_print(0,20,41, "Pickpocket:")
        libtcod.console_print(0,20,42, "Pistol:")
        libtcod.console_print(0,20,43, "Rifle:")

        libtcod.console_print(0,40,35, "Security:")
        libtcod.console_print(0,40,36, "Seduction:")
        libtcod.console_print(0,40,37, "Shotgun:")
        libtcod.console_print(0,40,38, "Stealth:")
        libtcod.console_print(0,40,39, "Streetwise:")
        libtcod.console_print(0,40,40, "Survival:")
        libtcod.console_print(0,40,41, "Throw:")
        libtcod.console_print(0,40,42, "Torture:")


        libtcod.console_print(0,15,35, str(target.skills.blade))
        libtcod.console_print(0,15,36, str(target.skills.blunt))
        libtcod.console_print(0,15,37, str(target.skills.brawl))
        libtcod.console_print(0,15,38, str(target.skills.computers))
        libtcod.console_print(0,15,39, str(target.skills.dodge))
        libtcod.console_print(0,15,40, str(target.skills.disguise))
        libtcod.console_print(0,15,41, str(target.skills.driving))
        libtcod.console_print(0,15,42, str(target.skills.etiquette))
        libtcod.console_print(0,15,43, str(target.skills.explosives))

        libtcod.console_print(0,35,35, str(target.skills.first_aid))
        libtcod.console_print(0,35,36, str(target.skills.investigate))
        libtcod.console_print(0,35,37,str(target.skills.leadership))
        libtcod.console_print(0,35,38, str(target.skills.lying))
        libtcod.console_print(0,35,39, str(target.skills.negotiate))
        libtcod.console_print(0,35,40, str(target.skills.persuasion))
        libtcod.console_print(0,35,41, str(target.skills.pickpocket))
        libtcod.console_print(0,35,42, str(target.skills.pistol))
        libtcod.console_print(0,35,43, str(target.skills.rifle))

        libtcod.console_print(0,55,35, str(target.skills.security))
        libtcod.console_print(0,55,36, str(target.skills.seduction))
        libtcod.console_print(0,55,37, str(target.skills.shotgun))
        libtcod.console_print(0,55,38, str(target.skills.stealth))
        libtcod.console_print(0,55,39,str(target.skills.streetwise))
        libtcod.console_print(0,55,40,str(target.skills.survival))
        libtcod.console_print(0,55,41, str(target.skills.throw))
        libtcod.console_print(0,55,42, str(target.skills.torture))

	if type(my_location) is str:
        	libtcod.console_print(0,40,13, "Location:" + my_location.name)
	#elif type(my_location) is list:
	#	print my_location
         #       libtcod.console_print(0,40,13, "Location:" + my_location[0])
	if target.combat_status.tied_up == True:
        	libtcod.console_set_default_foreground(0, libtcod.yellow)
        	libtcod.console_print(0,1,45, 'TIED UP')
        	libtcod.console_set_default_foreground(0, libtcod.white)

	if creation == True:
	        libtcod.console_print(0,1,47, "[a]ccept")
                libtcod.console_print(0,25,47, "[r]e-roll")
	if creation == False:
		libtcod.console_print(0,1,49, "[ESC]")
	if corpse == True:
		libtcod.console_print(0,1,48, "[s]trip")
	footsoldier = None
	if creation == False:
		for footsoldier in world.player_organization.footsoldiers:
			if footsoldier.npc == target:
        	        	libtcod.console_print(0,01,47, "[o]rders")
				my_footsoldier = footsoldier

	libtcod.console_flush()

	finished_viewing = False
	while finished_viewing == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			#print 'b'
			finished_viewing = True
			#return finished_viewing
		if key.c == ord('o') and my_footsoldier != None and creation == False:
			finished_viewing = show_orders(my_footsoldier,world,player_party)
			finished_viewing = True
			#return finished_viewing
		elif key.c == ord('s') and corpse == True and creation == False:
			if target.outfit.name != 'None' and target.outfit != None:
				my_location.items.append(target.outfit)
				target.outfit = naked
			if target.headwear.name != 'None' and target.headwear != None:
                                player_party.inventory.append(target.headwear)
                                target.headwear = no_headwear
                        if target.eyewear.name != 'None' and target.eyewear != None:
                                player_party.inventory.append(target.eyewear)
                                target.eyewear = no_eyewear
                        if target.facewear.name != 'None' and target.facewear != None:
                                player_party.inventory.append(target.facewear)
                                target.facewear = no_facewear
                        if target.handwear.name != 'None' and target.handwear != None:
                                player_party.inventory.append(target.handwear)
                                target.handwear = no_handwear
                        if target.legwear.name != 'None' and target.legwear != None:
                                player_party.inventory.append(target.legwear)
                                target.legwear = no_legwear
                        if target.footwear.name != 'None' and target.footwear != None:
                                player_party.inventory.append(target.footwear)
                                target.footwear = no_footwear
                        if target.outerwear.name != 'None' and target.outerwear != None:
                                player_party.inventory.append(target.outerwear)
                                target.outerwear = no_outerwear
                        if target.armor.name != 'None' and target.armor != None:
                                player_party.inventory.append(target.armor)
                                target.armor = no_armor
			finished_viewing = True
		elif key.c == ord('a') and creation == True:
			return True
                elif key.c == ord('r') and creation == True:
                        return False

	return target
			
def show_outfits(target,world):
        finished_outfits = False
        count = 1
        options_list = []
        options_list2 = []
        libtcod.console_clear(0)
	for item in target.inventory:
		if item.name == 'None':
			target.inventory.remove(item)
        while finished_outfits == False:
                for member in target.members:
                        option = [count, member]
                        options_list.append(option)
                        libtcod.console_print(0,1,count,"[" + str(count) + "] " + member.fname + " " + member.lname)
                        libtcod.console_print(0,24,count,member.headwear.name)
                        libtcod.console_print(0,38,count,member.outfit.name)
                        libtcod.console_print(0,54,count,member.legwear.name)
                        libtcod.console_print(0,66,count,member.footwear.name)

                        count += 1
                for item in target.inventory:
                        if item.item_type == 'outfit' or item.item_type == 'headwear' or item.item_type == 'facewear' or item.item_type == 'eyewear' or item.item_type == 'handwear' or item.item_type == 'legwear' or item.item_type == 'footwear' or item.item_type == 'outerwear' or item.item_type == 'armor' or item.item_type == 'tent':
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
                                        if option[1].headwear.name != "None":
                                                target.inventory.append(option[1].headwear)
                                        if option[1].eyewear.name != "None":
                                                target.inventory.append(option[1].eyewear)
                                        if option[1].facewear.name != "None":
                                                target.inventory.append(option[1].facewear)
                                        if option[1].handwear.name != "None":
                                                target.inventory.append(option[1].handwear)
                                        if option[1].legwear.name != "None":
                                                target.inventory.append(option[1].legwear)
                                        if option[1].footwear.name != "None":
                                                target.inventory.append(option[1].footwear)
                                        if option[1].outerwear.name != "None":
                                                target.inventory.append(option[1].outerwear)
                                        if option[1].armor.name != "None":
                                                target.inventory.append(option[1].armor)
                                        option[1].outfit = naked
					option[1].headwear = no_headwear
					option[1].facewear = no_facewear
					option[1].eyewear = no_eyewear
					option[1].handwear = no_handwear
					option[1].legwear = no_legwear
					option[1].footwear = no_footwear
                                        option[1].outerwear = no_outerwear
                                        option[1].armor = no_armor

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
                                        libtcod.console_print(0,1,count + 3,"[*] go back.")
                                        libtcod.console_flush()

                                        while outfit_assigned == False:
                                                key = libtcod.console_check_for_keypress()
                                                for option in options_list:
                                                        item_key = str(option[0])
                                                        if key.c == ord(item_key):
								if my_outfit.item_type == 'outfit':
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
                                                                elif my_outfit.item_type == 'eyewear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].eyewear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].eyewear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].eyewear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'facewear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].facewear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].facewear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].facewear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'handwear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].handwear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].handwear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].handwear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'legwear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].legwear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].legwear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].legwear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'footwear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].footwear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].footwear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].footwear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'headwear':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].headwear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].headwear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].headwear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'outerwear':
                                                                        if option[1].outerwear.name == 'None':
                                                                                option[1].outerwear = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outerwear.name != 'None':
                                                                                target.inventory.append(option[1].outerwear)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].outerwear = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                elif my_outfit.item_type == 'armor':
                                                                        if option[1].outfit.name == 'None':
                                                                                option[1].armor = my_outfit
                                                                                target.inventory.remove(my_outfit)
                                                                                finished_outfit = True
                                                                                return finished_outfit
                                                                        elif option[1].outfit.name != 'None':
                                                                                target.inventory.append(option[1].armor)
                                                                                target.inventory.remove(my_outfit)
                                                                                option[1].armor = my_outfit
                                                                                finished_outfit = True
                                                                                return finished_outfit

								for item in target.inventory:
									if item.name == None:
										target.inventory.remove(item)




							elif key.c == ord("*"):
								finished_outfit = True
								return finished_outfit

def show_ammo(target,world):
        finished_weapons = False
        count = 1
        options_list = []
        options_list2 = []
        libtcod.console_clear(0)
        while finished_weapons == False:
                libtcod.console_print(0,1,1,"AMMO:")
                for member in target.members:
                        option = [count, member]
                        options_list.append(option)
                        libtcod.console_print(0,1,count+1,"[" + str(count) + "] " + member.fname + " " + member.lname)
                        libtcod.console_print(0,24,count+1,member.weapon.name)
			if member.weapon.ammo != None:
	                        libtcod.console_print(0,40,count+1,str(member.weapon.ammo.current_rounds) + " / " + str(member.weapon.ammo.max_rounds))
                        count += 1
		item_count = 1
                for item in target.inventory:
			#item_count = 1
                        if item.item_type == 'ammo':
                                letter = num_to_letter(item_count)
                                option = [letter, item]
                                options_list2.append(option)
				libtcod.console_print(0,1,count + 3 + item_count,"[" + letter + "] " + item.name + " (" + str(item.current_rounds) + " / " + str(item.max_rounds) + ")")
				item_count += 1 
                libtcod.console_print(0,1,count + 7,"Use the number keys to remove a person's ammo.")
                libtcod.console_print(0,1,count + 8,"Use the letter keys to assign ammo.")

                libtcod.console_print(0,1,count + 10,"[ESC]")
		libtcod.console_flush()
		choose_weapon = False
                while choose_weapon == False:
			count = 1
                        #libtcod.console_clear(0)
                        key = libtcod.console_check_for_keypress()
                        if key.vk == libtcod.KEY_ESCAPE:
                                finished_weapons = True
                                return finished_weapons
                        for option in options_list:
                                item_key = str(option[0])
                                if key.c == ord(item_key):
                                        if option[1].weapon.name != "Punch" and option[1].weapon.ammo != None:
                                                target.inventory.append(option[1].weapon.ammo)
                                        option[1].weapon.ammo = None
                                        finished_weapons = True
                                        return finished_weapons
                        for option in options_list2:
                                item_key = str(option[0])
                                if key.c == ord(item_key):
					libtcod.console_clear(0)
                                        my_ammo = option[1]
                                        weapon_assigned = False
					print 'ammo selected'
                			libtcod.console_print(0,1,1,"CLIPS:")
                			for member in target.members:
                        			#option = [count, member]
                        			#options_list.append(option)
                        			libtcod.console_print(0,1,count+1,"[" + str(count) + "] " + member.fname + " " + member.lname)
                        			libtcod.console_print(0,24,count+1,member.weapon.name)
                        			if member.weapon.ammo != None:
                                			libtcod.console_print(0,40,count+1,str(member.weapon.ammo.current_rounds) + " / " + str(member.weapon.ammo.max_rounds))
                        			count += 1
                			item_count2 = 1
                			#for item in target.inventory:
                        			#item_count = 1
                        			#if item.item_type == 'ammo':
                                			#letter = num_to_letter(item_count)
                                			#option = [item_count2, item]
                                			#options_list2.append(option)
                                	#		libtcod.console_print(0,1,item_count2 + 3,"[" + letter + "] " + item.name + " (" + str(item.current_rounds) + " / " + str(item.max_rounds) + ")")
                                	#		item_count2 += 1 
		                                        #count += 1
                			libtcod.console_print(0,1,item_count2 + 9,"Use the number keys to assign the clip to someone.")
                                        #count += 2
                                        libtcod.console_print(0,1,item_count2 + 10,"[ESC]")
                                        libtcod.console_flush()

                                        while weapon_assigned == False:
                                                key2 = libtcod.console_check_for_keypress()
                                                for option in options_list:
							#print item_key
                                                        my_item_key = str(option[0])
							#print my_item_key
                                                        if key2.c == ord(my_item_key):
								#is this the right ammo

								right_ammo = False
								if option[1].weapon.name == "9mm Pistol" and my_ammo.name == "9mm clip":
									right_ammo = True
                                                                if option[1].weapon.name == "12g Shotgun" and my_ammo.name == "12g clip":
                                                                        right_ammo = True
                                                                if option[1].weapon.name == "Uzi" and my_ammo.name == "Uzi clip":
                                                                        right_ammo = True
                                                                if option[1].weapon.name == "AK47" and my_ammo.name == "AK47 clip":
                                                                        right_ammo = True
                                                                if option[1].weapon.name == "Molotov cocktail" and my_ammo.name == "Molotov ammo":
                                                                        right_ammo = True
                                                                if option[1].weapon.name == "Shuriken" and my_ammo.name == "Shuriken ammo":
                                                                        right_ammo = True

								if right_ammo == True and option[1].weapon.ammo == None:
                                                                	if option[1].weapon.ammo == None:
                                                                	        option[1].weapon.ammo = my_ammo
                                                                        	target.inventory.remove(my_ammo)
                                                                        	choose_weapon,finished_weapons = True,True
                                                                        	return finished_weapons
                                                                	elif option[1].weapon.name != 'Punch' :
                                                                	        target.inventory.append(option[1].weapon.ammo)
										option[1].weapon.ammo = None
                                                                	        #target.inventory.remove(my_weapon)
                                                                	        #option[1].weapon = my_weapon
                                                                	        choose_weapon,finished_weapons = True,True
                                                                	        return finished_weapons
								elif right_ammo == True and option[1].weapon.ammo != None:
                                                	#if key.vk == libtcod.KEY_ESCAPE:
                                                        		weapon_assigned = True
                                                        		return weapon_assigned 
                                                if key.vk == libtcod.KEY_ESCAPE:
                                                	weapon_assigned = True
                                                        return weapon_assigned 


                                count += 1
                #libtcod.console_print(0,1,count + 3,"Use the number keys to remove a person's ammo.")
                #libtcod.console_print(0,1,count + 5,"Use the letter keys to assign ammo.")

                #libtcod.console_print(0,1,count + 8,"[ESC]")
                libtcod.console_flush()
                choose_weapon = False
                while choose_weapon == False:
                        libtcod.console_flush()
                        key = libtcod.console_check_for_keypress()
                        if key.vk == libtcod.KEY_ESCAPE:
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
                                        libtcod.console_print(0,1,count + 3,"[ESC]")
                                        return finished_weapons
                choose_weapon = False
                while choose_weapon == False:
                        libtcod.console_flush()
                        key = libtcod.console_check_for_keypress()
                        if key.vk == libtcod.KEY_ESCAPE:
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
                                        libtcod.console_print(0,1,count + 3,"[ESC]")
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
                                                        elif key.vk == libtcod.KEY_ESCAPE:
                                                                finished_weapons = True
                                                                return finished_weapons 


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
		libtcod.console_print(0,1,count + 3,"Use the number keys to remove a person's weapon.")
                libtcod.console_print(0,1,count + 5,"Use the letter keys to assign a weapon.")
                
		libtcod.console_print(0,1,count + 7,"[A]MMO")
                libtcod.console_print(0,1,count + 8,"[ESC]")

		libtcod.console_flush()
		choose_weapon = False
		while choose_weapon == False:
	                libtcod.console_flush()
			key = libtcod.console_check_for_keypress()
			if key.vk == libtcod.KEY_ESCAPE:
				finished_weapons = True
				return finished_weapons
                        elif key.c == ord('A'):
                        	print 'A'
                                finished_weapons = False
                                while finished_weapons == False:
                                       	libtcod.console_clear(0)
                                        finished_weapons = show_ammo(player_party,world)
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
 #                                       count += 2
#                                        libtcod.console_print(0,1,count + 3,"[A]MMO")
					count += 1
                                        libtcod.console_print(0,1,count + 3,"[ESC]")
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
							elif key.vk == libtcod.KEY_ESCAPE:
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
					libtcod.console_print(0,1,1, 'Use ' + item_to_use.name + ' on who?')
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
                                                                        elif item_to_use.number == 1:
										item_to_use.number -= 1
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
									target = member[1]
									libtcod.console_clear(0)
									line = 1
									people2 = people
							                libtcod.console_print(0,1,line, 'Who will apply bandage?' )
									line += 1
									for member in people2:
	                                                                        libtcod.console_print(0,1,line, '[' + member[0] + ']' + member[1].fname + ' ' + member[1].lname)
										line += 1
									libtcod.console_flush()
									bandaging = True
									while bandaging == True:
										key = libtcod.console_check_for_keypress()
										for member in people2:
											if key.c == ord(member[0]):
												libtcod.console_clear(0)
												roll = random.randint(1,6)
												line = 1
												if roll >= member[1].skills.first_aid:
			                                                                        	libtcod.console_print(0,1,line, member[1].fname + ' ' + member[1].lname + ' did a shitty job.' )
				                                                                        target.health.bleeding_rate = target.health.bleeding_rate / 4
													line += 1
												elif roll <= member[1].skills.first_aid:
				                                                                        libtcod.console_print(0,1,line, member[1].fname + ' ' + member[1].lname+ " did a good job." )
													target.health.bleeding_rate = 0
													line += 1
												chance_upgrade = random.randint(1,6+member[1].skills.first_aid)
												if chance_upgrade == 1:
													member[1].skills.first_aid += 1
                                                                                                        line += 1
                                                                                                        libtcod.console_print(0,1,line, member[1].fname + ' ' + member[1].lname + "'s first aid skill is now " + str(member[1].skills.first_aid) + ".")

												confirm = False
                                                                                                line += 2
                                                                                                libtcod.console_print(0,1,line, '[c]ontinue' )
												libtcod.console_flush()
												while confirm == False:
													#libtcod.console_clear(0)
													key = libtcod.console_check_for_keypress()
													if key.c == ord('c'):
                                                                        					if item_to_use.number >= 2:
                                                                                					item_to_use.number -= 1
                                                                        					elif item_to_use.number == 1:
                                                                                					target.inventory.remove(bandages)
														return drugs_used
												bandaging = False

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
		while count <= 10:
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
		libtcod.console_print(0,1,line, '[*] go back' )
		libtcod.console_flush()
		#drop item
                key = libtcod.console_check_for_keypress()
		num_items = len(items)
		#options = []
		key_count = 1
		#for item in items:
		#	letter = num_to_letter(key_count)
		#	item = [letter,item]
		#	options.append(item)
		#	key_count += 1
		def fetch_item(items,key):
			for item in items:
				if item[0] == str(key):
					print 'found item'
					return item
		#print keys
		if key.c == ord('*'):
			libtcod.console_clear(0)
			finished_dropping = True
		for item in items:
			if key.c == ord(item[0]):
				my_location = find_location(target,world)
				#item = option[1]
				#print item.name
				target.inventory.remove(item[1])
				my_location.items.append(item[1])
				libtcod.console_clear(0)
				finished_dropping = True
				return finished_dropping
def show_reputation(player,world):
        libtcod.console_clear(0)

        libtcod.console_print(0,1,1,"REPUTATION:")

        libtcod.console_print(0,1,3,"[a]reas")
        libtcod.console_print(0,1,4,"[c]orporations")
        libtcod.console_print(0,1,5,"[g]angs")

	libtcod.console_flush()
	finished_choice = False
        while finished_choice == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        finished_choice = True
                elif key.c == ord('a'):
                        show_area_rep(player,world)
                        finished_choice = True
                elif key.c == ord('c'):
                        show_corps(player,world)
                        finished_choice = True

		elif key.c == ord('g'):
			show_gangs(player,world)
			finished_choice = True

def show_corps(player,world):
        my_location = find_location(player,world)
        finished_reputation = False
        options = []
        def show(world,options):
                libtcod.console_clear(0)
                libtcod.console_print(0,1,1,"CORPS:")
		count = 1
		for corp in world.corporations:
                	letter = num_to_letter(count)
                        option = [letter,corp]
                        options.append(option)

                        #libtcod.console_set_default_foreground(0, libtcod.light_blue)
                        libtcod.console_print(0,1,count+3,"[" + letter + "] " + corp.name)
                        if corp.player_reputation >= 1:
                        	libtcod.console_set_default_foreground(0, libtcod.light_green)
                        elif corp.player_reputation <= -1:
                        	print 'True'
                                libtcod.console_set_default_foreground(0, libtcod.dark_red)

                        libtcod.console_print(0,26,count+3,str(corp.player_reputation))
                        libtcod.console_set_default_foreground(0, libtcod.white) 
                        letter = num_to_letter(count)
                        option = [letter,corp]
			count += 1
                libtcod.console_print(0,1,count + 4,'[ESC]')

		libtcod.console_flush()
		return options
        def show_org(world,organization):
                libtcod.console_clear(0)

                libtcod.console_print(0,1,1, organization.name)
                #for area in world.areas:
                #       if area.name == organization.name:
                 #              libtcod.console_print(0,25,1, '(Residents)')

                if organization.player_reputation >= 1:
                        libtcod.console_set_default_foreground(0, libtcod.light_green)
                elif organization.player_reputation <= -1:
                #print 'True'
                        libtcod.console_set_default_foreground(0, libtcod.dark_red)

                libtcod.console_print(0,30,1, str(organization.player_reputation))
                libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_print(0,1,3, 'Gifts:')
                libtcod.console_print(0,30,3, str(organization.members_recruited))
                libtcod.console_print(0,1,4, 'Bought:')
                libtcod.console_print(0,30,4, "$" + str(organization.items_bought))
                libtcod.console_print(0,1,5, 'Theft:')
                libtcod.console_print(0,30,5, "$" + str(organization.theft_from))

                libtcod.console_print(0,1,7, 'Members Attacked:')
                libtcod.console_print(0,30,7, str(organization.members_attacked))
                libtcod.console_print(0,1,8, 'Members Killed:')
		if organization.members_killed >= 4:
			number_killed = organization.members_killed / 4
		else: 
			number_killed = organization.members_killed
                libtcod.console_print(0,30,8, str(number_killed))
                libtcod.console_print(0,1,9, 'Members Recruited:')
                libtcod.console_print(0,30,9, str(organization.members_recruited))
                libtcod.console_print(0,1,10, 'Members Kidnapped:')
                libtcod.console_print(0,30,10, str(organization.members_kidnapped))

                libtcod.console_print(0,1,12, 'Kills(Turf):')
                libtcod.console_print(0,30,12, str(organization.killed_on_turf))
                libtcod.console_print(0,1,13, 'Theft(Turf):')
                libtcod.console_print(0,30,13, "$" + str(organization.theft_on_turf))

                libtcod.console_print(0,1,15, 'Missions Completed:')
                libtcod.console_print(0,30,15, str(organization.missions_completed))
                libtcod.console_print(0,1,16, 'Missions Failed:')
                libtcod.console_print(0,30,16, str(organization.missions_failed))


                libtcod.console_print(0,1,18, '[ESC]')
                libtcod.console_flush()
                #finished_reputation = False
                #while finished_reputation == False:
                        #key_choice = libtcod.console_check_for_keypress()
                        #if key_choice.vk == libtcod.KEY_ESCAPE:
				#break
                                #print 'test'
                                #libtcod.console_clear(0)
				#libtcod.console_flush()
				#break
                         #       finished_reputation = True
			#	return
                		#return finished_reputation
        #options = show(world,options)
                finished_reputation = False
                while finished_reputation == False:
                        key2 = libtcod.console_check_for_keypress()
                        if key2.vk == libtcod.KEY_ESCAPE:
                                print 'test'
                                libtcod.console_clear(0)
                                finished_reputation = True
                                return finished_reputation
        show(world,options)
        while finished_reputation == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        finished_reputation = True
                for option in options:
                        if key.c == ord(option[0]):
                                #finished_org = False
                                while finished_reputation == False:
                                        finished_reputation = show_org(world,option[1])

						#show_org(world,option[1])
						#finished_rep = True
					#finished_choice = True
def show_area_rep(player,world):
	options = []
        def show(world,options):
                libtcod.console_clear(0)
                libtcod.console_print(0,1,1,"AREAS:")
                count = 1
                for area in world.areas:
                        areas = []
                        for organization in area.organizations:
                                print organization.name

                                #for area in world.areas:
                                #       areas.appened(area)

                                if organization.name == area.name:
                                        letter = num_to_letter(count)
                                        option = [letter,organization]
                                        options.append(option)

                                        #libtcod.console_set_default_foreground(0, libtcod.light_blue)
                                        libtcod.console_print(0,1,count+3,"[" + letter + "] " + organization.name)
                                        if organization.player_reputation >= 1:
                                                libtcod.console_set_default_foreground(0, libtcod.light_green)
                                        elif organization.player_reputation <= -1:
                                                print 'True'
                                                libtcod.console_set_default_foreground(0, libtcod.dark_red)

                                        libtcod.console_print(0,26,count+3,str(organization.player_reputation))

                                        libtcod.console_set_default_foreground(0, libtcod.white) 
                                        letter = num_to_letter(count)
                                        option = [letter,organization]
                                        options.append(option)
                                        count += 1
                libtcod.console_print(0,1,count + 5,'[ESC]')
                libtcod.console_flush()
	finished_reputation = False
        show(world,options)
        while finished_reputation == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        finished_reputation = True


def show_gangs(player,world):
	my_location = find_location(player,world)
	finished_reputation = False
	options = []
	def show(world,options):
        	libtcod.console_clear(0)
        	libtcod.console_print(0,1,1,"GANGS:")
		count = 1
		for area in world.areas:
			areas = []
			for organization in area.organizations:
				print organization.name

				#for area in world.areas:
				#	areas.appened(area)
			
				if organization.name == area.name:
					continue
				#	options.append(option)
 				#	count += 1
               	                letter = num_to_letter(count)
                    		option = [letter,organization]
                              	options.append(option)


				libtcod.console_print(0,1,count+3,"[" + letter + "] " + organization.name)
                                if organization.player_reputation >= 1:
                                        libtcod.console_set_default_foreground(0, libtcod.light_green)
                                elif organization.player_reputation <= -1:
                                        print 'True'
                                        libtcod.console_set_default_foreground(0, libtcod.dark_red)

				libtcod.console_print(0,26,count+3,str(organization.player_reputation))
                                libtcod.console_set_default_foreground(0, libtcod.white) 

				count += 1
			count += 1
		count += 1
		libtcod.console_print(0,1,count + 2,'[ESC]')
		libtcod.console_flush()

        #show(world,options)
        #while finished_reputation == False:
        #        key = libtcod.console_check_for_keypress()
        #        if key.vk == libtcod.KEY_ESCAPE:
        #                finished_reputation = True
        #        for option in options:
        #                if key.c == ord(option[0]):
                                #finished_org = False
        #                        while finished_reputation == False:
        #                                finished_reputation = show_org(world,option[1])

	def show_org(world,organization):
		libtcod.console_clear(0)

		libtcod.console_print(0,1,1, organization.name)
		#for area in world.areas:
		#	if area.name == organization.name:
	 	 #              libtcod.console_print(0,25,1, '(Residents)')

                if organization.player_reputation >= 1:
	                libtcod.console_set_default_foreground(0, libtcod.light_green)
                elif organization.player_reputation <= -1:
        	#print 'True'
                	libtcod.console_set_default_foreground(0, libtcod.dark_red)

                libtcod.console_print(0,30,1, str(organization.player_reputation))
		libtcod.console_set_default_foreground(0, libtcod.white)
                libtcod.console_print(0,1,3, 'Gifts:')
                libtcod.console_print(0,30,3, str(organization.members_recruited))
                libtcod.console_print(0,1,4, 'Bought:')
                libtcod.console_print(0,30,4, "$" + str(organization.items_bought))
                libtcod.console_print(0,1,5, 'Theft:')
                libtcod.console_print(0,30,5, "$" + str(organization.theft_from))

                libtcod.console_print(0,1,7, 'Members Attacked:')
                libtcod.console_print(0,30,7, str(organization.members_attacked))
                libtcod.console_print(0,1,8, 'Members Killed:')
                libtcod.console_print(0,30,8, str(organization.members_killed))
                libtcod.console_print(0,1,9, 'Members Recruited:')
                libtcod.console_print(0,30,9, str(organization.members_recruited))
                libtcod.console_print(0,1,10, 'Members Kidnapped:')
                libtcod.console_print(0,30,10, str(organization.members_kidnapped))
                libtcod.console_print(0,1,12, 'Kills(Turf):')
                libtcod.console_print(0,30,12, str(organization.killed_on_turf))
                libtcod.console_print(0,1,13, 'Theft(Turf):')
                libtcod.console_print(0,30,13, "$" + str(organization.theft_on_turf))
		
                libtcod.console_print(0,1,15, '[ESC]')
		libtcod.console_flush()
		finished_reputation = False
		while finished_reputation == False:
			key2 = libtcod.console_check_for_keypress()
			if key2.vk == libtcod.KEY_ESCAPE:
				print 'test'
				libtcod.console_clear(0)
				finished_reputation = True
				return finished_reputation
	show(world,options)
	while finished_reputation == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			finished_reputation = True
		for option in options:
			if key.c == ord(option[0]):
				#finished_org = False
				while finished_reputation == False:
					finished_reputation = show_org(world,option[1])
				#libtcod.console_clear(0)
				#show(world,options)
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
					#footsoldier = [option[1], 'No orders',player.location]
					footsoldier = Footsoldier(option[1],'No orders', player.location)
					world.player_organization.footsoldiers.append(footsoldier)
					find_home = False
					while find_home == False:
						if len(world.player_organization.locations_owned) >= 1:
							location = random.choice(world.player_organization.locations_owned)
							option[1].home = location
							location.actors.members.append(option[1])
							find_home = True
						else:
							my_area = find_area(player,world)
							my_area.randos.append(option[1])
							find_home = True
					player.members.remove(option[1])
					choice_made = True
					


def show_manage(player,world):
        libtcod.console_clear(0)
        libtcod.console_print(0,1,1,"MANAGE PARTY:")
        libtcod.console_print(0,1,3,"[d]ismiss member")
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

def show_party(target,world,party_actions):
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
			if member.health.current_health <= member.health.base_max /  2:
		                libtcod.console_set_default_foreground(0, libtcod.red)

			libtcod.console_print(0,1,count+1, "[" +str(count) + "]")
			if member == target.leader:
				libtcod.console_print(0,5,count+1, member.fname)
                        	spacing = len(member.fname) + 6
	                        libtcod.console_print(0,spacing,count+1, member.lname)
				spacing = len(member.fname) + 6 + len(member.lname)
                                libtcod.console_print(0,spacing,count+1, '*')

			else:
				libtcod.console_print(0,5,count+1, member.fname)
				spacing = len(member.fname) + 6
				libtcod.console_print(0,spacing,count+1, member.lname)
			libtcod.console_print(0,28,count+1, member.profession)
			if member.outerwear == no_outerwear or member.outerwear == None:
				libtcod.console_print(0,40,count+1, member.outfit.name)
			elif member.outerwear.name == 'None':
                                libtcod.console_print(0,40,count+1, member.outfit.name)

			else:
                                libtcod.console_print(0,40,count+1, member.outerwear.name)
	  #              libtcod.console_set_default_foreground(0, libtcod.white)

        	        libtcod.console_print(0,56,count+1, member.weapon.name)
			libtcod.console_flush()
			#party.append(member)
			option = [party_count,member]
			options.append(option)
			libtcod.console_set_default_foreground(0, libtcod.white)
			party_count += 1
			count += 1
		count += 3
		libtcod.console_print(0,1,count, "MONEY:      " + "$" + str(target.money))
		count += 1
		libtcod.console_print(0,1,count, "FAME:       " + str(target.fame))
		count += 1
                libtcod.console_print(0,1,count, "KILLS:      " + str(party_actions.kills))
		count += 1
                libtcod.console_print(0,1,count, "DRUGS SOLD: " + str(party_actions.drug_dealing))
                count += 1

                libtcod.console_print(0,30,count-4, "DAYS SURVIVED:  " + str(party_actions.days_survived))
		count += 1
                libtcod.console_print(0,30,count-4, "JOBS COMPLETED: " + str(party_actions.missions_completed))

                count += 2



		#stack medical,food,drink items
		medical = []
		food = []
		drink = []

		for item in target.inventory:
			target_item = item
			if item.item_type == 'medical' or item.item_type == 'food' or item.item_type == 'drink':
				#target.inventory.remove(item)
				for other_item in target.inventory:
					if item.name == other_item.name and other_item != target_item:
						item.number = item.number + other_item.number
						target.inventory.remove(other_item)
				#target.inventory.append(item)

		print_line = count + 2
                libtcod.console_print(0,1,print_line, "INVENTORY:")
		item_count = 1
		# types of items
		for item in target.inventory:
			print item.name
                	if item.item_type == 'junk':
				if item_count <= 12:
                	        	libtcod.console_print(0,1,print_line + item_count, item.name)
              		        	item_count += 1
                                elif item_count >= 13 and item_count >= 24 :
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1
                                elif item_count >= 25 and item_count >= 36 :
                                        libtcod.console_print(0,36,print_line + item_count - 24, item.name)
                                        item_count += 1

			elif item.item_type == 'medical' or item.item_type == 'food' or item.item_type == 'drink':
				if item_count <= 12:
					libtcod.console_print(0,1,print_line + item_count, item.name + "(" + str(item.number) + ")")
					item_count += 1
                                if item_count >= 13 and item_count <= 24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name + "(" + str(item.number) + ")")
                                        item_count += 1
                                if item_count >= 25 and item_count <= 36:
                                        libtcod.console_print(0,36,print_line + item_count - 24, item.name + "(" + str(item.number) + ")")
                                        item_count += 1
	                elif item.item_type == 'outfit':
				if item_count <= 12:
	                        	libtcod.console_print(0,1,print_line + item_count, item.name)
	                        	item_count += 1
                                if item_count >= 12 and item_count <= 24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1
                                if item_count >= 25 and item_count <= 36:
                                        libtcod.console_print(0,36,print_line + item_count - 24, item.name)
                                        item_count += 1

	                elif item.item_type == 'weapon':
				if item_count <= 12:
	                        	libtcod.console_print(0,1,print_line + item_count, item.name)
	                        	item_count += 1
                                if item_count >= 13 and item_count <=24:
                                        libtcod.console_print(0,24,print_line + item_count - 12, item.name)
                                        item_count += 1
                                if item_count >= 25 and item_count <= 36:
                                        libtcod.console_print(0,36,print_line + item_count - 24, item.name)
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
                                if item_count >= 25 and item_count <= 36:
                                        string = item.name + "'s " + item.location
                                        libtcod.console_print(0,36,print_line + item_count - 24, string)
                                        item_count += 1

			else:
                                if item_count <= 12:
                                        string = item.name 
                                        libtcod.console_print(0,1,print_line + item_count, string)
                                        item_count += 1
                                if item_count >= 13 and item_count <= 24:
                                        string = item.name 
                                        libtcod.console_print(0,24,print_line + item_count - 12, string)
                                        item_count += 1
                                if item_count >= 25 and item_count <= 36:
                                        string = item.name 
                                        libtcod.console_print(0,36,print_line + item_count - 24, string)
                                        item_count += 1


		print_line += 12
		return print_line
	while finished_showing == False:
		print_line = show()
		libtcod.console_print(0,1,print_line + 3, "OPTIONS:")
		libtcod.console_print(0,1,print_line + 4, "[a]ctions, [c]lothing, [d]rop item, [j]ournal, [m]anage party")
		libtcod.console_print(0,1,print_line + 5, "[o]rganization, [r]eputation, [u]se item, [w]eapons")
                libtcod.console_print(0,1,print_line + 7, '[ESC]')

		libtcod.console_flush()
		decision = False
		while decision == False:
	                key = libtcod.console_check_for_keypress()
			#go back
			if key.vk == libtcod.KEY_ESCAPE:
				#print 'true'
				finished_party = True
				return finished_party
                        #actions
                        elif key.c == ord('a'):
                                #print 'true'
                                finished_action = False
                                while finished_action == False:
                                        libtcod.console_clear(0)
                                        finished_action = show_actions(player_party,world,party_actions)
                                        decision = True
                        #journal
                        elif key.c == ord('j'):
                                #print 'true'
                                finished_action = False
                                while finished_action == False:
                                        libtcod.console_clear(0)
                                        finished_action = show_journal(player_party,world,party_actions)
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
					finished_viewing = show_organization(player_party,world)
					return finished_viewing

			#party members
			for option in options:
				char_key = str(option[0])
				if key.c == ord(char_key):
					finished_viewing = False
					while finished_viewing == False:
						my_location = find_location(player_party,world)
						finished_viewing = show_character(option[1], world,False,my_location,player_party,False)
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
		if item_count <= 40:
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
		elif item_count >= 41:
                        if item.item_type == "medical":
                                if item.number == 1:
                                        libtcod.console_print(0,30,line_count-40, "[" + letter + "]" + item.name)
                                        libtcod.console_print(0,52,line_count-40, "($" + str(item.base_value) + ")")
                                elif item.number >= 2:
                                        value = item.number * item.base_value
                                        libtcod.console_print(0,30,line_count-40, "[" + letter + "]" + item.name + "[" +  str(item.number) + "]")
                                        libtcod.console_print(0,52,line_count-40, "($" + str(value) + ")")
                        else:
                                libtcod.console_print(0,30,line_count-40, "[" + letter + "]" + item.name)
                                libtcod.console_print(0,52,line_count-40, "($" + str(item.base_value) + ")")


		item_count += 1
		line_count += 1
	line_count += 1
	libtcod.console_print(0,1,line_count, "[ESC]")
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
						new_item = item_to_buy[1]
                                		player.inventory.append(new_item)
					elif item_to_buy[1].item_type == 'medical':
						#see if item already in inventory
						found = False
						while found == False:
							for item in player.inventory:
								if item.item_type == item_to_buy[1].item_type and item.name == item_to_buy[1].name:
									item.number += item_to_buy[1].number
									found = True
							if found == False:
								new_item = item_to_buy[1]
								player.inventory.append(new_item)
								found = True
					if location.owned_by != 'No one':
						for area in world.areas:
							for organization in area.organizations:
								if location.owned_by == organization.name:
									organization.items_bought += value
									#print organization.name
									#if item_to_buy[1].base_value >= 1000:
									#	organization.player_reputation += item_to_buy[1].base_value / 1000
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
                if key.vk == libtcod.KEY_ESCAPE:
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
	libtcod.console_print(0,1,line_count, "[*] go back.")
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
                if key.c == ord('*'):
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

def haircuts(player,location):
        libtcod.console_clear
        libtcod.console_print(0,1,1, "Who will get a haircut?")
        line_count = 3
        options = []
        count = 1
        for member in player.members:
                letter = num_to_letter(count)
                option = [letter, member]
                options.append(option)
                count += 1
        for option in options:
                libtcod.console_print(0,1,line_count, "[" + option[0] + "] " + option[1].fname + " " + option[1].lname)
                line_count += 1
        line_count += 1
        libtcod.console_print(0,1,line_count, "[*] go back")

        choice_made = False
        libtcod.console_flush()
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
                for option in options:
                        if key.c == ord(option[0]):
                                target = option[1]
                                line_count = 1
                                libtcod.console_clear(0)
                                hair_options = []
                                hair_count = 1
                                for hair in shaved_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in spiky_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in short_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in long_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in parted_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in mohawk_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1
                                for hair in braided_hair:
                                        letter = num_to_letter(hair_count)
                                        option = [letter,hair]
                                        hair_options.append(option)
                                        hair_count += 1

                                for option in hair_options:
                                        libtcod.console_print(0,1,line_count, "[" + option[0] + "] " + option[1].name)
                                        line_count += 1
                                line_count += 1
                                libtcod.console_print(0,1,line_count, "[*] go back")
                                finished_hair = False
                                libtcod.console_flush()
                                while finished_hair == False:
                                        key = libtcod.console_check_for_keypress()
                                        for option in hair_options:
                                                if key.c == ord(option[0]) and player.money >= option[1].base_value:
                                                        player.money -= option[1].base_value
							for option in hair_options:
								if option[1] in target.traits:
									target.traits.remove(option[1])
                                                        target.traits.append(option[1])
                                                        return True
                                                elif key.c == ord('*'):
                                                        return True
                        elif key.c == ord('*'):
                                return True

def tattoos(player,location):
        libtcod.console_clear
        libtcod.console_print(0,1,1, "Who will get tattooed?")
        line_count = 3
	options = []
	count = 1
	for member in player.members:
		letter = num_to_letter(count)
		option = [letter, member]
		options.append(option)
		count += 1
	for option in options:
        	libtcod.console_print(0,1,line_count, "[" + option[0] + "] " + option[1].fname + " " + option[1].lname)
		line_count += 1
	line_count += 1
        libtcod.console_print(0,1,line_count, "[*] go back")

	choice_made = False
	libtcod.console_flush()
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				target = option[1]
				line_count = 1
				libtcod.console_clear(0)
				tattoo_options = []
				tattoo_count = 1
				for tattoo in possible_tattoos:
					letter = num_to_letter(tattoo_count)
					option = [letter,tattoo]
					tattoo_options.append(option)
					tattoo_count += 1
				for option in tattoo_options:
					libtcod.console_print(0,1,line_count, "[" + option[0] + "] " + option[1].name)
					line_count += 1
				line_count += 1
				libtcod.console_print(0,1,line_count, "[*] go back")
				finished_tattoo = False
				libtcod.console_flush()
				while finished_tattoo == False:
					key = libtcod.console_check_for_keypress()
					for option in tattoo_options:
						if key.c == ord(option[0]) and player.money >= option[1].base_value:
							player.money -= option[1].base_value
							target.traits.append(option[1])
							return True
						elif key.c == ord('*'):
							return True
			elif key.c == ord('*'):
				return True


def laundry(player,location):
	cost = len(player.members) * 7
        libtcod.console_clear
        libtcod.console_print(0,1,1, "LAUNDRY:")

        libtcod.console_print(0,1,3, "[d]o laundry ($" + str(cost) + ")")
        libtcod.console_print(0,1,4, "[l]eave")
	libtcod.console_flush()
	finished_laundry = False
	while finished_laundry == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('l'):
			finished_laundry = True
		elif key.c == ord('d') and player.money >= cost:
			player.money -= cost
                        for member in player.members:
                                if member.headwear != no_headwear and member.headwear != None:
                                        if member.headwear.blood >= 1:
                                                member.headwear.blood = 0
                                if member.facewear != no_facewear and member.facewear != None:
                                        if member.facewear.blood >= 1:
                                                member.facewear.blood = 0
                                if member.outfit != naked and member.outfit != None:
                                        if member.outfit.blood >= 1:
                                                member.outfit.blood = 0
                                if member.outerwear != no_outerwear and member.outerwear != None:
                                        if member.outerwear.blood >= 1:
                                                member.outerwear.blood = 0
                                if member.legwear != no_legwear and member.legwear != None:
                                        if member.legwear.blood >= 1:
                                                member.legwear.blood = 0
                                if member.footwear != no_footwear and member.footwear != None:
                                        if member.footwear.blood >= 1:
                                                member.footwear.blood = 0
                                if member.armor != no_armor and member.armor != None:
                                        if member.armor.blood >= 1:
                                                member.armor.blood = 0
			finished_laundry = True
			


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
	libtcod.console_print(0,1,line_count, "[r]eturn")
	libtcod.console_flush()
	choice_made = False
        while choice_made == False:
                key = libtcod.console_check_for_keypress()
		for available_service in available_services:
			if key.c == ord(available_service[0]):
				libtcod.console_clear
                                if available_service[1].name == "laundry":
                                        doing_laundry = False
                                        while doing_laundry == False:
                                                doing_laundry = laundry(player,location)
                                        finished_services = True
                                        return finished_services

				elif available_service[1].name == "heal injuries":
					healing_injuries = False
					while healing_injuries == False:
						healing_injuries = heal_injuries(player,location)
					finished_services = True
					return finished_services
                                elif available_service[1].name == "tattoos":
                                        getting_tattoos = False
                                        while getting_tattoos == False:
                                                getting_tattoos = tattoos(player,location)
                                        finished_services = True
                                        return finished_services
                                elif available_service[1].name == "haircuts":
                                        getting_haircuts = False
                                        while getting_haircuts == False:
                                                getting_haircuts = haircuts(player,location)
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
			libtcod.console_clear(0)
                        while finished_buying == False:

                                finished_buying = buy(player,location)
                        finished_bartering = True
                        return finished_bartering
                if key.c == ord('s') and location.services == True:
                        finished_services = False
			libtcod.console_clear(0)
                        while finished_services == False:
                                finished_services = services(player,location)
                        finished_bartering = True
                        return finished_bartering

#speak
def rob_npc(char,target,world,player,location,party_actions):
	my_location = find_location(player,world)
	my_area = find_area(player,world)
	player.fame += random.randint(2,5)
        line_count = 1
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " approaches " + target.fname + " " + target.lname + ".")
        line_count += 2
	#check if people are around
	if len(my_location.actors.members) >= 2:
		libtcod.console_print(0,1,line_count, target.fname + " " + target.lname + " yells for help.")
		line_count += 1
		for member in location.actors.members:
			if member.profession == target.profession and member != target:
		                libtcod.console_print(0,1,line_count, member.fname + " " + member.lname + " comes to help.")
                		line_count += 1
			else:
                                libtcod.console_print(0,1,line_count, member.fname + " " + member.lname + " leaves.")

				location.actors.members.remove(member)
	line_count += 2
	libtcod.console_print(0,1,line_count, "[c]onfirm")
	libtcod.console_flush()
	confirm = False

	while confirm == False:
	        key = libtcod.console_check_for_keypress()
		if key.c == ord('c'):
			print 'confirm'
			libtcod.console_clear(0)
			confirm = True
	print my_area.name
	finished_speaking = False
	while finished_speaking == False:
	        libtcod.console_clear(0)
	        line_count = 1
	        libtcod.console_print(0,1,line_count, '[a] "Hand over your money!"')
		line_count += 1
	        libtcod.console_print(0,1,line_count+1, '[b] "Hand over your weapons!"')
                line_count += 1
                libtcod.console_print(0,1,line_count+2, '[c] "Hand over your clothes!"')
		line_count += 1

	        if len(my_location.actors.members) == 1:
                	libtcod.console_print(0,1,line_count, '[d] "Where is the stash?"')
			line_count += 2
                        libtcod.console_print(0,1,line_count, '[e] Tie them up.')
                        line_count += 1

		elif target.affiliation == my_location.owned_by:
                        libtcod.console_print(0,1,line_count, '[g] "Who is the boss?"')
		line_count += 2
        	libtcod.console_print(0,1,line_count+5, '[ENTER] finished')
		libtcod.console_flush()
		finished_choice = False
		member_count = len(player_party.members)
		while finished_choice == False:

	        	key = libtcod.console_check_for_keypress()
			if key.c == ord('g') and target.affiliation == my_location.owned_by and len(my_location.parent_location.rooms) >= 1:
				line_count = 1
				libtcod.console_clear(0)
				found = False
				while found == False:
					if my_location.parent_location != None and len(my_location.parent_location.rooms) >= 1:
						for room in my_location.parent_location:
							for member in room.members:
								if member.profession == "Manager":
 									libtcod.console_print(0,1,line_count, '"' + member.fname + ' ' + member.lname + '"')
									libtcod.console_flush()
									found = True
					else:
						libtcod.console_print(0,1,line_count, '''"I don't know anything!"''')
						libtcod.console_flush()
						found = True
				line_count += 2
				confirm = False

 			elif key.c == ord('e') and len(my_location.actors.members) == 1:
				have_rope = False
				finished_search = False
				while finished_search == False:
					for item in player_party.inventory:
						if item.name == "Rope":
							player_party.inventory.remove(item)
							print 'found rope'
							have_rope = True
							#finished_search = True
					finished_search = True
				print 'clear'
				libtcod.console_clear(0)
				line_count = 1
				if have_rope == False:
                                        libtcod.console_print(0,1,line_count, 'You have no Rope.')
					line_count += 2
                                elif have_rope == True:
#                                        libtcod.console_print(0,1,line_count, 'You have tie up ')
					for member in my_location.actors.members:
						if member.tied_up == False:
	                                        	libtcod.console_print(0,1,line_count, 'You tie up ' + member.fname + " " + member.lname + ".")
							member.tied_up = True
							line_count += 2
						elif member.tied_up == True:
                                                        libtcod.console_print(0,1,line_count, member.fname + " " + member.lname + " is already tied up.")
							line_count += 2
				libtcod.console_print(0,1,line_count, '[c]ontinue')
				libtcod.console_flush()
				finished_tie = False
				while finished_tie == False:
					key = libtcod.console_check_for_keypress()
					if key.c == ord('c'):
						finished_tie = True
			elif key.c == ord('d'):
				#print 'stash'
				line_count = 1

				libtcod.console_clear(0)
				if len(my_location.hidden_items) >= 1:
					for item in my_location.hidden_items:
						libtcod.console_print(0,1,line_count, 'You got ' + item.name)
						player_party.inventory.append(item)
						for area in world.areas:
							for organization in area.organizations:
								if organization.name == my_location.owned_by:
									organization.theft_from += item.base_value
									player_actions.stealing += 1
						for corporation in world.corporations:
							if corporation.name == my_location.owned_by:
								corporation.theft_from += item.base_value
								party_actions.stealing += 1
						my_location.hidden_items.remove(item)
						line_count += 1
				elif len(my_location.hidden_items) <= 0:
					libtcod.console_print(0,1,line_count, "There's nothing here!")
					line_count += 1
				line_count += 1
				libtcod.console_print(0,1,line_count, '[c]ontinue')
                                found_org = False
                                #for area in world.areas:
	                           #     for organization in area.organizations:
				#		for member in my_location.actors.members:
        	                  #              	if member.affiliation == organization.name:
                	         #               	        #organization.player_reputation.theft += 1
                                #                	        found_org = True
                        	#if found_org == False:
                                #	for area in world.areas:
                                   #     	for organization in area.organizations:
                                  #              	if organization.name == my_area.name:
                                 #                       	 organization.player_reputation -= random.randint(1,2)
                                #for area in world.areas:
                                #	for organization in area.organizations:
                                #        	if organization.name == my_location.owned_by:
                                #                	organization. -= 1
				finished = False
				libtcod.console_flush()
				while finished == False:
					key = libtcod.console_check_for_keypress()
					if key.c == ord('c'):
						finished_speaking = False
						finished_choice = True
						finished = True
						#return False
				#return True
			elif key.vk == libtcod.KEY_ENTER:
				return True
			elif key.c == ord('a') or key.c == ord('b') or key.c == ord('c'):
				npc_attack = 0
				player_attack = 0
				for member in my_location.actors.members:
					npc_attack += member.weapon.damage
					#if member.affiliation != 'No one' and member.affiliation != None:
					#	for area in world.areas:
                                        #                for organization in area.organizations:
                                        #                        if organization.name == member.affiliation:
                                        #                                organization.killed += 1

				for member in player.members:
					player_attack += member.weapon.damage

				if player_attack >= npc_attack + 1:
					libtcod.console_clear(0)
					money = 0
					#member_count = 0
					for member in my_location.actors.members:
						#member_count += 1
						money += member.start_money
						member.start_money = 0
					found_org = False
					#for area in world.areas:
					#	for organization in area.organizations:
					#		if member.affiliation == organization.name:
					#			organization.player_reputation -= 5
					#			found_org = True
					#if found_org == False:
					#	for area in world.areas:
					#		for organization in area.organizations:
					#			if organization.name == my_area.name:
					#				organization.player_reputation -= random.randint(1,3)
					#for area in world.areas:
					#	for organization in area.organizations:
					#		if organization.name == my_location.owned_by:
					#			organization.player_reputation -= 3
					def handle_theft(item,target,player,world,my_location):
						for area in world.areas:
							for organization in area.organizations:
								if target.affiliation == organization.name:
									organization.theft += item.base_value
					if key.c == ord('a'):
						line_count = 1
						libtcod.console_print(0,1,line_count,'You got $' + str(money) + '.')
						for member in my_location.actors.members:
							party_actions.stealing += 1
							for area in world.areas:
								for area in world.areas:
									for organization in area.organizations:
										if organization.name == member.affiliation:
											organization.theft_from += money
											print str(organization.theft_from)
										elif organization.name == my_location.owned_by and organization.name != member.affiliation:
											organization.theft_from += money
                                                	for corporation in world.corporations:
                                                        	if corporation.name == my_location.owned_by:
                                                        	        corporation.theft_from += money
                                                        		party_actions.stealing += 1
					elif key.c == ord('b'):
						for member in my_location.actors.members:
							if member.weapon != punch:
								line_count += 1
		                	                	libtcod.console_print(0,1,line_count,'You got ' + member.weapon.name + '.')
								player_party.inventory.append(member.weapon)
								value = member.weapon.base_value
								member.weapon = punch
								party_actions.stealing += 1
                                                        	for area in world.areas:
	                                                	        for organization in area.organizations:
        	                                        	                if organization.name == member.affiliation:
                	                                       		                organization.theft_from += value
										elif organization.name != member.affiliation and organization.name == my_location.owned_by:
											organization.theft_from += value
                                                		for corporation in world.corporations:
                                                        		if corporation.name == my_location.owned_by:
                                                        		        corporation.theft_from += value
                                                        		        party_actions.stealing += 1										#else:
											
					elif key.c == ord('c'):
						for member in my_location.actors.members:
							clothes = False
							if member.headwear != no_headwear and member.headwear.name != 'None':
								print member.headwear.name
								player_party.inventory.append(member.headwear)
								line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.headwear.name + '.')
								value = member.headwear.base_value
								member.headwear = no_headwear
								party_actions.stealing += 1
								clothes = True
                                                       	        for area in world.areas:
                                                       	                for organization in area.organizations:
                                                       	                        if organization.name == member.affiliation:
                                                       	                                organization.theft_from += value
										elif organization.name != organization.name and organization.name == my_location.owned_by:
											organization.theft_from += value
                                                                                else:
	                                                                                for area in world.areas:
        	                                                                                if organization.name == area.name and organization.name == my_location.area:
                	                                                                                organization.theft_from += value /4
                                                		for corporation in world.corporations:
                                                        		if corporation.name == my_location.owned_by:
                                                                		corporation.theft_on_turf += value / 4
                                                                		#player_actions.stealing += 1


                                                        if member.facewear != no_facewear and member.facewear.name != 'None':
								#print member.facewear.name
                                                                player_party.inventory.append(member.facewear)
                                                                #member.facewear = no_facewear
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.facewear.name + '.')
								value = member.facewear.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
											else:
												for area in world.areas:
													if organization.name == area.name and organization.name == my_location.area:
														organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4
                                                                                party_actions.stealing += 1

								member.facewear = no_facewear
								clothes = True
                                                        if member.eyewear != no_eyewear and member.eyewear.name != 'None':
                                                                player_party.inventory.append(member.eyewear)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.eyewear.name + '.')
								value = member.eyewear.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and organization.name == my_location.area:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4


								clothes = True
                                                                member.eyewear = no_eyewear

                                                        if member.outfit != naked and member.outfit.name != 'None':
                                                                player_party.inventory.append(member.outfit)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.outfit.name + '.')
								value = member.outfit.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and organization.name == my_location.area:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4


                                                                member.outfit = naked
								clothes = True
                                                        if member.handwear != no_handwear and member.handwear.name != 'None':
                                                                player_party.inventory.append(member.handwear)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.handwear.name + '.')
								value = member.handwear.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_locatio.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and my_location.area == organization.name:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4
                                                                                #player_actions.stealing += 1




								clothes = True
                                                                member.handwear = no_handwear
                                                        if member.legwear != no_legwear and member.legwear.name != 'None':
                                                                player_party.inventory.append(member.legwear)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.legwear.name + '.')
								value = member.legwear.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and organization.name == my_location.area:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4
                                                                                #player_actions.stealing += 1

								clothes = True
                                                                member.legwear = no_legwear
                                                        if member.footwear != no_footwear and member.footwear.name != 'None':
                                                                player_party.inventory.append(member.footwear)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.footwear.name + '.')
								value = member.footwear.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value
                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and organization.name == my_location.area:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4
                                                                                #player_actions.stealing += 1


								clothes = True
                                                                member.footwear = no_footwear
                                                        if member.armor != no_armor and member.armor.name != 'None':
                                                                player_party.inventory.append(member.armor)
                                                                line_count += 1
                                                                libtcod.console_print(0,1,line_count,'You got ' + member.armor.name + '.')
								value = member.armor.base_value
								party_actions.stealing += 1
                                                                for area in world.areas:
                                                                        for area in world.areas:
                                                                                for organization in area.organizations:
                                                                                        if organization.name == member.affiliation:
                                                                                                organization.theft_from += value

                                                                                        elif organization.name != organization.name and organization.name == my_location.owned_by:
                                                                                                organization.theft_on_turf += value
                                                                                        else:
                                                                                                for area in world.areas:
                                                                                                        if organization.name == area.name and organization.name == my_location.area:
                                                                                                                organization.theft_from += value / 4
                                                                for corporation in world.corporations:
                                                                        if corporation.name == my_location.owned_by:
                                                                                corporation.theft_on_turf += value / 4
                                                                                #player_actions.stealing += 1


								clothes = True
                                                                member.armor = no_armor
							if clothes == False:
								libtcod.console_print(0,1,line_count,member.fname + ' ' + member.lname + " is naked!")
								line_count += 1
					player.money += money
        				libtcod.console_print(0,1,line_count+2, "[c]ontinue.")
					libtcod.console_flush()
					confirm_steal = False
					while confirm_steal== False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('c'):
							libtcod.console_clear(0)
							
							finished_speaking = False
							finished_choice = True
							confirm_steal = True
							#return finished_speaking
				elif player_attack <= npc_attack:
					finished_speaking = battle(player_party,my_location.actors,my_location,world,True,party_actions)
                       		        #for area in world.areas:
                               		#        for organization in area.organizations:
                                	#                if organization.name == my_location.owned_by:
                                       	#	                organization.player_reputation -= 3

					return finished_speaking
#	else:

def recruit(char,target,world,player,location):
	#choice_made = False
        line_count = 1
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " attempts to recruit " + target.fname + " " + target.lname + ".")
	line_count += 1
	libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " succeeded!")
        if len(player.members) >= player.leader.skills.leadership + 3:
		line_count += 1
        	libtcod.console_print(0,1,line_count, "Leader does not have enough skill. Raise your leader's Leadership skill to have more people.")

	line_count += 2
	libtcod.console_print(0,1,line_count, "[b]ack")
        libtcod.console_flush()
        key = libtcod.console_check_for_keypress()
	#choice_made = False
        if key.c == ord('b'):
		if len(player.members) >= player.leader.skills.leadership + 3:
			return True
		else:
                	libtcod.console_clear(0)
			print 'ok'
			#world.organization.footsoldiers.append(target)
			for area in world.areas:
				for organization in area.organizations:
					if organization.name == char.affiliation:
						organization.player_reputation -= 4
			target.controlled_by = 'player'
                	player.members.append(target)
			for member in player.members:
				member.controlled_by = 'player'
                	location.actors.members.remove(target)
	        	choice_made = True
			return choice_made
def show_delivery(job,party_actions,accept,world,location,player):
        line_count = 1
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, "You will deliver " + job.mission.item.name + " to " + job.mission.target.fname + " " + job.mission.target.lname + "(" + job.mission.target.profession + ").")
        line_count += 2
        libtcod.console_print(0,1,line_count, "LOCATION: " + job.mission.target_location.name + " (" + job.mission.target_location.area + ")")
        line_count += 2
        job.mission.deadline.correct(party_actions)
        libtcod.console_print(0,1,line_count, "DEADLINE: " + str(job.mission.deadline.day) + "/" +str(job.mission.deadline.month) + "/" + str(job.mission.deadline.year)) 
        line_count += 2
	print job.broker_location.name
        libtcod.console_print(0,1,line_count, "RETURN TO: " + job.broker.npc.fname + " " + job.broker.npc.lname)
 	line_count += 1
        libtcod.console_print(0,1,line_count, "           " + job.broker_location.name) 
        line_count += 2
        libtcod.console_print(0,1,line_count, "REWARD: $" + str(job.reward)) 


        if accept == False:
                line_count += 2
                if job.mission.is_complete == False:
                        libtcod.console_print(0,1,line_count, "INCOMPLETE")
                elif job.mission.is_complete == True:
                        libtcod.console_print(0,1,line_count, "COMPLETE") 

        line_count += 2
        if accept == True:
                libtcod.console_print(0,1,line_count, "[a]ccept")
                line_count += 2
        libtcod.console_print(0,1,line_count, "[ESC]")
        libtcod.console_flush()
        finished_show_assassination = False
        while finished_show_assassination == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        #finished_show_assination = True
                        return True
                elif key.c == ord('a') and accept == True:
                        world.missions.append(job)
			player.inventory.append(job.mission.item)
                        location.broker.broker.jobs.remove(job)
                        return True


def show_assassination(job,party_actions,accept,world,location):
	line_count = 1
	libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, "You will assassinate " + job.mission.target.fname + " " + job.mission.target.lname + "(" + job.mission.target.profession + ").")
	line_count += 2
        libtcod.console_print(0,1,line_count, "LOCATION: " + job.mission.target_location.name + " (" + job.mission.target_location.area + ")")
	line_count += 2
	job.mission.deadline.correct(party_actions)
        libtcod.console_print(0,1,line_count, "DEADLINE: " + str(job.mission.deadline.day) + "/" +str(job.mission.deadline.month) + "/" + str(job.mission.deadline.year))
	line_count += 2 
        print job.broker_location.name
        libtcod.console_print(0,1,line_count, "RETURN TO: " + job.broker.npc.fname + " " + job.broker.npc.lname)
        line_count += 1
        libtcod.console_print(0,1,line_count, "           " + job.broker_location.name) 
	line_count += 2
        libtcod.console_print(0,1,line_count, "REWARD: $" + str(job.reward)) 

	#line_count += 1
	if accept == False:
	        line_count += 2
		if job.mission.is_complete == False:
	        	libtcod.console_print(0,1,line_count, "INCOMPLETE")
		elif job.mission.is_complete == True:
			libtcod.console_print(0,1,line_count, "COMPLETE") 

	line_count += 2
	if accept == True:
		libtcod.console_print(0,1,line_count, "[a]ccept")
		line_count += 2
	libtcod.console_print(0,1,line_count, "[ESC]")
	libtcod.console_flush()
        finished_show_assassination = False
        while finished_show_assassination == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        #finished_show_assination = True
			return True
		elif key.c == ord('a') and accept == True:
			world.missions.append(job)
			location.broker.broker.jobs.remove(job)
			return True
def show_complete_jobs(char,target,player,world,location,party_actions):
	line_count = 1
	libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, "COMPLETE JOBS:")
	line_count += 2
	jobs_complete = []
	job_count = 1
        for job in world.missions:
                if job.broker.npc.fname == location.broker.fname and job.broker.npc.lname and location.broker.lname:
                        print 'true'
                        if job.type == 'Assassination':
                                if job.mission.is_complete == True:
                                        letter = num_to_letter(job_count)
					job_complete =[letter,job]
					jobs_complete.append(job_complete)
					job_count += 1
                        elif job.type == 'Delivery':
                                if job.mission.is_complete == True:
                                        letter = num_to_letter(job_count)
                                        job_complete =[letter,job]
                                        jobs_complete.append(job_complete)
                                        job_count += 1

	for job in jobs_complete:
	        libtcod.console_print(0,1,line_count, "[" + job[0] + "]" + job[1].type + " ($" + str(job[1].reward) + ")")
		line_count += 1
	line_count += 1
        libtcod.console_print(0,1,line_count, "[ESC]")
	libtcod.console_flush()
	
        finished_turn_in = False
        while finished_turn_in == False:
                key = libtcod.console_check_for_keypress()
                if key.vk == libtcod.KEY_ESCAPE:
                        finished_turn_in = True
                else:
                        for job in jobs_complete:
                                if key.c == ord(job[0]):
					player.money += job[1].reward
					job[1].broker.player_reputation += random.randint(20,30)
					for area in world.areas:
						for organization in area.organizations:
							if organization == job[1].broker.affiliation:
								organization.player_reputation += random.randint(5,10)
								organization.missions_completed += 1
					party_actions.missions_completed += 1
					player.fame += random.randint(5,10)
					if job[1] in world.missions:
						world.missions.remove(job[1])
					finished_turn_in = True

def broker_refuse(char,target,player,world,location,party_actions):
        line_count = 1
        world = handle_jobs(player,world)
        libtcod.console_clear(0)
	phrases = ['"Get lost, noob."','"Huh? Do I know you?"','"I do not deal with bums off the street."']
	refuse = random.choice(phrases)
        libtcod.console_print(0,1,1, refuse)
        libtcod.console_print(0,1,3, '[ESC]')
	libtcod.console_flush()
	finished = False
	while finished == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			finished = True
			return finished
def show_broker(char,target,player,world,location,party_actions):
	line_count = 1
	world = handle_jobs(player,world)
        libtcod.console_clear(0)
        libtcod.console_print(0,1,line_count, "BROKER: " + target.fname + " " + target.lname)
	line_count += 1
	libtcod.console_print(0,1,line_count, "PLAYER REP: " + str(location.broker.broker.player_reputation))
	line_count += 2
	missions_here = []
	print str(len(location.broker.broker.jobs))
	if target.broker != None:
		if len(target.broker.jobs) >= 1:
			job_count = 1
			for job in target.broker.jobs:
				if job != None:
					letter = num_to_letter(job_count)
			        	libtcod.console_print(0,1,line_count, "[" + letter + "]" + job.type)
        	                	libtcod.console_print(0,25,line_count, job.employer.name)
        	                	libtcod.console_print(0,50,line_count, "$" + str(job.reward))
					this_mission = [letter,job]
					missions_here.append(this_mission)
					job_count += 1
					line_count += 1
	missions_to_turn_in = False
	for job in world.missions:
		if job.broker.npc.fname == location.broker.fname and job.broker.npc.lname and location.broker.lname:
			print 'true'
			if job.type == 'Assassination':
				if job.mission.is_complete == True:
					missions_to_turn_in = True
                        elif job.type == 'Delivery':
                                if job.mission.is_complete == True:
                                        missions_to_turn_in = True

	if missions_to_turn_in == True:
		line_count += 1
		libtcod.console_print(0,1,line_count, "[ENTER] turn in complete jobs.")
		line_count += 1
	line_count += 1
        libtcod.console_print(0,1,line_count, "[ESC]")
	libtcod.console_flush()

	finished_broker = False
	while finished_broker == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			finished_broker = True
		elif key.vk == libtcod.KEY_ENTER:
			finished_broker = show_complete_jobs(char,target,player,world,location,party_actions)
			finished_broker = True
		else:
			for job in missions_here:
				if key.c == ord(job[0]):
					if job[1].type == "Assassination":
						finished_broker = show_assassination(job[1],party_actions,True,world,location)
					elif job[1].type == "Delivery":
                                                finished_broker = show_delivery(job[1],party_actions,True,world,location,player)

	return finished_broker
def conversation(char,target,player,world,location,party_actions):
	line_count = 1
	libtcod.console_clear(0)
	libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " is talking to " + target.fname + " " + target.lname + ".")
	line_count += 2
	libtcod.console_print(0,1,line_count, "[a] make small talk.")
	line_count += 1
	libtcod.console_print(0,1,line_count, "[b] rob them.")
        line_count += 1
	if target in world.player_organization.footsoldiers:
        	libtcod.console_print(0,1,line_count, "[c] rejoin party.")
	else:
        	libtcod.console_print(0,1,line_count, "[c] recruit them.")
	if location.has_broker == True and location.broker != None and target.broker != None:
                libtcod.console_print(0,1,line_count, "[d] see missions..")
		line_count += 1
	delivery = False
	can_deliver = False
	target_job = None
	while delivery == False:
		for job in world.missions:
			if job.mission.target.fname == target.fname and job.mission.target.lname == target.lname:
				print 'mission target' 
				found_item = False
				for item in player.inventory:
					if item.name == job.mission.item.name and item.is_quest == True:
       	        				libtcod.console_print(0,1,line_count, "[e] deliver item.")
       	        				line_count += 1
						#job.is_complete = True
						#player.inventory.remove(mission.job.item)
						target_job = job
						delivery = True
						can_deliver = True
			else:
				print 'not mission target'
		delivery = True
			

	line_count += 2
	libtcod.console_print(0,1,line_count, "[ESC]")
	libtcod.console_flush()
	choice_made = False
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			finished_speaking = True
			return finished_speaking
                elif key.c == ord('c') and len(player.members) <= 8:
			
		        libtcod.console_clear(0)
			for footsoldier in world.player_organization.footsoldiers:
				if target == footsoldier.npc:
	                        	libtcod.console_print(0,1,line_count, target.fname +" " + target.lname + " rejoins your party.")
					#world.player_organization.footsoldiers[0].remove(target)
			else:
			        libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " attempts to recruit " + target.fname + " " + target.lname + ".")
			        line_count += 1
      				libtcod.console_print(0,1,line_count, char.fname + " " + char.lname + " succeeded!")
			if len(player.members) + len(world.player_organization.footsoldiers) >= player.leader.skills.leadership + 3:
                                line_count += 2
                                libtcod.console_print(0,1,line_count, "You need to raise your leader's Leadership skill to recruit more.")
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
		                        if len(player.members) + len(world.player_organization.footsoldiers) >= player.leader.skills.leadership + 3:
						return True
	        		        libtcod.console_clear(0)
	        		        print 'ok'
	        		        #world.organization.footsoldiers.append(target)
	        		        player.members.append(target)
	        		        location.actors.members.remove(target)
					for footsoldier in world.player_organization.footsoldiers:
						if footsoldier.npc == target:
							world.player_organization.footsoldiers.remove(footsoldier)
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

			streetwise_roll = random.randint(1,6)
			investigate_roll = random.randint(1,6)
			if streetwise_roll <= char.skills.streetwise + 1 and investigate_roll <= char.skills.investigate + 1:
				#find a tip
				print 'passed streetwise roll'
				#drug dealer
				dealers = []
				for area in world.areas:
					for location in area.locations:
						if len(location.rooms) >= 2:
							for room in location.rooms:
								for member in room.actors.members:
									if member.profession == "Drug Dealer":
										dealers.append(member)
				if len(dealers) <= 1:
                                	libtcod.console_print(0,1,1, target.fname + " " + target.lname + " says:")
                                	dialogue = random.choice(standard_npc_responses)
                                	libtcod.console_print(0,1,2, dialogue + ".")
                                	libtcod.console_print(0,1,4, "[ESC]")
				elif len(dealers) >= 2:
					dealer = random.choice(dealers)
                                        libtcod.console_print(0,1,1, dealer.fname + " " + dealer.lname + "(" + dealer.profession + ") lives at " + dealer.home.parent_location.name + " in " + dealer.home.parent_location.area + ".")
                                        libtcod.console_print(0,1,4, "[ESC]")

			else:
				print 'failed streetwise roll'
				libtcod.console_print(0,1,1, target.fname + " " + target.lname + " says:")
				dialogue = random.choice(standard_npc_responses)
				libtcod.console_print(0,1,2, dialogue + ".")
				libtcod.console_print(0,1,4, "[ESC]")
			libtcod.console_flush()
			confirm = False
			while confirm == False:
				key = libtcod.console_check_for_keypress()
        	       		if key.vk == libtcod.KEY_ESCAPE:
                	       		finished_speaking = True
					choice_made = True
                	       		return finished_speaking
		elif key.c == ord('b'):
			finished_speaking = rob_npc(char,target,world,player,location,party_actions)
			libtcod.console_clear(0)
			finished_speaking = True
			return finished_speaking
		elif key.c == ord('d') and location.has_broker == True:
			if player.fame >= location.broker.broker.min_fame:
				finished_speaking = show_broker(char,target,player,world,location,party_actions)
			else:
                                finished_speaking = broker_refuse(char,target,player,world,location,party_actions)

			libtcod.console_clear(0)
			finished_speaking = True
			return finished_speaking
		elif key.c == ord('e') and can_deliver == True and target_job != None:
			for job in world.missions:
				if job == target_job:
					job.mission.is_complete = True
					for item in player.inventory:
						if item.name == job.mission.item.name and item.is_quest == True:
							if job.mission.num_required == 0:
								player.inventory.remove(item)
							elif job.mission.num_required >= 1:
								if item.number != None:
									if job.mission.num_required <= item.number:
										player.inventory.remove(item)
					libtcod.console_clear(0)
					finished_speaking = True
					return finished_speaking
def speak_to_who(player,world,target,location,finished_speaking,party_actions):

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
			libtcod.console_clear(0)
                        return finished_speaking
                elif key.c  != ord('r'):
                        for option in possible_options:
				if key.c == ord(option[0]):
                               	        finished_speaking = conversation(option[1], target,player, world,location,party_actions)
					libtcod.console_clear(0)
                               	        finished_speaking = True
                               	        return finished_speaking

def speak(player,world,location,party_actions):
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
	finished_speaking = False
	
	while finished_speaking == False:
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				target = option[1]
				#npc_chosen = True
				finished_speaking = False
				finish = False
				while finished_speaking == False:
					finished_speaking = speak_to_who(player,world,target,location,finish,party_actions)
		if key.c == ord('r'):
			finished_speaking = True
			return finished_speaking



#loot
def loot(party,world,party_actions):
	finished_loot = False
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	items_to_loot = []
	for item in my_location.items:
		if item.item_type == 'junk' and item.can_loot == True:
			items_to_loot.append(item)
		elif item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'medical' or item.item_type == 'limb':
			items_to_loot.append(item)
		elif item.name != 'None' and item.item_type != 'container' or item.item_type == 'tent' and item.can_loot == True:
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

	option_count += 1
	libtcod.console_print(0,1, print_line + option_count, "[ESC]")
	libtcod.console_flush()
	choice_made = False
	while choice_made == False:
		key = libtcod.console_check_for_keypress()
		#choice_made = True
		for option in options:
	               	if key.vk == libtcod.KEY_ESCAPE:
	                       	finished_loot,choice_made = True,True
	                       	libtcod.console_clear(0)
	                       	return finished_loot,finished_loot
			elif key.c == ord(option[0]):
				print option[1].name
				#item = item[1]
				owners_here = False
				attackers = []
				for member in my_location.actors.members:
					if member.home == my_location and my_location.owned_by != 'Player':
						attackers.append(member)
						owners_here = True
					elif member.affiliation == my_location.owned_by:
						attackers.append(member)
						owners_here = True
				
				if owners_here == False or my_location.owned_by == 'Player':
					party.inventory.append(option[1])
					my_location.items.remove(option[1])
					libtcod.console_clear(0)
					return finished_loot,finished_loot
				elif owners_here == True and my_location.owned_by != 'Player':
					decided = False
                                        libtcod.console_clear(0)
                                        libtcod.console_print(0,1, 1, "That's my " + option[1].name + ", asshole!")
                                        libtcod.console_print(0,1, 3, "[f]ight, [l]eave)")
                                        libtcod.console_flush()
					my_location.actors.members = attackers
					decision = False
					while decision == False:
						key = libtcod.console_check_for_keypress()
						if key.c == ord('f'):
							for member in attackers:
								for area in world.areas:
									for organization in world.areas:
										if member.affiliation == organization.name:
											organization.members_attacked += 1
							battle(party,my_location.actors,my_location,world,True,party_actions)
							libtcod.console_clear(0)
							finished_loot,choice_made = True,True
							return finished_loot,finished_loot
						elif key.c == ord('l'):
							travel(party,world,my_location,my_area,party_actions)
                                                        libtcod.console_clear(0)
                                                        finished_loot,choice_made = True,True
                                                        return finished_loot,finished_loot



def show_patrol(party,world,my_location,party_actions):
	libtcod.console_clear(0)
	libtcod.console_print(0, 1, 1, 'A security patrol approaches...')
        #libtcod.console_print(0, 1, 2, '"Intruders! Get them!"')
	open = False
	if world.time.hour >= my_location.time_open and world.time.hour <= my_location.time_close:
		open = True
		print 'open'
	line_count = 3
	if open == True:
        	libtcod.console_print(0, 1, line_count, '[a]ct natural')
	line_count += 1
	libtcod.console_print(0, 1, line_count, '[f]ight')
	line_count += 1
        libtcod.console_print(0, 1, line_count, '[h]ide')
        #libtcod.console_print(0, 1, 5, '[r]un')

	libtcod.console_flush()
	decision = False
	num_patrol = random.randint(1,3)
	patrol_count = 1
	patrol_members = []
	#member = create_npc('Security Guard',my_location.owned_by,'None')
	while patrol_count <= num_patrol:
	        member = create_npc('Security Guard',my_location.owned_by,my_location.owned_by)
		patrol_members.append(member)
		patrol_count += 1
	actors = NPC(patrol_members,0,[],0)
	while decision == False:
		key = libtcod.console_check_for_keypress()
		if key.c == ord('a') and open== True:
			fight = check_dress_code(player_party,my_location)
			if fight == True:
				libtcod.console_clear(0)
           	        	for member in patrol_members:
           	                	for corp in world.corporations:
               		                	if corp.name == member.affiliation:
                        		        	corp.members_attacked += 1
                        	#for room in my_location.parent_location.rooms:
                        	#	room.alarm_level += random.randint(2,5)
                        	libtcod.console_clear(0)
                        	battle(party,actors,my_location,world,True,party_actions)
                        	libtcod.console_clear(0)
                        	decision = True
			elif fight == False:
				libtcod.console_clear(0)
				libtcod.console_print(0, 1, 1, 'The patrol leaves.')
				libtcod.console_print(0, 1, 3, '[c]ontinue')
				libtcod.console_flush()
				confirm = False
				while confirm == False:
					key = libtcod.console_check_for_keypress()
					if key.c == ord('c'):
						libtcod.console_clear(0)
						decision = True
						confirm = True
			else:
                                libtcod.console_clear(0)
                                libtcod.console_print(0, 1, 1, 'The patrol leaves.')
                                libtcod.console_print(0, 1, 3, '[c]ontinue')
                                libtcod.console_flush()
                                confirm = False
                                while confirm == False:
                                        key = libtcod.console_check_for_keypress()
                                        if key.c == ord('c'):
                                                libtcod.console_clear(0)
                                                decision = True
                                                confirm = True

		if key.c == ord('f'):
			for member in patrol_members:
				for corp in world.corporations:
					if corp.name == member.affiliation:
						corp.members_attacked += 1
			for room in my_location.parent_location.rooms:
				room.alarm_level += random.randint(2,5)
			libtcod.console_clear(0)
			battle(party,actors,my_location,world,True,party_actions)
			libtcod.console_clear(0)
			decision = True
		elif key.c == ord('h'):
			members_stealth = []
			libtcod.console_clear(0)
			line_count = 1
			party_detected = False
			for member in party.members:
				roll = random.randint(1,6)
				if roll <= member.skills.stealth:
					member_stealth_roll = [member,'passed']
				else:
					member_stealth_roll = [member,'failed']
				members_stealth.append(member_stealth_roll)
			for member in members_stealth:
				if member[1] == 'failed':
					stealth = member[0].skills.stealth + member[0].skills.security

					if stealth <= 1:
						stealth = 2
					detection_roll = random.randint(1,stealth)
					if detection_roll == 1:
						party_detected = True
						print member[0].fname + " " + member[0].lname + " detected"
					else:
						print member[0].fname + " " + member[0].lname + ' not detected'
			if party_detected == False:
			        libtcod.console_print(0, 1, 1, 'The patrol passes by.')
			elif party_detected == True:
			        libtcod.console_print(0, 1, 1, '"Intruders! Get them!"')
		        libtcod.console_print(0, 1, 3, '[c]ontinue')
			libtcod.console_flush()
			finished_hide = False
			while finished_hide == False:
				key2 = libtcod.console_check_for_keypress()
				if key2.c == ord('c') and party_detected == True:
                        		for member in patrol_members:
                                		for corp in world.corporations:
                                        		if corp.name == member.affiliation:
                                                		corp.members_attacked += 1
                        		for room in my_location.rooms:
                                		room.alarm_level += random.randint(2,5)
                        		libtcod.console_clear(0)
                        		battle(party,actors,my_location,world,True,party_actions)
                        		libtcod.console_clear(0)
					finished_hide = True
                                elif key2.c == ord('c') and party_detected == False:
					libtcod.console_clear(0)
					finished_hide = True
			decision = True
		#elif key.c == ord('r'):
		#	members_dexterity = 0
		#	patrol_dexterity = 0
		#	libtcod.console_clear(0)

		#	for member in party.members:
		#		roll = random.randint(1,15)
		#		if roll <= member.stats.dexterity:
		#			members_dexterity += member.stats.dexterity 
		#		else:
			#		members_dexterity += member.stats.dexterity / 2
                 #       for member in patrol_members:
                  #              roll = random.randint(1,15)
                   #             if roll <= member.stats.dexterity:
                    #                    patrol_dexterity += member.stats.dexterity 
                     
			#         else:
                         #               patrol_dexterity += member.stats.dexterity / 2
			#if members_dexterity >= patrol_dexterity + 1:

def show_rooms(party,world,my_location,party_actions):
	print len(my_location.rooms)
	libtcod.console_clear(0)
#	libtcod.console_print(0, 1, 1, 'ROOMS:')
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
			if room_count <= 40:
				libtcod.console_print(0,1,room_count + 1, '[' + option[0] + ']' + option[1].name + "(" + str(option[1].floor) + ")")
                        elif room_count >= 41 and room_count <= 80:
                                libtcod.console_print(0,42,room_count - 39, '[' + option[0] + ']' + option[1].name + "(" + str(option[1].floor) + ")")
			room_count += 1
		key = libtcod.console_check_for_keypress()
		for option in options:
			if key.c == ord(option[0]):
				print party.location.name + " " + str(party.location.floor)
                                print option[1].name + " " + str(option[1].floor)

				#party.location = option[1]
				if party.location.floor > option[1].floor:
					floors_travelled =  party.location.floor - option[1].floor
					print 'travelled down ' + str(floors_travelled) + " floors"
				elif party.location.floor < option[1].floor:
					floors_travelled = option[1].floor - party.location.floor
					print 'travelled up' + str(floors_travelled) + " floors"
				elif party.location.floor == option[1].floor:
					floors_travelled = 0
                                party.location = option[1]
				extra_time = 0
				if floors_travelled == 0:
					world.time.minute += 1
				elif floors_travelled >= 1:
					print floors_travelled
					extra_time = floors_travelled * 1
					world.time.minute += extra_time + 1

				#chance_encounter = random.randint(1,7)
				player_live_here = False
				for room in party.location.rooms:
					if room.owned_by == 'Player':
						player_live_here = True
				check_count =1
				while check_count <= extra_time + 1:
				
					chance = random.randint(1,10) - my_location.alarm_level - my_location.security_level
					if chance <= 0:
						chance = 2
					chance_encounter = random.randint(1,chance)
					if chance_encounter <= 1 and player_live_here == False and my_location.security_level != 0:
						finished_encounter = False
						while finished_encounter == False:
							show_patrol(party,world,my_location,party_actions)
							finished_encounter = True
					check_count +=1
				world.time.correct(party_actions) 
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
				if location.name != 'Your Squat':
					world.player_organization.rent_due.append(location)
			world.player_organization.rent_paid = False
			world.player_organization.rent_checked = True
			return world.player_organization.rent_checked 
			#print 'checked rent'
def show_location(party,world,location):
	libtcod.console_clear(0)
	libtcod.console_print(0,1,1,'[a] ' +location.name)
	if location.parent_location != None:
	        libtcod.console_print(0,1,2,location.parent_location.name)
        libtcod.console_print(0,1,3,'[ESC]')
	libtcod.console_flush()
	finished = False
	while finished == False:
		key = libtcod.console_check_for_keypress()
		if key.vk == libtcod.KEY_ESCAPE:
			finished = True
		elif key.c == ord('a'):
			party.location = location
			finished = True
def show_organization(party,world):
	libtcod.console_clear(0)
	finished_organization = False
	line_count = 1
	my_location = find_location(party,world)
	my_area = find_area(party,world)
	print world.player_organization
	locations = []
	if len(world.player_organization.locations_owned) >= 1:
                libtcod.console_print(0,1,line_count,'LOCATIONS:')
                line_count += 2
		my_location = []
		count = 1
		for location in world.player_organization.locations_owned:
			libtcod.console_print(0,1,line_count,"[" + str(count) + "]" + location.name)
			letter = num_to_letter(count)
			this_location = [str(count),location]
			locations.append(this_location)
			line_count += 1
			count += 1
		print world.player_organization.rent_amount
		line_count +=1
                libtcod.console_print(0,1,line_count,"$" + str(world.player_organization.rent_amount))

		if world.player_organization.rent_paid == False:
			line_count += 2
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
		real_footsoldier_count = 1
		for footsoldier in world.player_organization.footsoldiers:
			letter = num_to_letter(real_footsoldier_count)
			option = [letter,footsoldier]
                	libtcod.console_print(0,1,line_count,'[' + letter + '] ' + footsoldier.npc.fname + ' ' + footsoldier.npc.lname)
                        libtcod.console_print(0,30,line_count,footsoldier.npc.profession)
	                libtcod.console_print(0,45,line_count, footsoldier.orders)
			if footsoldier.home == 'No home' or footsoldier.home == None:
	                        libtcod.console_print(0,65,line_count, 'No home')
			else:

                        	libtcod.console_print(0,65,line_count, footsoldier.home.name)

			my_footsoldiers.append(option)
			line_count += 1
			#footsoldier_count += 2
			real_footsoldier_count += 1
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
			libtcod.console_clear(0)
			finished_organization = True
			return True
		elif key.c == ord('p') and world.player_organization.rent_paid == False:
			#places_rented = []
			#for place in world.player_organization.locations_owned:
			
			rent = world.player_organization.rent_amount
			if party.money >= rent:
				party.money -= rent
				world.player_organization.rent_paid = True
				return True
		elif key.c != ord('*') and key.c != ord('p'):
			for option in my_footsoldiers:
				print '[' + option[0] + '] ' + option[1].npc.fname + ' ' + option[1].npc.lname
				if key.c == ord(option[0]):
					footsoldier.npc = show_character(footsoldier.npc,world,False,my_location,party,False)

					finished_organization = True
			for location in locations:
				if key.c == ord(location[0]):
					show_location(party,world,location[1])
					finished_organization = True
	libtcod.console_clear(0)
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


def party_turn(player_party,world,party_actions):

	world.player_organization.check_rent = check_rent(player_party,world)
	check_evicted(player_party,world)
#describe the location
	my_location = find_location(player_party,world)
        #handle cold
       	player_party.handle_morale(world,my_location)
	#check reputation
	for area in world.areas:
		for organization in area.organizations:
			organization.check_reputation(player_party,world)
	for corporation in world.corporations:
		corporation.check_reputation(player_party,world)
	#make sure no one is still on fire
	for member in player_party.members:
		if member.combat_status.on_fire == True:
			member.combat_status.on_fire = False
        #make sure thee isn't a corpse and a living person
        for corpse in my_location.corpses:
	        for member in my_location.actors.members:
                        if corpse.fname == member.fname and corpse.lname == member.lname: 
        	                my_location.actors.members.remove(member) 
				if member in my_location.regulars:
					my_location.regulars.remove(member)
                        elif corpse == member: 
                                my_location.actors.members.remove(member) 

	#make sure homes are proper
	#for location in world.player_organization.locations_owned:
	turn_finished = False
	described = False
	while described == False:
		#check_rent(player_party,world)
		#find the player party
		my_location = find_location(player_party,world)
		my_location_items = my_location.items
		#for item in my_location.items:
		#	if item.item_type == 'Medical' and item.name == 'None':
		#		my_location.items.remove(item)
		#	for item2 in my_location.items:
		#		if item2.item_type == 'Medical':
		#			if item2.number == item.number:
		#				my_location.items.remove(item2)
		#my_location.items = set(my_location.items)
                #my_location.items = list(my_location.items)

		my_area = find_area(player_party,world)
		#make sure there are no duplicate npcs at location
		my_location.area = my_area.name
		my_location.actors.members = set(my_location.actors.members)
                my_location.actors.members = list(my_location.actors.members)
		#brokers and bodyguards
                if my_location.has_broker == True and my_location.broker != None:
                        print 'broker is here'
                        print my_location.broker.fname + " " + my_location.broker.lname
                        my_location.actors.members.append(my_location.broker)
			if my_location.broker.broker != None:
				print my_location.broker.broker.guards
				if len(my_location.broker.broker.guards) >= 1:
					print 'guards here'
					for guard in my_location.broker.broker.guards:
						print guard.fname + " " + guard.lname
						print guard
						my_location.actors.members.append(guard)
		for member in my_location.actors.members:
			if member == None:
				my_location.actors.members.remove(member)
			for member2 in my_location.actors.members:
				if member2 == None:
					my_location.actors.members.remove(member2)
				elif member != None:
					if member.fname == member2.fname and member.lname == member2.lname:
						if member != member2:
							my_location.actors.members.remove(member2)
							if member2 in my_location.regulars:
								my_location.regulars.remove(member2)
							
						#elif member == member2:
						#	my_location.regulars.remove(member2)
		#make sure there isn't a corpse and a living person in the same place
		for corpse in my_location.corpses:
			for member in my_location.actors.members:
				if corpse.fname == member.fname and corpse.lname == member.lname:
					my_location.actors.members.remove(member)
				elif corpse == member:
					my_location.actors.members.remove(member) 
		#is there security here / check dress code
		if my_location.security_level >= 1:
			if my_location.dress_code.name != 'none':
				passed_check = True
				num_violations = 0
				#hats and headwear
				if len(my_location.dress_code.headwear) == 0:
					for member in player_party.members:
						if member.headwear != no_headwear:
							passed_check = False
							num_violations += 1
				elif len(my_location.dress_code.headwear) >= 1:
					if member.headwear not in my_location.dress_code.headwear:
						passed_check = False
						num_violations += 1

                                #shirts
                                if len(my_location.dress_code.outfit) == 0:
                                        for member in player_party.members:
                                                if member.outfit != naked:
                                                        passed_check = False
							num_violations += 1

                                elif len(my_location.dress_code.outfit) >= 1:
                                        if member.outfit not in my_location.dress_code.outfit:
                                                passed_check = False
						num_violations += 1

                                #outerwear
                                if len(my_location.dress_code.outerwear) == 0:
                                        for member in player_party.members:
                                                if member.outerwear != no_outerwear:
                                                        passed_check = False
							num_violations += 1

                                elif len(my_location.dress_code.outerwear) >= 1:
                                        if member.outerwear not in my_location.dress_code.outerwear:
                                                passed_check = False
						num_violations += 1

                                #legwear
                                if len(my_location.dress_code.legwear) == 0:
                                        for member in player_party.members:
                                                if member.legwear != legwear:
                                                        passed_check = False
							num_violations += 1

                                elif len(my_location.dress_code.legwear) >= 1:
                                        if member.legwear not in my_location.dress_code.legwear:
                                                passed_check = False
						num_violations += 1

                                #footwear
                                if len(my_location.dress_code.footwear) == 0:
                                        for member in player_party.members:
                                                if member.footwear != footwear:
                                                        passed_check = False
							num_violations += 1

                                elif len(my_location.dress_code.footwear) >= 1:
                                        if member.footwear not in my_location.dress_code.footwear:
                                                passed_check = False
						num_violations += 1

				print 'dress code: ' + str(passed_check)
				print str(num_violations) + ' violations.'
				#is there anyone here to notice we aren't wearing the right clothes
				violations_noticed = 0
				if len(my_location.actors.members) >= 1:
					for member in my_location.actors.members:
												
						notice_roll = random.randint(1,10)
						if my_location.alarm_level >= 1:
							notice_roll += my_location.alarm_level
						if notice_roll <= my_location.security_level:
							violations_noticed += 1
							my_location.alarm_level += 1
					print str(violations_noticed) + ' violations noticed.'
					#if violations_noticed <= 4:
					#	chance_call_security = 5
					#elif violations_noticed >= 5:
					#	chance_call_security = 7
					#call_security_count = 0
					#alarm_count = 0
					#while violations_noticed <= call_security_count:
					#	chance = random.randint(1,10)
					#	if chance <= chance_call_security:
					#		alarm_count += 1
					#	call_security_count += 1
					print str(my_location.alarm_level) + ' suspicion.'
					if my_location.parent_location == None:
						for room in my_location.rooms:
							room.alarm_level = my_location.alarm_level
					else:
						for room in my_location.parent_location.rooms:
							room.alarm_level = my_location.alarm_level
		#print my_location .name
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
			open = True
		else:
			open = False
		employees = []
		if open == True:
                        libtcod.console_set_default_foreground(0, libtcod.green)
			libtcod.console_print(0,12,4, 'OPEN')
                        libtcod.console_set_default_foreground(0, libtcod.white)

			my_location.is_indoors = True
			employees = my_location.regulars
			employees = set(employees)
			employees = list(employees)
			my_location.actors.members = employees
		elif open == False and my_location.is_store == True:
                        libtcod.console_set_default_foreground(0, libtcod.dark_grey)
                        libtcod.console_print(0,12,4, 'CLOSED')
                        libtcod.console_set_default_foreground(0, libtcod.white)

			my_location.is_indoors = False
			my_location.actors.members = []
	                #employees = []
        	        if my_location.is_store == True and open == False:
                	        #employees = []
				if len(my_location.regulars) >= 1:
                        		for member in my_location.regulars:
						if member != None:
                                			if member.profession == 'Security Guard':
                                			        employees.append(member)
		#are we indoors
		if my_location.is_indoors == True:
                        libtcod.console_set_default_foreground(0, libtcod.light_green)
                        libtcod.console_print(0,1,4, 'INDOORS')
                        libtcod.console_set_default_foreground(0, libtcod.white)

			if open == True:
				if heater not in my_location.items:
					my_location.items.append(heater)
			
		else:
			libtcod.console_set_default_foreground(0, libtcod.dark_grey)
                        libtcod.console_print(0,1,4, 'OUTDOORS')
			libtcod.console_set_default_foreground(0, libtcod.white)
			if heater in my_location.items:
				my_location.items.remove(heater)

#		if my_location.has_broker == True and my_location.broker != None:
#	                print 'broker is here'
 #                       print my_location.broker.fname + " " + my_location.broker.lname
  #                      employees.append(my_location.broker)

                #make sure there are no duplicate employees at location
                my_location.area = my_area.name
                my_employees = set(employees)
                for employee in employees:
                        if employee == None:
                                employees.remove(employee)
                        for employee2 in employees:
                                if employee2 == None:
                                        employees.remove(employee2)
                                elif employee2 != None:
                                        if employee.fname == employee2.fname and employee.lname == employee2.lname:
                                                if employee != employee2:
                                                        employees.remove(employee2)


                #if len(employees) >= 1:
                 #       for members in es:
                  #              my_location.actors.members.append(employee)
		#employees = set(employees)

		#time
		world.time.correct(party_actions)
		hour = world.time.get_hour()
		month = world.time.get_month()
		am_pm = world.time.get_am_or_pm()
		libtcod.console_print(0,40,1, month + " " + str(world.time.day) + ", " + str(world.time.year))
		#libtcod.console_set_default_foreground(0, libtcod.grey)
		if world.weather.temperature >= 1 and world.weather.temperature <= 19:
			libtcod.console_set_default_foreground(0, libtcod.yellow)
		elif world.weather.temperature >= 20:
			libtcod.console_set_default_foreground(0, libtcod.orange)
		elif world.weather.temperature <= 0 and world.weather.temperature >= -19:
			libtcod.console_set_default_foreground(0, libtcod.blue)
		elif world.weather.temperature <= -20:
			libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                libtcod.console_print(0,40,4, str(world.weather.temperature) + "C")
		
		libtcod.console_set_default_foreground(0, libtcod.white)
		if world.weather.clouds == 'Sunny':
			libtcod.console_set_default_foreground(0, libtcod.yellow)
                elif world.weather.clouds == 'Overcast':
                        libtcod.console_set_default_foreground(0, libtcod.gray)
                elif world.weather.clouds == 'Dark clouds':
                        libtcod.console_set_default_foreground(0, libtcod.dark_gray)
                elif world.weather.clouds == 'Light rain':
                        libtcod.console_set_default_foreground(0, libtcod.light_blue)
                elif world.weather.clouds == 'Heavy rain' or world.weather.clouds == "Heavy freezing rain":
                        libtcod.console_set_default_foreground(0, libtcod.dark_blue)
                elif world.weather.clouds == 'Light snow' or world.weather.clouds == "Light freezing rain" or world.weather.clouds == "Heavy snow":
                        libtcod.console_set_default_foreground(0, libtcod.blue)

                libtcod.console_print(0,40,3, str(world.weather.clouds))
                libtcod.console_set_default_foreground(0, libtcod.white)

		if world.weather.precipitation == True:
			libtcod.console_print(0,40,5, str(world.weather.precipitation_type))
		libtcod.console_set_default_foreground(0, libtcod.white)

		if world.time.minute <= 9:
			minute = '0' + str(world.time.minute)
		else:
			minute = world.time.minute
		libtcod.console_print(0,40,2, str(hour) + ':' + str(minute) + ' ' + am_pm)
		#libtcod.console_print(0,40,3, "$" + str(player_party.money))
		#is this location owned
		if my_location.owned_by != "No one" and my_location.owned_by != None:
	                #libtcod.console_set_default_foreground(0, libtcod.yellow)
                        libtcod.console_print(0,1,5, "OWNER:")
	                libtcod.console_set_default_foreground(0, libtcod.white)
			if my_location.owned_by != None:
				if type(my_location.owned_by) is str:
					libtcod.console_print(0,8,5, my_location.owned_by)
				if type(my_location.owned_by) is not str:
                                        libtcod.console_print(0,8,5, my_location.owned_by.name)

		#rooms
		if my_location.parent_location != None:
			my_location.rooms = my_location.parent_location.rooms
		if len(my_location.rooms) >= 1:
			libtcod.console_print(0,40,7, str(len(my_location.rooms)) + ' rooms[*]')
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
			#check if cold
			if member.health.body_temp <= 10 and member.health.body_temp >= -25:
                                message = member.fname + ' ' + member.lname + " is cold."
                                messages.append(message)
                        elif member.health.body_temp <= -26:
                                message = member.fname + ' ' + member.lname + " is freezing!"
                                messages.append(message)
                        elif member.health.body_temp >= 70 and member.health.body_temp <= 99:
                                message = member.fname + ' ' + member.lname + " is hot"
                                messages.append(message)
                        elif member.health.body_temp >= 100:
                                message = member.fname + ' ' + member.lname + " is very hot!"
                                messages.append(message)


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
                        if member.mind.sanity <= 20 and member.mind.sanity >= 0:
                                message = member.fname + ' ' + member.lname + " is acing strangely."
                                messages.append(message)
                        elif member.mind.sanity <= -1:
                                message = member.fname + ' ' + member.lname + " is acting crazy."
                                messages.append(message)

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
					if item.name == "Blood":
                                                libtcod.console_set_default_foreground(0, libtcod.dark_red)

					if item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
						libtcod.console_set_default_foreground(0, libtcod.orange)
					libtcod.console_print(0,1,line_count, item.name)
                                        if item.name == "Blood" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.white)

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
					name = item.location.capitalize()

					libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        libtcod.console_print(0,1,line_count, name)
					libtcod.console_set_default_foreground(0, libtcod.white)
                                        item_count += 1
                                        line_count += 1
                                else:
                                        libtcod.console_print(0,1,line_count, item.name)
                                        item_count += 1
                                        line_count += 1


                        elif item_count >= 7 and item_count <=12:
				#line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        if item.name == "Blood":
                                                libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        if item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.orange)
                                        libtcod.console_print(0,20,line_count-6, item.name)
                                        if item.name == "Blood" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0,libtcod.white) 
					

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
					name = item.location.capitalize()
					libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        libtcod.console_print(0,20,line_count-6, name)
					libtcod.console_set_default_foreground(0, libtcod.white)
                                        item_count += 1
                                        line_count += 1
                                else:
                                        libtcod.console_print(0,20,line_count-6, item.name)
                                        item_count += 1
                                        line_count += 1


                        elif item_count >= 13 and item_count <=18:
                                #line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        if item.name == "Blood":
                                                libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        if item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.orange)
                                        libtcod.console_print(0,40,line_count-12, item.name)
                                        if item.name == "Blood" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.white)


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
					name = item.location.capitalize()

					libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        libtcod.console_print(0,40,line_count-12, item.name)
					libtcod.console_set_default_foreground(0, libtcod.white)
                                        item_count += 1
                                        line_count += 1
                                else:
                                        libtcod.console_print(0,40,line_count-12, item.name)
                                        item_count += 1
                                        line_count += 1



                        elif item_count >= 19 and item_count <=24:
                                #line_count -= 7     
                                #line_count = item_count + line_count
                                if item.item_type == 'weapon' or item.item_type == 'outfit' or item.item_type == 'junk':
                                        if item.name == "Blood":
                                                libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        if item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.orange)
                                        libtcod.console_print(0,60,line_count-18, item.name)
                                        if item.name == "Blood" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == 'Radiator':
                                                libtcod.console_set_default_foreground(0, libtcod.white)

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
					name = item.location.capitalize()
					libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                        libtcod.console_print(0,60,line_count-18, name)
					libtcod.console_set_default_foreground(0, libtcod.white)
                                        item_count += 1
                                        line_count += 1
                                else:
                                        libtcod.console_print(0,60,line_count-18, item.name)
                                        item_count += 1
                                        line_count += 1


			else:
				possible_regulars = []
			count = 1
		line_count = 18
		if len(my_location.actors.members) >= 1 or len(my_location.corpses) >= 1:
			libtcod.console_print(0,1,line_count, 'PEOPLE HERE:')
                        if my_location.broker != None and my_location.time_open <= world.time.hour:
                                my_location.actors.members.append(my_location.broker)
				if len(my_location.broker.broker.guards) >= 1:
					for guard in my_location.broker.broker.guards:
						my_location.actors.members.append(guard)
				#print 'broker is here'
				#print my_location.broker.fname + " " + my_location.broker.lname
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
				libtcod.console_set_default_foreground(0, libtcod.dark_red)
                                libtcod.console_print(0,1,line_count, corpse.profession + " corpse")
				libtcod.console_set_default_foreground(0, libtcod.white)

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
	exit = False
        while action == False:
		#get a decision
                libtcod.console_flush()
                key = libtcod.console_check_for_keypress()


                #attack
                if key.c == ord('a'):
                        finished_fighting = False
			while finished_fighting == False:
				for member in my_location.actors.members:
					for area in world.areas:
						for organization in area.organizations:
							if organization.name == member.affiliation:
								organization.members_attacked += 1
				finished_fighting = battle(player_party,my_location.actors,my_location,world,True,party_actions)
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
					finished_loot = loot(player_party,world,party_actions)
				looting = False
			action = True

		#
		#investigate
                if key.c == ord('i'):
			finished_viewing = False
			while finished_viewing == False:
                        	investigate(my_location,world,player_party,party_actions)
				world.time.minute += 5
				world.time.correct(party_actions)
				finished_viewing = True

                        action = True  		
		
		#
		#travel
                if key.c == ord('t'):
			time = world.time.hour
                        my_location, turn_finished, my_area = travel(player_party,world,my_location,my_area,party_actions)
                        #handle drugs, injuries, etc
                        handle_party_drugs(player_party,world)
			handle_party_mind
			handle_npcs(player_party,world)
			world = handle_jobs(player_party,world)
			handle_missions(player_party,world,party_actions)
			if time <= world.time.hour - 1:
	                	handle_footsoldiers(player_party,world,party_actions)
				#player_party.handle_cold(world,my_location)
				player_party.handle_morale(world,my_location)
			player_party.area = my_area.name
			player_party.area_x = my_area.x
			player_party.area_y = my_area.y
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
				finished_party = show_party(player_party,world,party_actions)

				action = True
                #rest
                if key.c == ord('r'):
                        finished_rest = False
                        while finished_rest == False:
				can_rest = False
				if my_location.owned_by == 'Player' or my_location.owned_by == None or my_location.owned_by == 'No one':
					can_rest = True
				else:
					can_rest = False
				if can_rest == True:
                                	finished_rest = show_rest(player_party,world)

                                	action = True
				if can_rest == False:
					#libtcod.console_clear(0)
					finished_rest = True
					action = True
		#speak
                if key.c == ord('s'):
                        finished_speaking = False
                        while finished_speaking == False:
                                finished_speaking = speak(player_party,world,my_location,party_actions)

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
				finished_move = show_rooms(player_party,world,my_location,party_actions)
				action = True


		if key.vk == libtcod.KEY_ESCAPE:
			exit = True
			action = True
			#finished_turn = True
			#if finished_showing == True:
			#	described = False
	return action, exit

#start the game
game = Game(True, True)
messages = []
def run():
	global game, player_party, world,party_actions
	while not libtcod.console_is_window_closed():
		while game.running == True and game.starting == True:
			start = startup()
			libtcod.console_flush()
			party_actions = Party_Actions(0,0,0,0,0,0,0,0,0,0)
			begin = 0
			if start == 2:
				try:
	                	        libtcod.console_clear(0)
	                	        libtcod.console_print(0,1,1, 'Loading.')
	                	        libtcod.console_flush()
					game, world, player_party,party_actions = load_game()
	
					begin = 2
				except:
					begin = 1
			elif start == 1:
				begin = 1
			elif start == 3:
				return True
			if begin == 1:
				player = main_menu()
				#party_actions = Party_Actions(0,0,0,0,0,0,0,0)

	        		player_party, world,party_actions = create_party(player)
				print player_party
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
			#print player_party
			#if len(messages) >= 1:
			#	for message in messages:
			#		new_messages.append(message)
			while turn_finished == False:
				#save_game()
				#world,player_party = load_game()
				my_location = find_location(player_party,world)
				turn_finished,exit = party_turn(player_party,world,party_actions)
				if exit == True:
                                        libtcod.console_clear(0)
                                        game.running,game.starting,confirm = True,True,True
		confirm = False
		libtcod.console_clear(0)
		while game.running == True and game.starting == False and confirm == False and len(player_party.members) <= 0:
			while confirm == False:
		                libtcod.console_print(0,1,1, 'GAME OVER.')
        	                libtcod.console_print(0,1,3, '[c]ontinue')
	
        	                libtcod.console_flush()
				key = libtcod.console_check_for_keypress()
				if key.c == ord('c'):
					libtcod.console_clear(0)
					game.running,game.starting,confirm = True,True,True

run()
