import random
import libtcodpy as libtcod



global location_id
global item_id

from namegen import *


class Message:
	def __init__(self,message,time,color):
		self.message = message
		self.time = time
		self.color = color

class Party:
	def __init__(self,is_player,leader,members,location,area,district,money,inventory,safehouse,fame,x,y,area_x,area_y):
		self.is_player = is_player
		self.leader = leader
		self.members = members
		self.location = location
		self.area = area
		self.district = district
		self.money = money
		self.inventory = inventory
		self.safehouse = safehouse
		self.fame = fame
		self.x = x
		self.y = y
		self.area_x = area_x
		self.area_y = area_y
	def handle_cold(self,world,location):
		for member in self.members:
			clothing_warmth = member.check_clothing_warmth()
			#are we indoors
			indoors = False
			heated = False
			base = 0
			if location.is_indoors == True:
				indoors = True
				if world.weather.temperature <= 0:
					base += 4
			for item in location.items:
				if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == "Wood stove" or item.name == "Fire":
					heated = True
			if location.parent_location != None:
				for item in location.parent_location.items:
	                                if item.name == "Radiator" or item.name == "Barrel fire" or item.name == "Space heater" or item.name == "Wood stove":
						heated = True
			if world.weather.temperature <= 8 and heated == True:
				print 'heated'
				world.weather.temperature = random.randint(9,20)

			member.health.cold_rating = clothing_warmth  + world.weather.temperature / 2 
			#are we outdoots
			wet_rating = 0
			if location.is_indoors == False:
				#is it raining
				#head
				if world.weather.precipitation_amount >= 1:
					if member.headwear != None:
						if member.headwear.waterproof <= world.weather.precipitation_amount:
							how_wet = world.weather.precipitation_amount - member.headwear.waterproof 
							wet_rating += how_wet
							member.headwear.wet += how_wet
                        	#face
                        	if world.weather.precipitation_amount >= 1:
                               		if member.facewear != None:
                                	        if member.facewear.waterproof <= world.weather.precipitation_amount: 
                                	                how_wet = world.weather.precipitation_amount - member.facewear.waterproof
                                	                wet_rating += how_wet
                                	                member.facewear.wet += how_wet


                        	#hands
                        	if world.weather.precipitation_amount >= 1:
                        	        if member.handwear != None:
                        	                if member.handwear.waterproof <= world.weather.precipitation_amount: 
                        	                        how_wet = world.weather.precipitation_amount - member.handwear.waterproof 
                        	                        wet_rating += how_wet
                        	                        member.handwear.wet += how_wet

                        	#feet
                        	if world.weather.precipitation_amount >= 1:
                        	        if member.footwear != None:
                        	                if member.footwear.waterproof <= world.weather.precipitation_amount: 
                        	                        how_wet = world.weather.precipitation_amount - member.footwear.waterproof  
                        	                        wet_rating += how_wet
                        	                        member.footwear.wet += how_wet
				#outfit
				outerwear = False
			
                        	if world.weather.precipitation_amount >= 1:
                        	        if member.outerwear != None and member.outerwear != "No outerwear":
                        	                if member.outerwear.waterproof <= world.weather.precipitation_amount: 
                        	                        how_wet = world.weather.precipitation_amount - member.outerwear.waterproof  
                        	                        wet_rating += how_wet
                        	                        member.outerwear.wet += how_wet
							if member.outerwear.wet >= 5:
								if member.outfit != None and member.outfit != 'No top':
									if member.outfit.waterproof >= how_wet:
										how_wet = member.outfit.waterproof - how_wet
                        	                        		member.outfit.wet += how_wet
					elif member.outerwear == 'No outerwear':
						if member.outfit != None and member.outfit != "No outfit":
	                                	        if member.outfit.waterproof <= world.weather.precipitation_amount: 
	                                	                how_wet = world.weather.temperature - member.outerwear.waterproof  
	                                	                wet_rating += how_wet
	                                	                member.outfit.wet += how_wet
			elif location.is_indoors == True or world.weather.precipitation <= 0:
				#dry clothing when not in the rain
				dry_bonus = 0
				if world.weather.temperature >= -5:
					dry_bonus += 1
				elif weather.temperature >= 15:
					dry_bonus += 1
				#head
				if member.headwear.wet >= 1:
					member.headwear.wet -= dry_bonus
				if member.headwear.wet <= -1:
					member.headwear.wet = 0
                                #face
                                if member.facewear.wet >= 1:
                                        member.facewear.wet -= dry_bonus
                                if member.facewear.wet <= -1:
                                        member.facewear.wet = 0
                                #hands
                                if member.handwear.wet >= 1:
                                        member.handwear.wet -= dry_bonus
                                if member.handwear.wet <= -1:
                                        member.handwear.wet = 0
                                #feet
                                if member.footwear.wet >= 1:
                                        member.footwear.wet -= dry_bonus
                                if member.footwear.wet <= -1:
                                        member.footwear.wet = 0
                                #outerwear
                                if member.outerwear.wet >= 1:
                                        member.outerwear.wet -= dry_bonus
                                if member.outerwear.wet <= -1:
                                        member.outerwear.wet = 0
                                #outfit
                                if member.outfit.wet >= 1:
                                        member.outfit.wet -= dry_bonus
                                if member.outfit.wet <= -1:
                                        member.outfit.wet = 0



			if member.health.cold_rating >= 30 and member.health.cold_rating <= 29:
				member.health.body_temp += random.randint(2,6)
			elif member.health.cold_rating >= 40:
				member.health.body_temp += random.randint(2,6)
			elif member.health.cold_rating <= 19 and member.health.cold_rating >= -5 and member.health.body_temp <= -1 and world.weather.temperature <= 14:
				member.health.body_temp += random.randint(2,6)
                        elif member.health.cold_rating <= 19 and member.health.cold_rating >= -5 and member.health.body_temp >= 51 and world.weather.temperature <= 14:
                                member.health.body_temp -= random.randint(2,6)
                        elif member.health.cold_rating <= 19 and member.health.cold_rating >= -5 and member.health.body_temp >= 0 and member.health.body_temp <= 50:
                                member.health.body_temp = member.health.body_temp
                        elif member.health.cold_rating >= 20 and member.health.body_temp >= 0 and member.health.body_temp <= 50:
                                member.health.body_temp += random.randint(2,6)
                        elif member.health.cold_rating >= 20 and member.health.body_temp >= 51:
                                member.health.body_temp -= random.randint(2,6)




			elif member.health.cold_rating <= 6 and member.health.cold_rating <= -10:
				member.health.body_temp -= random.randint(2,6)
			elif member.health.cold_rating >= -11:
                                member.health.body_temp -= random.randint(12,18)
			if member.health.body_temp <= -100:
				member.health.body_temp = -100
			elif member.health.body_temp >= 150:
				member.health.body_temp = 150
	#def handle_precipitation(self,world,location):
		
	def handle_morale(self,world,location):
		self.handle_cold(world,location)
#		print 'big success'
	def party_value(self):
		value = 0

		for member in self.members:
			if member.headwear != None or member.headwear != "No headwear":
				value += member.headwear.base_value
                        if member.facewear != None or member.facewear != "No facewear":
                                value += member.facewear.base_value
                        if member.handwear != None or member.handwear != "No handwear":
                                value += member.handwear.base_value
                        if member.footwear != None or member.footwear != "No footwear":
                                value += member.footwear.base_value
                        if member.outerwear != None or member.outerwear != "No outerwear":
                                value += member.outerwear.base_value
                        if member.outfit != None or member.outfit != "Naked":
                                value += member.outfit.base_value
                        if member.armor != None or member.armor != "No armor":
                                value += member.armor.base_value
		for item in self.inventory:
			if item.number == None or item.number == 1:
				value += item.base_value
			elif item.number >= 2:
				value += item.base_value * item.number
		return value

class Party_Actions:
	def __init__(self,days_survived,kills,stealing,robbery,drug_dealing,kidnapping,torture,citizens_killed,faction_members_killed,missions_completed):
		self.days_survived = days_survived
		self.kills = kills
		self.stealing = stealing
		self.robbery = robbery
		self.drug_dealing = drug_dealing
		self.kidnapping = kidnapping
		self.torture = torture
		self.citizens_killed = citizens_killed
		self.faction_members_killed = faction_members_killed
		self.missions_completed = missions_completed
#party_actions = Party_Actions(0,0,0,0,0,0,0,0)
class NPC:
        def __init__(self,members,money,inventory,fame):
                self.members = members
                self.money = money
                self.inventory = inventory
                self.fame = fame

#is_player,leader,members,location,area,district,money,inventory,safehouse,fame

class Char:
	def __init__(self, gender,age, profession,affiliation, health, stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,start_money,controlled_by,combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,driver,passenger,is_broker,broker,is_quest_npc,quest_npc):
		self.gender = gender
		self.age = age
		self.profession = profession
		self.affiliation = affiliation
		self.health = health
		self.stats = stats
		self.injuries = injuries
		self.skills = skills 
		self.skills_xp = skills_xp

		self.weapon = weapon
		self.outfit = outfit
		self.tool = tool

		self.traits = traits
		self.drugs = drugs

		self.fname = fname
		self.lname = lname

		self.start_money = start_money
		self.controlled_by = controlled_by

		self.combat_status = combat_status
		self.home = home

		self.mind = mind

		self.hunger = hunger
		self.thirst = thirst
		self.sleep = sleep

		self.headwear = headwear
		self.facewear = facewear
		self.eyewear = eyewear
		self.handwear = handwear
		self.legwear = legwear
		self.footwear = footwear

		self.outerwear = outerwear
		self.armor = armor
	
		self.driver = driver
		self.passenger = passenger

		self.is_broker = is_broker
		self.broker = broker
		self.is_quest_npc = is_quest_npc
		self.quest_npc = quest_npc

	def bleed(self):
		self.health.current_blood -= self.health.bleeding_rate

	def damage(self,damage):
		self.health.current_health -= damage
	def handle_mind(self):
		base_happiness = 50
		base_stress = 0
		base_sanity = 100
		#injuries
		if len(self.injuries) >= 1:
			if self.mind.happiness >= 50:
				base_happiness -= len(self.injuries) * 4
				base_stress -= len(self.injuries) * 4
			if self.mind.stress <= 50:
				base_stress += len(self.injuries) * 4
		#stamina
		if self.health.current_stamina >= 80:
			base_happiness += 10
		elif self.health.current_stamina <= 79 and self.health.current_stamina >= 60:
			base_stress += 10
			self.sleep -= 1
		elif self.health.current_stamina <= 59 and self.health.current_stamina >= 40:
			base_stress += 25
			base_happiness -= 10
			self.sleep -= 2
		elif self.health.current_stamina <= 39 and self.health.current_stamina  >= 15:
			base_stress += 45
			base_happiness -= 25
			self.sleep -= 4
		elif self.health.current_stamina <= 14:
			base_stress += 60
			base_happiness -= 40
			self.sleep -= 8

		#pain
                for injury in self.injuries:
        	        #cause pain
                	if injury.cause_pain >= 1:
                        	self.health.current_pain += (injury.cause_pain / 2)

		if self.health.current_pain <= 25:
			base_happiness -= 2
			base_stress += 3
		if self.health.current_pain >= 26 and self.health.current_pain <= 50:
			base_happiness -= 4
			base_stress += 7
		if self.health.current_pain >= 51 and  self.health.current_pain <= 75:
			base_happiness -= 10
			base_stress += 15
		if self.health.current_pain >= 75:
			base_happiness -= 20
			base_stress -= 30
		#bleeding
		base_happiness -= self.health.bleeding_rate * 2
                base_stress -= self.health.bleeding_rate * 2
		if self.health.current_blood <= 50:
			base_happiness -= 20
			base_stress += 25
                elif self.health.current_blood <= 25:
                        base_happiness -= 40
                        base_stress += 50
		#hunger and thirst
		if self.thirst <= -1:
			base_happiness -= 20
			base_stress += 20
		if self.hunger <= -1:
			base_happiness -= 15
			base_stress += 15

		#cold
		if self.health.body_temp <= -1 and self.health.body_temp >= -24:
                        base_happiness -= 20
                        base_stress += 20
                elif self.health.body_temp <= -25:
                        base_happiness -= 40
                        base_stress += 40
                #sleep
                if self.sleep <= -1:
                        base_happiness -= 20
                        base_stress += 20


		#drugs,withdrawls,cravings
		for drug in self.drugs:
			if drug.name == "Morphine" or drug.name == "Heroin":
				base_happiness += 30
				base_stress -= 30
				base_sanity -= 10
			if drug.name == "Cocaine" or drug.name == "Crack" or drug.name == "Speed":
				base_happiness += 30
				base_stress += 15
				base_sanity -= 20
			if drug.name == 'Cocaine withdrawl'or drug.name == 'Speed withdrawl':
				base_happiness -= 30
				base_stress += 20
				base_sanity -= 40
			elif drug.name == 'Opiate withdrawl':
				base_happiness -= 30
				base_stress += 25
				base_sanity -= 20
		#addictions

		if self.mind.addictions.opiates.addiction_level >= 1:
			base_stress += self.mind.addictions.opiates.addiction_level * 5
			base_happiness -= self.mind.addictions.opiates.addiction_level * 5
			base_sanity -= 5 * self.mind.addictions.opiates.addiction_level
			opiate_craving_roll = random.randint(1,10)
                elif self.mind.addictions.cocaine.addiction_level >= 1:
                        base_stress += self.mind.addictions.cocaine.addiction_level * 5
                        base_happiness -= self.mind.addictions.cocaine.addiction_level * 5
                        base_sanity -= 5 * self.mind.addictions.cocaine.addiction_level

                elif self.mind.addictions.speed.addiction_level >= 1:
                        base_stress += self.mind.addictions.speed.addiction_level * 5
                        base_happiness -= self.mind.addictions.speed.addiction_level * 5
                        base_sanity -= 5 * self.mind.addictions.speed.addiction_level

                #stress
                base_happiness -= self.mind.stress / 2
		if base_happiness >= 0:
			happy = 100 - base_happiness
		elif base_happiness >= 100:
			happy = 100
		elif base_happiness <= -1:
			happy = base_happiness * -1
			happy = happy + 100
		if base_stress >= 0:
			my_stress = 100 - base_stress
		elif base_stress <= -1:
			my_stress = base_stress * -1
			my_stress = my_stress + 100
		if happy >= 100:
			happy = happy - 100
                base_sanity -= self.mind.stress + (happy / 4) 
		base_sanity -= self.mind.trauma
		#trauma
		if self.mind.stress >= 50 or self.mind.happiness <= 0 or self.mind.sanity <= 10:
			self.mind.trauma += 1


		self.mind.stress = base_stress
		self.mind.happiness = base_happiness
		self.mind.sanity = base_sanity
		#handle blind
		blind_found = False
		for injury in self.injuries:
			if injury.name == "blind":
				injury.time_had += 60
				if injury.time_had >= injury.time_to_heal:
					injuries.remove(injury)
					self.combat_status.blind = False
					blind_found = True
		if blind_found == False and self.combat_status.blind == True:
			self.combat_status.blind = False
		#handle concussion
                concussion_found = False
                for injury in self.injuries:
                        if injury.name == "mild concussion" or injury.name == "severe concussion":
                                injury.time_had += 60
                                if injury.time_had >= injury.time_to_heal:
                                        self.injuries.remove(injury)
                                        self.combat_status.concussion = False
                                        concussion_found = True
                if concussion_found == False and self.combat_status.concussion == True:
                        self.combat_status.concussion = False

			
	
	def handle_drugs(self):
		for drug in self.drugs:
			if drug.time_to_wear_off <= 1:
				if drug.name == 'Morphine' or drug.name == 'Heroin':
					self.drugs.remove(drug)
					#self.mind.addictions.opiates.addiction_level += 1
					self.drugs.append(opiate_withdrawl)
				elif drug.name == 'Speed':
					self.drugs.remove(drug)
					self.drugs.append(speed_withdrawl)
					#self.mind.addictions.speed.addiction_level += 1
				elif drug.name == 'Crack' or drug.name == 'Cocaine':
					self.drugs.remove(drug)
					self.drugs.append(cocaine_withdrawl)
				else:
					self.drugs.remove(drug)
				self.health.current_pain = 0
				for injury in self.injuries:
                			#cause pain
                			if injury.cause_pain >= 1:
                        			target.health.current_pain += (injury.cause_pain / 2)


			elif drug.time_to_wear_off >= 2:
				drug.time_to_wear_off -= 1
	       		if drug.name == 'Morphine':
        	        	self.health.current_pain -= 50
        	        	if self.health.current_pain <= 0 and self.health.base_current_pain >= self.health.current_pain:
        	        	        self.health.current_pain = 0
                        if drug.name == 'Heroin':
                                self.health.current_pain -= 50
                                if self.health.current_pain <= 0 and self.health.base_current_pain >= self.health.current_pain:
                                        self.health.current_pain = 0
			#elif drug.name == 'Opiate withdrawl':
			#	self.health.current_pain += 15
			#	self.health.current_stamina -= 10
			#	if self.health.current_stamina <= 0:
			#		self.health.current_stamina = 0
				
        		elif drug.name == 'Speed':
        		        self.health.current_stamina += 50
        		        if self.health.current_stamina >= 100:
        		                self.health.current_stamina = 100

                        elif drug.name == 'Crack':
                                self.health.current_stamina += 50
                                if self.health.current_stamina >= 100:
                                        self.health.current_stamina = 100
                        elif drug.name == 'Cocaine':
                                self.health.current_stamina += 50
                                if self.health.current_stamina >= 100:
                                        self.health.current_stamina = 100
                        elif drug.name == 'Coffee':
                                self.health.current_stamina += 15
                                if self.health.current_stamina >= 100:
                                        self.health.current_stamina = 100
			
				#self.mind.happiness += random.randint(20,40)
			#if drug.name == 'Cocaine' or drug.name == 'Crack':
        	        #	drug_type = 'Cocaine'
			#	self.mind.addictions.cocaine.addiction_level += 1
        	        #elif drug.name == 'Heroin' or drug.name == 'Morphine':
        	        #        drug_type = 'Opiates'
			#	self.mind.addictions.heroin.addiction_level += 1
        	      	#elif drug.name == 'Speed' or drug.name == 'Meth':
        	        #        drug_type = 'Speed'
			#	self.mind.addictions.speed.addiction_level += 1
        	        #print drug_type     
		        #for addiction in self.mind.addictions:
        	        	#print addiction.name + " " + drug_type
        	         #       if addiction.name == drug_type:
        	          #      	print addiction.name + " " + drug_type
        	           #             addiction.times_used += 1
        	            #            roll = random.randint(1,10)
        	             #           roll += self.stats.willpower
        	              #          addiction.addiction_level += 1
                                #print drug_target.fname + " " + drug_target.lname + " got addicted to " + drug_type
	def can_walk(self):
		if self.health.current_stamina <= 0:
			self.combat_status.knocked_down = True
	def check_clothing_warmth(self):
		total_warmth = 0
		if self.headwear != None:
			if self.headwear.name != "None":
				if self.headwear.wet <= 4:
					total_warmth += self.headwear.warmth

                if self.facewear != None:
                        if self.facewear.name != "None":
				if self.facewear.wet <= 4:
                                	total_warmth += self.facewear.warmth
                if self.outfit != None:
                        if self.outfit.name != "None":
				if self.outfit.wet <= 4:
                                	total_warmth += self.outfit.warmth
                if self.outerwear != None:
                        if self.outerwear.name != "None":
                                total_warmth += self.outerwear.warmth
                if self.handwear != None:
                        if self.handwear.name != "None":
				if self.handwear.wet <= 4:
                                	total_warmth += self.handwear.warmth
                if self.legwear != None:
                        if self.legwear.name != "None":
				if self.legwear.wet <= 4:
                                	total_warmth += self.legwear.warmth
                if self.footwear != None:
                        if self.footwear.name != "None":
				if self.footwear.wet <= 4:
                                	total_warmth += self.footwear.warmth
                if self.armor != None:
                        if self.armor.name != "None":
                                total_warmth += self.armor.warmth
		return total_warmth

class Date_of_Birth:
	def __init__(self,day,month,year):
		self.day = day
		self.month = month
		self.year = year

class Health:
	def __init__(self, base_max, max_health, current_health,base_blood,max_blood,current_blood,bleeding_rate,base_pain,max_pain,
	current_pain,base_current_pain,base_stamina,current_stamina,max_stamina, body_temp,cold_rating):
		self.base_max = base_max
		self.max_health = max_health
		self.current_health = current_health
		
		self.base_blood = base_blood
		self.max_blood = max_blood
		self.current_blood = current_blood
		self.bleeding_rate = bleeding_rate

		self.base_pain = base_pain
		self.max_pain = max_pain
		self.current_pain = current_pain
		self.base_current_pain = base_current_pain

		self.base_stamina = base_stamina
		self.current_stamina = current_stamina
		self.max_stamina = max_stamina

		self.body_temp = body_temp
		self.cold_rating = cold_rating

class Mind:
	def __init__(self,happiness,stress,sanity,horny,addictions,trauma,morale):
		self.happiness = happiness
		self.stress = stress
		self.sanity = sanity
		self.horny = horny
		self.addictions = addictions
		self.trauma = trauma
		self.morale = morale

class Addictions:
	def __init__(self,cocaine,opiates,speed,caffeine,nicotine):
		self.cocaine = cocaine
		self.opiates = opiates
		self.speed = speed
		self.caffeine = caffeine
		self.nicotine = nicotine
class Addiction:
	def __init__(self,name,times_used,addiction_level,addictiveness,traits):
		self.name = name
		self.times_used = times_used
		self.addiction_level = addiction_level
		self.addictiveness = addictiveness
		self.traits = traits
#nicotine_addiction = Addiction('Nicotine',0,0,4)
#caffeine_addiction = Addiction('Caffeine',0,0,2)
#cocaine_addiction = Addiction('Cocaine',0,0,7)
#opiates_addiction = Addiction('Opiates',0,0,10)
#speed_addiction = Addiction('Speed',0,0,7)

#starting_addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction)

#organizations

class Organization:
	def __init__(self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid,month,rent_checked,debts,
		rent_amount,items_bought,members_killed,theft_from,members_attacked,members_recruited,theft_on_turf,killed_on_turf,members_kidnapped,gifts,missions_completed,missions_failed):
		self.name = name
		self.is_player = is_player
		self.footsoldiers = footsoldiers
		self.player_reputation = player_reputation

		self.hq = hq
		self.locations_owned = locations_owned
		self.power = power
		self.territory = territory

		self.rent_due = rent_due
		self.rent_paid = rent_paid
		self.month = month
		self.rent_checked = rent_checked
		self.debts = debts
		self.rent_amount = rent_amount

		self.items_bought = items_bought
		self.members_killed = members_killed
		self.theft_from = theft_from

		self.members_attacked = members_attacked
		self.members_recruited = members_recruited
		self.theft_on_turf = theft_on_turf
		self.killed_on_turf = killed_on_turf

		self.members_kidnapped = members_kidnapped
		self.gifts = gifts

		self.missions_completed = missions_completed
		self.missions_failed = missions_failed
	def check_reputation(self,player,world):
		items_bought_bonus = 0
		killed_penalty = 0
		theft_penalty = 0
		members_attacked_penalty = 0
		members_recruited_penalty = 0
		theft_on_turf_penalty = 0
		killed_on_turf_penalty = 0
		#bonuses
		if self.items_bought >= 10000:
			items_bought_bonus += self.items_bought / 500
		#penalties
		killed_penalty -= self.members_killed * 3

		if self.theft_from >= 100:
			theft_penalty -= self.theft_from / 100

		if self.members_attacked >= 1:
			members_attacked_penalty -= self.members_attacked

		if self.members_recruited >= 1:
			members_recruited_penalty = self.members_recruited

		if self.theft_on_turf >= 1000:
			theft_on_turf_penalty = self.theft_on_turf / 1000

		if self.killed_on_turf >= 1:
			killed_on_turf_penalty = self.killed_on_turf

		self.player_reputation = (items_bought_bonus + killed_penalty + theft_penalty + members_attacked_penalty + members_recruited_penalty + 
					theft_on_turf_penalty + killed_on_turf_penalty) / 5

#corporations

class Corporation:
	def __init__(self,name,industries,locations,debts,items_bought,members_killed,theft_from,members_attacked,members_recruited,theft_on_turf,killed_on_turf,members_kidnapped,gifts,player_reputation,missions_completed,missions_failed):
		self.name = name
		self.industries = industries
		self.locations = locations

		self.debts = debts
                self.items_bought = items_bought
                self.members_killed = members_killed
                self.theft_from = theft_from

                self.members_attacked = members_attacked
                self.members_recruited = members_recruited
                self.theft_on_turf = theft_on_turf
                self.killed_on_turf = killed_on_turf

                self.members_kidnapped = members_kidnapped
                self.gifts = gifts
		self.player_reputation = player_reputation
		self.missions_completed = missions_completed
		self.missions_failed = missions_failed
        def check_reputation(self,player,world):
                items_bought_bonus = 0
                killed_penalty = 0
                theft_penalty = 0
                members_attacked_penalty = 0
                members_recruited_penalty = 0
                theft_on_turf_penalty = 0
                killed_on_turf_penalty = 0
                #bonuses
                if self.items_bought >= 10000:
                        items_bought_bonus += self.items_bought / 500
                #penalties
                killed_penalty -= self.members_killed * 4
		#if self.members_killed >= 4:
		#	self.members_killed = self.members_killed / 4
                if self.theft_from >= 100:
                        theft_penalty -= self.theft_from / 100

                if self.members_attacked >= 1:
                        members_attacked_penalty -= self.members_attacked

                if self.members_recruited >= 1:
                        members_recruited_penalty = self.members_recruited

                if self.theft_on_turf >= 1000:
                        theft_on_turf_penalty = self.theft_on_turf / 1000

                if self.killed_on_turf >= 1:
                        killed_on_turf_penalty = self.killed_on_turf

                self.player_reputation = (items_bought_bonus + killed_penalty + theft_penalty + members_attacked_penalty + members_recruited_penalty + 
                                        theft_on_turf_penalty + killed_on_turf_penalty) / 5
#corporations


#tech companies
thetacom = Corporation('Thetacom',['Telecom'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
newgen_global = Corporation('NewGen',['Security','Big Data'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
facebook = Corporation('Facebook',['Social Media'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
twitter = Corporation('Twitter',['Social Media'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
aci_data = Corporation('ACI Data',['Big Data'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
google = Corporation('Google',['Big Data','Security','Health'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  

tech_corps = [thetacom,newgen_global,facebook,twitter,aci_data,google]

#real estate
united_solidarity = Corporation('United Solidarity',['Health', 'Big Data'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
chh = Corporation('CHH',['Security', 'Big Data'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  
gcw_global = Corporation('GCW Global',['Security'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)  

real_estate_corps = [united_solidarity,chh,gcw_global]

#food
quikmart = Corporation('Quik-e Mart',['Food'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
starfucks = Corporation('Starfucks',['Food'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
pizza_corp = Corporation('Pizza Corp',['Food'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
mcshits = Corporation('McShits',['Food'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)

food_corps = [quikmart,starfucks,pizza_corp,mcshits]

#weapons
technoco = Corporation('Technoco',['weapons'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
united_tactical = Corporation('United Tactical',['weapons'],[],[],0,0,0,0,0,0,0,0,0,0,0,0)
weapons_corps = [technoco,united_tactical]


#health corps

#health_corps = [goodgle,united_solidarity]


corps = []
for corp in real_estate_corps:
	corps.append(corp)
for corp in tech_corps:
	corps.append(corp)
for corp in food_corps:
        corps.append(corp)
for corp in weapons_corps:
        corps.append(corp)

class Loan:
	def __init__(self,owed_to,loan_amount,amount_owed,time_due,min_rep):
		self.owed_to = owed_to
		self.loan_amount = amount
		self.amount_owed = amount_owed
		self.time_due = time_due
		self.min_rep = min_rep

#due time
#example loan:     Loan('Crankensteins',10000,due_time,0) 


#Broker
class Broker:
	def __init__(self,npc,factions,min_fame,jobs,player_reputation,missions_completed,missions_failed,guards,affiliation):
		self.npc = npc
		self.factions = factions
		self.min_fame = min_fame
		self.jobs = jobs
		self.player_reputation = player_reputation
		self.missions_completed = missions_completed
		self.missions_failed = missions_failed
		self.guards = guards
		self.affiliation = affiliation
class Job:
	def __init__(self,name,type,employer,mission,reward,broker,broker_location):
		self.name = name
		self.type = type
		self.employer = employer
		self.mission = mission
		self.reward = reward
		self.broker = broker
		self.broker_location = broker_location
#Mission types
class Assassination:
	def __init__(self,target,deadline,is_complete,target_location):
		self.target = target
		self.deadline = deadline
		self.is_complete = is_complete
		self.target_location = target_location
class Delivery:
	def __init__(self,item,deadline,target,target_location,is_complete,num_required):
		self.item = item
		self.deadline = deadline
		self.target = target
		self.target_location = target_location
		self.is_complete = is_complete
		self.num_required = num_required
class Territory:
	def __init__(self,top_left_x,top_left_y,bottom_right_x,bottom_right_y):
		self.top_left_x = top_left_x
		self.top_left_y = top_left_y
		self.bottom_right_x = bottom_right_x
		self.bottom_right_y = bottom_right_y

class Footsoldier:
	def __init__(self,npc,orders,home):
		self.npc = npc
		self.orders = orders
		self.home = home
class Permissions:
	def __init__(self,can_eat,can_drink,can_buy_food,can_buy_drink,can_use_drugs,can_rest,can_sleep):
		self.can_eat = can_eat
		self.can_drink = can_drink
		self.can_buy_food = can_buy_food
		self.can_buy_drink = can_buy_drink
		self.can_use_drugs = can_use_drugs
		self.can_rest = can_rest
		self.can_sleep = can_sleep
default_permissions = Permissions(True,True,False,False,False,True,True)

start_health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100,50,5)

class Stats:
	def __init__(self, strength, dexterity, intelligence, willpower, charisma, base_strength, base_dexterity, base_intelligence,base_willpower, 
	base_charisma):
		self.strength = strength
		self.dexterity = dexterity
		self.intelligence = intelligence
		self.willpower = willpower
		self.charisma = charisma
		self.base_strength = base_strength
		self.base_dexterity = base_dexterity
		self.base_intelligence = base_intelligence
		self.base_willpower = base_willpower
		self.base_charisma = base_charisma
		
class Skills:
	def __init__(self, brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival,throw, torture, trivia,driving,blade,blunt):
		self.brawl = brawl
		self.computers = computers
		self.dodge = dodge 
		self.disguise = disguise
		self.etiquette = etiquette
		self.explosives = explosives
		self.first_aid = first_aid
		self.investigate = investigate
		self.leadership = leadership
		self.lying = lying
		self.negotiate = negotiate
		self.rifle = rifle
		self.pickpocket = pickpocket
		self.persuasion = persuasion
		self.pistol = pistol
		self.security = security
		self.seduction = seduction
		self.stealth = stealth
		self.shotgun = shotgun
		self.streetwise = streetwise
		self.survival = survival
		self.throw = throw
		self.torture = torture
		self.trivia = trivia
		self.driving = driving
		self.blade = blade
		self.blunt = blunt


class Skills_XP:
        def __init__(self, brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia):
                self.brawl = brawl
                self.computers = computers
                self.dodge = dodge 
                self.disguise = disguise
                self.etiquette = etiquette
                self.explosives = explosives
                self.first_aid = first_aid
                self.investigate = investigate
                self.leadership = leadership
                self.lying = lying
                self.negotiate = negotiate
                self.rifle = rifle
                self.pickpocket = pickpocket
                self.persuasion = persuasion
                self.pistol = pistol
                self.security = security
                self.seduction = seduction
                self.stealth = stealth
                self.shotgun = shotgun
                self.streetwise = streetwise
                self.throw = throw
                self.torture = torture
                self.trivia = trivia

		
class Stat_Mod:
	def __init__(self, stat, mod):
		self.stat = stat
		self.mod = mod
class Skill_Mod:
        def __init__(self, skill, mod):
                self.skill = skill
                self.mod = mod


class Temporary_Status:
	def __init__(self,type,is_true,num_turns,max_turns):
		self.type = type
		is_true = is_true
		num_turns = num_turns
		max_turns = max_turns

class Combat_Status:
	def __init__(self, knocked_down,stunned,defending,blind,unconscious,on_fire,concussion,gone_insane,turns_stunned,max_stunned,turns_blind,max_blind,
			turns_on_fire,max_on_fire,tied_up,gagged,turns_unconscious,turns_concussion,turns_insane,max_unconscious,max_concussion,max_insane):
		self.knocked_down = knocked_down
		self.stunned = stunned
		self.defending = defending

		self.blind = blind
		self.unconscious = unconscious
		self.on_fire = on_fire
		self.concussion = concussion
		self.gone_insane = gone_insane

		self.turns_stunned = turns_stunned
		self.max_stunned = max_stunned
		self.turns_blind = turns_blind
		self.max_blind = max_blind
		self.turns_on_fire = turns_on_fire
		self.max_on_fire = max_on_fire

		self.tied_up = tied_up
		self.gagged = gagged
		
		self.turns_unconscious = turns_unconscious
		self.turns_concussion = turns_concussion
		self.turns_insane = turns_insane

		self.max_unconscious = max_unconscious
		self.max_concussion = max_concussion
		self.max_insane = max_insane
		
#health mods
class Health_Mod:
        def __init__(self, name, mod):
                self.name = name
                self.mod = mod

reduce_pain = Health_Mod('reduce pain',-50)
gain_stamina = Health_Mod('gain stamina',50)

lower_max_health = Health_Mod('lower max health',10)

def health_mod(target,health_mod,value):
	if health_mod.name == 'reduce pain':
		target.health.current_pain -= 50
		if target.health.current_pain <= 0:
			target.health.current_pain = 0
        elif health_mod.name == 'gain stamina':
                target.health.current_stamina += 50
                if target.health.current_stamina >= 100:
                        target.health.current_stamina = 100
        elif health_mod.name == 'lower max health':
        	base = value / 2
        	value = random.randint(base,value)
                target.health.max_health -= value
                if target.health.max_health <= 0:
			print 'skip'

# I N J U R I E S

class Injury:
	def __init__(self, name, location,description, stat_mods, skill_mods, health_mods,can_heal,time_had,time_to_heal,damage_bonus,cost_to_heal,
	cause_bleeding,cause_pain,cause_stamina_loss,color):
		self.name = name
		self.location = location
		self.description = description
		self.stat_mods = stat_mods
		self.skill_mods = skill_mods
		self.health_mods = health_mods

		self.can_heal = can_heal
		self.time_had = time_had
		self.time_to_heal = time_to_heal
		self.damage_bonus = damage_bonus
		self.cost_to_heal = cost_to_heal
		
		self.cause_bleeding = cause_bleeding
		self.cause_pain = cause_pain
		self.cause_stamina_loss = cause_stamina_loss

		self.color = color
#bear_mace

bear_maced = Injury("blind","eyes", "'s eyes",[],[],lower_max_health,True,0,60,0,100,0,35,0,libtcod.yellow)
mild_concussion = Injury("mild concussion","head", "'s head",[],[],lower_max_health,True,0,120,0,100,0,35,0,libtcod.yellow)
severe_concussion = Injury("severe concussion","head", "'s head",[],[],lower_max_health,True,240,60,0,100,0,35,0,libtcod.yellow)


#bruises


bruised_groin = Injury("bruise","groin", "'s groin was bruised",[],[],lower_max_health,True,0,48,10,100,0,35,25,libtcod.grey)
bruised_torso = Injury("bruise","torso", "'s torso was bruised",[],[],lower_max_health,True,0,48,4,100,0,20,25,libtcod.grey)
bruised_neck = Injury("bruise","neck", "'s neck was bruised",[],[],lower_max_health,True,0,48,10,100,0,25,25,libtcod.grey)
bruised_face = Injury("bruise","face", "'s face was bruised",[],[],lower_max_health,True,0,48,10,100,0,15,15,libtcod.grey)
bruised_left_arm = Injury("bruise","left arm", "'s left arm was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10,libtcod.grey)
bruised_right_arm = Injury("bruise","right arm", "'s right arm was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10,libtcod.grey)
bruised_left_leg = Injury("bruise","left leg", "'s left leg was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10,libtcod.grey)
bruised_right_leg = Injury("bruise","right leg", "'s right leg was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10,libtcod.grey)

bruises = [bruised_groin,bruised_torso,bruised_neck,bruised_face,bruised_left_arm,bruised_right_arm,bruised_left_leg,bruised_right_leg]

#maimed

maimed_groin = Injury("maimed","groin", "'s groin was maimed",[],[],lower_max_health,True,0,48,20,100,5,60,35,libtcod.red)
maimed_torso = Injury("maimed","torso", "'s torso was maimed",[],[],lower_max_health,True,0,48,8,100,5,40,50,libtcod.red)
maimed_neck = Injury("maimed","neck", "'s neck was maimed",[],[],lower_max_health,True,0,48,10,100,16,40,50,libtcod.red)
maimed_face = Injury("maimed","face", "'s face was maimed",[],[],lower_max_health,True,0,48,10,100,10,45,55,libtcod.red)
maimed_left_arm = Injury("maimed","left arm", "'s left arm was maimed",[],[],lower_max_health,True,0,48,8,100,5,40,50,libtcod.red)
maimed_right_arm = Injury("maimed","right arm", "'s right arm was maimed",[],[],lower_max_health,True,0,48,8,100,5,40,50,libtcod.red)
maimed_left_leg = Injury("maimed","left leg", "'s left leg was maimed",[],[],lower_max_health,True,0,48,8,100,5,30,50,libtcod.red)
maimed_right_leg = Injury("maimed","right leg", "'s right leg was maimed",[],[],lower_max_health,True,0,48,8,100,5,30,50,libtcod.red)

maimings = [maimed_groin,maimed_torso,maimed_neck,maimed_face,maimed_left_arm,maimed_right_arm,maimed_left_leg,maimed_right_leg]


#mangled

mangled_groin = Injury("mangled","groin", "'s groin was mangled",[],[],lower_max_health,True,0,48,15,100,3,60,35,libtcod.red)
mangled_torso = Injury("mangled","torso", "'s torso was mangled",[],[],lower_max_health,True,0,48,9,100,3,40,50,libtcod.red)
mangled_neck = Injury("mangled","neck", "'s neck was mangled",[],[],lower_max_health,True,0,48,10,100,15,40,50,libtcod.red)
mangled_face = Injury("mangled","face", "'s face was mangled",[],[],lower_max_health,True,0,48,10,100,6,45,55,libtcod.red)
mangled_left_arm = Injury("mangled","left arm", "'s left arm was mangled",[],[],lower_max_health,True,0,48,6,100,3,40,50,libtcod.red)
mangled_right_arm = Injury("mangled","right arm", "'s right arm was mangled",[],[],lower_max_health,True,0,48,6,100,3,40,50,libtcod.red)
mangled_left_leg = Injury("mangled","left leg", "'s left leg was mangled",[],[],lower_max_health,True,0,48,6,100,3,30,50,libtcod.red)
mangled_right_leg = Injury("mangled","right leg", "'s right leg was mangled",[],[],lower_max_health,True,0,48,6,100,3,30,50,libtcod.red)

manglings = [mangled_groin,mangled_torso,mangled_neck,mangled_face,mangled_left_arm,mangled_right_arm,mangled_left_leg,mangled_right_leg]

#fractures

fractured_skull = Injury("fracture","skull", "'s skull was fractured",[],[],lower_max_health,True,0,48,120,2000,0,45,40,libtcod.red)
broken_jaw = Injury("broken","jaw", "'s jaw was broken",[],[],lower_max_health,True,0,48,20,800,0,25,30,libtcod.red)

broken_ribs = Injury("broken","ribs", "'s ribs were broken",[],[],lower_max_health,True,0,48,20,800,0,25,30,libtcod.dark_yellow)
broken_neck = Injury("broken","neck", "'s neck was broken",[],[],lower_max_health,True,0,48,120,2000,0,45,40,libtcod.dark_yellow)
broken_right_collarbone = Injury("broken","right collarbone", "'s right collarbone was broken",[],[],lower_max_health,True,0,48,35,500,0,30,10,libtcod.dark_yellow)
broken_left_collarbone = Injury("broken","left collarbone", "'s left collarbone was broken",[],[],lower_max_health,True,0,48,35,500,0,30,10,libtcod.dark_yellow)
broken_left_arm = Injury("broken","left arm", "'s left arm was broken",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
broken_right_arm = Injury("broken","right arm", "'s right arm was broken",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
broken_left_leg = Injury("broken","left leg", "'s left leg was broken",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
broken_right_leg = Injury("broken","right leg", "'s right leg was broken",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)


fractured_left_arm = Injury("fracture","left arm", "'s left arm was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
fractured_right_arm = Injury("fracture","right arm", "'s right arm was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
fractured_left_leg = Injury("fracture","left leg", "'s left leg was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)
fractured_right_leg = Injury("fracture","right leg", "'s right leg was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10,libtcod.dark_yellow)

fractures = [fractured_skull,broken_ribs,broken_neck,broken_right_collarbone,broken_left_collarbone,fractured_left_arm,
	fractured_right_arm, fractured_left_leg, fractured_right_leg,broken_left_arm,broken_right_arm,broken_left_leg,
	broken_right_leg,broken_jaw]

#minor cuts

minor_cut_head = Injury("cut","head","'s head was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)
minor_cut_torso = Injury("cut","torso","'s torso was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)
minor_cut_neck = Injury("cut","neck","'s neck was cut",[],[],lower_max_health,False,0,48,16,900,3,10,5,libtcod.light_red)
minor_cut_face = Injury("cut","face","'s face was cut",[],[],lower_max_health,False,0,48,12,400,2,10,5,libtcod.light_red)
minor_cut_left_arm = Injury("cut","left arm","'s left arm was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)
minor_cut_right_arm = Injury("cut","right arm","'s right arm was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)
minor_cut_left_leg = Injury("cut","left leg","'s left leg was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)
minor_cut_right_leg = Injury("cut","right_leg","'s right leg was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5,libtcod.light_red)

minor_cuts = [minor_cut_head,minor_cut_torso,minor_cut_neck,minor_cut_face,minor_cut_left_arm,minor_cut_right_arm,minor_cut_left_leg,minor_cut_right_leg]


#major cuts

major_cut_head = Injury("cut","head","'s head was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
major_cut_torso = Injury("cut","torso","'s torso was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
major_cut_neck = Injury("cut","neck","'s throat was badly cut",[],[],lower_max_health,False,0,48,32,900,4,20,25,libtcod.red)
major_cut_face = Injury("cut","face","'s face was badly cut",[],[],lower_max_health,False,0,48,24,400,4,20,25,libtcod.red)
major_cut_left_arm = Injury("cut","left arm","'s left arm was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
major_cut_right_arm = Injury("cut","right arm","'s right arm was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
major_cut_left_leg = Injury("cut","left leg","'s left leg was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
major_cut_right_leg = Injury("cut","right leg","'s right leg was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)

major_cuts = [major_cut_head,major_cut_torso,major_cut_neck,major_cut_face,major_cut_left_arm,major_cut_right_arm,major_cut_left_leg,major_cut_right_leg]

#slashes

slash_head = Injury("slash","head","'s head was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
slash_torso = Injury("slash","torso","'s torso was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
slash_neck = Injury("slash","neck","'s throat was slashed",[],[],lower_max_health,False,0,48,32,900,4,20,25,libtcod.red)
slash_face = Injury("slash","face","'s face was slashed",[],[],lower_max_health,False,0,48,24,400,4,20,25,libtcod.red)
slash_left_arm = Injury("slash","left arm","'s left arm was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
slash_right_arm = Injury("slash","right arm","'s right arm was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
slash_left_leg = Injury("slash","left leg","'s left leg was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)
slash_right_leg = Injury("slash","right leg","'s right leg was slashed",[],[],lower_max_health,False,0,48,16,400,4,20,25,libtcod.red)

slashes = [slash_head,slash_torso,slash_neck,slash_face,slash_left_arm,slash_right_arm,slash_left_leg,slash_right_leg]




#severed limbs

severed_head = Injury("severed","head","'s head was severed",[],[],lower_max_health,False,0,48,16,400,10,200,100,libtcod.dark_red)
severed_left_arm = Injury("severed","left arm","'s left arm was severed",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)
severed_right_arm = Injury("severed","right arm","'s right arm was severed!",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)
severed_left_leg = Injury("severed","left leg","'s left leg was severed",[],[],lower_max_health,False,0,48,16,4000,6,20,50,libtcod.dark_red)
severed_right_leg = Injury("severed","right leg","'s right leg was severed",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)

severed_limbs = [severed_head,severed_left_arm,severed_right_arm,severed_left_leg,severed_right_leg]


#blown off limbs

blown_off_head = Injury("blown off","head","'s head was blown off",[],[],lower_max_health,False,0,48,16,400,10,200,100,libtcod.dark_red)
blown_off_left_arm = Injury("blown_off","left arm","'s left arm was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)
blown_off_right_arm = Injury("blown off","right arm","'s right arm was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)
blown_off_left_leg = Injury("blown off","left leg","'s left leg was blown off",[],[],lower_max_health,False,0,48,16,4000,6,20,50,libtcod.dark_red)
blown_off_right_leg = Injury("blown off","right leg","'s right leg was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50,libtcod.dark_red)

blown_off_limbs = [blown_off_head,blown_off_left_arm,blown_off_right_arm,blown_off_left_leg,blown_off_right_leg]


#stab

stab_torso = Injury("stab wound","torso"," was stabbed in the torso",[],[],lower_max_health,False,0,48,15,1000,10,30,30,libtcod.dark_red)
stab_neck = Injury("stab wound","neck"," was stabbed in the neck",[],[],lower_max_health,False,0,48,90,1000,10,45,60,libtcod.dark_red)
stab_face = Injury("stab wound","face", "was stabbed in the face",[],[],lower_max_health,False,0,48,30,1000,10,45,30,libtcod.dark_red)
stab_left_arm = Injury("stab wound","left arm"," was stabbed in the left arm",[],[],lower_max_health,False,0,48,15,1000,10,30,30,libtcod.dark_red)
stab_right_arm = Injury("stab wound","right arm"," was stabbed in the right arm",[],[],lower_max_health,False,0,48,15,1000,10,30,30,libtcod.dark_red)
stab_left_leg = Injury("stab wound","left leg","was stabbed in the left leg",[],[],lower_max_health,False,0,48,15,1000,10,30,30,libtcod.dark_red)
stab_right_leg = Injury("stab wound","right leg"," was stabbed in the right leg",[],[],lower_max_health,False,0,48,15,1000,10,30,30,libtcod.dark_red)

stab_wounds = [stab_torso,stab_neck,stab_face,stab_left_arm,stab_right_arm,stab_left_leg,stab_right_leg]




#9mm
head_9mm = Injury("gunshot wound","head"," was shot in the head",[],[],lower_max_health,False,0,48,60,1200,6,50,40,libtcod.dark_red)
torso_9mm = Injury("gunshot wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,48,35,1200,6,40,20,libtcod.dark_red)
neck_9mm = Injury("gunshot shot","neck"," was shot in the neck",[],[],lower_max_health,False,0,48,60,3000,6,45,30,libtcod.dark_red)
face_9mm = Injury("gunshot wound","face"," was shot in the face",[],[],lower_max_health,False,0,48,60,3200,6,45,30,libtcod.dark_red)
left_arm_9mm = Injury("gunshot wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,48,30,800,3,30,20,libtcod.dark_red)
right_arm_9mm = Injury("gunshot wound","right arm"," was shot in the right arm,",[],[],lower_max_health,False,0,48,30,800,3,30,20,libtcod.dark_red)
left_leg_9mm = Injury("gunshot wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,48,30,800,3,30,20,libtcod.dark_red)
right_leg_9mm = Injury("gunshot wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,48,30,800,3,30,20,libtcod.dark_red)

shot_9mm = [head_9mm,torso_9mm,neck_9mm,face_9mm,left_arm_9mm,right_arm_9mm,left_leg_9mm,right_leg_9mm]



#12 gauge shotgun

torso_12g = Injury("shotgun wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,48,40,1100,6,45,40,libtcod.dark_red)
face_12g = Injury("shotgun wound","face"," was shot in the face",[],[],lower_max_health,False,0,48,80,4000,8,45,45,libtcod.dark_red)
left_arm_12g = Injury("shotgun wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,48,40,1100,5,30,20,libtcod.dark_red)
right_arm_12g = Injury("shotgun wound","right arm"," was shot in the right arm",[],[],lower_max_health,False,0,48,40,1100,5,30,20,libtcod.dark_red)
left_leg_12g = Injury("shotgun wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,48,40,1100,5,30,20,libtcod.dark_red)
right_leg_12g = Injury("shotgun wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,48,40,1100,5,30,20,libtcod.dark_red)

shot_12g = [torso_12g,face_12g,left_arm_12g,right_arm_12g,left_leg_12g,right_leg_12g]

#ak47

ak47_torso = Injury("gunshot wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,0,55,700,6,50,50,libtcod.dark_red)
ak47_face = Injury("gunshot wound","face"," was shot in the face",[],[],lower_max_health,False,0,0,75,2700,6,50,50,libtcod.dark_red)
ak47_left_arm = Injury("gunshot wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,0,45,700,4,35,20,libtcod.dark_red)
ak47_right_arm = Injury("gunshot wound","right arm"," was shot in the right arm",[],[],lower_max_health,False,0,0,45,700,4,35,20,libtcod.dark_red)
ak47_left_leg = Injury("gunshot wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,0,45,700,4,35,20,libtcod.dark_red)
ak47_right_leg = Injury("gunshot wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,0,45,700,4,35,20,libtcod.dark_red)

shot_ak47 = [ak47_torso,ak47_face,ak47_left_arm,ak47_right_arm,ak47_left_leg,ak47_right_leg]

#burns
burn_torso = Injury("burn","torso"," 's torso was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)
burn_face = Injury("burn","face"," 's face was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)
burn_right_arm = Injury("burn","right arm"," 's torso was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)
burn_left_arm = Injury("burn","left arm"," 's torso was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)
burn_right_leg = Injury("burn","right leg"," 's right leg was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)
burn_left_leg = Injury("burn","left leg"," 's left leg was burned",[],[],lower_max_health,False,0,0,30,500,0,20,20,libtcod.dark_orange)

burns = [burn_torso,burn_face,burn_right_arm,burn_left_arm,burn_right_leg,burn_left_leg]




class Want:
	def __init__(self,name,type,wear_off,time_had):
		self.name = name
		self.type = type
		self.wear_off = wear_off
		self.time_had = time_had

craving_cocaine = Want('Craving cocaine','want',180,0)
craving_opiates = Want('Craving opiates','want',180,0)
craving_speed = Want('Craving speed','want',180,0)


#vehicles
class Vehicle:
	def __init__(self,name,item_type,can_loot,base_value,driver,speed,motor,passengers,max_passengers):
		self.name = name
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
		self.driver = driver
		self.speed = speed
		self.motor = motor
		self.passengers = passengers
		max_passengers = max_passengers

bmx_bike = Vehicle('BMX bike','vehicle',True,600,None,12,False,[],1)
mountain_bike = Vehicle('Mountain bike','vehicle',True,750,None,17,False,[],0)
shopping_cart = Vehicle('Shopping cart','vehicle',True,50,None,1,False,[],1)

#weapons and ammo
class Weapon:
	def __init__(self,name,weapon_type, damage, max_condition, condition,item_type,can_loot,base_value,needs_ammo,ammo,has_melee,melee,has_fire_modes,fire_modes,current_fire_mode,type_ammo):
		self.name = name
		self.weapon_type = weapon_type
		self.damage = damage
		self.max_condition = max_condition
		self.condition = condition
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
		self.needs_ammo = needs_ammo
		self.ammo = ammo
		self.has_melee = has_melee
		self.melee = melee
		self.has_fire_modes = has_fire_modes
		self.fire_modes = fire_modes
		self.current_fire_mode = current_fire_mode
		self.type_ammo = type_ammo
class Ammo:
	def __init__(self,name,item_type,can_loot,base_value,max_rounds,current_rounds,value,is_clip,type):
		self.name = name
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
		self.max_rounds = max_rounds
		self.current_rounds = current_rounds
		self.value = value
		self.is_clip = is_clip
		self.type = type
#ammo
pistol_9mm_ammo = Ammo('9mm clip','ammo',True,150,15,15,100,True,"9mm")
shotgun_12g_ammo = Ammo('12g clip','ammo',True,200,5,5,90,True,"12g")
ak47_ammo = Ammo('AK47 clip','ammo',True,300,30,30,250,True,"AK47")
uzi_ammo = Ammo('Uzi clip','ammo',True,320,32,30,300,True,"Uzi")

molotov_ammo = Ammo('Molotov ammo','ammo',True,80,6,6,30,False,"Molotov")
shuriken_ammo = Ammo('Shuriken ammo','ammo',True,100,8,8,100,False,"Shuriken")

#empty ammo
pistol_9mm_ammo_empty = Ammo('9mm clip','ammo',True,0,0,0,0,True,"9mm")
shotgun_12g_ammo_empty = Ammo('12g clip','ammo',True,0,0,0,0,True,"12g")
ak47_ammo_empty = Ammo('AK47 clip','ammo',True,0,0,0,0,True,"AK47")
uzi_ammo_empty = Ammo('Uzi clip','ammo',True,0,0,0,0,True,"Uzi")

molotov_ammo_empty = Ammo('Molotov ammo','ammo',True,0,0,0,0,False,"Molotov")
shuriken_ammo_empty = Ammo('Shuriken ammo','ammo',True,0,0,0,0,False,"Shuriken")



#brawl
punch = Weapon("Punch",'brawl', 10,5,5,'weapon',True,0,False,None,False,None,False,[],'none',None)
brass_knuckles = Weapon("Brass knuckles",'brawl', 20,5,5,'weapon',True,80,False,None,False,None,False,[],'none',None)

#blunt
crowbar = Weapon("Crowbar",'blunt', 15,5,5,'weapon',True,30,False,None,False,None,False,[],'none',None)
shovel = Weapon("Shovel",'blunt', 10,5,5,'weapon',True,35,False,None,False,None,False,[],'none',None)
baseball_bat = Weapon("Baseball Bat", "blunt",20,5,5,'weapon',True,25,False,None,False,None,False,[],'none',None)

#blades
knife = Weapon("Knife", "blade",15,5,5,'weapon',True,25,False,None,False,None,False,[],'none',None)
sword = Weapon("Sword", "blade",25,5,5,'weapon',True,600,False,None,False,None,False,[],'none',None)
machete = Weapon("Machete", "blade",20,5,5,'weapon',True,120,False,None,False,None,False,[],'none',None)

#gun melee attacks
pistol_9mm_melee = Weapon("9mm Pistol(Melee)", "brawl", 8,5,5,'weapon',True,450,False,None,False,None,False,[],'none',None)
shotgun_12g_melee = Weapon("12g Shotgun(Melee)", "brawl", 9,5,5,'weapon',True,400,False,None,False,None,False,[],'none',None)
uzi_melee = Weapon("Uzi(Melee)", "pistol",6,5,5,'brawl',True,1500,False,None,False,None,False,[],'none',None)
ak47_melee = Weapon("AK-47(Melee)", "rifle",11,5,5,'brawl',True,2500,False,None,False,None,False,[],'none',None)

#guns
pistol_9mm = Weapon("9mm Pistol", "pistol", 25,5,5,'weapon',True,450,True,pistol_9mm_ammo,True,pistol_9mm_melee,False,[],'none',"9mm")
shotgun_12g = Weapon("12g Shotgun", "shotgun", 40,5,5,'weapon',True,400,True,shotgun_12g_ammo,True,shotgun_12g_melee,False,[],'none',"12g")
uzi = Weapon("Uzi", "pistol",30,5,5,'weapon',True,1500,True,uzi_ammo,True,uzi_melee,True,['single','burst','auto'],'single',"Uzi")
ak47 = Weapon("AK-47", "rifle",35,5,5,'weapon',True,2500,True,ak47_ammo,True,ak47_melee,True,['single','burst','auto'],'single',"AK47")

#throwing weapons
molotov = Weapon("Molotov", "throw",15,5,5,'weapon',True,15,True,molotov_ammo,True,punch,False,[],'none',"Molotov")
shuriken = Weapon("Shuriken", "throw",15,5,5,'weapon',True,95,True,shuriken_ammo,True,punch,False,[],'none',"Shuriken")

#tools
bear_mace = Weapon("Bear mace", "tool",0,5,5,'weapon',True,60,False,None,True,punch,False,[],'none',"Bear mace")
flashbang = Weapon("Flashbang", "tool",0,5,5,'weapon',True,140,False,None,True,punch,False,[],'none',"Flashbang")


class Attack:
	def __init__self(self, type, weapon, attack_mod, injury_inficted):
		self.type = type
		self.weapon = weapon
		self.attack_mod = attack_mod
		self.injury_inflicted = injury_inflicted
class Clothing_Properties:
	def __init__(self,damage,blood,wet,dirty,body_odor,warmth):
		self.damage = damage
		self.blood = blood
		self.wet = wet
		self.dirty = dirty
		self.body_odor = body_odor
		self.warmth = warmth
default_properties = Clothing_Properties(0,0,0,0,0,0)
#outfits
class Outfit:
	def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
		self.name = name
		self.outfit_type = outfit_type
		self.defense = defense
		self.max_condition = max_condition 
		self.condition = condition
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
		self.waterproof = waterproof


class Headwear:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Eyewear:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Facewear:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Hands:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Legs:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Feet:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
		self.properties =properties
                self.waterproof = waterproof

class Armor:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof


class Outerwear:
        def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value,damage,blood,wet,dirty,body_odor,warmth,waterproof):
                self.name = name
                self.outfit_type = outfit_type
                self.defense = defense
                self.max_condition = max_condition 
                self.condition = condition
                self.item_type = item_type
                self.can_loot = can_loot
                self.base_value = base_value
                self.damage = damage
                self.blood = blood
                self.wet = wet
                self.dirty = dirty
                self.body_odor = body_odor
                self.warmth = warmth
                self.waterproof = waterproof



#headwear
no_headwear = Headwear("None", "None",1,5,5,'headwear',True,0,0,0,0,0,0,0,0)

headband = Headwear("Headband", "Headband",1,5,5,'headwear',True,15,0,0,0,0,0,0,1)
baseball_cap = Headwear("Baseball cap", "Baseball cap",1,5,5,'headwear',True,45,0,0,0,0,0,0,2)
dad_hat = Headwear("Dad hat", "Dad hat",1,5,5,'headwear',True,35,0,0,0,0,0,1,2)
toque = Headwear("Toque", "Toque",1,5,5,'headwear',True,20,0,0,0,0,0,4,2)
beret = Headwear("Beret", "Beret",1,5,5,'headwear',True,20,0,0,0,0,0,1,1)
red_beret = Headwear("Red beret", "Red beret",1,5,5,'headwear',True,20,0,0,0,0,0,1,1)
fedora = Headwear("Fedora", "Fedora",1,5,5,'headwear',True,60,0,0,0,0,0,1,2)

army_hat = Headwear("Army hat", "Army hat",1,5,5,'headwear',True,20,0,0,0,0,0,1,2)

bicycle_helmet = Headwear("Bicycle helmet", "Bicycle helmet",4,5,5,'headwear',True,50,0,0,0,0,0,0,2)
army_helmet = Headwear("Army helmet", "Army helmet",6,5,5,'headwear',True,100,0,0,0,0,0,3,5)
cowboy_hat = Headwear("Cowboy hat", "Cowboy hat",1,5,5,'headwear',True,100,0,0,0,0,0,0,2)

cat_ears = Headwear("Cat ears", "Cat ears",1,5,5,'headwear',True,100,0,0,0,0,0,0,0)


headwear_types = [headband,baseball_cap,dad_hat,toque,cowboy_hat]

#eyewear
no_eyewear = Eyewear("None", "None",0,5,5,'eyewear',True,0,0,0,0,0,0,0,0)

sunglasses = Eyewear("Sunglasses", "Sunglasses",0,5,5,'eyewear',True,30,0,0,0,0,0,0,0)

#facewear
no_facewear = Facewear("None", "None",1,5,5,'facewear',True,0,0,0,0,0,0,0,0)
black_facemask = Facewear("Black facemask", "Black facemask",1,5,5,'facewear',True,15,0,0,0,0,0,0,2)
red_facemask = Facewear("Red facemask", "Red facemask",1,5,5,'facewear',True,15,0,0,0,0,0,0,2)


balaclava = Facewear("Balaclava", "Balaclava",1,5,5,'facewear',True,15,0,0,0,0,0,3,3)
clown_mask = Facewear("Clown mask", "Clown mask",2,5,5,'facewear',True,80,0,0,0,0,0,0,1)
anonymous_mask = Facewear("Anonymous mask", "Anonymous mask",2,5,5,'facewear',True,80,0,0,0,0,0,0,1)

skull_mask = Facewear("Skull mask", "Skull mask",1,5,5,'facewear',True,15,0,0,0,0,0,3,3)


#hands
no_handwear = Hands("None", "None",1,5,5,'handwear',True,0,0,0,0,0,0,0,0)
fingerless_gloves = Hands("Fingerless gloves", "Black glove",1,5,5,'handwear',True,10,0,0,0,0,0,1,2)
black_gloves = Hands("Black gloves", "Black glove",1,5,5,'handwear',True,10,0,0,0,0,0,2,2)
leather_gloves = Hands("Leather gloves", "Leather glove",2,5,5,'handwear',True,50,0,0,0,0,0,2,4)

#legs
no_legwear = Legs("None", "None",1,5,5,'legwear',True,0,0,0,0,0,0,0,0)

shorts = Legs("Shorts", "Shorts",1,1,5,'legwear',True,20,0,0,0,0,0,0,1)
jeans = Legs("Jeans", "Jeans",2,2,5,'legwear',True,30,0,0,0,0,0,2,1)
ripped_jeans = Legs("Ripped jeans", "Ripped jeans",2,2,5,'legwear',True,45,0,0,0,0,0,1,1)
khakis = Legs("Khakis", "Khakis",2,5,5,'legwear',True,45,0,0,0,0,0,2,1)
camo_pants = Legs("Camo pants", "Camo pants",2,2,5,'legwear',True,15,0,0,0,0,0,2,2)
black_pants = Legs("Black pants", "Black pants",2,2,5,'legwear',True,15,0,0,0,0,0,2,2)

track_pants = Legs("Track pants", "Track pants",2,2,5,'legwear',True,15,0,0,0,0,0,1,2)
suit_pants = Legs("Suit pants", "Suit pants",2,2,5,'legwear',True,90,0,0,0,0,0,2,2)
work_pants = Legs("Work pants", "Work pants",2,2,5,'legwear',True,40,0,0,0,0,0,1,2)
sweat_pants = Legs("Sweat pants", "Sweat pants",2,2,5,'legwear',True,40,0,0,0,0,0,2,2)

long_skirt = Legs("Long skirt", "Long skirt",1,1,5,'legwear',True,45,0,0,0,0,0,1,1)
short_skirt = Legs("Short skirt", "Short skirt",1,1,5,'legwear',True,40,0,0,0,0,0,1,1)
leggings = Legs("Leggings", "Leggings",1,5,5,'legwear',True,25,0,0,0,0,0,1,1)

mens_legwear = [shorts,jeans,khakis,track_pants,work_pants,ripped_jeans,camo_pants,sweat_pants]
womens_legwear = [shorts,jeans,khakis,track_pants,sweat_pants, work_pants,long_skirt,short_skirt,leggings]

#feet
no_footwear = Legs("None", "None",1,5,5,'footwear',True,0,0,0,0,0,0,0,0)

running_shoes = Legs("Running shoes", "Running shoes",2,1,5,'footwear',True,100,0,0,0,0,0,1,2)
sandals = Legs("Sandals", "Sandals",1,1,5,'footwear',True,40,0,0,0,0,0,0,2)
high_heels = Legs("High heels", "High heels",1,5,5,'footwear',True,50,0,0,0,0,0,0,1)
dress_shoes = Legs("Dress shoes", "Dress shoes",1,5,5,'footwear',True,130,0,0,0,0,0,1,2)
light_boots = Legs("Light boots", "Light boots",3,5,5,'footwear',True,150,0,0,0,0,0,2,3)
combat_boots = Legs("Combat boots", "Combat boots",4,5,5,'footwear',True,200,0,0,0,0,0,3,4)
cowboy_boots = Legs("Cowboy boots", "Cowboy boots",4,5,5,'footwear',True,200,0,0,0,0,0,1,4)

mens_footwear = [running_shoes,sandals,light_boots,combat_boots,cowboy_boots]
womens_footwear = [running_shoes,sandals,high_heels,light_boots,combat_boots,cowboy_boots]

#clothes
naked = Outfit("None", "Clothes",1,5,5,'outfit',True,0,0,0,0,0,0,0,0)
tshirt = Outfit("T-Shirt", "Clothes",2,5,5,'outfit',True,25,0,0,0,0,0,1,1)
tanktop = Outfit("Tanktop", "Clothes",2,5,5,'outfit',True,25,0,0,0,0,0,1,1)

dress_shirt = Outfit("Dress shirt", "Clothes",2,5,5,'outfit',True,60,0,0,0,0,0,2,2)
work_shirt = Outfit("Work shirt", "Clothes",2,5,5,'outfit',True,35,0,0,0,0,0,3,3)
hawaiian_shirt = Outfit("Hawaiian shirt", "Clothes",2,5,5,'outfit',True,35,0,0,0,0,0,2,2)

plaid_shirt = Outfit("Plaid shirt", "Clothes",2,5,5,'outfit',True,40,0,0,0,0,0,2,2)
tie_dye_shirt = Outfit("Tie dye shirt", "Clothes",2,5,5,'outfit',True,30,0,0,0,0,0,1,1)
dress = Outfit("Dress", "Clothes",2,5,5,'outfit',True,80,0,0,0,0,0,1,2)
nice_dress = Outfit("Nice dress", "Clothes",1,5,5,'outfit',True,500,0,0,0,0,0,1,1)

#outerwear
no_outerwear = Outerwear("None", "Clothes",1,5,5,'outerwear',True,0,0,0,0,0,0,0,0)
hoodie = Outerwear("Hoodie", "clothes",3,5,5,'outerwear',True,45,0,0,0,0,0,2,2)
sweater = Outerwear("Sweater", "Clothes",2,5,5,'outerwear',True,70,0,0,0,0,0,2,2)
fancy_sweater = Outerwear("Fancy sweater", "Clothes",2,5,5,'outerwear',True,100,0,0,0,0,0,2,2)
jean_jacket = Outfit("Jean jacket", "Clothes",2,5,5,'outerwear',True,50,0,0,0,0,0,2,2)
bomber_jacket = Outfit("Bomber jacket", "Clothes",2,5,5,'outerwear',True,65,0,0,0,0,0,3,3)
windbreaker = Outfit("Windbreaker", "Clothes",1,5,5,'outerwear',True,30,0,0,0,0,0,2,4)
vest = Outfit("Vest", "Clothes",1,5,5,'outerwear',True,30,0,0,0,0,0,1,1)

sports_jacket = Outerwear("Sports jacket", "Clothes",2,5,5,'outerwear',True,80,0,0,0,0,0,3,3)
trenchcoat= Outerwear("Trench coat", "Clothes",3,4,5,'outerwear',True,100,0,0,0,0,0,4,4)
cheap_suit= Outerwear("Cheap suit", "Clothes",2,4,5,'outerwear',True,130,0,0,0,0,0,2,2)
leather_jacket = Outerwear("Leather jacket", "Clothes",5,5,5,'outerwear',True,150,0,0,0,0,0,3,4)
army_uniform = Outerwear("Army jacket", "Clothes",4,5,5,'outerwear',True,100,0,0,0,0,0,3,3)
nice_suit = Outerwear("Nice suit", "Clothes",2,5,5,'outerwear',True,500,0,0,0,0,0,2,1)



#armor
no_armor = Armor("None", "Clothes",1,5,5,'armor',True,0,0,0,0,0,0,0,0)

body_armor = Armor("Body armor", "Clothes",8,5,5,'armor',True,750,0,0,0,0,0,2,0)

#backpack
class Backpack:
	def __init__(self,name,can_carry,condition,base_value,item_type,can_loot):
		self.name = name
		self.can_carry = can_carry
		self.condition = condition
		self.base_value = base_value
		self.item_type = item_type
		self.can_loot = can_loot

small_backpack = Backpack('Small backpack',4,5,70,'backpack',True)
large_backpack = Backpack('Large backpack',7,5,130,'backpack',True)


class Dress_Code:
	def __init__(self,name,headwear,outfit,outerwear,legwear,footwear,weapons):
		self.name = name
		self.headwear = headwear
		self.outfit = outfit
		self.outerwear = outerwear
		self.legwear = legwear
		self.footwear = footwear
		self.weapons = weapons

no_dress_code = Dress_Code('none',[],[],[],[],[],[])
office_dress_code = Dress_Code('Office',[],[dress_shirt,nice_dress],[cheap_suit,nice_suit],[suit_pants,black_pants,long_skirt,short_skirt],[dress_shoes,high_heels],[])


#traits
class Trait:
	def __init__(self,name,description,base_value):
		self.name = name
		self.decription = description
		self.base_value = base_value

#personality traits
alcoholic = Trait("Alcoholic","Alcoholic",0)
alert = Trait("Alert","Alert",0)
aloof = Trait("Aloof","Aloof",0)
angry = Trait("Angry","Angry",0)
blowhard = Trait("Blowhard","Blowhard",0)
bratty = Trait("Bratty","Bratty",0)
calm = Trait("Calm","Calm",0)
carefree = Trait("Carefree","Carefree",0)
cautious = Trait("Causious","Cautious",0)
cocky = Trait("Cocky","Cocky",0)
creative = Trait("Creative", "Creative",0)
demonic = Trait("Demonic","Demonic",0)
devious = Trait("Devious","Devious",0)
depressed = Trait("Depressed", "Depressed",0)
dramatic = Trait("Dramatic","Dramatic",0)
emotional = Trait("Emotional","Emotional",0)
empathic = Trait("Empathic", "Empathic",0)
evil = Trait("Evil","Evil",0)
fearful = Trait("Fearful","Fearful",0)
flaky = Trait("Flaky","Flaky",0)
furry = Trait("Furry","Furry",0)
generous = Trait("Generous","Generous",0)
gloomy = Trait("Gloomy", "Gloomy",0)
goofy = Trait("Goofy","Goofy",0)
helpful = Trait("Helpful","Helpful",0)
horny = Trait("Always Horny", "Always Horny",0)
irritable = Trait('Irritable','Irritable',0)
late = Trait("Always late","Always late",0)
lazy = Trait("Lazy", "Lazy",0)
nauseous = Trait('Nauseous','Nauseous',0)
sadist = Trait("Sadist","Sadist",0)
smoker = Trait("Smoker", "Smoker",0)
stoner = Trait("Stoner", "Stoner",0)
tremors = Trait('Tremors', 'Tremors',0)
pyromaniac = Trait('Pyromaniac', 'Pyromaniac',0)
abrupt = Trait('Abrupt', 'Abrupt',0)
adventurous = Trait('Adventurous', 'Adventurous',0)
benevolent = Trait('Benevolent', 'Benevelent',0)
arrogant = Trait('Arrogant', 'Arrogant',0)
caring = Trait('Caring', 'Caring',0)
decisive = Trait('Decisive', 'Decisive',0)
crazy = Trait('Crazy', 'Crazy',0)
focused = Trait('Focused', 'Focused',0)
imaginative = Trait('Imaginative', 'Imaginative',0)
hateful = Trait('Hateful', 'Hateful',0)
neat = Trait('Neat', 'Neat',0)

angelic = Trait('Angelic', 'Angelic',0)


addiction_traits = [bratty,flaky,fearful,depressed,gloomy,late,lazy,angry,tremors,irritable,nauseous]

personality_traits = [alert,aloof,blowhard,cocky,creative,devious,dramatic,emotional,
		empathic,evil,fearful,flaky,furry,generous,goofy,helpful,late,lazy,horny,sadist,smoker,pyromaniac,angelic,
		adventurous,benevolent,arrogant,caring,decisive,crazy,focused,imaginative,hateful,neat]


#likes
loves_cats = Trait("Loves cats", "Lazy",0)
loves_dogs = Trait("Loves dogs", "Loves dogs",0)
loves_metal = Trait("Loves metal","Loves metal",0)
loves_rap = Trait("Loves rap","Loves rap",0)
loves_country = Trait("Loves country","Loves country",0)
loves_killing = Trait("Loves killing","Loves killing",0)
loves_stealing = Trait("Loves stealing","Loves stealing",0)
loves_art = Trait("Loves art","Loves art",0)
loves_poetry = Trait("Loves poetry","Loves poetry",0)
loves_literature = Trait("Loves literature","Loves literature",0)
loves_money = Trait("Loves money","Loves money",0)
loves_drugs = Trait("Loves drugs","Loves drugs",0)
loves_to_draw = Trait("Loves to draw","Loves to draw",0)
loves_singing = Trait("Loves singings","Loves singing",0)
loves_booze = Trait("Loves booze","Loves booze",0)

likes = [loves_cats,loves_dogs,loves_metal,loves_rap,loves_country,loves_killing,loves_stealing,loves_art,loves_poetry,loves_literature,
	loves_money,loves_drugs,loves_to_draw,loves_singing]

#physical_traits


#height
tall = Trait("Tall","Tall",0)
short = Trait("Short","Short",0)
average = Trait("Average Height","Average Height",0)

heights = [tall,short,average]

#body
skinny = Trait("Skinny","Skinny",0)
thin = Trait("Thin","Thin",0)
fat = Trait("Fat","Fat",0)
muscular = Trait("Muscular","Muscular",0)
stocky = Trait("Stocky","Stocky",0)

body_types = [skinny,fat,muscular,stocky,thin]

#shaved heads
shaved_blonde_hair = Trait("Blonde Hair(Shaved)","Blonde Hair(Shaved)",30)
shaved_brown_hair = Trait("Brown Hair(Shaved)","Brown Hair(Shaved)",30)
shaved_red_hair = Trait("Red Hair(Shaved)", "Red Hair(Shaved)",30)
shaved_black_hair = Trait("Black Hair(Shaved)","Black Hair(Shaved)",30)

shaved_hair = [shaved_brown_hair,shaved_blonde_hair,shaved_red_hair,shaved_black_hair]

#spiky hair
spiky_blonde_hair = Trait("Blonde Hair(Spiky)","Blonde Hair(Spiky)",30)
spiky_brown_hair = Trait("Brown Hair(Spiky)","Brown Hair(Spiky",30)
spiky_red_hair = Trait("Red Hair(Spiky", "Red Hair(Spiky",30)
spiky_black_hair = Trait("Black Hair(Spiky","Black Hair(Spiky",30)
spiky_blue_hair = Trait("Blue Hair(Spiky)", "Blue Hair(Spiky",30)
spiky_green_hair = Trait("Green Hair(Spiky)", "Green Hair(Spiky)",30)

spiky_hair = [spiky_blonde_hair,spiky_brown_hair,spiky_red_hair,spiky_blue_hair,spiky_green_hair]

#short hair
short_blonde_hair = Trait("Blonde Hair(Short)","Blonde Hair(Short)",30)
short_brown_hair = Trait("Brown Hair(Short)","Brown Hair(Short)",30)
short_red_hair = Trait("Red Hair(Short)", "Red Hair(Short)",30)
short_black_hair = Trait("Black Hair(Short)","Black Hair(Short)",30)
short_blue_hair = Trait("Blue Hair(Short)", "Blue Hair(Short)",30)
short_green_hair = Trait("Green Hair(Short)", "Green Hair(Short)",30)

short_hair = [short_blonde_hair,short_brown_hair,short_red_hair]


#long hair
long_blonde_hair = Trait("Blonde Hair(Long)","Blonde Hair(Long)",30)
long_brown_hair = Trait("Brown Hair(Long)","Brown Hair(Long)",30)
long_red_hair = Trait("Red Hair(Long)", "Red Hair(Long)",30)
long_black_hair = Trait("Black Hair(Long)","Black Hair(Long)",30)
long_blue_hair = Trait("Blue Hair(Long)", "Blue Hair(Long)",30)
long_green_hair = Trait("Green Hair(Long)", "Green Hair(Long)",30)

long_hair = [long_blonde_hair,long_brown_hair,long_red_hair]

#parted hair
parted_blonde_hair = Trait("Blonde Hair(Parted)","Blonde Hair(Parted)",30)
parted_brown_hair = Trait("Brown Hair(Parted)","Brown Hair(Parted)",30)
parted_red_hair = Trait("Red Hair(Parted)", "Red Hair(Parted)",30)
parted_black_hair = Trait("Black Hair(Parted)","Black Hair(Parted)",30)

parted_hair = [parted_blonde_hair,parted_brown_hair,parted_red_hair,parted_black_hair]

#mohawks
mohawk_blonde_hair = Trait("Blonde Hair(Mohawk)","Blonde Hair(Mohawk)",30)
mohawk_brown_hair = Trait("Brown Hair(Mohawk)","Brown Hair(Mohawk)",30)
mohawk_red_hair = Trait("Red Hair(Mohawk)", "Red Hair(Mohawk)",30)
mohawk_black_hair = Trait("Black Hair(Mohawk)","Black Hair(Mohawk)",30)

mohawk_hair = [mohawk_blonde_hair,mohawk_brown_hair,mohawk_red_hair,mohawk_black_hair]

#braids
braided_blonde_hair = Trait("Blonde Hair(Braids)","Blonde Hair(Braids)",60)
braided_brown_hair = Trait("Brown Hair(Braids)","Brown Hair(Braids)",60)
braided_red_hair = Trait("Red Hair(Braids)", "Red Hair(Braids)",60)
braided_black_hair = Trait("Black Hair(Braids)","Black Hair(Braids)",60)

braided_hair = [braided_blonde_hair,braided_brown_hair,braided_red_hair,braided_black_hair]


#facial_hair
mustache = Trait("Mustache","Mustache",60)
handlebar_mustache = Trait("Handlebar mustache","Handlebar mustache",60)
goatee = Trait("Goatee","Goatee",60)
full_beard = Trait("Full beard","Full beard",60)

facial_hair = [mustache,handlebar_mustache,goatee,full_beard]


#eyes
blue_eyes = Trait("Blue Eyes", "Blue Eyes",0)
brown_eyes = Trait("Brown Eyes","Brown Eyes",0)
green_eyes = Trait("Green Eyes","Green Eyes",0)
light_blue_eyes = Trait("Blue Eyes(Light)", "Blue Eyes(Light)",0)
light_brown_eyes = Trait("Brown Eyes(Light)","Brown Eyes(Light)",0)
light_green_eyes = Trait("Green Eyes(Light)","Green Eyes(Light)",0)
dark_blue_eyes = Trait("Blue Eyes(Dark)", "Blue Eyes(Dark)",0)
dark_brown_eyes = Trait("Brown Eyes(Dark)","Brown Eyes(Dark)",0)
dark_green_eyes = Trait("Green Eyes(Dark)","Green Eyes(Dark",0)
eyes = [blue_eyes,brown_eyes,green_eyes,light_blue_eyes,light_brown_eyes,light_green_eyes,dark_green_eyes,dark_blue_eyes,dark_brown_eyes]

#flair
earrings = Trait('Earrings', 'Earrings',75)

nose_ring = Trait('Nose ring', 'Nose ring',130)
tattoo_face = Trait("Face tattoos", "Face tattoos",200)
tattoo_arms = Trait("Sleeve tattoos", "Sleeve tattoos",3000)
tattoo_neck = Trait("Tattooed neck", "Tattooed neck",350)
tattoo_knuckles = Trait("Tattooed knuckles", "Tattooed knuckles",300)
tattoo_dragon = Trait("Tattoo(Dragon)", "Tattoo(Dragon)",400)
tattoo_skull = Trait("Tattoo(Skull)", "Tattoo(Skull)",375)
tattoo_unicorn = Trait("Tattoo(Unicorn)", "Tattoo(Unicorn)",600)
tattoo_heart = Trait("Tattoo(Heart)", "Tattoo(Heart)",250)
tattoo_mom = Trait("Tattoo(Mom)", "Tattoo(Mom)",200)
tattoo_teardrop = Trait("Tattoo(Teardrop)", "Tattoo(Teardop)",40)
tattoo_tribal = Trait("Tattoo(Tribal)", "Tattoo(Tribal)",400)
tattoo_butterfly = Trait("Tattoo(Butterfly)", "Tattoo(Butterfly)",275)

possible_tattoos = [earrings,nose_ring,tattoo_face,tattoo_arms,tattoo_neck,tattoo_knuckles,tattoo_dragon,tattoo_skull,tattoo_unicorn,tattoo_heart,
tattoo_mom,tattoo_teardrop,tattoo_tribal,tattoo_butterfly]

tattoo_slaver = Trait("Tattoo(Slaver)", "Tattoo(Slaver)",275)
tattoo_slave = Trait("Tattoo(Slave)", "Tattoo(Slave)",275)




gold_teeth = Trait("Gold teeth", "Gold teeth",5000)

scars_face = Trait('Scars(Face)', 'Scars',0)
scars_wrist = Trait('Scars(Wrists)', 'Scars',0)
scars_torso = Trait('Scars(Torso)', 'Scars',0)
scars_arms = Trait('Scars(Arms)', 'Scars',0)
scars_legs = Trait('Scars(Legs)', 'Scars',0)

scars = [scars_face,scars_wrist,scars_torso,scars_arms,scars_legs]

flair = [earrings,nose_ring,tattoo_face,tattoo_arms,tattoo_neck,tattoo_knuckles,gold_teeth,tattoo_dragon,tattoo_skull,tattoo_unicorn,tattoo_heart,
	tattoo_mom, tattoo_teardrop,tattoo_tribal,tattoo_butterfly,scars_face,scars_wrist,scars_torso,scars_arms,scars_legs]

#bionic_limbs
bionic_right_eye = Trait('Bionic Eye(Right)', 'Bionic Eye',5000)
bionic_left_eye = Trait('Bionic Eye(Left)', 'Bionic Eye',5000)
bionic_right_arm = Trait('Bionic Arm(Right)', 'Bionic Arm(Right)',15000)
bionic_left_arm = Trait('Bionic Arm(Left)', 'Bionic Arm(Left)',15000)
bionic_right_leg = Trait('Bionic Leg(Right)', 'Bionic Leg(Right)',15000)
bionic_left_leg = Trait('Bionic Leg(Left)', 'Bionic Leg(Left)',15000)

bionic_limbs = [bionic_right_eye,bionic_left_eye,bionic_right_arm,bionic_left_arm,bionic_right_leg,bionic_left_leg]




def gen_player_traits(gender):
	traits = []
	global personality_traits,likes,flair
	#physical traits

	#eyes
	my_eyes = random.choice(eyes)
	traits.append(my_eyes)

	#hair
	hair_types = [long_hair,short_hair,spiky_hair,shaved_hair,braided_hair,mohawk_hair,parted_hair]
	hair_type = random.choice(hair_types)
	hair_style = random.choice(hair_type)
	traits.append(hair_style)

	if gender == 'Male':
		chance = random.randint(1,2)
		if chance == 1:
			beard = random.choice(facial_hair)
			traits.append(beard)
	#height
	height = random.choice(heights)
	traits.append(height)
	#body
	body = random.choice(body_types)
	traits.append(body)
	#personality
	my_personality_traits = []
	num_personality_traits = random.randint(1,2)
	pers_count = 1
	while pers_count <= num_personality_traits:
		personality = random.choice(personality_traits)
		my_personality_traits.append(personality)
		pers_count += 1
	my_personality_traits = set(my_personality_traits)
        my_personality_traits = list(my_personality_traits)

	for trait in my_personality_traits:
		traits.append(trait)
	#likes
	my_likes = []
	roll = random.randint(1,2)
	count = 1
	while count <= roll:
		like = random.choice(likes)
		my_likes.append(like)
		count += 1
	my_likes = set(my_likes)
	my_likes = list(my_likes)
	for trait in my_likes:
		traits.append(trait)
	#flair
	my_flair = []
	chance = random.randint(1,22)
	if chance >= 1 and chance <= 12:
		flair_choice = random.choice(flair)
		my_flair.append(flair_choice)
        elif chance >= 13 and chance <= 20:
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
        elif chance >= 21:
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
                flair_choice = random.choice(flair)
                my_flair.append(flair_choice)
	my_flair = set(my_flair)
	my_flair = list(my_flair)	
	for trait in my_flair:
		traits.append(trait)

	#bionic stuff
	bionic_chance = random.randint(1,12)
	if bionic_chance == 1:
		bionic_limb = random.choice(bionic_limbs)
		traits.append(bionic_limb)
	#traits = set(traits)
	#traits = list(traits)

	return traits

def gen_skills(class_type):
	skills = ['brawl', 'computers', 'dodge', 'disguise', 'etiquette', 'explosives','first_aid', 'hand_to_hand',  'investigate', 'leadership', 'lockpick',
'lying', 'negotiate', 'rifle', 'pickpocket',"pistol", 'persuasion', 'seduction', 'shotgun', 'stealth', 'streetwise',"survival" 'throw', 'torture', 'trivia']
	brawl = 0
	computers = 0
	dodge = 0
	disguise = 0
	etiquette = 0
	explosives = 0
	first_aid = 0
	investigate = 0
	leadership = 0
	lying = 0
	negotiate = 0
	rifle = 0
	pickpocket = 0
	pistol = 0
	persuasion = 0
	security = 0
	seduction = 0
	shotgun = 0
	stealth = 0
	streetwise =  0
	survival = 0
	throw = 0
	torture = 0
	trivia = 0
	driving = 0
	blade =0
	blunt = 0

        skills = [brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership, 
	lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt]

	if class_type == 'Hustler':
		brawl = random.randint(3,4)
		computer = random.randint(0,3)
		dodge = random.randint(3,4)
		disguise = random.randint(1,4)
		etiquette = random.randint(1,3)
		first_aid = random.randint(1,2)
		investigate = random.randint(1,2)
		leadership = random.randint(0,2)
		lying = random.randint(1,3)
		negotiate = random.randint(3,4)
		rifle = 0
		pickpocket = random.randint(2,4)
                pistol = random.randint(1,2)
		persuasion = random.randint(2,4)
		security = random.randint(0,2)
		seduction = random.randint(0,2)
		shotgun = 0
		streetwise = random.randint(2,3)
		survival = random.randint(1,2)
		throw = random.randint(0,1)
		trivia = random.randint(2,4)
		driving = random.randint(0,2)
		blade = random.randint(0,2)
		blunt = random.randint(0,2)

	elif class_type == "Crimepunk":
	        brawl = random.randint(1,3)
	        computers = random.randint(0,1)
	        dodge = random.randint(2,4)
	        disguise = random.randint(2,3)
       		etiquette = random.randint(0,1)
       		explosives = random.randint(0,1)
	        first_aid = random.randint(2,3)
	        investigate = random.randint(0,1)
	        leadership = random.randint(0,1)
	        lying = random.randint(1,2)
	        negotiate = random.randint(2,4)
	        rifle = random.randint(0,1)
	        pickpocket = 0
                pistol = random.randint(1,3)
	        persuasion = random.randint(1,3)
  		seduction = 0
	        shotgun = 0
    	  	stealth = random.randint(0,3)
    	  	streetwise = random.randint(2,4)
                survival = random.randint(1,2)

   	     	throw = random.randint(0,1)
   	     	torture = random.randint(0,3)
   	     	trivia = random.randint(1,3)
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)

	elif class_type == "Scumbag":
	        brawl = random.randint(1,3)
	        computers = random.randint(0,1)
	        dodge = random.randint(2,4)
	        disguise = random.randint(2,4)
	        etiquette = 0
	        explosives = random.randint(2,4)
	        first_aid = random.randint(0,2)
	        investigate = random.randint(2,3)
	        leadership = random.randint(0,1)
	        security = random.randint(2,4)
                survival = random.randint(1,2)

	        lying = random.randint(0,2)
	        negotiate = 0
	        rifle = random.randint(1,3)
	        pickpocket = 0
                pistol = random.randint(1,3)
	        persuasion = 0
	        seduction = 0
	        shotgun = random.randint(2,3)
	        stealth = random.randint(2,4)
	        streetwise = random.randint(1,3)
	        throw = random.randint(1,2)
		torture = random.randint(2,3)
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)
		
        elif class_type == "Hipster":
                brawl = random.randint(1,3)
                computers = random.randint(0,1)
                dodge = random.randint(0,2)
                disguise = random.randint(2,4)
                etiquette = random.randint(0,2)
                explosives = 0
                first_aid = random.randint(0,2)
                investigate = random.randint(2,3)
                leadership = random.randint(0,1)
                security = random.randint(0,1)
                lying = random.randint(0,2)
                negotiate = random.randint(0,1)
                rifle = 0
                pickpocket = 0
		pistol = random.randint(0,1)
                persuasion = random.randint(1,2)
                seduction = random.randint(1,2)
                shotgun = 0
                stealth = 0
                streetwise = random.randint(0,1)
                survival = random.randint(1,2)

                throw = random.randint(0,1)
                torture = 0 
                driving = random.randint(0,2)
                blade = random.randint(0,1)
                blunt = random.randint(0,1)

	elif class_type == "Script Kiddie":
	        brawl = random.randint(0,1)
	        computers = random.randint(4,6)
	        dodge = random.randint(0,1)
	        disguise = random.randint(1,2)
	        etiquette = random.randint(0,1)
	        explosives = random.randint(0,1)
	        first_aid = 0
	        investigate = random.randint(3,4)
	        leadership = random.randint(0,2)
	        security = random.randint(1,2)
	        lying = random.randint(1,3)
	        negotiate = random.randint(1,2)
	        rifle = 0
	        pickpocket = 0
		pistol = 0
	        persuasion = random.randint(0,1)
	        seduction = 0
	        shotgun = 0
	        stealth = random.randint(1,2)
	        streetwise =  0
	        throw = 0
		torture = random.randint(0,2)
                driving = random.randint(0,2)
                blade = 0
                blunt = 0
                survival = random.randint(1,2)

	elif class_type == "Wastoid":
	        brawl = random.randint(1,3)
	        computers = 0
	        dodge = 0
	        disguise = random.randint(0,2)
	        etiquette = random.randint(0,2)
	        explosives = 0
	        first_aid = random.randint(1,3)
	        investigate = random.randint(1,3)
	        leadership = 0
	        security = 0
	        lying = 0
	        negotiate = random.randint(1,2)
	        rifle = 0
	        pickpocket = 0
		pistol = 0
	        persuasion = 0
	        seduction = random.randint(4,8)
	        shotgun = 0
	        stealth = 0
	        streetwise =  random.randint(2,4)
	        throw = 0
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)
                survival = random.randint(1,2)

        elif class_type == "Sex Worker":
                brawl = random.randint(1,3)
                computers = random.randint(0,1)
                dodge = random.randint(0,2)
                disguise = random.randint(0,2)
                etiquette = random.randint(0,2)
                explosives = 0
                first_aid = random.randint(1,3)
                investigate = random.randint(1,3)
                leadership = random.randint(0,2)
                security = random.randint(0,2)
                lying = random.randint(1,2)
                negotiate = random.randint(1,2)
                rifle = 0
                pickpocket = random.randint(0,3)
                pistol = 0
                persuasion = random.randint(1,4)
                seduction = random.randint(2,6)
                shotgun = 0
                stealth = random.randint(0,2)
                streetwise =  random.randint(2,4)
                throw = 0
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)
                survival = random.randint(1,2)

        elif class_type == "Lost Soul":
                brawl = random.randint(1,3)
                computers = random.randint(0,1)
                dodge = random.randint(0,2)
                disguise = random.randint(0,2)
                etiquette = random.randint(0,2)
                explosives = 0
                first_aid = random.randint(0,2)
                investigate = random.randint(1,3)
                leadership = random.randint(2,4)
                security = random.randint(0,2)
                lying = random.randint(1,2)
                negotiate = random.randint(1,2)
                rifle = 0
                pickpocket = random.randint(1,3)
                pistol = 0
                persuasion = random.randint(1,4)
                seduction = random.randint(2,3)
                shotgun = 0
                stealth = random.randint(0,2)
                streetwise =  random.randint(2,4)
                throw = 0
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)
                survival = random.randint(1,2)

	skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
lying, negotiate, rifle, pickpocket,pistol, persuasion,security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
	return skills

def gen_player_weapons(class_type):
	if class_type == 'Hustler':
		hustler_weapons = [brass_knuckles,knife,baseball_bat, pistol_9mm,crowbar]
		weapon = random.choice(hustler_weapons)
	elif class_type == 'Crimepunk':
		drug_dealer_weapons = [pistol_9mm, shotgun_12g,uzi]
		weapon = random.choice(drug_dealer_weapons)
	elif class_type == 'Hipster':
		hipster_weapons = [brass_knuckles, knife,baseball_bat]
		weapon = random.choice(hipster_weapons)
	elif class_type == "Scumbag":
		robber_weapons = [shotgun_12g,ak47,uzi]
		weapon = random.choice(robber_weapons)
	elif class_type == "Hacker":
		weapon = punch
	elif class_type == "Wastoid" or class_type == 'Lost Soul' or class_type == 'Sex Worker':
		sex_worker_weapons = [punch,brass_knuckles,knife,baseball_bat]
		weapon = random.choice(sex_worker_weapons)
	else:
		weapon = punch
	return weapon

def gen_player_outfit(class_type,gender):
	if gender == "Male":
		outfits = [tanktop,work_shirt,tshirt,dress_shirt,plaid_shirt]
	elif gender == "Female":
		outfits = [dress,tshirt,tanktop,plaid_shirt,work_shirt]
	outfit = random.choice(outfits)

	chance_headwear = random.randint(1,3)
	if chance_headwear == 1:
		headwear = random.choice(headwear_types)
	else:
		headwear = no_headwear
	facewear = no_facewear
	chance_eyewear = random.randint(1,5)
	if chance_eyewear == 1:
		eyewear = sunglasses
	else:
		eyewear = no_eyewear
	chance_handwear = random.randint(1,9)
	if chance_handwear == 1:
		handwear = fingerless_gloves
	else:
		handwear = no_handwear
	if gender == "Male":
		legwear = random.choice(mens_legwear)
		footwear = random.choice(mens_footwear)
	elif gender == "Female" and outfit != dress:
		legwear = random.choice(womens_legwear)
		footwear = random.choice(womens_footwear)
        elif gender == "Female" and outfit == dress:
                legwear = no_legwear
                footwear = high_heels
	chance_outerwear = random.randint(1,3)
	if chance_outerwear != 1:
		possible_outerwear = [leather_jacket,trenchcoat,sports_jacket,hoodie,sweater,jean_jacket,windbreaker,bomber_jacket]
		outerwear = random.choice(possible_outerwear)
	else:
		outerwear = no_outerwear
	armor = no_armor
	return outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor




class Time: 
        def __init__(self,year,month,day,hour,minute):
                self.year = year
                self.month = month
                self.day = day
                self.hour = hour
		self.minute = minute
        def correct(self,party_actions):
                count = 1
                while count <= 8:
                        if self.month >= 13:
                                self.year += 1
				self.month = 1

			if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
                        	if self.day >= 31:
                                	self.month += 1
					self.day = 1
			elif self.month == 2:
				if self.day >= 28:
					self.month += 1
					self.day = 1
			elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
				if self.day >= 30:
					self.month += 1
					self.day = 1
                        if self.hour >= 24:
                                self.hour = 0
                                self.day += 1
				party_actions.days_survived += 1
			if self.minute >= 60:
				self.hour += 1
				self.minute = 0
			count += 1
	def get_month(self):
		if self.month == 1:
			return "January"
		elif self.month == 2:
			return "Febuary"
		elif self.month == 3:
			return "March"
		elif self.month == 4:
			return "April"
		elif self.month == 5:
			return "May"
		elif self.month == 6:
			return "June"
		elif self.month == 7:
			return "July"
		elif self.month == 8:
			return "August"
		elif self.month == 9:
			return "September"
		elif self.month == 10:
			return "October"
		elif self.month == 11:
			return "November"
		elif self.month == 12:
			return "December"


	def get_am_or_pm(self):
		if self.hour <= 11:
			return "a.m."
		elif self.hour >= 12:
			return "p.m."

	def get_hour(self):
		print self.hour
		if self.hour == 0:
			return 12
		elif self.hour >= 1 and self.hour <= 12:
			return self.hour
		elif int(self.hour) == 13:
			return 1
		elif self.hour == 14:
			return 2
		elif self.hour == 15:
			return 3
		elif self.hour == 16:
			return 4
		elif self.hour == 17:
			return 5
		elif self.hour == 18:
			return 6
		elif self.hour == 19:
			return 7
		elif self.hour == 20:
			return 8
		elif self.hour == 21:
			return 9
		elif self.hour == 22:
			return 10
		elif self.hour == 23:
			return 11

start_time = Time(2069,8,1,12,0)

class City:
	def __init__(self,areas,name,time,player_organization,corporations,missions,weather):
		self.areas = areas
		self.name = name
		self.time = time
		self.player_organization = player_organization
		self.corporations = corporations
		self.missions = missions
		self.weather = weather

class Area:
	def __init__(self,locations,name,organizations,x,y,randos,price,region,is_hidden):
		self.locations = locations
		self.name = name
		self.organizations = organizations
		self.x = x
		self.y = y
		self.randos = randos
		self.price = price
		self.region = region
		self.is_hidden = is_hidden
	def clean_up(self):
		possible_locations = []
		for location in self.locations:
			#owner_here = False
			#for actor in locations.actors:
			#	if actor.home == location:
			#		owner_here = True
			if location.is_bar == True:
				for item in location.items:
                        		if item.item_type == "weapon" or item.item_type == "outfit" or item.item_type == 'medical':
                        	        	location.items.remove(item)
                		for corpse in location.corpses:
                        		location.corpses.remove(corpse)
			else:
				possible_locations.append(location)
		if len(possible_locations) >= 1:
			target = random.choice(possible_locations)
			owner_here = False
			if len(target.actors.members) >= 1:
				for member in target.actors.members:
					if member != None:
						if member.home != None:
							if member.home == target:
								owner_here = True
			elif len(target.actors.members) <= 0:
				owner_here = False
			if owner_here == False:
				for item in target.items:
					if item.item_type == "weapon" or item.item_type == "outfit" or item.item_type == 'medical':
						target.items.remove(item)
				for corpse in target.corpses:
					target.corpses.remove(corpse)
		

class Location:

	def __init__(self,name,city,area,type,x,y,actors,items,is_safehouse,corpses,is_store,sold_here,can_sell,services,services_here,time_open,time_close,is_bar,regulars,is_entrance,rooms,is_library,is_hq,owned_by,bombs_here,floors,parent_location,is_apt,hidden_items,floor,is_exit,security_level,alarm_level,dress_code,has_broker,broker,is_indoors,employees,security):
		self.name = name
		self.city = city
		self.area = area
		self.type = type
		self.x = x
		self.y = y
		self.actors = actors
		self.items = items
		self.is_safehouse = is_safehouse
		self.corpses = corpses
		self.is_store = is_store
		self.sold_here = sold_here
		self.can_sell = can_sell
		self.services = services
		self.services_here = services_here
		self.time_open = time_open
		self.time_close = time_close
		self.is_bar = is_bar
		self.regulars = regulars
		self.is_entrance = is_entrance
		self.rooms = rooms
		self.is_library = is_library
		self.is_hq = is_hq	
		self.owned_by = owned_by
		self.bombs_here = bombs_here
		self.floors = floors
		self.parent_location = parent_location
		self.is_apt = is_apt
		self.hidden_items = hidden_items
		self.floor = floor
		self.is_exit = is_exit
		self.security_level = security_level
		self.alarm_level = alarm_level
		self.dress_code = dress_code
		self.has_broker = has_broker
		self.broker = broker
		self.is_indoors = is_indoors
		self.employees = employees
		self.security = security
class Container:
	def __init__(self,name,item_type,items,money,is_visible,max_items,max_money,base_value,can_loot,is_destroyed,lock_level):
		self.name = name
		self.item_type = item_type
		self.items = items
		self.money = money
		self.is_visible = is_visible
		self.max_items = max_items
		self.max_money = max_money
		self.base_value = base_value
		self.can_loot = can_loot
		self.is_destroyed = is_destroyed
		self.lock_level = lock_level
fridge = Container('Fridge','container',[],0,True,18,0,1200,True,False,0)
small_safe = Container('Small safe','container',[],0,True,0,15000,300,False,False,7)

class Junk:
	def __init__(self,name,base_value,item_type,can_loot):
		self.name = name
		self.base_value = base_value
		self.item_type = item_type
		self.can_loot = can_loot

class Limb:
        def __init__(self,name,injury_name,location,item_type,can_loot,base_value):
                self.name = name
		self.injury_name = injury_name
		self.location = location
                self.item_type = item_type
                self.can_loot = can_loot
		self.base_value = base_value
#limb = Limb(name,'Right hand','limb',True)

class Service:
	def __init__(self,name,cost,description):
		self.name = name
		self.cost = cost
		self.description = description

#Junk
blood = Junk('Blood', 0,'junk',False)

broken_desk = Junk('Broken desk', 0,'junk',False)
broken_light = Junk('Broken light', 0,'junk',False)
broken_glass = Junk('Broken glass', 0,'junk',False)
broken_monitor = Junk('Broken monitor', 0,'junk',True)
cat = Junk('Cat', 90,'junk',True)
copper_wire = Junk('Copper wire', 75,'junk',True)
hole_in_wall = Junk('Hole in wall', 0,'junk',False)
hole_in_floor = Junk('Hole in floor', 0,'junk',False)
toilet = Junk('Broken toilet', 0,'junk',False)
old_newspaper = Junk('Old newspaper', 10,'junk',True)
office_chair = Junk('Office chair', 0,'junk',True)
pile_of_rubble = Junk('Pile of rubble', 0,'junk',False)
smokeable_butt = Junk('Cigarette butt',0,'junk',True)
dirty_table = Junk('Dirty table',0,'junk',False)
trash = Junk('Trash',0,'junk',False)

beer = Junk('Beer', 5,'junk',True)
#coffee = Junk('Coffee', 3,'junk',True)
#crack = Junk('Crack', 50,'junk',True)
#hamburger = Junk('Hamburger', 8,'junk',True)
#fries = Junk('Fries', 4,'junk',True)
#pizza = Junk('Pizza', 5,'junk',True)

#store
counter = Junk('Counter',0,'junk',False)

#bar
bar_stool = Junk('Bar stool',0,'junk',False)
booth = Junk('Booth',0,'junk',False)

#furniture
dirty_couch = Junk('Dirty couch',0,'junk',False)
stinky_couch = Junk('Stinky couch',0,'junk',False)
stained_couch = Junk('Stained couch',0,'junk',False)
bong = Junk('Bong',0,'junk',False)
strobe_light = Junk('Strobe light',150,'junk',False)
sound_system = Junk('Sound system',1000,'junk',False)
bed = Junk('Bed',500,'junk',False)
bunk_bed = Junk('Bunk bed',700,'junk',False)

table = Junk('Table',200,'junk',False)
coffee_table = Junk('Coffee table',200,'junk',False)
dining_table = Junk('Dining table',500,'junk',False)



desk = Junk('Desk',200,'junk',False)
bookshelf = Junk('Bookshelf',200,'junk',False)
dresser = Junk('Dresser',350,'junk',False)

chair = Junk('Chair',50,'junk',True)
rug = Junk('Rug',500,'junk',True)
couch = Junk('Couch',400,'junk',False)

toilet2 = Junk('Toilet',400,'junk',False)
sink = Junk('Sink',400,'junk',False)
stove = Junk('Stove',400,'junk',False)
shower = Junk('Shower',400,'junk',False)


#camp
class Tent:
        def __init__(self,name,base_value,item_type,can_loot,set_up,num_hold,is_full,warmth,is_damaged):
                self.name = name
                self.base_value = base_value
                self.item_type = item_type
                self.can_loot = can_loot
		self.set_up = set_up
		self.num_hold = num_hold
		self.is_full = is_full
		self.warmth = warmth
		self.is_damaged = is_damaged

tent1 = Tent('Two person tent',150,'tent',True,False,2,False,5,False)
tent2 = Tent('Four person tent',400,'tent',True,False,4,False,5,False)


furniture = [strobe_light,sound_system,bed,bunk_bed,table,chair,couch,small_safe]

#outdoors
small_tree = Junk('Small tree',700,'junk',False)
tree = Junk('Tree',700,'junk',False)
fountain = Junk('Fountain',700,'junk',False)
hedge = Junk('Hedge',700,'junk',False)
dog = Junk('Dog',700,'junk',False)
bush = Junk('Bush',700,'junk',False)
shrub = Junk('Shrub',700,'junk',False)
log = Junk('Log',700,'junk',False)
stream = Junk('Stream',700,'junk',False)
rock = Junk('Rock',700,'junk',False)
grave = Junk('Grave',700,'junk',False)


#heat
barrel_fire = Junk('Barrel fire',700,'junk',False)
space_heater = Junk('Space heater',700,'junk',False)
heater = Junk('Radiator',700,'junk',False)
fire = Junk('Fire',700,'junk',False)



#library 
library_card = Junk('Library card',100,'junk',True)
desktop_computer = Junk('Desktop computer',200,'junk',False)
#gear
sleeping_bag = Junk('Sleeping bag',80,'junk',True)
rope = Junk('Rope',25,'junk',False)
lighter = Junk('Lighter',25,'junk',False)

#computers
laptop_computer = Junk('Laptop computer',500,'junk',True)
tablet = Junk('Tablet computer',350,'junk',True)
smartphone = Junk('Smartphone',350,'junk',True)
server = Junk('Server',2000,'junk',False)
microcontroller = Junk('Microcontroller',30,'junk',False)
tv = Junk('TV',300,'junk',False)

#files
client_list = Junk('Client list',20000,'junk',True)
company_plans = Junk('Company plans',50000,'junk',True)
meeting_minutes = Junk('Meeting minutes',5000,'junk',True)
confidential_memo = Junk('Confidential memo',15000,'junk',True)
payroll = Junk('Payroll',5000,'junk',True)


area_id = 1
location_id = 1

class Weather:
	def __init__(self,temperature,clouds,precipitation,precipitation_type,precipitation_amount):
		self.temperature = temperature
		self.clouds = clouds
		self.precipitation = precipitation
		self.precipitation_type = precipitation_type
		self.precipitation_amount = precipitation_amount
#weather
def get_weather(time):
	#temperature
	month = time.get_month()
	if month == "January":
		base_temp = -25
	elif month == "Febuary":
		base_temp = -25
        elif month == "March":
                base_temp = -15
        elif month == "April":
                base_temp = -5
	elif month == "May":
		base_temp = 5
        elif month == "June":
                base_temp = 10
        elif month == "July":
                base_temp = 20
        elif month == "August":
                base_temp = 25
        elif month == "September":
                base_temp = 15
        elif month == "October":
                base_temp = 5
        elif month == "November":
                base_temp = -5
        elif month == "December":
                base_temp = -15
	variance = 0
	roll = random.randint(1,2)
	if roll == 1:
		var_roll = random.randint(1,7)
		variance -= var_roll
	elif roll == 2:
		var_roll = random.randint(1,7)
		variance = var_roll
	temperature = base_temp + variance

	#weather
	
	#clouds
	cloud_roll = random.randint(1,5)
	if cloud_roll == 1:
		clouds = "Sunny"
	elif cloud_roll == 2:
		clouds = "A few clouds"
	elif cloud_roll == 3:
		clouds = "Overcast"
	elif cloud_roll == 4:
		clouds = "Cloudy"
	elif cloud_roll  == 5:
		clouds = "Dark clouds"

	#precipitation
	precipitation = False
	precipitation_amount = 0
	precipitation_roll = random.randint(1,6)
	if precipitation_roll == 1 and cloud_roll >= 4:
		base_amount = cloud_roll
		precipitation_roll = random.randint(1,3)
		precipitation_amount = base_amount + precipitation_roll
		precipitation = True
		if temperature >= 0:
			if precipitation_amount <=4:
				precipitation_type = "Light rain"
			else:
               		        precipitation_type = "Heavy rain"

		elif temperature >= -5 and temperature <= -1:
			if precipitation_amount <= 4:
				precipitation_type = "Light freezing rain"
			else:
				precipitation_type = "Heavy freezing rain"
		elif temperature <= -6:
			if precipitation_amount <= 4:
				precipitation_type = "Light snow"
			else:
				precipitation_type = "Heavy snow"
	else:
		precipitation = False
		precipitation_type = 'None'
	weather = Weather(temperature,clouds,precipitation,precipitation_type,precipitation_amount)
	return weather

#Campsite
class Campsite:
	def __init__(self,location,has_fire,tents_set_up,has_water):
		self.location = location
		self.has_fire = has_fire
		self.tents_set_up = tents_set_up
		self.has_water = has_water

#NPCs
def create_npc(profession,affiliation,home,gender):
	#gender
	if gender == None:
		genders = ['Male', 'Female']
		gender = random.choice(genders)
	#age
	age = random.randint(18,45)
	#health
	#health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)
	#stats


	#squatter,crimepunk,scumbag

	if profession == 'Squatter' or profession == "Crimepunk" or profession == "Scumbag" or profession == "Wastoid" or profession == "Junkfreak" or profession == "Pissboi" or profession == "Meatball" or profession == 'Sex Worker' or profession == 'Lost Soul' or profession == 'Biker':
		if profession == 'Scumbag' or profession == 'Crimepunk':
			strength = random.randint(10,18)
		else:
			strength =random.randint(5,15)
		strength, base_strength = strength,strength
		if profession == 'Crimepunk' or profession == 'Junkfreak' or profession == 'Hustler' or profession == 'Sex Worker':
			dexterity = random.randint(10,18)
		else:
			dexterity = random.randint(5,15)
		dexterity, base_dexterity = dexterity,dexterity
		willpower = random.randint(5,15)
		willpower, base_willpower = willpower,willpower
		if profession == 'Hustler':
			intelligence = random.randint(1,10)
		else:
			intelligence = random.randint(5,15)
		intelligence, base_intelligence = intelligence,intelligence
		if profession == 'Hustler' or profession == 'Sex Worker' or profession == 'Lost Soul':
			charisma = random.randint(10,15)
		else:
			charisma = random.randint(5,15)
		charisma, base_charisma = charisma,charisma
		max_health = strength * 10	
		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
		health.current_stamina = random.randint(50,95)
		npc_stats = Stats(strength, dexterity, intelligence, willpower, charisma, base_strength, base_dexterity, base_intelligence,base_willpower,base_charisma)
		#injuries
		injuries = []
		#skills
        	brawl = 2
        	computers = random.randint(0,2)
        	dodge = random.randint(0,2)
        	disguise = random.randint(0,2)
        	etiquette = random.randint(0,2)
        	explosives = random.randint(0,2)
        	first_aid = random.randint(0,2)
        	investigate = random.randint(0,2)
        	leadership = random.randint(0,2)
        	lying = random.randint(0,2)
        	negotiate = random.randint(0,2)
        	rifle = random.randint(0,2)
        	pickpocket = random.randint(0,2)
        	pistol = random.randint(0,2)
        	persuasion = random.randint(0,2)
        	security = random.randint(0,2)        	
		seduction = random.randint(0,2)
        	shotgun = random.randint(0,2)
        	stealth = random.randint(0,2)
        	streetwise =  random.randint(0,2)
                survival = random.randint(1,2)

        	throw = random.randint(0,2)
        	torture = random.randint(0,2)
		trivia = random.randint(0,2)
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)

		skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
		lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
                skills_xp = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
		#weapon
		weapons = [machete,brass_knuckles,knife,baseball_bat,pistol_9mm,shotgun_12g,crowbar]
		weapon = random.choice(weapons)
		if weapon.name =='Punch':
			skills.brawl = random.randint(1,3)
                if weapon.name == "Knife" or weapon.name == 'Sword' or weapon.name == 'Machete':
			skills.blade = random.randint(1,3)
		if weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
                        skills.blunt = random.randint(1,3)
                elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
                        skills.pistol = random.randint(1,3)
                elif weapon.name == "12g Shotgun": 
                        skills.shotgun = random.randint(1,3) 
                elif weapon.name == "AK-47": 
                        skills.rifle = random.randint(1,3) 

		#outfit
		#possible_outfits = [hoodie,tshirt,trenchcoat]
		outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_player_outfit(profession,gender)
		#tool
		tool = None
		#traits
		traits = gen_player_traits(gender)
		#if profession.name == 'Lost Soul':
		#	traits.append(demonic)
		#drugs
		drugs = []
		chance = 3
		roll = random.randint(1,3)
		if roll == 3:
			possible_drugs = [crack,cocaine,weed,morphine,speed]
			new_drug = random.choice(possible_drugs)
			drugs.append(new_drug)
		else:
			drugs = []
		#name
        	if gender == 'Male':
        	        fname = random.choice(male_fnames)
        	elif gender == "Female":
        	        fname = random.choice(female_fnames)
        	lname = random.choice(surnames)
		#money
		money = random.randint(50,200)
		#combat status
		combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)
		#mind
		happiness = random.randint(40,100)
		stress = random.randint(0,20)
		sanity = random.randint(40,100)
		horny = random.randint(0,50)
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
		#for trait in traits:
		#	if trait.name == 'Loves drugs':
		#		possible_drugs = [speed_addiction,opiates_addiction,cocaine_addiction]
		#		drug = random.choice(possible_drugs)
		#		drug.addiction_level = random.randint(2,5)

		addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
		trauma = 0
		mind = Mind(happiness,stress,sanity,horny,addictions,trauma,morale)

		hunger,thirst,sleep = random.randint(3,20),random.randint(6,40),random.randint(50,95)

		#home
		home = 'None'
		
		#traits = set(traits)
		#traits = list(traits)
		#finally make the npc
		npc = Char(gender,age, profession,affiliation,health, npc_stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'enemy',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
		return npc
        elif profession == 'Telemarketer' or profession == 'Data Miner' or profession == 'Fast Food Worker' or profession == 'Fast Food Manager' or profession == 'Vlogger' or profession == 'Shopkeeper' or profession == 'Programmer' or profession == 'Janitor' or profession == 'Warehouse Worker' or profession == 'Warehouse Manager' or profession == 'Chatbot Operator' or profession =='Housekeeper' or profession == 'Bike Courier' or profession == 'Nurse' or profession == 'Hipster' or profession == 'Hippie' or profession == 'Stripper' or profession == 'Mechanic' or profession == 'Security Guard' or profession== 'Manager' or profession == 'Receptionist' or profession == 'Building Manager' or profession == "Office Worker" or profession == "Broker":
		strength = random.randint(4,8)
		base_strength = strength
                dexterity = random.randint(4,8)
                dexterity, base_dexterity = dexterity,dexterity
                willpower = random.randint(5,15)
                willpower, base_willpower = willpower,willpower
                intelligence = random.randint(5,15)
                intelligence, base_intelligence = intelligence,intelligence
                charisma = random.randint(5,15)
                charisma, base_charisma = charisma,charisma
                max_health = strength * 10      
                health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
                health.current_stamina = random.randint(50,95)
                npc_stats = Stats(strength, dexterity, intelligence, willpower, charisma, base_strength, base_dexterity, base_intelligence,base_willpower,base_charisma)
                #injuries
                injuries = []
                #skills
                brawl = 2
                computers = random.randint(0,2)
                dodge = random.randint(0,2)
                disguise = random.randint(0,2)
                etiquette = random.randint(0,2)
                explosives = random.randint(0,2)
                first_aid = random.randint(0,2)
                investigate = random.randint(0,2)
                leadership = random.randint(0,2)
                lying = random.randint(0,2)
                negotiate = random.randint(0,2)
                rifle = random.randint(0,2)
                pickpocket = random.randint(0,2)
                pistol = random.randint(0,2)
                persuasion = random.randint(0,2)
                security = random.randint(0,2)          
                seduction = random.randint(0,2)
                shotgun = random.randint(0,2)
                stealth = random.randint(0,2)
                streetwise =  random.randint(0,2)
                survival =  random.randint(0,2)

                throw = random.randint(0,2)
                torture = random.randint(0,2)
                trivia = random.randint(0,2)
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)

                skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
                skills_xp = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
                #weapon
                weapons = [punch]
                weapon = random.choice(weapons)
                if weapon.name =='Punch':
                        skills.brawl = random.randint(1,3)
                if weapon.name == "Knife" or weapon.name == 'Sword' or weapon.name == 'Machete':
                        skills.blade = random.randint(1,3)
                if weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
                        skills.blunt = random.randint(1,3)
                elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
                        skills.pistol = random.randint(1,3)
                elif weapon.name == "12g Shotgun": 
                        skills.shotgun = random.randint(1,3) 
                elif weapon.name == "AK-47": 
                        skills.rifle = random.randint(1,3) 

                #outfit
                #possible_outfits = [hoodie,tshirt,trenchcoat]
                outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_player_outfit(profession,gender)
                #tool
                tool = None
                #traits
                traits = gen_player_traits(gender)
                #if profession.name == 'Lost Soul':
                #       traits.append(demonic)
                #drugs
                drugs = []
                chance = 3
                roll = random.randint(1,3)
                if roll == 3:
                        possible_drugs = [crack,cocaine,weed,morphine,speed]
                        new_drug = random.choice(possible_drugs)
                        drugs.append(new_drug)
                else:
                        drugs = []
                #name
                if gender == 'Male':
                        fname = random.choice(male_fnames)
                elif gender == "Female":
                        fname = random.choice(female_fnames)
                lname = random.choice(surnames)
                #money
                money = random.randint(50,200)
                #combat status
                combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)
                #mind
                happiness = random.randint(40,100)
                stress = random.randint(0,20)
                sanity = random.randint(40,100)
                horny = random.randint(0,50)
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
                #for trait in traits:
                #       if trait.name == 'Loves drugs':
                #               possible_drugs = [speed_addiction,opiates_addiction,cocaine_addiction]
                #               drug = random.choice(possible_drugs)
                #               drug.addiction_level = random.randint(2,5)

                addictions = Addictions(cocaine_addiction,opiates_addiction,speed_addiction,caffeine_addiction,nicotine_addiction)
                trauma = 0
                mind = Mind(happiness,stress,sanity,horny,addictions,trauma,morale)

                hunger,thirst,sleep = random.randint(3,20),random.randint(6,40),random.randint(50,95)

                #home
                home = 'None'

                if profession == "Security Guard":
                        outfit = dress_shirt
                        legwear = black_pants
                        footwear = combat_boots
                        handwear = black_gloves
                        outerwear  = no_outerwear
                        skills.rifle = random.randint(2,5)
			weapons = [pistol_9mm,shotgun_12g,ak47,uzi]
                        weapon = random.choice(weapons)
			if weapon.name == "9mm Pistol" or weapon.name == "Uzi":
				skills.pistol += random.randint(2,4)
                        elif weapon.name == "AK47":
                                skills.rifle += random.randint(2,4)
                        elif weapon.name == "12g Shotgun":
                                skills.shotgun += random.randint(2,4)


                        armor = body_armor
                elif profession == "Receptionist":
                        outfit = dress_shirt
                        legwear = suit_pants
                        footwear = dress_shoes
                        outerwear  = nice_suit
			weapon = punch
                elif profession == "Manager" or profession == "Office Worker":
                        outfit = dress_shirt
                        legwear = suit_pants
                        footwear = dress_shoes
                        outerwear  = nice_suit
                        weapon = punch
                elif profession == "Building Manager":
                        outfit = dress_shirt
                        legwear = suit_pants
                        footwear = dress_shoes
                        outerwear  = nice_suit
                        weapon = punch
                #bear mace chance
		roll = random.randint(1,6)
		if roll == 6:
			weapon = bear_mace
                #traits = set(traits)
                #traits = list(traits)
                #finally make the npc
                npc = Char(gender,age, profession,affiliation,health, npc_stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'enemy',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)

                return npc

	elif profession == "Gamer Assassin" or profession == "Flower Child" or  profession == "Pissboi Leader" or profession == "Pissboi Enforcer" or profession == 'Crankenstein' or profession == "Crankenstein Enforcer" or profession == "Crankenstein Leader" or profession == "Drunkard"  or profession == "Crackhead" or profession == "Drunkard" or profession == "Script Kiddie" or profession == "Crackhead" or profession == "Clerk" or profession == "Nudist" or profession == "Hobo" or  profession == "Rocker" or profession == "Marxist" or profession == 'Rude Boy' or profession == 'Grimesmacker' or profession == 'Cannibal' or profession == 'Slaver' or profession == 'Slave' or profession == 'Cat Person' or profession == 'Booze Knight' or profession == 'Anarchist'or profession == 'Mercenary' or profession == 'Occultist' or profession == 'Scavenger' or profession == 'Survivalist' or profession == "Drug Dealer" or profession == "Commando" or profession == "Skullhead":
		strength, base_strength = 9,9
		dexterity, base_dexterity = 8,8
		willpower, base_willpower = 9,9
		intelligence, base_intelligence = 10,10
		charisma, base_charisma = 9,9
		max_health = strength * 10	
		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100,50,5)
		health.current_stamina = random.randint(50,95)
		npc_stats = Stats(strength, dexterity, intelligence, willpower, charisma, base_strength, base_dexterity, base_intelligence,base_willpower,base_charisma)
		#injuries
		injuries = []
		#skills
		weapon = None
		#brawl
        	brawl = random.randint(1,3)
        	#computers
		computers = 0
		#dodge
        	dodge = random.randint(1,4)
		#disguise
        	disguise = random.randint(0,3) 
		#etiquette
        	etiquette = 0
		#explosives
        	explosives = random.randint(0,2)
		#first aid
        	first_aid = random.randint(0,2)
		#investigate
        	investigate = random.randint(0,3)
		if profession == "Crankenstein Leader" or profession == "Pissboi Leader":
			leadership = 9
		elif profession == "Marxist" or profession == "Commando" or profession == "Skullhead":
			leadership = random.randint(3,5)
			rifle = random.randint(3,5)
			weapon = ak47
                elif profession == "Pissboi" or profession == 'Grimesmacker' or profession == "Drug Dealer":
                        leadership = random.randint(3,5)
                        pistol = random.randint(3,5)
                        weapon = uzi
		elif profession == 'Slave':
			weapon = punch
			leadership = random.randint(0,1)
		elif profession == 'Anarchist':
			leadership = random.randint(1,3)
			weapon = molotov
			throw = random.randint(3,5)
		else:
        		leadership = random.randint(0,1)
		#lying
        	lying = random.randint(1,2)
		#negotiate
        	negotiate = 0
		if profession == "Crankenstein" or profession == "Crankenstein Leader" or profession == "Crankenstein Enforcer":
        		rifle = 6
                elif profession == "Pissboi Leader" or profession == "Pissboi Enforcer" or profession == "Gamer Assassin" or profession == "Flower Child":
                        rifle = 6
		else:
			rifle = 0
        	pickpocket = random.randint(0,3)
        	pistol = 0
        	persuasion = random.randint(1,2)
        	security = random.randint(0,3)
        	seduction = random.randint(0,2)
        	shotgun = random.randint(0,1)
        	stealth = 0
        	streetwise =  random.randint(1,3)
		survival = random.randint(0,2)
        	throw = random.randint(0,2)
        	torture = random.randint(0,1)
		trivia = random.randint(0,1)
                driving = random.randint(0,2)
                blade = random.randint(0,2)
                blunt = random.randint(0,2)

		skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
		lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
		skills_xp = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise,survival, throw, torture, trivia,driving,blade,blunt)
		#weapon
		weapons = [machete,brass_knuckles,knife,baseball_bat,pistol_9mm,shotgun_12g]
		if weapon == None:
			weapon = random.choice(weapons)
		if weapon.name == "Punch":
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
		elif weapon.name == 'Molotov':
			skills.throw = random.randint(2,5)
		#if profession == "Crankenstein" or profession == "Crankenstein Leader" or profession == "Crankenstein Enforcer" or profession == "Marxist" or 'Slaver':
		#	weapon = ak47
		#	skills.rifle = random.randint(3,5)
		#outfit
		possible_outfits = [tanktop,work_shirt,tshirt,plaid_shirt]
                outfit,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor = gen_player_outfit(profession,gender)

		if profession == "Crankenstein" or profession == "Crankenstein Leader" or profession == "Crankenstein Enforcer":
			head_options = [toque,baseball_cap,no_headwear]
			headwear = random.choice(head_options)
			armor = body_armor
			facewear = no_facewear
			eyewear = sunglasses
			footwear = light_boots
			legwear = ripped_jeans
			handwear = no_handwear
			outfit = random.choice(possible_outfits)
			outerwear = leather_jacket
			skills.pistol += 1
			weapon = uzi
                elif profession == "Pissboi" or profession == "Pissboi Leader" or profession == "Pissboi Enforcer":
                        headwear = cowboy_hat
                        outfit = plaid_shirt
                        eyewear = sunglasses
                        footwear = cowboy_boots
                        legwear = jeans
                        handwear = fingerless_gloves
		elif profession == "Marxist" or profession == "Commando" or profession == "Skullhead":
			outerwear = army_uniform
			outfit = tanktop
			if profession == "Marxist":
				headwear = red_beret
			else:
				headwear = army_hat
			if profession == "Skullhead":
				facewear = skull_mask
			else:
				facewear = balaclava
			eyewear = no_eyewear
			legwear = camo_pants
			handwear = black_gloves
			footwear = combat_boots
			armor = body_armor
			skills.rifle += random.randint(1,3)
			weapon = ak47
		elif profession == "Gamer Assassin":
			facewear = anonymous_mask
			headwear = fedora
		elif profession == "Nudist":
			outfit = naked
			legwear = no_legwear
			headwear = no_headwear
			footwear = sandals
			weapon = sword
			skills.blade += 2
			outerwear  = no_outerwear
		elif profession == 'Clerk':
			outerwear = cheap_suit
			outfit = dress_shirt
			legwear = suit_pants
			footwear = dress_shoes
			skills.lying = random.randint(2,5)
			skills.disguise = random.randint(2,5)
			skills.etiquette = random.randint(2,5)
			skills.computers = random.randint(2,5)
			skills.persuasion = random.randint(2,5)
		elif profession == 'Flower Child':
			outfit = tie_dye_shirt
			legwear = jeans
			footwear = sandals
		elif profession == 'Grimesmacker':
			facewear = clown_mask
                elif profession == "Slaver":
                        outfit = random.choice(possible_outfits)
                        legwear = camo_pants
			facewear = balaclava
                        headwear = army_hat
                        footwear = combat_boots
                        handwear = black_gloves
                        outerwear  = leather_jacket
			skills.rifle = random.randint(2,5)
			weapon = ak47
			armor = body_armor
		elif profession == 'Slave':
			weapon = punch
		elif profession == 'Cat Person':
			headwear = cat_ears
                elif profession == 'Anarchist':
                        headwear = balaclava
		elif profession == 'Survivalist':
			outerwear = army_uniform
			legwear = camo_pants
		#tool
		tool = None
		#traits
		traits = gen_player_traits(gender)
		if profession == 'Slaver':
			traits.append(tattoo_slaver)
		elif profession == 'Slave':
			traits.append(tattoo_slave)
		elif profession == 'Cat Person':
			if furry not in traits:
				traits.append(furry)
		#drugs
		drugs = []
		chance = 3
		roll = random.randint(1,6)
		if roll == 3:
			drugs_possible = [heroin,morphine,weed,speed,crack,cocaine]
			new_drug = random.choice(drugs_possible)
			drugs.append(new_drug)
		else:
			drugs = []
		#name
        	if gender == 'Male':
        	        fname = random.choice(male_fnames)
        	elif gender == "Female":
        	        fname = random.choice(female_fnames)
        	lname = random.choice(surnames)
		#money
		money = random.randint(100,400)
                combat_status = Combat_Status(False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,0,0,0,0,0,0)

                #mind
                happiness = random.randint(40,100)
                stress = random.randint(0,50)
                sanity = random.randint(40,100)
                horny = random.randint(0,50)
		morale = random.randint(1,50)
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
		
		hunger,thirst,sleep = random.randint(3,20),random.randint(6,40),random.randint(50,95)


		home = 'None'

                #traits = set(traits)
                #traits = list(traits)
		#finally make the npc
		npc = Char(gender,age, profession,affiliation,health, npc_stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'enemy',combat_status,home,mind,hunger,thirst,sleep,headwear,facewear,eyewear,handwear,legwear,footwear,outerwear,armor,None,None,False,None,False,None)
		return npc


workers = ['Telemarketer','Chatbot Operator','Fast Food Worker','Vlogger','Programmer','Janitor','Warehouse Worker','Housekeeper','Bike Courier', 'Nurse',
	'Hippie','Security Guard','Stripper','Mechanic']

#Cliff Heights


#abandoned_building_names = ['Abandoned Factory', 'Abandoned Office', 'Abandoned Store', 'Abandoned Laundromat','Abandoned Mall',
#			'Abandoned School','Abandoned Gas Station','Abandoned House',"Abandoned Church"]


#tech
class Tech:
	def __init__(self,name,base_value,can_loot,is_quest,number):
		self.name = name
		self.base_value = base_value
		self.can_loot = can_loot
		self.is_quest = is_quest
		self.number = number

water_purifer = Tech("Water purifier",4000,True,False,1)
medical_scanner = Tech("Medical scanner", 5000,True,False,1)
explosives = Tech("Explosives", 1500,True,False,5)
printer = Tech("3D printer", 6500,True,False,1)
holographic_projector = Tech("Holographic projector", 3500,True,False,1)
nanites = Tech("Nanites", 750,True,False,10)


#medical
class Medical:
	def __init__(self,name, base_value,number,item_type,can_loot,time_to_wear_off,nutrition,is_quest):
		self.name = name
		self.base_value = base_value
		self.number = number
		self.item_type = item_type
		self.can_loot = can_loot
		self.time_to_wear_off = time_to_wear_off
		self.nutrition = nutrition
		self.is_quest = is_quest

bandages = Medical('Bandages', 100,10,'medical',True,48,0,False)
morphine = Medical('Morphine', 100,1,'medical',True,4,0,False)
speed = Medical('Speed', 50,1,'medical',True,3,0,False)

speed_3g = Medical('Speed', 50,3,'medical',True,3,0,False)
speed_7g = Medical('Speed', 50,7,'medical',True,3,0,False)
speed_14g = Medical('Speed', 50,7,'medical',True,3,0,False)
speed_28g = Medical('Speed', 50,28,'medical',True,3,0,False)
speed_1000g = Medical('Speed', 50,1000,'medical',True,3,0,False)

crack = Medical('Crack', 80,1,'medical',True,3,0,False)
crack_3g = Medical('Crack', 80,3,'medical',True,3,0,False)
crack_7g = Medical('Crack', 80,7,'medical',True,3,0,False)
crack_14g = Medical('Crack', 80,14,'medical',True,3,0,False)
crack_28g = Medical('Crack', 80,28,'medical',True,3,0,False)
crack_1000g = Medical('Crack', 80,1000,'medical',True,3,0,False)

coffee = Medical('Coffee', 4,1,'medical',True,3,0,False)

cocaine = Medical('Cocaine', 100,1,'medical',True,3,0,False)
cocaine_3g = Medical('Cocaine', 100,3,'medical',True,3,0,False)
cocaine_7g = Medical('Cocaine', 100,7,'medical',True,3,0,False)
cocaine_14g = Medical('Cocaine', 100,14,'medical',True,3,0,False)
cocaine_28g = Medical('Cocaine', 100,28,'medical',True,3,0,False)
cocaine_1000g = Medical('Cocaine', 100,1000,'medical',True,3,0,False)



weed = Medical('Weed', 10,1,'medical',True,3,0,False)
weed_3g = Medical('Weed', 10,3,'medical',True,3,0,False)
weed_7g = Medical('Weed', 10,7,'medical',True,3,0,False)
weed_14g = Medical('Weed', 10,14,'medical',True,3,0,False)
weed_28g = Medical('Weed', 10,28,'medical',True,3,0,False)
weed_112g = Medical('Weed',10,112,'medical',True,3,0,False)
weed_1000g = Medical('Weed',10,1000,'medical',True,3,0,False)

heroin = Medical('Heroin', 90,1,'medical',True,3,0,False)
heroin_3g = Medical('Heroin', 90,3,'medical',True,3,0,False)
heroin_7g = Medical('Heroin', 90,7,'medical',True,3,0,False)
heroin_14g = Medical('Heroin', 90,14,'medical',True,3,0,False)
heroin_28g = Medical('Heroin', 90,28,'medical',True,3,0,False)
heroin_1000g = Medical('Heroin', 90,1000,'medical',True,3,0,False)

#withdrawls

opiate_withdrawl = Medical('Opiate withdrawl', 90,1,'medical',True,3,0,False)
cocaine_withdrawl = Medical('Cocaine withdrawl', 90,1,'medical',True,3,0,False)
speed_withdrawl = Medical('Speed withdrawl', 90,1,'medical',True,3,0,False)

#cravings
opiate_craving = Medical('Opiate craving', 90,1,'medical',True,3,0,False)
cocaine_craving = Medical('Cocaine craving', 90,1,'medical',True,3,0,False)
speed_craving = Medical('Speed craving', 90,1,'medical',True,3,0,False)

#food
hamburger = Medical('Hamburger', 8,1,'food',True,3,40,False)
fries = Medical('Fries', 4,1,'food',True,3,25,False)
pizza = Medical('Pizza', 4,1,'food',True,3,35,False)
chips = Medical('Chips', 2,1,'food',True,3,15,False)
chocolate_bar = Medical('Chocalate bar', 2,1,'food',True,3,20,False)
beef_jerky = Medical('Beef jerky', 3,1,'food',True,3,25,False)
peanuts = Medical('Peanuts', 3,1,'food',True,3,5,False)
candy = Medical('Candy', 3,1,'food',True,3,8,False)
corn_dog = Medical('Corn dog', 5,1,'food',True,3,10,False)
donut = Medical('Donut', 2,1,'food',True,3,5,False)

#weird food
human_jerky = Medical('Human jerky', 8,1,'food',True,3,40,False)

#drinks
cola = Medical('Cola', 2,1,'drink',True,3,50,False)
energy_drink = Medical('Energy drink', 3,1,'drink',True,3,40,False)
slurpy = Medical('Slurpy', 4,1,'drink',True,3,60,False)

drinks = [cola,energy_drink,slurpy]


#random wasteland location
def gen_wasteland(x,y):
        item_count = 1
        items = []
        num_items = random.randint(2,4)

        possible_items =  [tree,shrub,log,log,stream,rock]

        while item_count <= num_items:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1
#        items.append(desktop_computer)


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
	items = []
	regulars = []
	tree_count = 0
	num_tree = random.randint(2,8)
	while tree_count <= num_tree:
		trees = [tree,small_tree,shrub,log,tree,tree,tree,small_tree,bush,stream,rock]
		new_tree = random.choice(trees)
		items.append(new_tree)
		tree_count += 1
	print items
        building = Location('Wasteland','Templeville','Wasteland','Wasteland',x,y,actors,items,False,[],True,items,False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.items = items
        return building

#abandoned apt building
def gen_abandoned_apt_building(x,y,neighborhood_name):
	actors = NPC([],0,[],0)
	floors =[]
	rooms = []

	num_floors = 1
	rooms_per_floor = random.randint(4,24)
	floor1 = []
	floor2 = []
	room_count = 1
	print 'init appt building'
	#items = []
	while room_count <= rooms_per_floor:
		items = []
		possible_items =  [broken_desk,broken_light,broken_glass,broken_monitor,cat,copper_wire,hole_in_wall,hole_in_floor,toilet,old_newspaper,
        	office_chair,pile_of_rubble,smokeable_butt,trash]
		num_items = random.randint(4,8)
		item_count = 1
		while item_count <= num_items:
			item = random.choice(possible_items)
			items.append(item)
			item_count += 1
		is_vacant = random.randint(1,4)
		#items = []
		if is_vacant == 1:
			apt_name = 'Abandoned Apartment'
		        actors = NPC([],0,[],0)
			#items = []
			owned_by = 'No one'

		elif is_vacant != 1:
               		professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
               		profession = random.choice(professions)
			members = []
			member_valid = False
			while member_valid == False:
				try:
               				member = create_npc(profession,'none','None',None)
					print member
					member_valid = True
				except:
					member_valid = False
               		members.append(member)
			items.append(bed)
			#occupant_count += 1
			apt_name = member.fname + " " + member.lname + "'s squat" 
                        actors = NPC(members,0,[],0)
			owned_by = member.fname + " " + member.lname
			#actors = NPC([],0,[],0)
                #items.append(sink)
                #items.append(stove)
                #items.append(toilet2)
                #items.append(shower)

       		room = Location(apt_name,'Templeville',neighborhood_name,apt_name,x,y,actors,items,False,[],True,[],False,False,
       		[],13,23,False,[],False,[],False,False,'No one',[],[],None,True,[],1,False,0,0,no_dress_code,False,None,[],[])
		room.is_bar = False
		room.is_store = False
		room.is_apt = False
		rooms.append(room)
		room_count += 1
	print 'floors created'
	actors = NPC([],0,[],0)
        building = Location("Abandoned Apt. Building",'Templeville',neighborhood_name,'Abandoned Apt. Building',x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
	for room in building.rooms:
		#print room.name
		room.parent_location = building
		for actor in actors.members:
			print actor.fname
			actor.home = room
	print 'finished apt building'
        return building

##wasteland location
#def gen_random_wasteland(x,y):
 #       actors = NPC([],0,[],0)
#
 #       building = Location("Abandoned Apt. Building",'Templeville','Cliff Heights','Abandoned Apt. Building',x,y,actors,[],False,[],True,[],False,True,
#	        [],0,0,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None)

 #       return building


#abandoned buildings

def gen_abandoned_building(is_safehouse,locations,name,x,y,neighborhood_name):
	names = []

	where = ['Templeville','Cliff Heights','Abandoned Building']
	num_items = random.randint(4,11)
	possible_items =  [broken_desk,broken_light,broken_glass,broken_monitor,cat,copper_wire,hole_in_wall,hole_in_floor,toilet,old_newspaper,
	office_chair,pile_of_rubble,smokeable_butt,trash,barrel_fire]
	

	#actors
	members = []
	corpses = []
	roll = random.randint(1,2)
	if roll == 2:
		num_members = random.randint(1,4)

		items = []
		count = 1
		while count <= num_members:
			professions = ['Squatter', "Crimepunk", "Scumbag","Wastoid","Junkfreak","Lost Soul","Drunkard","Crackhead","Meatball","Hobo","Rocker","Sex Worker"]
			profession = random.choice(professions)
			member = create_npc(profession,'none','None',None)
			members.append(member)
			inventory = []
			if random.randint(1,3) == 3:
				new_items = [crack, weed,bandages,cocaine,speed,morphine,heroin]
				item_chosen = random.choice(new_items)
				inventory.append(item_chosen)
			else:
				inventory = []
			#roll = random.randint(1,20)
			fame = 20
			count += 1
		money = 0
		for member in members:
			money += member.start_money
		actors = NPC(members,money,inventory,fame)
		corpses = []
	else:
		actors = NPC([],0,[],0)
	#print actors
	item_count = 1
	items = []
	while num_items >= item_count:
		item = random.choice(possible_items)
		#print item.name
		items.append(item)
		#print item_count
		item_count += 1

#	x = random.randint(1,32)
#	y = random.randint(1,32)

	if is_safehouse == True:
		building = Location(str(name),'Templeville',neighborhood_name,'Abandoned Building',x,y,actors,items,True,corpses,False,[],False,False,[],0,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
	elif is_safehouse == False:
		building = Location(str(name),'Templeville',neighborhood_name,'Abandoned Building',x,y,actors,items,False,corpses,False,[],False,False,[],0,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
			
	
	return building

# pawn & gun
def gen_pawn_shop(x,y,neighborhood_name):
	actors = NPC([],0,[],0)
	name = gen_pawn_name()
	building = Location(name,'Templeville',neighborhood_name,name,x,y,actors,[counter,trash],False,[],True,
	[pistol_9mm,shotgun_12g,ak47,uzi,machete,pistol_9mm_ammo,shotgun_12g_ammo,uzi_ammo,ak47_ammo,body_armor,bear_mace,combat_boots,bicycle_helmet,army_helmet,clown_mask,leather_gloves,tent1,tent2,laptop_computer,microcontroller],True,False,[],8,19,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	owner = random.choice(weapons_corps)
	building.owned_by = owner.name
	return building	
#thrift shop
def gen_thrift_store(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

	building = Location("Thrift Store",'Templeville',neighborhood_name,'Thrift Store',x,y,actors,[counter,chair],False,[],True,[brass_knuckles,molotov,knife,baseball_bat,crowbar,shuriken,tshirt,tanktop,
	sweater,hoodie,jean_jacket,vest,bomber_jacket,cheap_suit,nice_suit,dress_shirt,hawaiian_shirt,work_shirt,plaid_shirt,trenchcoat,leather_jacket,army_uniform,nice_dress,shorts,jeans,track_pants,black_pants,camo_pants,sweat_pants,short_skirt,long_skirt,leggings,khakis,light_boots,running_shoes,dress_shoes,cowboy_boots,high_heels,sandals,baseball_cap,headband,dad_hat,toque,cowboy_hat,army_hat,fedora,balaclava,fingerless_gloves,black_gloves,sunglasses,sleeping_bag,rope,lighter],False,False,[],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.owned_by = united_solidarity.name
        return building
#bar
def gen_bar(x,y,name,neighborhood_name):
	actors = NPC([],0,[],0)

	regulars= []
	num_regulars = random.randint(10,22)
	count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
	        	professions = ["Flower Child", "Gamer Assassin","Crimepunk", "Pissboi","Wastoid","Junkfreak","Meatball","Crankenstein","Crackhead","Script Kiddie","Sex Worker","Lost Soul","Drunkard","Clerk","Nudist","Rocker","Mercenary",'Occultist','Scavenger','Survivalist']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
		if profession == "Crankenstein" or profession == "Pissboi" or profession == "Flower Child" or profession == "Gamer Assassin"or profession == "Clerk" or profession == "Nudist" or profession == 'Cat Person':
                	regular = create_npc(profession,'none','None',None)
		else:
			regular = create_npc(profession,'none','None',None)
			
                regulars.append(regular)
                if random.randint(1,3) == 3:
         		inventory = [morphine,crack,speed,heroin]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

	building = Location(name,'Templeville',neighborhood_name,'Abandoned Building',x,y,actors,[bar_stool,bar_stool,bar_stool,bar_stool,counter,booth,booth,
	booth, booth],False,[],True,[beer,cola,hamburger,fries],False,False,[],11,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	return building

#doctor

heal_injuries = Service("heal injuries",5000,"heal all the characters injuries")
max_health = Service("restore health",500,"restore character to max health")
#cosmetic
tattoos = Service("tattoos",0,"tattoos")
haircuts = Service("haircuts",0,"haircuts")
#laundry
laundromat = Service("laundry",0,"laundry")

def gen_general_store(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

        building = Location("General store",'Templeville',neighborhood_name,'Doctor',x,y,actors,[counter],False,[],True,[cola,energy_drink,peanuts,human_jerky,sleeping_bag,knife,rope,tent1,shovel],False,True,
        [],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
        return building


def gen_laundromat(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

        building = Location("Laundromat",'Templeville',neighborhood_name,'Laundromat',x,y,actors,[counter],False,[],True,[],False,True,
        [laundromat],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
        return building
def gen_tattoo_shop(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

        building = Location("Tattoo shop",'Templeville',neighborhood_name,'Doctor',x,y,actors,[counter],False,[],True,[],False,True,
        [tattoos],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
        return building
def gen_barber_shop(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

        building = Location("Barber shop",'Templeville',neighborhood_name,'Doctor',x,y,actors,[counter],False,[],True,[],False,True,
        [haircuts],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
        return building
def gen_doctor(x,y,neighborhood_name):
        actors = NPC([],0,[],0)

        building = Location("Doctor",'Templeville',neighborhood_name,'Doctor',x,y,actors,[counter],False,[],True,[bandages,heroin,speed],False,True,
	[heal_injuries],13,23,False,[],False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.owned_by = random.choice(real_estate_corps)
        return building

#crackhouse
def gen_crackhouse(x,y,neighborhood_name):
	item_count = 1
	items = []
        num_items = random.randint(4,11)
        possible_items =  [broken_desk,broken_light,broken_glass,cat,hole_in_wall,hole_in_floor,office_chair,pile_of_rubble,smokeable_butt,trash,dirty_couch,stained_couch,stinky_couch]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
                	professions = ["Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Hobo','Wastoid','Rocker','Squatter',"Mercenary",'Occultist','Scavenger','Survivalist']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
		affiliation = 'none'
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [crack]
                else:
                        inventory = []
		for regular in regulars:
			regular.drugs = [crack]
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Crack House','Templeville',neighborhood_name,'Crack House',x,y,actors,items,False,[],True,[crack],False,False,[],1,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
        return building
#coffee shop
def gen_coffee_shop(x,y,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(4,11)
        possible_items =  [counter,table]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
                	professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Hobo','Squatter','Rocker',"Mercenary",'Occultist','Scavenger','Survivalist']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Coffee Shop','Templeville',neighborhood_name,'Coffee Shop',x,y,actors,items,False,[],True,[crack],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
	building.owned_by = starfucks
        return building

def gen_mcshits(x,y,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(4,11)

        possible_items =  [counter,table]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
                	professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Hobo','Rocker','Squatter',"Mercenary",'Occultist','Scavenger','Survivalist']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [cocaine,heroin,morphine,weed]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('McShits','Templeville',neighborhood_name,'McShits',x,y,actors,items,False,[],True,[hamburger,fries,cola],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
	building.owned_by = mcshits
        return building

def gen_pizza_place(x,y,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(4,11)

        possible_items = [counter,table]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
                	professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Hobo']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [weed]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('World Famous Pizza','Templeville',neighborhood_name,'World Famous Pizza',x,y,actors,items,False,[],True,[pizza,fries,cola],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
        building.owned_by = pizza_corp
	return building

#convenience store
def gen_convenience_store(x,y,neighborhood_name):
	corp = quikmart
        item_count = 1
        items = []
        num_items = random.randint(4,11)

        possible_items = [counter,table]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
		roll = random.randint(1,2)
		if roll == 1:
                	professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Hobo','Rocker',"Mercenary",'Occultist','Scavenger','Survivalist']
		elif roll == 2:
			professions = workers
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,weed,crack,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Convenience store','Templeville',neighborhood_name,'Convenience store',x,y,actors,items,False,[],True,[cola,energy_drink,chocolate_bar,candy,chips,peanuts,beef_jerky,corn_dog],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
	building.owned_by = corp.name
        return building



#library
def gen_library(x,y,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(4,11)

        possible_items =  [counter,table,desktop_computer]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1
        items.append(desktop_computer)


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,crack,speed,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Public Library','Templeville',neighborhood_name,'Public Library',x,y,actors,items,False,[],True,[library_card],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,True,[],[])
        return building

def create_stash(power):
        num_items = random.randint((power /3),power)
        count = 1
        items = []
        while count <= num_items:
                possible_items = [crack_14g,crack_28g,pistol_9mm,shotgun_12g,uzi,speed_28g,speed_14g,ak47,cocaine_14g,cocaine_28g,weed_28g,weed_112g]
                item = random.choice(possible_items)
                items.append(item)
                count += 1
        return items


#gang hq
def gen_gang_hq(x,y,name,locations,neighborhood_name):
	print 'init'
        item_count = 1
        items = []
        num_items = random.randint(4,10)

        possible_items =  [table,dirty_couch,stinky_couch,sound_system,strobe_light,bong]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1
	print 'items'
        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(20,30)
        count = 1
	power = None
        #while count <= num_regulars:
        #        professions = ["Crankenstein","Crimepunk"]
	#	profession = random.choice(professions)
        #        regular = create_npc(profession,'none','None')
        #        regulars.append(regular)
        #        if random.randint(1,3) == 3:
        #        	inventory = [morphine]
        #        else:
        #                inventory = []
        #        fame = 20
        #        money = 5
        #        count += 1
        #        regulars = NPC(regulars,money,inventory,fame)
	if name == "Crankensteins":
		power = 15
	        while count <= num_regulars:
	                professions = ["Crankenstein"]
	                profession = random.choice(professions)
	                regular = create_npc(profession,'profession','None',None)
	                regulars.append(regular)
	                inventory = []
	                fame = 20
	                money = 5
	                count += 1
			items_sold = [speed_7g,speed_14g,speed_28g,uzi,ak47]
        elif name == "Pissbois":
		power = 15
                while count <= num_regulars:
                        professions = ["Pissboi"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',"Male")
                        regulars.append(regular)
			items_sold = [crack_7g,crack_14g,crack_28g,sword]
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Gamer Assassins":
		power = 15
                while count <= num_regulars:
                        professions = ["Gamer Assassin"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = [speed_7g,speed_14g,speed_28g,cocaine_14g,cocaine_28g]

                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Flower Collective":
		power = 18
                while count <= num_regulars:
                        professions = ["Flower Child"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = [weed,weed_3g,weed_7g,weed_28g,weed_112g]

                        fame = 20
                        money = 5
                        count += 1
	elif name == "Clerks":
		power = 15
		while count <= num_regulars:
                        professions = ["Clerk"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = [cocaine_7g,cocaine_14g,cocaine_28g]

                        inventory = []
                        fame = 20
                        money = 500
                        count += 1
        elif name == "Nudists":
		power = 13
		while count <= num_regulars:
                        professions = ["Nudist"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
			items_sold = []
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Red Faction":
		power = 17
                while count <= num_regulars:
                        professions = ["Marxist"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = []

                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
			#power = 15
        elif name == "Rude Boys":
                power = 19
                while count <= num_regulars:
                        professions = ["Rude Boy"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',"Male")
                        regulars.append(regular)
                        items_sold = []

                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
                        #power = 15

        elif name == "Grimesmackers":
		power = 19
                while count <= num_regulars:
                        professions = ["Grimesmacker"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
			items_sold = [speed,speed_3g,speed_7g,speed_14g,heroin,heroin_3g,heroin_7g,cocaine,cocaine_3g,cocaine_7g]
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Cannibals":
		power = 4
                while count <= num_regulars:
                        professions = ["Cannibal"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = []

                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Slavers":
		power = 18
                while count <= num_regulars:
                        professions = ["Slaver",'Slave']
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = []

                        fame = 20
                        money = 5
                        count += 1
        elif name == "Cat People":
		power = 15
                while count <= num_regulars:
                        professions = ["Cat Person"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = []

                        fame = 20
                        money = 5
			count += 1
        elif name == "Booze Knights":
                power = 18
                while count <= num_regulars:
                        professions = ["Booze Knight"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = []

                        fame = 20
                        money = 5
                        count += 1

        elif name == "Anarchists":
		power = 19
                while count <= num_regulars:
                        professions = ["Anarchist"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = [molotov]

                        fame = 20
                        money = 5
                        count += 1
        elif name == "Sex Cult":
		power = 6
                while count <= num_regulars:
                        professions = ["Occultist","Hipster","Slave"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        inventory = []
                        items_sold = []

                        fame = 20
		
                        money = 5
                        count += 1
        elif name == "Patriot Nazis":
		power = 20
                while count <= num_regulars:
                        professions = ["Survivalist","Biker","Scumbag"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = [cocaine_14g,cocaine_28g,heroin_14g,heroin_28g,speed_28g,speed_14g,weed_112g]

                        items_sold = []

                        fame = 20
                        money = 5
			power = 5
                        count += 1
                        count += 1
        elif name == "Hell's Satans":
                power = 10
                while count <= num_regulars:
                        professions = ["Biker"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',"Male")
                        regulars.append(regular)
                        items_sold = [cocaine_14g,cocaine_28g,heroin_14g,heroin_28g,speed_28g,speed_14g,weed_112g]

                       # items_sold = []

                        fame = 20
                        money = 5
                        power = 5
                        count += 1
        elif name == "Skullheads":
                power = 4
                while count <= num_regulars:
                        professions = ["Skullhead"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None',None)
                        regulars.append(regular)
                        items_sold = []

                       # items_sold = []

                        fame = 20
                        money = 5
                        #power = 12
                        count += 1
	print 'chars'
	if power == None:
		power = random.randint(4,7)

	#amount_sold = random.randint(2,power)
	print 'stuff sold'
	possible_items = [pistol_9mm,shotgun_12g,ak47,crack_7g,crack_14g,crack_28g,morphine,speed_7g,speed_14g,speed_28g,body_armor,cocaine_3g,cocaine_7g,cocaine_14g,cocaine_28g,weed_3g,weed_7g,weed_14g,weed_28g,weed_112g]
	
	item_count = 1
	
	print 'stash'
	stash_items = create_stash(power)
	money = random.randint(2000,10000)
	stash = Container(name + ' Stash','container',stash_items,money,False,power,20000,10000,True,False,0)
	items.append(stash)


	building = Location(name + ' HQ','Templeville',neighborhood_name, name + ' HQ',x,y,actors,items,False,[],True,items_sold,False,False,[],6,23,True,regulars,False,[],False,True,name,[],[],None,False,[],1,True,power,0,no_dress_code,False,None,False,[],[])
	print 'HQ created'
#name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory)
#	max_locations = 12
	
#	if x - power >= 1:
#		top_left_x = x - power
#	else:
#		top_left_x = 1
#	if y - power >= 1:
#		top_left_y = y - power
#	else:
#		top_left_y = 1
#	if x + power <= 16:
#		bottom_right_x = x + power
#	else:
#		bottom_right_x = 20
#	if y + power >= 16:
#		bottom_right_y = y + power
#	else:
#		bottom_right_y = 20
 #       territory = Territory(top_left_x,top_left_y,bottom_right_x,bottom_right_y)

	locations_owned = [building]
	locations.append(building)
	location_count = 1
	finished_assigning = False
	if len(locations_owned) <= power:
		while location_count <= power:
			try:
				location = random.choice(locations)
				if location.owned_by == "No one":
					location.owned_by = name
      					locations_owned.append(location)
       					location_count += 1
					location_valid = True
				else:
					location_count += 1
			except:
				location_count += 1
				location_valid = True
		

	print 'locations assigned'
	territory = []
	footsoldiers = []
	for regular in regulars:
		footsoldier = [regular, 'No orders']
		footsoldiers.append(footsoldier)
	print 'footsoldiers added'
	organization = Organization(name,False,footsoldiers,0,building,locations_owned,power,[],[],False,0,False,[],0,0,0,0,0,0,0,0,0,0,0,0)
#self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid
        return building, organization

def gen_office(x,y,corp,type,neighborhood_name):
        rooms = []
        floors = []
        actors = NPC([],0,[],0)
        num_rooms = random.randint(4,6)
	num_floor = random.randint(4,15)
	security_level = random.randint(2,7)
        room_count = 1
	floor_count = 1
	print 'init office'
	while floor_count <= num_floor and num_rooms <= 75:
		room_count = 1
		while room_count <= num_rooms:
			room_chance = random.randint(1,7)
			if floor_count >= 8:
				security_level = security_level * 5
	                items = []
			hidden_item = None
			if room_chance != 1:
				chance_manager = random.randint(1,7)
				if chance_manager == 1:
					profession = 'Manager'
					possible_hidden_items = [client_list,company_plans,meeting_minutes,confidential_memo,payroll,cocaine_3g]
					hidden_item = random.choice(possible_hidden_items)
				else:
					if type == 'Troll Farm':
						professions = ['Programmer','Chatbot Operator','Receptionist',"Office Worker"]
		                		profession = random.choice(professions)
					elif type == 'Call Centre':
						professions = ['Telemarketer',"Office Worker"]
						profession = random.choice(professions)
					elif type == 'Data Mine':
						professions = ['Data Miner','Office Worker']
						profession = random.choice(professions)

					elif type == "Office Building":
						profession = "Office Worker"
       		        	members = []
        	        	member = create_npc(profession,'none','None',None)
				member.affiliation = corp.name
        	        	members.append(member)
        	        	items.append(desk)
               			items.append(chair)
                		items.append(desktop_computer)
	                	apt_name = member.fname + " " + member.lname + "'s office" 
       		        	actors = NPC(members,0,[],0)
                		owned_by = corp.name
                		room = Location(apt_name,'Templeville',neighborhood_name,apt_name,x,y,actors,items,False,[],True,[],False,False,
                		        [],13,23,False,[],False,[],False,False,'No one',[],[],None,True,[],floor_count,False,security_level,0,office_dress_code,False,None,True,[],[])
				room.regulars = members

				room.is_store = True
				room.time_open = 9
				room.time_close = 17
				if hidden_item != None:
					room.hidden_items.append(hidden_item)
                		rooms.append(room)
                		room_count += 1
			elif room_chance == 1:
                        #if room_chance != 1:
                                members = []
                                #member = create_npc(profession,'none','None')
                                #member.affiliation = corp.name
                                #members.append(member)
                                #items.append(desk)
                                #items.append(chair)
				num_server = random.randint(4,10)
				server_count = 1
				while server_count <= num_server:
					items.append(server)
					server_count += 1
                                items.append(server)
                                apt_name = "Server room" 
                                actors = NPC(members,0,[],0)
                                owned_by = corp.name
                                room = Location(apt_name,'Templeville','Cliff Heights',apt_name,x,y,actors,items,False,[],True,[],False,False,
                                        [],13,23,False,[],False,[],False,False,'No one',[],[],None,True,[],floor_count,False,security_level,0,office_dress_code,False,None,True,[],[])
                                room.regulars = members

                                room.is_store = True
                                room.time_open = 9
                                room.time_close = 17
                                if hidden_item != None:
                                        room.hidden_items.append(hidden_item)
                                rooms.append(room)
                                room_count += 1

		floor_count += 1
	print 'rooms created'
        building_name = type 
        members = []
        member = create_npc('Building Manager','none','None',None)
	member.affiliation = corp.name
        members.append(member) 
        guard_amount = random.randint(2,6) 
        guard_count = 0
        while guard_count <= guard_amount:
                member = create_npc('Security Guard',corp.name,'None',None)
		member.affiliation = corp.name
                members.append(member) 
                guard_count += 1 
	print 'security created'
        actors = NPC(members,0,[],0)
        building = Location(building_name,'Templeville','Cliff Heights',building_name,x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,corp.name,[],floors,None,False,[],1,True,security_level,0,office_dress_code,False,None,False,[],[])
	building.is_store = True
	building.time_open = 9
	building.time_close = 17
	building.regulars = members
        for room in building.rooms:
                #print room.name
                room.parent_location = building
                for actor in actors.members:
                        #print actor.fname
                        actor.home = room
	print 'office finished'
        return building


def gen_data_mine(x,y,corp,neighborhood_name):
	rooms = []
	floors = []
        actors = NPC([],0,[],0)
	num_floors = random.randint(4,10)
	num_rooms = random.randint(4,10)
	floor_count = 1
	while floor_count <= num_floors:
		room_count = 1
		while room_count <= num_rooms:
			items = []
			chance_manager = random.randint(1,7)
			if chance_manager == 1:
				profession = 'Manager'
			else:
				profession = 'Data Miner'
        	        members = []
                	member = create_npc(profession,'none','None',None)
			member.affiliation = corp.name
                	members.append(member)
			items.append(desk)
			items.append(chair)
			items.append(desktop_computer)
                	apt_name = member.fname + " " + member.lname + "'s office" 
                	actors = NPC(members,0,[],0)
                	owned_by = corp.name
                	room = Location(apt_name,'Templeville','Cliff Heights',apt_name,x,y,actors,items,False,[],True,[],False,False,
	        	        [],13,23,False,[],False,[],False,False,'No one',[],[],None,True,[],floor_count,False,5,0,office_dress_code,False,None,True,[],[])
			rooms.append(room)
			room_count += 1
		floor_count +=1
        building_name = 'Data Mine(' + corp.name + ')'

        members = []
        member = create_npc('Receptionist','none','None',None)
	member.affiliation = corp.name
        members.append(member)
	guard_amount = random.randint(1,4) 
	guard_count = 0
	while guard_count <= guard_amount:
        	member = create_npc('Security Guard','none','None',None)
		member.affiliation = corp.name
        	members.append(member)
		guard_count += 1 
        actors = NPC(members,0,[],0)
        building = Location(building_name,'Templeville',neighborhood_name,building_name,x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,corp.name,[],floors,None,False,[],1,True,2,0,office_dress_code,False,None,False,[],[])
        for room in building.rooms:
                #print room.name
                room.parent_location = building
                for actor in actors.members:
                        #print actor.fname
                        actor.home = room
	return building

def gen_house(x,y,neighborhood_name,type):
        actors = NPC([],0,[],0)
        floors =[]
        rooms = []
        #print 'apt building'
        num_floors = 2
        max = 5
        max_rooms = max
        floor1 = []
        floor2 = []
        room_count = 1
	finished = False
	owner = None
        #items = []
        floor_count = 1
        while finished == False:
		if floor_count == 1:
                	#room_count = 1
			has_bathroom = False
			has_bedroom = False
			has_dining_room = False
			has_living_room = False
		        actors = NPC([],0,[],0)
			bathroom = Location('Bathroom','Templeville',neighborhood_name,"Bathroom",x,y,actors,[toilet2,sink,shower],False,[],True,[],False,False,
                                	[],0,0,False,[],False,[],False,False,'No one',[],[],None,True,[],floor_count,False,0,0,no_dress_code,False,None,True,[],[])
			chance_owner = random.randint(1,2)
                        spare_bedroom = Location('Spare bedroom','Templeville',neighborhood_name,"Bedroom",x,y,actors,[bed,dresser,chair,heater],False,[],True,[],False,False,
                                        [],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],1,False,0,0,no_dress_code,False,None,True,[],[])

			if type == "family":
	                        actors = NPC([],0,[],0)

				members = []
                        	roll = random.randint(1,6)
                                if roll == 1:
                                	professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Drug Dealer","Biker"]
                                        for worker in workers:
                                        	professions.append(worker)
                                else:
                                        professions = workers
                                profession = random.choice(professions)
                                members = []
                                member = create_npc(profession,'none','None',None)
				if owner == None:
					owner = member.fname + " " + member.lname
                                members.append(member)

				if member.gender == "Male":
	                                roll = random.randint(1,6)
	                                if roll == 1:
        	                                professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Drug Dealer","Biker"]
                	                        for worker in workers:
                        	                        professions.append(worker)
                        	        else:
                        	                professions = workers
                        	        profession = random.choice(professions)
	                                member = create_npc(profession,'none','None',"Female")
					members.append(member)
                                elif member.gender == "Female":
                                        roll = random.randint(1,6)
                                        if roll == 1:
                                                professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Drug Dealer","Biker"]
                                                for worker in workers:
                                                        professions.append(worker)
                                        else:
                                                professions = workers
                                        profession = random.choice(professions)
                                        member = create_npc(profession,'none','None',"Male")
                                        members.append(member)


				actors.members = members




                        bedroom = Location('Bedroom','Templeville',neighborhood_name,"Bedroom",x,y,actors,[bed,dresser,tv,bookshelf,desk,chair,heater],False,[],True,[],False,False,
                                	[],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],2,False,0,0,no_dress_code,False,None,True,[],[])
                        actors = NPC([],0,[],0)

			living_room = Location('Living room','Templeville',neighborhood_name,"Living room",x,y,actors,[tv,couch,desk,rug,coffee_table,chair,chair,heater],False,[],True,[],False,False,
                        	        [],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],floor_count,False,0,0,no_dress_code,False,None,True,[],[])
			living_room.is_bar = True
                        kitchen = Location('Kitchen','Templeville',neighborhood_name,"Kitchen",x,y,actors,[sink,stove,fridge],False,[],True,[],False,False,
                                        [],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],2,False,0,0,no_dress_code,False,None,True,[],[])
                        dining_room = Location('Dining room','Templeville',neighborhood_name,"Dining room",x,y,actors,[dining_table,chair,chair,chair,chair],False,[],True,[],False,False,
                                        [],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],2,False,0,0,no_dress_code,False,None,True,[],[])
                        basement = Location('Basement','Templeville',neighborhood_name,"Dining room",x,y,actors,[chair],False,[],True,[],False,False,
                                        [],0,0,False,[],False,[],False,False,owner,[],[],None,True,[],-1,False,0,0,no_dress_code,False,None,True,[],[])

			rooms.append(living_room)
			rooms.append(bathroom)
			rooms.append(spare_bedroom)
			rooms.append(bedroom)
			rooms.append(dining_room)
			rooms.append(kitchen)
			rooms.append(basement)
		
			floor_count += 1
		finished = True

        building = Location('House','Templeville',neighborhood_name,'House',x,y,actors,[],False,[],True,[],False,True,
        [],0,0,False,[],False,rooms,False,False,owner,[],floors,None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.security_level = 0
	building.is_bar = False
	building.is_store = False
        for room in building.rooms:
                #print room.name
		room.security_level = 0
		room.is_bar = False
		room.is_store = False
                room.parent_location = building
                for actor in actors.members:
                        #print actor.fname
                        actor.home = room
	return building
def gen_apt_building(x,y,neighborhood_name):
        actors = NPC([],0,[],0)
	floors =[]
	rooms = []
	#print 'apt building'
	num_floors = random.randint(4,8)
	max = 10
	max_rooms = max
	floor1 = []
	floor2 = []
	room_count = 1
	#items = []
	floor_count = 1
	while floor_count <= num_floors:
		room_count = 1
		while room_count <= max_rooms:
			try:
				is_vacant = random.randint(1,7)
				items = []
				if is_vacant == 1:
					apt_name = 'Vacant Apartment'
				        actors = NPC([],0,[],0)
					items = []
					owned_by = 'No one'

				elif is_vacant != 1:
					roll = random.randint(1,6)
					if roll == 1:
               					professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Drug Dealer","Biker"]
						for worker in workers:
							professions.append(worker)
					else:
						professions = workers
        	       			profession = random.choice(professions)
					members = []
               				member = create_npc(profession,'none','None',None)
               				members.append(member)
					items.append(bed)
					#occupant_count += 1
					apt_name = member.fname + " " + member.lname + "'s apartment" 
               	        		actors = NPC(members,0,[],0)
					owned_by = member.fname + " " + member.lname
					items.append(bed)
					items.append(table)
					items.append(chair)
                       	 		items.append(chair)
					#items.append(shower)
					#items.append(heater)
					#items.append(toilet)
					if roll != 1:
						items.append(desk)
						comp = random.randint(1,2)
						if comp == 1:
							items.append(laptop)
						elif comp == 2:
							items.append(tablet)
						bookshelf_chance = random.randint(1,2)
						if bookshelf_chance == 1:
							items.append(bookshelf)
						smartphone_chance = random.randint(1,2)
						if smartphone_chance == 1:
							items.append(smartphone)
					rug_chance = random.randint(1,2)
					if rug_chance == 1:
						items.append(rug)
				
					#actors = NPC([],0,[],0)
                			items.append(sink)
                			items.append(stove)
                			items.append(toilet2)
                			items.append(shower)
					items.append(heater)
					bike_chance = random.randint(1,6)
					if bike_chance == 1:
						bikes= [bmx_bike,mountain_bike]
						bike = random.choice(bikes)
						items.append(bike)
				hidden_items = []
				chance_hidden_items = random.randint(1,4)
                #chance_hidden_items = 1

				if chance_hidden_items == 1:
					num_hidden_items = random.randint(1,4)
					count = 1
					while count <= num_hidden_items:
						if roll == 1:
							possible_hidden_items = [pistol_9mm,shotgun_12g,uzi,ak47,body_armor,cocaine_14g,crack_14g,speed_14g,heroin_14g,weed_28g,weed_112g]
						else:
							possible_hidden_items(pistol_9mm,weed_28g,cocaine_14g,nice_suit,nice_dress)
						hidden_item = random.choice(possible_hidden_items)
						hidden_items.append(hidden_item)
						count += 1
				if profession == "Drug Dealer":
					possible_drugs = [crack_28g,speed_28g,cocaine_28g,heroin_28g]
					num_drugs = random.randint(2,10)
					member.money = random.randint(500,2000)
					drug_count = 1
					drugs = []
					while drug_count <= num_drugs:
						drug = random.choice(possible_drugs)
						items.append(drug)
						drug_count += 1
					money = random.randint(3000,10000)
					stash = Container(member.fname + ' Stash','container',drugs,money,True,5,20000,10000,True,False,0)
					items.append(stash)

       				room = Location(apt_name,'Templeville',neighborhood_name,apt_name,x,y,actors,items,False,[],True,[],False,False,[],13,23,False,[],False,[],False,False,'No one',[],[],
				None,True,hidden_items,floor_count,False,4,0,no_dress_code,False,None,True,[],[])
				room.is_bar = False
				room.is_store = False
				rooms.append(room)
				room_count += 1
			except:
				room_count  = room_count
		floor_count += 1
	building_name = gen_apt_name()
	actors = NPC([],0,[],0)
        building = Location(building_name,'Templeville',neighborhood_name,building_name,x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,False,[],1,True,2,0,no_dress_code,False,None,False,[],[])
	building.time_open = 9
	building.time_close = 17
	#is owned by corp
	chance_corp = 1
	if chance_corp == 1:
		owned_by_corp = random.choice(real_estate_corps)
		building.owned_by  = owned_by_corp.name
        members = []
        member = create_npc('Building Manager','none','None',None)

        member.affiliation = owned_by_corp.name
        members.append(member) 
        guard_amount = random.randint(1,6) 
        guard_count = 0
        while guard_count <= guard_amount:
                member = create_npc('Security Guard','none','None',None)
                member.affiliation = owned_by_corp.name
                members.append(member) 
                guard_count += 1 
	building.actors.members = members
	for room in building.rooms:
		#print room.name
		room.parent_location = building
		for actor in actors.members:
			#print actor.fname
			actor.home = room
        return building

#shack
def gen_shack(x,y,neighborhood_name):
        actors = NPC([],0,[],0)
	floors =[]
	rooms = []


	num_occupants = random.randint(1,4)
	floor1 = []
	floor2 = []
	occupant_count = 1
	#items = []
	members = []
	first = True
	owner = None
	while occupant_count <= num_occupants:
		items = []
   		professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Biker","Survivalist"]
        	profession = random.choice(professions)
		#members = []
		verified = False
		while verified == False:
			try:
           			member = create_npc(profession,'none','None',None)
           			verified = True
           		except:
           			verified = False
           	if first == True:
			owner = member
			first = False
                #owned_by = member.fname + " " + member.lname

           	members.append(member)
		#items.append(bed)
		#unt += 1
		apt_name = 'Shack'
                actors = NPC(members,0,[],0)
		#owned_by = member.fname + " " + member.lname
		items.append(bed)
		items.append(table)
		items.append(chair)
                #items.append(chair)
		#rug_chance = random.randint(1,2)
		#if rug_chance == 1:
		#	items.append(rug)
		#actors = NPC([],0,[],0)
		occupant_count += 1
	items.append(barrel_fire)
	hidden_items = []
        chance_hidden_items = random.randint(1,3)
        #chance_hidden_items = 1

        if chance_hidden_items == 1:
        	num_hidden_items = random.randint(1,4)
                count = 1
                while count <= num_hidden_items:
                	possible_hidden_items = [pistol_9mm,shotgun_12g,uzi,ak47,body_armor,cocaine_28g,crack_28g,heroin_28g,speed_28g,weed_112g]
                        hidden_item = random.choice(possible_hidden_items)
                        hidden_items.append(hidden_item)
			count += 1

	#rooms = floor1
	actors = NPC(members,0,[],0)
    	building = Location(apt_name,'Templeville',neighborhood_name,'House',x,y,actors,items,False,[],True,[],False,True,
    	[],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,True,hidden_items,1,True,0,0,no_dress_code,False,None,True,[],[])
	building.is_bar = False
	building.is_store = False
	building.time_open = 1
	building.time_close = 21
	if owner != None:
		building.owned_by = owner.fname + " " + owner.lname
        for room in building.rooms:
                #print room.name
		room.rooms = building.rooms
                room.parent_location = building
                for actor in actors.members:
                        print actor.fname
                        actor.home = room
	#building.owned_by = owned_by
	#for room in building.rooms:
	#	room.rooms = building.rooms
	

    	return building

#park
def gen_park(x,y,name,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(4,6)
        possible_items =  [small_tree,tree,fountain,dog]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(10,22)
        count = 1
        while count <= num_regulars:
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Rocker",'Cannibal','Slaver','Marxist','Rude Boy','Grimesmacker','Scavenger','Occultist','Survivalist','Mercenary']
		for worker in workers:
			professions.append(worker)
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,crack,speed,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)
	name = gen_park_name()
        building = Location(name,'Templeville',neighborhood_name,name,x,y,actors,items,False,[],True,[crack],False,False,[],3,4,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.is_indoors = False
        return building

#park
def gen_graveyard(x,y,name,neighborhood_name):
        item_count = 1
        items = []
        num_items = random.randint(14,20)
        possible_items =  [small_tree,tree,fountain,dog,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave,grave]

        while num_items >= item_count:
                item = random.choice(possible_items)
                #print item.name
                items.append(item)
                #print item_count
                item_count += 1


        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(5,10)
        count = 1
        while count <= num_regulars:
                professions = ["Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker",'Scavenger','Occultist','Survivalist', "Occultist"]
                #for worker in workers:
                        #professions.append(worker)
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None',None)
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,crack,speed,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)
        #name = gen_park_name()
        building = Location(name,'Templeville',neighborhood_name,name,x,y,actors,items,False,[],True,[crack],False,False,[],3,4,True,regulars,False,[],False,False,'No one',[],[],None,False,[],1,True,0,0,no_dress_code,False,None,False,[],[])
	building.is_indoors = False
        return building

#abandoned apt building

def gen_neighborhood(type,neighborhood_name,flag):
	global location_id
	if flag == "temple":
		max_x = 8
		max_y = 8
	else:
		max_y = 32
		max_x = 32
	organizations = []
        organization = Organization(neighborhood_name,False,[],0,None,[],0,[],[],False,0,False,[],0,0,0,0,0,0,0,0,0,0,0,0)
        organizations.append(organization)
	num_locations = 0
	num_abandoned_apt = 0
	locations = []
	count = 1
	first_building = True
	#abandoned buildings
	name = 'Abandoned Building'
	if neighborhood_name == 'Cliff Heights':
		num_abandoned_buildings = random.randint(6,11)
		num_abandoned_apt = 8
        elif neighborhood_name == 'Bad Town':
                num_abandoned_buildings = random.randint(20,21)
	elif neighborhood_name == 'Elephant Rock':
		num_abandoned_buildings = random.randint(14,20)
        elif neighborhood_name == "Bastard's Cove":
                num_abandoned_buildings = random.randint(20,24)
        elif neighborhood_name == "The Scabs":
                num_abandoned_buildings = random.randint(17,20)
        elif neighborhood_name == "Bernal Park":
                num_abandoned_buildings = random.randint(17,20)
        elif neighborhood_name == "Maplewood":
                num_abandoned_buildings = random.randint(17,20)
        elif neighborhood_name == "Rose Heights":
                num_abandoned_buildings = random.randint(4,6)
        elif neighborhood_name == "McQueeney Square":
                num_abandoned_buildings = random.randint(2,4)
        elif neighborhood_name == "Temple Acres":
                num_abandoned_buildings = random.randint(2,4)
	else:
		num_abandoned_buildings = 0

	while count <= num_abandoned_buildings:
		if first_building == True:
			x = random.randint(1,max_x)
			y = random.randint(1,max_y)
			abandoned_building = gen_abandoned_building(True,locations,name,x,y,neighborhood_name)
			locations.append(abandoned_building)
			first_building = False
			num_locations += 1
			count += 1
		elif first_building == False:
			checked = False
			exists = False
			while checked == False:
				x = random.randint(1,max_x)
				y = random.randint(1,max_y)
				for location in locations:
					if location.x == x and location.y == y:
						exists = True
						checked = True
					if exists == False:
						checked = True
				
			abandoned_building = gen_abandoned_building(True,locations,name,x,y,neighborhood_name)
			locations.append(abandoned_building)
			num_locations += 1
			count += 1
	
	#num_abandoned_apt = 0
#	apt_count = 1
#	if num_abandoned_apt >= 1:
#		while apt_count <= num_abandoned_apt:
 #                       checked = False
  #                      exists = False
   #                     while checked == False:
    #                            x = random.randint(1,16)
     #                           y = random.randint(1,16)
      #                          for location in locations:
        #                                if location.x == x and location.y == y:
       #                                         exists = True
         #                                       checked = True
          #                              if exists == False:
           #                                     checked = True
                                
            #            abandoned_apt_building = gen_abandoned_apt_building(x,y)
             #           locations.append(abandoned_apt_building)
              #          num_locations += 1
               #         apt_count += 1


	#pawn shop
	def get_unused_location():
	        checked = False
	        exists = False
       		x = random.randint(1,32)
               	y = random.randint(1,32)
        	for location in locations:
	                if location.x != x and location.y != y:
        	                #exists = False
                                checked = True
		        elif location.x == x and location.y == y:
				x = random.randint(1,32)
               			y = random.randint(1,32)
				#exists = False
                  		#for location in locations:
                       		#        if location.x == x and location.y == y:
                       		#       	        checked = False
			        #        elif location.x != x and location.y != y:
                                #                checked = True

	        if checked == True:
			return x, y
	 	       	#checked = True
	#x, y = get_unused_location()

#pawn shop
        if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Elephant Rock' or neighborhood_name == "Bernal Park" or neighborhood_name == "Maplewood" or neighborhood_name == "Rose Heights":
		pawn_count = 1
		pawn_max = 1
		while pawn_count <= pawn_max:
			x, y = get_unused_location()
			pawn_shop = gen_pawn_shop(x,y,neighborhood_name)
			locations.append(pawn_shop)
			print 'pawn shop'
			pawn_count += 1
			num_locations += 1

	#thrift store
        if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Bad Town' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Bernal Park' or neighborhood_name == 'Rose Heights':
		num_stores = 1
		store_count = 1
		while store_count <= num_stores:
			x, y = get_unused_location()
	        	thrift_store = gen_thrift_store(x,y,neighborhood_name)
	        	locations.append(thrift_store)
			print 'thrift store'
			num_locations += 1
			store_count += 1

        #bar
	bar_names = []
	if neighborhood_name == 'Cliff Heights':
		bar_names = ['GiddyUps','The Giant']
	elif neighborhood_name == 'Bad Town':
		bar_names = ['The Lazy Den']
	elif neighborhood_name == 'Elephant Rock':
		bar_names = ['Quest']
	elif neighborhood_name == 'The Scabs':
		bar_names = ['Chateau Below','The Tank']
        elif neighborhood_name == 'Rose Heights':
                bar_names = ['The Keg',"Eddie's","Roughriders"]
	elif neighborhood_name == "Temple Acres":
		bar_names = []

	if bar_names != None:
		max_bars = random.randint(3,5)
		count = 1
		for bar_name in bar_names:
		        x, y = get_unused_location()
		        maggies_bar = gen_bar(x,y,bar_name,neighborhood_name)
		        locations.append(maggies_bar)
			count += 1
			num_locations += 1

			print 'bar'
	#doctor
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
        	x, y = get_unused_location()
        	doctor = gen_doctor(x,y,neighborhood_name)
        	locations.append(doctor)
        	print 'doctor'
        #laundry
        if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'Bad Town' or neighborhood_name == 'McQueeney Square':
                x, y = get_unused_location()
                laundromat = gen_laundromat(x,y,neighborhood_name)
                locations.append(laundromat)
                num_locations += 1
                print 'laundromat'

        #tattoos
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights':
        	x, y = get_unused_location()
        	tattoos = gen_tattoo_shop(x,y,neighborhood_name)
        	locations.append(tattoos)
		num_locations += 1
        	print 'tattoos'
        #barbers
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights' or neighborhood_name == "Mcqueeney Square":
        	x, y = get_unused_location()
        	barber = gen_barber_shop(x,y,neighborhood_name)
        	locations.append(barber)
        	print 'barber'
		num_locations += 1
        #crackhouses
	if neighborhood_name != 'Cliff Heights' and neighborhood_name != 'Rose Heights' and neighborhood_name != "Temple Acres":
		num_crackhouses = random.randint(1,4)
		if neighborhood_name == "Camp":
			num_crackhouses = random.randint(1,2)
		count = 1
		while count <= num_crackhouses:
		        x, y = get_unused_location()
		        crackhouse = gen_crackhouse(x,y,neighborhood_name)
		        locations.append(crackhouse)
			print 'crackhouse'
			count += 1
			num_locations += 1

        #coffee shop
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Bad Town' or neighborhood_name == 'The Scabs' or neighborhood_name == 'McQueeney Square' or neighborhood_name == "Temple Acres":
		num_coffee_shop = 1
		count = 1
		while count <= num_coffee_shop:
        		x, y = get_unused_location()
        		coffee_shop = gen_coffee_shop(x,y,neighborhood_name)
        		locations.append(coffee_shop)
			print 'coffee shop'
			count += 1
        if neighborhood_name == 'Rose Heights':
                num_coffee_shop = 2
                count = 1
                while count <= num_coffee_shop:
                        x, y = get_unused_location()
                        coffee_shop = gen_coffee_shop(x,y,neighborhood_name)
                        locations.append(coffee_shop)
                        print 'coffee shop'
                        count += 1
        #mcshits
        if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
	        x, y = get_unused_location()
	        mcshits = gen_mcshits(x,y,neighborhood_name)
	        locations.append(mcshits)
		print 'mcshits'
		num_locations += 1

        #pizza
        if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Elephant Rock' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square' or neighborhood_name == "Temple Acres":
	        x, y = get_unused_location()
	        pizza_place = gen_pizza_place(x,y,neighborhood_name)
	        locations.append(pizza_place)
		print 'pizza'
		num_locations += 1
	
	#convenience store
	num_convenience_store = 1
	if neighborhood_name == 'Cliff Heights':
        	num_convenience_store = 2
        elif neighborhood_name == 'Bad Town':
                num_convenience_store = 2
	elif neighborhood_name == 'Elephant Rock':
		num_convenience_store = 1
	elif neighborhood_name == 'The Scabs':
		num_convenience_store = 2
        elif neighborhood_name == 'Rose Heights':
                num_convenience_store = 2
	elif neighborhood_name == 'McQueeney Square':
		num_convenience_store = 3
	elif neighborhood_name == "Temple Acres":
		num_convenience_store = 2
	if num_convenience_store !=  None and neighborhood_name != "Camp":
        	count = 1
        	while count <= num_convenience_store:
        	        x, y = get_unused_location()
        	        store = gen_convenience_store(x,y,neighborhood_name)
        	        locations.append(store)
        	        print 'convenience store'
        	        count += 1
			num_locations += 1

        #library
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'McQueeney Square' or neighborhood_name == "Temple Acres":
	        x, y = get_unused_location()
	        library = gen_library(x,y,neighborhood_name)
	        locations.append(library)
		#organizations = []
		print 'library'
		num_locations += 1
	#offices
	num_troll_farm = 0
	num_call_centre = 0
	num_data_mind = 0
	num_office = 0
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
		num_troll_farm = 5
		if neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
			num_troll_farm = 10
		farm_count = 1
		print 'troll farms'
		while farm_count <= num_troll_farm:
			x,y = get_unused_location()
			corp = random.choice(tech_corps)
			troll_farm = gen_office(x,y,corp,'Troll Farm',neighborhood_name)
			locations.append(troll_farm)
			print 'troll farm ' +str(farm_count) + ' of ' + str(num_troll_farm) + " created."
			num_locations += 1
			farm_count += 1
        	print 'call centres'
                num_call_centre = 3
		if neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
			num_call_centre = 7
                call_centre_count = 1
                while call_centre_count <= num_call_centre:
                        x,y = get_unused_location()
                        corp = random.choice(tech_corps)
                        troll_farm = gen_office(x,y,corp,'Call Centre',neighborhood_name)
                        locations.append(troll_farm)
                        print 'call centre ' +str(call_centre_count) + ' of ' + str(num_call_centre) + " created."

                        num_locations += 1
                        call_centre_count += 1
                num_data_mine = 0
		print 'data mines'
                if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'The Scabs':
                        num_data_mine = 7
                data_mine_count = 4
                while data_mine_count <= num_data_mine:
                        x,y = get_unused_location()
                        corp = random.choice(tech_corps)
                        troll_farm = gen_office(x,y,corp,'Data Mine',neighborhood_name)
                        locations.append(troll_farm)
                        print 'data mine ' + str(data_mine_count) + ' of ' + str(num_data_mine) + " created."

                        num_locations += 1
                        data_mine_count += 1
                num_office = 4
                if neighborhood_name == 'McQueeney Square':
                        num_call_centre = 7
		if neighborhood_name == "Cliff Heights" or neighborhood_name == "Rose Heights" or neighborhood_name == "McQueeney Square":
			num_call_centre = 5
                office_count = 1
		print 'office buildings'
                while office_count <= num_call_centre:
                        x,y = get_unused_location()
                        corp = random.choice(tech_corps)
                        troll_farm = gen_office(x,y,corp,'Office Building',neighborhood_name)
                        print 'office ' +str(office_count) + ' of ' + str(num_call_centre) + " created."

                        locations.append(troll_farm)
                        num_locations += 1
                        office_count += 1
	print 'all offices finished'



        #apt building
	print 'apt buildings'
        apt_count = 1
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square' or neighborhood_name == "Rose Heights":
        	num_apt = random.randint(8,9)
        elif neighborhood_name == 'Bad Town':
                num_apt = 5
	elif neighborhood_name == 'Elephant Rock' or neighborhood_name == "Temple Acres":
		num_apt = random.randint(20,25)
	elif neighborhood_name == 'The Scabs':
		num_apt = 7
	else:
		num_apt = 0
        while apt_count <= num_apt:
                x, y = get_unused_location()
                apt_finished = False
                while apt_finished == False:
                        try:
                                apt_building = gen_apt_building(x,y,neighborhood_name)
                                locations.append(apt_building)
                                apt_finished = True
                                apt_count += 1
				num_locations += 1
                        except:
                                apt_finished = False
	print 'apts finished'
        #parks
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Elephant Rock' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square' or neighborhood_name == "Temple Acres":
        	max_parks = random.randint(2,3)
	else:
		max_parks = 0
	count = 1
	if neighborhood_name != "Camp":
		while count <= max_parks:
			x, y = get_unused_location()
			park = gen_park(x,y,neighborhood_name,neighborhood_name)
			locations.append(park)
			count += 1
			num_locations += 1

			print 'park'
	#graveyard
	count = 1
	max_grave = 0
	if neighborhood_name == 'Cliff Heights' or neighborhood_name == 'Elephant Rock' or neighborhood_name == 'The Scabs' or neighborhood_name == 'Rose Heights' or neighborhood_name == 'McQueeney Square':
		max_grave = 1
	elif neighborhood_name == "Temple Acres":
		max_grave = 3
	while count <= max_grave:
	        x, y = get_unused_location()
                park = gen_graveyard(x,y,"Graveyard",neighborhood_name)
                locations.append(park)
		num_locations += 1
                count += 1


	#gang hq
	#organizations = []
	if neighborhood_name == 'Cliff Heights':
		gang_names = ["Crankensteins", "Pissbois","Hell's Satans"]
	elif neighborhood_name == 'Bad Town':
		gang_names = ['Red Faction','Slavers']
	elif neighborhood_name == 'Elephant Rock':
		gang_names = ['Anarchists','Sex Cult']
	elif neighborhood_name == 'The Scabs':
		gang_names = ['Flower Collective','Patriot Nazis']
	elif neighborhood_name == 'Rose Heights':
		gang_names = ['Clerks','Grimesmackers']
        elif neighborhood_name == 'McQueeney Square':
                gang_names = ['Gamer Assassins','Rude Boys','Booze Knights']
	else:
		gang_names = []
	for name in gang_names:
			gang_valid = False
			while gang_valid == False:
				location_valid = False
				while location_valid == False:
					try:
						x, y = get_unused_location()
						location_valid = True
					except:
						location_valid = False
						print 'try another location'
				print x, y
				gang_good = False
				while gang_good == False:
					try:
						gang_hq,organization = gen_gang_hq(x,y,name,locations,neighborhood_name)
						num_locations += 1
				

						print gang_hq
						print organization
						print organization.name
						organizations.append(organization)
						gang_valid,gang_good = True,True
					except:
						print 'try again'
						gang_good = False
				#gang_valid = False
        #houses

	if neighborhood_name == "Elephant Rock" or neighborhood_name == "Cliff Heights" or neighborhood_name == "McQueeney Square" or neighborhood_name == "Temple Acres":
		if neighborhood_name == "Temple Acres":
			max_house = 30
		else:
			max_house = random.randint(8,15)
		count = 1
		while count <= max_house and num_locations <= 79 :
			x,y = get_unused_location() 
			house = gen_house(x,y,neighborhood_name,'family')
			locations.append(house)
			num_locations += 1
			count += 1

        count  = 1
	if neighborhood_name == 'Elephant Rock':
		max_shacks = 22
	elif neighborhood_name == 'The Scabs':
		max_shacks = 32
	elif neighborhood_name == 'Bad Town':
		max_shacks = 55
        else:
		max_shacks = random.randint(6,12)
	count = 1

        while count <= max_shacks and num_locations <= 79:
                x,y = get_unused_location()
                shack = gen_shack(x,y,neighborhood_name)
                locations.append(shack)
		print shack
                count += 1
		num_locations += 1

	#price
	if neighborhood_name == 'Cliff Heights':
		price = 3000
	elif neighborhood_name == 'Bad Town':
		price = 1400
	elif neighborhood_name == 'Elephant Rock':
		price = 1600
	elif neighborhood_name == 'The Scabs':
		price = 2300
        elif neighborhood_name == 'Rose Heights':
                price = 3200
        elif neighborhood_name == 'McQueeney Square':
                price = 3400
	elif neighborhood_name == "Temple Acres":
		price = 6000
	else:
		price = 0

	#assign homes/addictions to npcs
	for location in locations:
		for member in location.actors.members:
			if member == None:
				location.actors.members.remove(member)
			else:
				member.home = location
				for drug in member.drugs:
					if drug.name == 'Crack' or drug.name == 'Cocaine':
			                        member.mind.addictions.cocaine.addiction_level = random.randint(3,7)
                                        elif drug.name == 'Heroin' or drug.name == 'Morphine':
                                                member.mind.addictions.opiates.addiction_level = random.randint(3,7)
                                        elif drug.name == 'Speed':
                                                member.mind.addictions.speed.addiction_level = random.randint(3,7)
		if len(location.rooms) >= 1:
			for location in location.rooms:
				for member in location.actors.members:
					if member == None:
						location.actors.members.remove(member)
					else:
						member.home = location
                                		for drug in member.drugs:
                                        		if drug.name == 'Crack' or drug.name == 'Cocaine':
                                                		member.mind.addictions.cocaine.addiction_level = random.randint(3,7)
                                        		elif drug.name == 'Heroin' or drug.name == 'Morphine':
                                                		member.mind.addictions.opiates.addiction_level = random.randint(3,7)
                                        		elif drug.name == 'Speed':
                                                		member.mind.addictions.speed.addiction_level = random.randint(3,7)

	#assign apartments to controlling factions
	for location in locations:
		if location.owned_by != 'No one':
			for room in location.rooms:
				room.owned_by = location.owned_by
	print 'assigned rooms'
	type_randos = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Crankenstein','Flower Child','Rocker','Clerk',"Mercenary",'Occultist','Scavenger','Survivalist']
	for worker in workers:
		type_randos.append(worker)
	num_randos = random.randint(40,60)
	rando_count = 1
	randos = []
	while rando_count <= num_randos:
		try:
			profession = random.choice(type_randos)
			rando = create_npc(profession,'none','None',None)
			randos.append(rando)
			rando_count += 1
		except:
			rando_count += 1
	for rando in randos:
		if rando != None:
			if len(rando.drugs) >= 1:
	        		for drug in rando.drugs:
        			        if drug.name == 'Crack' or drug.name == 'Cocaine':
                			        cocaine_addiction = Addiction('Cocaine',0,random.randint(3,7),7,[])
                		        elif drug.name == 'Heroin' or drug.name == 'Morphine':
                		        	opiates_addiction = Addiction('Opiates',0,random.randint(3,7),7,[])
                		        elif drug.name == 'Speed':
                		        	speed_addiction = Addiction('Speed',0,random.randint(3,7),7,[])
		elif rando == None:
			randos.remove(rando)
	#add brokers
	for location in locations:
		if location.is_bar == True:
			chance_broker = 1
			if chance_broker == 1:
				location.has_broker = True
				new_broker = create_npc('Broker','none','None',None)
				num_connections = random.randint(1,6)
				min_fame = 0
				faction_count = 0
				factions = []
                                gang_found = False
                                for organization in organizations:
	                                if location.owned_by == organization or location.owned_by == organization.name:
						gang = organization
        	                                gang_found = True
				if gang_found == False:
					while faction_count <= num_connections:
						#gangs = location.factions
						possible_corps = []
						for corp in tech_corps:
							possible_corps.append(corp)
                                	        for corp in real_estate_corps:
                                	                possible_corps.append(corp)
                                	        for corp in weapons_corps:
                                	                possible_corps.append(corp)
                                	        for corp in food_corps:
                                	                possible_corps.append(corp)
						for organization in organizations:
							possible_corps.append(organization)
                              		        corp = random.choice(possible_corps)
                               		        if len(factions) >= 1:
                               		                if corp not in factions:
                               		                        factions.append(corp)
						faction_count += 1
				if gang_found == True:
					factions = [gang]
				location.broker = new_broker
				for organization in organizations:
					if location.owned_by == organization or location.owned_by == organization.name:
						
						faction = [organization]
				location.broker.broker = Broker(new_broker,factions,min_fame,[],0,0,0,[],None)
				location.has_broker = True
	if flag == 'temple':
		x = random.randint(8,14)
		y = random.randint(8,14)
	else:
		x = random.randint(1,48)
		y = random.randint(1,48)

#        organization = Organization(neighborhood_name,False,[],0,None,[],0,[],[],False,0,False)
#	organizations.append(organization)
	cliff_heights = Area(locations,neighborhood_name,organizations,x,y,randos,price,flag,False)

	return cliff_heights

def gen_compound(type,neighborhood_name,flag,organization):
        def get_unused_location(locations):
                checked = False
                exists = False
                x = random.randint(1,32)
                y = random.randint(1,32)
                if len(locations) >= 1:
                        for location in locations:
                                if location.x != x and location.y != y:
                                        #exists = False
                                        checked = True
                                elif location.x == x and location.y == y:
                                        x = random.randint(1,32)
                                        y = random.randint(1,32)
                                        #exists = False
                                #for location in locations:
                                #        if location.x == x and location.y == y:
                                #                       checked = False
                                #        elif location.x != x and location.y != y:
                                #                checked = True
                else:
                        x = random.randint(1,32)
                        y = random.randint(1,32)
                        return x, y

                if checked == True:
                        return x, y
                        #checked = True

        locations = []
        x, y = get_unused_location(locations)
        location, organization = gen_gang_hq(x,y,"Skullheads",locations,neighborhood_name)
        locations.append(location)
        locations = set(locations)
        locations = list(locations)
        organizations = []
#       if organization == None:
#               organizations = []
#       else:
        organizations.append(organization)
        x = random.randint(1,32)
        y = random.randint(1,32)        
        randos = []
        #locations = []
        price = 0
        num_shack = 6
        shack_count = 0
        while shack_count <= num_shack:
                x, y = get_unused_location(locations)
                shack = gen_abandoned_building(False,locations,"Ruin",x,y,neighborhood_name)
                locations.append(shack)
                shack_count += 1
        #x, y = get_unused_location(locations)
        #general_store = gen_general_store(x,y)
        #locations.append(general_store)
        camp = Area(locations,neighborhood_name,organizations,x,y,randos,price,flag,False)
        return camp

def gen_camp(type,neighborhood_name,flag,organization):
        def get_unused_location(locations):
                checked = False
                exists = False
                x = random.randint(1,32)
                y = random.randint(1,32)
		if len(locations) >= 1:
                	for location in locations:
                	        if location.x != x and location.y != y:
                	                #exists = False
                	                checked = True
                	        elif location.x == x and location.y == y:
                	                x = random.randint(1,32)
                	                y = random.randint(1,32)
                	                #exists = False
                                #for location in locations:
                                #        if location.x == x and location.y == y:
                                #                       checked = False
                                #        elif location.x != x and location.y != y:
                                #                checked = True
		else:
                	x = random.randint(1,32)
                        y = random.randint(1,32)
			return x, y

                if checked == True:
                        return x, y
                        #checked = True

	locations = []
	x, y = get_unused_location(locations)
	location, organization = gen_gang_hq(x,y,"Cannibals",locations,neighborhood_name)
	locations.append(location)
	locations = set(locations)
	locations = list(locations)
	organizations = []
#	if organization == None:
#		organizations = []
#	else:
	organizations.append(organization)
        x = random.randint(1,32)
        y = random.randint(1,32)	
	randos = []
	#locations = []
	price = 0
	num_shack = 6
	shack_count = 0
	while shack_count <= num_shack:
		x, y = get_unused_location(locations)
		shack = gen_shack(x,y,neighborhood_name)
		locations.append(shack)
		shack_count += 1
	x, y = get_unused_location(locations)
	general_store = gen_general_store(x,y,neighborhood_name)
	locations.append(general_store)
	camp = Area(locations,neighborhood_name,organizations,x,y,randos,price,flag,False)
	return camp
def gen_world_tile():
        actors = NPC(members,0,[],0)
	num_items = random.randint(4,14)
	item_count = 1
	items = 0
	while item_count <= num_items:
		possible_items = [tree,bush,small_tree]

        building = Location("Wasteland",'Templeville',' ','Wasteland',x,y,actors,items,False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,True,1,True,False,None,[],[])

def gen_new_city():
	
	player_organization = Organization("Player Organization",False,[],0,None,[],0,[],[],False,0,False,[],0,0,0,0,0,0,0,0,0,0,0,0)
	player_organization.locations_owned = []
	player_organization.rent_amount = 0
#self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid
	city_created = False
	while city_created == False:
		cliff_heights = gen_neighborhood('Slum','Cliff Heights','temple')
        	bad_town = gen_neighborhood('Slum','Bad Town','temple')
        	elephant_rock = gen_neighborhood('Slum','Elephant Rock','temple')
                the_scabs = gen_neighborhood('Slum','The Scabs','temple')
                rose_heights = gen_neighborhood('Slum','Rose Heights','temple')
		mcqueeney_square = gen_neighborhood('Slum','McQueeney Square','temple')
                temple_acres = gen_neighborhood('Slum','Temple Acres','temple')

		try:
                	camp = gen_camp('Slum','Camp','camp',[])
		except:
			camp = gen_camp('Slum','Camp','camp',[])
		try:
			compound = gen_compound("Skullheads Compound","Compound","badlands",[])
		except:
                        compound = gen_compound("Skullheads Compound","Compound","badlands",[])

		city_created = True
	areas = [cliff_heights,bad_town,elephant_rock,the_scabs,rose_heights,mcqueeney_square,temple_acres,camp,compound]
	#make sure locations are unique
	finished_checking = False
	has_changed = False
	while finished_checking == False:
		def check_areas(areas):
			changed = False
			for area in areas:
				checked_area = False
				def check(areas,area,changed):
					for area2 in areas:
						if area2.x == area.x and area2.y == area2.y:
							if area.region == "temple":
								area.x = random.randint(8,12)
								area.y = random.randint(8,12)

                                                        elif area.region == "camp":
                                                                area.x = random.randint(15,24)
                                                                area.y = random.randint(15,24)
                                                        elif area.region == "badlands":
                                                                area.x = random.randint(35,40)
                                                                area.y = random.randint(35,40)

							else:
								area.x = random.randint(1,48)
								area.y = random.randint(1,48)
							changed= True
							checked = False
							return checked
					checked = True
					changed = False
					return checked
				checked_area = check(areas,area,changed)
			return changed
		has_changed = check_areas(areas)
		if has_changed == True:
			has_changed = check_areas(areas)
		else:
			finished_checking = True
						
	name = "Templeville"
	time = start_time
	weather = get_weather(time)
	city = City(areas,name,time,player_organization,corps,[],weather)
	return city


