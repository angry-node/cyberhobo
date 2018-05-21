import random
global location_id
global item_id

from namegen import *


class Party:
	def __init__(self,is_player,leader,members,location,area,district,money,inventory,safehouse,fame,x,y):
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

class NPC:
        def __init__(self,members,money,inventory,fame):
                self.members = members
                self.money = money
                self.inventory = inventory
                self.fame = fame

#is_player,leader,members,location,area,district,money,inventory,safehouse,fame

class Char:
	def __init__(self, gender,age, profession,affiliation, health, stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,start_money,controlled_by,combat_status,home,mind,hunger,thirst,sleep):
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
			base_sanity -= 5 * addiction_level
			opiate_craving_roll = random.randint(1,10)
                elif self.mind.addictions.cocaine.addiction_level >= 1:
                        base_stress += self.mind.addictions.cocaine.addiction_level * 5
                        base_happiness -= self.mind.addictions.cocaine.addiction_level * 5
                        base_sanity -= 5 * addiction_level

                elif self.mind.addictions.speed.addiction_level >= 1:
                        base_stress += self.mind.addictions.speed.addiction_level * 5
                        base_happiness -= self.mind.addictions.speed.addiction_level * 5
                        base_sanity -= 5 * addiction_level

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

class Health:
	def __init__(self, base_max, max_health, current_health,base_blood,max_blood,current_blood,bleeding_rate,base_pain,max_pain,
	current_pain,base_current_pain,base_stamina,current_stamina,max_stamina):
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

class Mind:
	def __init__(self,happiness,stress,sanity,horny,addictions,trauma):
		self.happiness = happiness
		self.stress = stress
		self.sanity = sanity
		self.horny = horny
		self.addictions = addictions
		self.trauma = trauma

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



class Organization:
	def __init__(self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid,month,rent_checked):
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

class Territory:
	def __init__(self,top_left_x,top_left_y,bottom_right_x,bottom_right_y):
		self.top_left_x = top_left_x
		self.top_left_y = top_left_y
		self.bottom_right_x = bottom_right_x
		self.bottom_right_y = bottom_right_y

class Footsoldier:
	def __init__(self,npc,orders):
		self.npc = npc
		self.orders = orders
		

start_health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)

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

class Combat_Status:
	def __init__(self, knocked_down,stunned,defending,blind,unconscious):
		self.knocked_down = knocked_down
		self.stunned = stunned
		self.defending = defending
		self.blind = blind
		self.unconscious = unconscious


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
	cause_bleeding,cause_pain,cause_stamina_loss):
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

#bruises

bruised_groin = Injury("bruise","groin", "'s groin was bruised",[],[],lower_max_health,True,0,48,10,100,0,35,25)
bruised_torso = Injury("bruise","torso", "'s torso was bruised",[],[],lower_max_health,True,0,48,4,100,0,20,25)
bruised_neck = Injury("bruise","neck", "'s neck was bruised",[],[],lower_max_health,True,0,48,10,100,0,25,25)
bruised_face = Injury("bruise","face", "'s face was bruised",[],[],lower_max_health,True,0,48,10,100,0,15,15)
bruised_left_arm = Injury("bruise","left arm", "'s left arm was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10)
bruised_right_arm = Injury("bruise","right arm", "'s right arm was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10)
bruised_left_leg = Injury("bruise","left leg", "'s left leg was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10)
bruised_right_leg = Injury("bruise","right leg", "'s right leg was bruised",[],[],lower_max_health,True,0,48,4,100,0,15,10)

bruises = [bruised_groin,bruised_torso,bruised_neck,bruised_face,bruised_left_arm,bruised_right_arm,bruised_left_leg,bruised_right_leg]

#fractures

fractured_skull = Injury("fracture","skull", "'s skull was fractured",[],[],lower_max_health,True,0,48,120,2000,0,45,40)
broken_ribs = Injury("broken","ribs", "'s ribs were broken",[],[],lower_max_health,True,0,48,20,800,0,25,30)
broken_neck = Injury("broken","neck", "'s neck was broken",[],[],lower_max_health,True,0,48,120,2000,0,45,40)
broken_right_collarbone = Injury("broken","right collarbone", "'s right collarbone was broken",[],[],lower_max_health,True,0,48,35,500,0,30,10)
broken_left_collarbone = Injury("broken","left collarbone", "'s left collarbone was broken",[],[],lower_max_health,True,0,48,35,500,0,30,10)



fractured_left_arm = Injury("fracture","left arm", "'s left arm was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10)
fractured_right_arm = Injury("fracture","right arm", "'s right arm was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10)
fractured_left_leg = Injury("fracture","left leg", "'s left leg was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10)
fractured_right_leg = Injury("fracture","right leg", "'s right leg was fractured",[],[],lower_max_health,True,0,48,16,600,0,20,10)

fractures = [fractured_skull,broken_ribs,broken_neck,broken_right_collarbone,broken_left_collarbone,fractured_left_arm,
	fractured_right_arm, fractured_left_leg, fractured_right_leg]

#minor cuts

minor_cut_head = Injury("cut","head","'s head was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)
minor_cut_torso = Injury("cut","torso","'s torso was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)
minor_cut_neck = Injury("cut","neck","'s neck was cut",[],[],lower_max_health,False,0,48,16,900,3,10,5)
minor_cut_face = Injury("cut","face","'s face was cut",[],[],lower_max_health,False,0,48,12,400,2,10,5)
minor_cut_left_arm = Injury("cut","left arm","'s left arm was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)
minor_cut_right_arm = Injury("cut","right arm","'s right arm was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)
minor_cut_left_leg = Injury("cut","left leg","'s left leg was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)
minor_cut_right_leg = Injury("cut","right_leg","'s right leg was cut",[],[],lower_max_health,False,0,48,8,400,2,10,5)

minor_cuts = [minor_cut_head,minor_cut_torso,minor_cut_neck,minor_cut_face,minor_cut_left_arm,minor_cut_right_arm,minor_cut_left_leg,minor_cut_right_leg]


#major cuts

major_cut_head = Injury("cut","head","'s head was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)
major_cut_torso = Injury("cut","torso","'s torso was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)
major_cut_neck = Injury("cut","neck","'s throat was badly cut",[],[],lower_max_health,False,0,48,32,900,4,20,25)
major_cut_face = Injury("cut","face","'s face was badly cut",[],[],lower_max_health,False,0,48,24,400,4,20,25)
major_cut_left_arm = Injury("cut","left arm","'s left arm was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)
major_cut_right_arm = Injury("cut","right arm","'s right arm was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)
major_cut_left_leg = Injury("cut","left leg","'s left leg was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)
major_cut_right_leg = Injury("cut","right leg","'s right leg was badly cut",[],[],lower_max_health,False,0,48,16,400,4,20,25)

major_cuts = [major_cut_head,major_cut_torso,major_cut_neck,major_cut_face,major_cut_left_arm,major_cut_right_arm,major_cut_left_leg,major_cut_right_leg]


#severed limbs

severed_head = Injury("severed","head","'s head was severed",[],[],lower_max_health,False,0,48,16,400,10,200,100)
severed_left_arm = Injury("severed","left arm","'s left arm was severed",[],[],lower_max_health,False,0,48,16,4000,6,30,50)
severed_right_arm = Injury("severed","right arm","'s right arm was severed!",[],[],lower_max_health,False,0,48,16,4000,6,30,50)
severed_left_leg = Injury("severed","left leg","'s left leg was severed",[],[],lower_max_health,False,0,48,16,4000,6,20,50)
severed_right_leg = Injury("severed","right leg","'s right leg was severed",[],[],lower_max_health,False,0,48,16,4000,6,30,50)

severed_limbs = [severed_head,severed_left_arm,severed_right_arm,severed_left_leg,severed_right_leg]


#blown off limbs

blown_off_head = Injury("blown off","head","'s head was blown off",[],[],lower_max_health,False,0,48,16,400,10,200,100)
blown_off_left_arm = Injury("blown_off","left arm","'s left arm was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50)
blown_off_right_arm = Injury("blown off","right arm","'s right arm was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50)
blown_off_left_leg = Injury("blown off","left leg","'s left leg was blown off",[],[],lower_max_health,False,0,48,16,4000,6,20,50)
blown_off_right_leg = Injury("blown off","right leg","'s right leg was blown off",[],[],lower_max_health,False,0,48,16,4000,6,30,50)

blown_off_limbs = [blown_off_head,blown_off_left_arm,blown_off_right_arm,blown_off_left_leg,blown_off_right_leg]


#stab

stab_torso = Injury("stab wound","torso"," was stabbed in the torso",[],[],lower_max_health,False,0,48,15,1000,5,30,20)
stab_neck = Injury("stab wound","neck"," was stabbed in the neck",[],[],lower_max_health,False,0,48,90,1000,5,45,40)
stab_face = Injury("stab wound","face", "was stabbed in the face",[],[],lower_max_health,False,0,48,30,1000,5,45,30)
stab_left_arm = Injury("stab wound","left arm"," was stabbed in the left arm",[],[],lower_max_health,False,0,48,15,1000,5,30,20)
stab_right_arm = Injury("stab wound","right arm"," was stabbed in the right arm",[],[],lower_max_health,False,0,48,15,1000,5,30,20)
stab_left_leg = Injury("stab wound","left leg","was stabbed in the left leg",[],[],lower_max_health,False,0,48,15,1000,5,30,20)
stab_right_leg = Injury("stab wound","right leg"," was stabbed in the right leg",[],[],lower_max_health,False,0,48,15,1000,5,30,20)

stab_wounds = [stab_torso,stab_neck,stab_face,stab_left_arm,stab_right_arm,stab_left_leg,stab_right_leg]




#9mm
head_9mm = Injury("gunshot wound","head"," was shot in the head",[],[],lower_max_health,False,0,48,60,1200,6,50,40)
torso_9mm = Injury("gunshot wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,48,35,1200,6,40,20)
neck_9mm = Injury("gunshot shot","neck"," was shot in the neck",[],[],lower_max_health,False,0,48,60,3000,6,45,30)
face_9mm = Injury("gunshot wound","face"," was shot in the face",[],[],lower_max_health,False,0,48,60,3200,6,45,30)
left_arm_9mm = Injury("gunshot wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,48,30,800,3,30,20)
right_arm_9mm = Injury("gunshot wound","right arm"," was shot in the right arm,",[],[],lower_max_health,False,0,48,30,800,3,30,20)
left_leg_9mm = Injury("gunshot wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,48,30,800,3,30,20)
right_leg_9mm = Injury("gunshot wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,48,30,800,3,30,20)

shot_9mm = [head_9mm,torso_9mm,neck_9mm,face_9mm,left_arm_9mm,right_arm_9mm,left_leg_9mm,right_leg_9mm]



#12 gauge shotgun

torso_12g = Injury("shotgun wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,48,40,1100,6,45,40)
face_12g = Injury("shotgun wound","face"," was shot in the face",[],[],lower_max_health,False,0,48,80,4000,8,45,45)
left_arm_12g = Injury("shotgun wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,48,40,1100,5,30,20)
right_arm_12g = Injury("shotgun wound","right arm"," was shot in the right arm",[],[],lower_max_health,False,0,48,40,1100,5,30,20)
left_leg_12g = Injury("shotgun wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,48,40,1100,5,30,20)
right_leg_12g = Injury("shotgun wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,48,40,1100,5,30,20)

shot_12g = [torso_12g,face_12g,left_arm_12g,right_arm_12g,left_leg_12g,right_leg_12g]

#ak47

ak47_torso = Injury("gunshot wound","torso"," was shot in the torso",[],[],lower_max_health,False,0,0,55,700,6,50,50)
ak47_face = Injury("gunshot wound","face"," was shot in the face",[],[],lower_max_health,False,0,0,75,2700,6,50,50)
ak47_left_arm = Injury("gunshot wound","left arm"," was shot in the left arm",[],[],lower_max_health,False,0,0,45,700,4,35,20)
ak47_right_arm = Injury("gunshot wound","right arm"," was shot in the right arm",[],[],lower_max_health,False,0,0,45,700,4,35,20)
ak47_left_leg = Injury("gunshot wound","left leg"," was shot in the left leg",[],[],lower_max_health,False,0,0,45,700,4,35,20)
ak47_right_leg = Injury("gunshot wound","right leg"," was shot in the right leg",[],[],lower_max_health,False,0,0,45,700,4,35,20)

shot_ak47 = [ak47_torso,ak47_face,ak47_left_arm,ak47_right_arm,ak47_left_leg,ak47_right_leg]

class Want:
	def __init__(self,name,type,wear_off,time_had):
		self.name = name
		self.type = type
		self.wear_off = wear_off
		self.time_had = time_had

craving_cocaine = Want('Craving cocaine','want',180,0)
craving_opiates = Want('Craving opiates','want',180,0)
craving_speed = Want('Craving speed','want',180,0)



#weapons
class Weapon:
	def __init__(self,name,weapon_type, damage, max_condition, condition,item_type,can_loot,base_value):
		self.name = name
		self.weapon_type = weapon_type
		self.damage = damage
		self.max_condition = max_condition
		self.condition = condition
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
punch = Weapon("Punch",'brawl', 10,5,5,'weapon',True,0)
crowbar = Weapon("Crowbar",'brawl', 15,5,5,'weapon',True,0)
shovel = Weapon("Shovel",'brawl', 10,5,5,'weapon',True,0)
baseball_bat = Weapon("Baseball Bat", "brawl",20,5,5,'weapon',True,25)
knife = Weapon("Knife", "brawl",20,5,5,'weapon',True,25)
pistol_9mm = Weapon("9mm Pistol", "pistol", 25,5,5,'weapon',True,450)
shotgun_12g = Weapon("12g Shotgun", "shotgun", 40,5,5,'weapon',True,400)
uzi = Weapon("Uzi", "pistol",30,5,5,'weapon',True,1500)
ak47 = Weapon("AK-47", "rifle",35,5,5,'weapon',True,2500)
sword = Weapon("Sword", "brawl",25,5,5,'weapon',True,600)

class Attack:
	def __init__self(self, type, weapon, attack_mod, injury_inficted):
		self.type = type
		self.weapon = weapon
		self.attack_mod = attack_mod
		self.injury_inflicted = injury_inflicted
#outfits
class Outfit:
	def __init__(self, name, outfit_type,defense,max_condition,condition,item_type,can_loot,base_value):
		self.name = name
		self.outfit_type = outfit_type
		self.defense = defense
		self.max_condition = max_condition 
		self.condition = condition
		self.item_type = item_type
		self.can_loot = can_loot
		self.base_value = base_value
#clothes
naked = Outfit("Naked", "Clothes",1,5,5,'outfit',True,0)
tshirt = Outfit("T-Shirt", "Clothes",2,5,5,'outfit',True,25)
dress = Outfit("Dress", "Clothes",2,5,5,'outfit',True,80)
tracksuit = Outfit("Track Suit", "Clothes",2,5,5,'outfit',True,50)
hoodie = Outfit("Hoodie", "Clothes",3,5,5,'outfit',True,45)
trenchcoat= Outfit("Trench Coat", "Clothes",5,4,5,'outfit',True,100)
cheap_suit= Outfit("Cheap Suit", "Clothes",5,4,5,'outfit',True,130)
leather_jacket = Outfit("Leather Jacket", "Clothes",9,5,5,'outfit',True,150)
army_uniform = Outfit("Army Uniform", "Clothes",6,5,5,'outfit',True,100)
nice_suit = Outfit("Nice Suit", "Clothes",5,5,5,'outfit',True,500)
nice_dress = Outfit("Nice Dress", "Clothes",5,5,5,'outfit',True,500)
body_armor = Outfit("Body Armor", "Clothes",15,5,5,'outfit',True,750)

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




#traits
class Trait:
	def __init__(self,name,description):
		self.name = name
		self.decription = description

#personality traits
alcoholic = Trait("Alcoholic","Alcoholic")
alert = Trait("Alert","Alert")
aloof = Trait("Aloof","Aloof")
angry = Trait("Angry","Angry")
blowhard = Trait("Blowhard","Blowhard")
bratty = Trait("Bratty","Bratty")
calm = Trait("Calm","Calm")
carefree = Trait("Carefree","Carefree")
cautious = Trait("Causious","Cautious")
cocky = Trait("Cocky","Cocky")
creative = Trait("Creative", "Creative")
demonic = Trait("Demonic","Demonic")
devious = Trait("Devious","Devious")
depressed = Trait("Depressed", "Depressed")
dramatic = Trait("Dramatic","Dramatic")
emotional = Trait("Emotional","Emotional")
empathic = Trait("Empathic", "Empathic")
evil = Trait("Evil","Evil")
fearful = Trait("Fearful","Fearful")
flaky = Trait("Flaky","Flaky")
furry = Trait("Furry","Furry")
generous = Trait("Generous","Generous")
gloomy = Trait("Gloomy", "Gloomy")
goofy = Trait("Goofy","Goofy")
helpful = Trait("Helpful","Helpful")
horny = Trait("Always Horny", "Horny")
irritable = Trait('Irritable','Irritable')
late = Trait("Always late","Always late")
lazy = Trait("Lazy", "Lazy")
nauseous = Trait('Nauseous','Nauseous')
sadist = Trait("Sadist","Sadist")
smoker = Trait("Smoker", "Smoker")
stoner = Trait("Stoner", "Stoner")
tremors = Trait('Tremors', 'Tremors')

addiction_traits = [bratty,flaky,fearful,depressed,gloomy,late,lazy,angry,tremors,irritable,nauseous]

personality_traits = [alert,aloof,blowhard,cocky,creative,devious,dramatic,emotional,
	empathic,evil,fearful,flaky,furry,generous,goofy,helpful,horny,late,lazy,sadist,smoker]


#likes
loves_cats = Trait("Loves cats", "Lazy")
loves_dogs = Trait("Loves dogs", "Loves dogs")
loves_metal = Trait("Loves metal","Loves metal")
loves_rap = Trait("Loves rap","Loves rap")
loves_country = Trait("Loves country","Loves country")
loves_killing = Trait("Loves killing","Loves killing")
loves_stealing = Trait("Loves stealing","Loves stealing")
loves_art = Trait("Loves art","Loves art")
loves_poetry = Trait("Loves poetry","Loves Poetry")
loves_literature = Trait("Loves literature","Loves literature")
loves_money = Trait("Loves money","Loves money")
loves_drugs = Trait("Loves drugs","Loves drugs")

likes = [loves_cats,loves_dogs,loves_metal,loves_rap,loves_country,loves_killing,loves_stealing,loves_art,loves_poetry,loves_literature,
	loves_money,loves_drugs]

#physical_traits

pale_skin = Trait("Pale","Pale")
fair_skin = Trait("Fair Skin","Fair skin")
dark_skin = Trait("Dark skin","Dark skin")

skin_types = [pale_skin,fair_skin,dark_skin]

#height
tall = Trait("Tall","Tall")
short = Trait("Short","Short")
average = Trait("Average Height","Average Height")

heights = [tall,short,average]

#body
skinny = Trait("Skinny","Skinny")
thin = Trait("Thin","Thin")
fat = Trait("Fat","Fat")
muscular = Trait("Muscular","Muscular")
stocky = Trait("Stocky","Stocky")

body_types = [skinny,fat,muscular,stocky,thin]

#shaved heads
shaved_blonde_hair = Trait("Blonde Hair(Shaved)","Blonde Hair(Shaved)")
shaved_brown_hair = Trait("Brown Hair(Shaved)","Brown Hair(Shaved")
shaved_red_hair = Trait("Red Hair(Shaved", "Red Hair(Shaved")
shaved_black_hair = Trait("Black Hair(Shaved","Black Hair(Shaved")

shaved_hair = [shaved_brown_hair,shaved_blonde_hair,shaved_red_hair,shaved_black_hair]

#spiky hair
spiky_blonde_hair = Trait("Blonde Hair(Spiky)","Blonde Hair(Spiky)")
spiky_brown_hair = Trait("Brown Hair(Spiky)","Brown Hair(Spiky")
spiky_red_hair = Trait("Red Hair(Spiky", "Red Hair(Spiky")
spiky_black_hair = Trait("Black Hair(Spiky","Black Hair(Spiky")
spiky_blue_hair = Trait("Blue Hair(Spiky)", "Blue Hair(Spiky")
spiky_green_hair = Trait("Green Hair(Spiky)", "Green Hair(Spiky)")

spiky_hair = [spiky_blonde_hair,spiky_brown_hair,spiky_red_hair,spiky_blue_hair,spiky_green_hair]

#short hair
short_blonde_hair = Trait("Blonde Hair(Short)","Blonde Hair(Short)")
short_brown_hair = Trait("Brown Hair(Short)","Brown Hair(Short)")
short_red_hair = Trait("Red Hair(Short)", "Red Hair(Short)")
short_black_hair = Trait("Black Hair(Short)","Black Hair(Short)")
short_blue_hair = Trait("Blue Hair(Short)", "Blue Hair(Short)")
short_green_hair = Trait("Green Hair(Short)", "Green Hair(Short)")

short_hair = [short_blonde_hair,short_brown_hair,short_red_hair]


#long hair
long_blonde_hair = Trait("Blonde Hair(Long)","Blonde Hair(Long)")
long_brown_hair = Trait("Brown Hair(Long)","Brown Hair(Long)")
long_red_hair = Trait("Red Hair(Long)", "Red Hair(Long)")
long_black_hair = Trait("Black Hair(Long)","Black Hair(Long)")
long_blue_hair = Trait("Blue Hair(Long)", "Blue Hair(Long)")
long_green_hair = Trait("Green Hair(Long)", "Green Hair(Long)")

long_hair = [long_blonde_hair,long_brown_hair,long_red_hair]

#parted hair
parted_blonde_hair = Trait("Blonde Hair(Parted)","Blonde Hair(Parted)")
parted_brown_hair = Trait("Brown Hair(Parted)","Brown Hair(Parted)")
parted_red_hair = Trait("Red Hair(Parted)", "Red Hair(Parted)")
parted_black_hair = Trait("Black Hair(Parted)","Black Hair(Parted)")

parted_hair = [parted_blonde_hair,parted_brown_hair,parted_red_hair,parted_black_hair]

#mohawks
mohawk_blonde_hair = Trait("Blonde Hair(Mohawk)","Blonde Hair(Mohawk)")
mohawk_brown_hair = Trait("Brown Hair(Mohawk)","Brown Hair(Mohawk)")
mohawk_red_hair = Trait("Red Hair(Mohawk)", "Red Hair(Mohawk)")
mohawk_black_hair = Trait("Black Hair(Mohawk)","Black Hair(Mohawk)")

mohawk_hair = [mohawk_blonde_hair,mohawk_brown_hair,mohawk_red_hair,mohawk_black_hair]

#braids
braided_blonde_hair = Trait("Blonde Hair(Braids)","Blonde Hair(Braids)")
braided_brown_hair = Trait("Brown Hair(Braids)","Brown Hair(Braids)")
braided_red_hair = Trait("Red Hair(Braids)", "Red Hair(Braids)")
braided_black_hair = Trait("Black Hair(Braids)","Black Hair(Braids)")

braided_hair = [braided_blonde_hair,braided_brown_hair,braided_red_hair,braided_black_hair]


#eyes
blue_eyes = Trait("Blue Eyes", "Blue Eyes")
brown_eyes = Trait("Brown Eyes","Brown Eyes")
green_eyes = Trait("Green Eyes","Green Eyes")
light_blue_eyes = Trait("Blue Eyes(Light)", "Blue Eyes(Light)")
light_brown_eyes = Trait("Brown Eyes(Light)","Brown Eyes(Light)")
light_green_eyes = Trait("Green Eyes(Light)","Green Eyes(Light)")
dark_blue_eyes = Trait("Blue Eyes(Dark)", "Blue Eyes(Dark)")
dark_brown_eyes = Trait("Brown Eyes(Dark)","Brown Eyes(Dark)")
dark_green_eyes = Trait("Green Eyes(Dark)","Green Eyes(Dark")
eyes = [blue_eyes,brown_eyes,green_eyes,light_blue_eyes,light_brown_eyes,light_green_eyes,dark_green_eyes,dark_blue_eyes,dark_brown_eyes]

#flair
earrings = Trait('Earrings', 'Earrings')

nose_ring = Trait('Nose ring', 'Nose ring')
tattoo_face = Trait("Face tattoos", "Face tattoos")
tattoo_arms = Trait("Tattooed arms", "Tattooed arms")
tattoo_neck = Trait("Tattooed neck", "Tattooed neck")
tattoo_knuckles = Trait("Tattooed knuckles", "Tattooed knuckles")

gold_teeth = Trait("Gold teeth", "Gold teeth")

scars = Trait('Scars', 'Scars')

flair = [earrings,nose_ring,tattoo_face,tattoo_arms,scars,tattoo_neck,tattoo_knuckles,gold_teeth]

#bionic_limbs
bionic_right_eye = Trait('Bionic Eye(Right)', 'Bionic Eye')
bionic_left_eye = Trait('Bionic Eye(Left)', 'Bionic Eye')
bionic_right_arm = Trait('Bionic Arm(Right)', 'Bionic Arm(Right)')
bionic_left_arm = Trait('Bionic Arm(Left)', 'Bionic Arm(Left)')
bionic_right_leg = Trait('Bionic Leg(Right)', 'Bionic Leg(Right)')
bionic_left_leg = Trait('Bionic Leg(Left)', 'Bionic Leg(Left)')

bionic_limbs = [bionic_right_eye,bionic_left_eye,bionic_right_arm,bionic_left_arm,bionic_right_leg,bionic_left_leg]




def gen_player_traits():
	traits = []

	#physical traits

	#eyes
	my_eyes = random.choice(eyes)
	traits.append(my_eyes)

	#hair
	hair_types = [long_hair,short_hair,spiky_hair,shaved_hair,braided_hair,mohawk_hair,parted_hair]
	hair_type = random.choice(hair_types)
	hair_style = random.choice(hair_type)
	traits.append(hair_style)
	#height
	height = random.choice(heights)
	traits.append(height)
	#body
	body = random.choice(body_types)
	traits.append(body)
	#personality
	num_personality_traits = random.randint(1,2)
	pers_count = 1
	while pers_count <= num_personality_traits:
		personality = random.choice(personality_traits)
		traits.append(personality)
		pers_count += 1

	#likes
	roll = random.randint(1,2)
	count = 1
	while count <= roll:
		like = random.choice(likes)
		traits.append(like)
		count += 1
	#flair
	chance = random.randint(1,6)
	if chance == 6:
		flair_choice = random.choice(flair)
		traits.append(flair_choice)

	#bionic stuff
	bionic_chance = random.randint(1,12)
	if bionic_chance == 1:
		bionic_limb = random.choice(bionic_limbs)
		traits.append(bionic_limb)

	return traits

def gen_skills(class_type):
	skills = ['brawl', 'computers', 'dodge', 'disguise', 'etiquette', 'explosives','first_aid', 'hand_to_hand',  'investigate', 'leadership', 'lockpick',
'lying', 'negotiate', 'rifle', 'pickpocket',"pistol", 'persuasion', 'seduction', 'shotgun', 'stealth', 'streetwise', 'throw', 'torture', 'trivia']
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
	throw = 0
	torture = 0
	trivia = 0

        skills = [brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership, 
	lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia]

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
		throw = random.randint(0,1)
		trivia = random.randint(2,4)

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
   	     	throw = random.randint(0,1)
   	     	torture = random.randint(0,3)
   	     	trivia = random.randint(1,3)

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
                throw = random.randint(0,1)
                torture = 0 

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
	skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
lying, negotiate, rifle, pickpocket,pistol, persuasion,security, seduction, shotgun, stealth, streetwise, throw, torture, trivia)
	return skills

def gen_player_weapons(class_type):
	if class_type == 'Hustler':
		hustler_weapons = [knife,baseball_bat, pistol_9mm,crowbar]
		weapon = random.choice(hustler_weapons)
	elif class_type == 'Crimepunk':
		drug_dealer_weapons = [pistol_9mm, shotgun_12g,uzi]
		weapon = random.choice(drug_dealer_weapons)
	elif class_type == 'Hipster':
		hipster_weapons = [punch, knife,baseball_bat]
		weapon = random.choice(hipster_weapons)
	elif class_type == "Scumbag":
		robber_weapons = [shotgun_12g,ak47,uzi]
		weapon = random.choice(robber_weapons)
	elif class_type == "Hacker":
		weapon = punch
	elif class_type == "Wastoid" or class_type == 'Lost Soul' or class_type == 'Sex Worker':
		sex_worker_weapons = [punch, knife,baseball_bat]
		weapon = random.choice(sex_worker_weapons)
	else:
		weapon = punch
	return weapon

def gen_player_outfit(class_type,gender):
	if class_type == "Hustler" or class_type == "Crimepunk" or class_type == "Scumbag" or class_type == 'Lost Soul':
		outfits = [trenchcoat,hoodie,tracksuit]
	elif class_type == "Hipster" or class_type == "Wastoid" or class_type == "Script Kiddie" or class_type == 'Sex Worker':
		if gender == "Male":
			outfits = [tshirt,tracksuit,hoodie]
		elif gender == "Female":
			outfits = [dress,tshirt,hoodie]
	outfit = random.choice(outfits)
	return outfit




class Time: 
        def __init__(self,year,month,day,hour,minute):
                self.year = year
                self.month = month
                self.day = day
                self.hour = hour
		self.minute = minute
        def correct(self):
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

start_time = Time(2069,03,21,1,0)

class City:
	def __init__(self,areas,name,time,player_organization):
		self.areas = areas
		self.name = name
		self.time = time
		self.player_organization = player_organization

class Area:
	def __init__(self,locations,name,organizations,x,y,randos):
		self.locations = locations
		self.name = name
		self.organizations = organizations
		self.x = x
		self.y = y
		self.randos = randos


	def clean_up(self):
		possible_locations = []
		for location in self.locations:
			if location.is_bar == True:
				for item in location.items:
                        		if item.item_type == "weapon" or item.item_type == "outfit":
                        	        	location.items.remove(item)
                		for corpse in location.corpses:
                        		location.corpses.remove(corpse)
			else:
				possible_locations.append(location)
		if len(possible_locations) >= 1:
			target = random.choice(possible_locations)
			for item in target.items:
				if item.item_type == "weapon" or item.item_type == "outfit":
					target.items.remove(item)
			for corpse in target.corpses:
				target.corpses.remove(corpse)
				

class Location:

	def __init__(self,name,city,area,type,x,y,actors,items,is_safehouse,corpses,is_store,sold_here,can_sell,services,services_here,time_open,time_close,is_bar,regulars,is_entrance,rooms,is_library,is_hq,owned_by,bombs_here,floors,parent_location,is_apt):
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

class Container:
	def __init__(self,name,item_type,items,money,is_visible,max_items,max_money,base_value):
		self.name = name
		self.item_type = item_type
		self.items = items
		self.money = money
		self.is_visible = is_visible
		self.max_items = max_items
		self.max_money = max_money
		self.base_value = base_value
fridge = Container('Fridge','container',[],0,True,18,0,1200)
small_safe = Container('Small safe','container',[],0,True,0,10000,300)

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
chair = Junk('Chair',50,'junk',True)
rug = Junk('Rug',500,'junk',True)
couch = Junk('Couch',400,'junk',False)

toilet2 = Junk('Toilet',400,'junk',False)
sink = Junk('Sink',400,'junk',False)
stove = Junk('Stove',400,'junk',False)
shower = Junk('Shower',400,'junk',False)




furniture = [strobe_light,sound_system,bed,bunk_bed,table,chair,couch,small_safe]

#outdoors
small_tree = Junk('Small tree',700,'junk',False)
tree = Junk('Tree',700,'junk',False)
fountain = Junk('Fountain',700,'junk',False)
hedge = Junk('Hedge',700,'junk',False)
dog = Junk('Dog',700,'junk',False)



#library 
library_card = Junk('Library card',100,'junk',True)
desktop_computer = Junk('Desktop computer',200,'junk',False)
#gear
sleeping_bag = Junk('Sleeping bag',300,'junk',True)
rope = Junk('Rope',25,'junk',False)

area_id = 1
location_id = 1




#NPCs
def create_npc(profession,affiliation,home):
	#gender
	genders = ['Male', 'Female']
	gender = random.choice(genders)
	#age
	age = random.randint(18,45)
	#health
	#health = Health(100,100,100,100,100,100,0,0,100,0,0,100,100,100)
	#stats


	#squatter,crimepunk,scumbag

	if profession == 'Squatter' or profession == "Crimepunk" or profession == "Scumbag" or profession == "Wastoid" or profession == "Junkfreak" or profession == "Pissboi" or profession == "Meatball" or profession == 'Sex Worker' or profession == 'Lost Soul':
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
		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100)
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
        	throw = random.randint(0,2)
        	torture = random.randint(0,2)
		trivia = random.randint(0,2)
		skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
		lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia)
                skills_xp = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia)
		#weapon
		weapons = [knife,baseball_bat,pistol_9mm,shotgun_12g,shovel,crowbar]
		weapon = random.choice(weapons)

                if weapon.name == "Knife" or weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
                        skills.brawl = random.randint(1,3)
                elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
                        skills.pistol = random.randint(1,3)
                elif weapon.name == "12g Shotgun": 
                        skills.shotgun = random.randint(1,3) 
                elif weapon.name == "AK-47": 
                        skills.rifle = random.randint(1,3) 

		#outfit
		possible_outfits = [hoodie,tshirt,trenchcoat]
		outfit = random.choice(possible_outfits)
		#tool
		tool = None
		#traits
		traits = gen_player_traits()
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
		combat_status = Combat_Status(False,False,False,False,False)
		#mind
		happiness = random.randint(40,100)
		stress = random.randint(0,20)
		sanity = random.randint(40,100)
		horny = random.randint(0,50)
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

		#home
		home = 'None'

		#finally make the npc
		npc = Char(gender,age, profession,affiliation,health, npc_stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'enemy',combat_status,home,mind,hunger,thirst,sleep)
		return npc
#crankenstein,sex worker,lost soul,gamer assassin,bike courier,script kiddie
	elif profession == "Gamer Assassin" or profession == "Flower Child" or profession == "Pissboi Leader" or profession == "Pissboi Enforcer" or profession == 'Crankenstein' or profession == "Crankenstein Enforcer" or profession == "Crankenstein Leader" or profession == "Drunkard"  or profession == "Crackhead" or profession == "Drunkard" or profession == "Script Kiddie" or profession == "Crackhead" or profession == "Clerk" or profession == "Nudist" or profession == "Hobo" or  profession == "Rocker" or profession == "Marxist":
		strength, base_strength = 9,9
		dexterity, base_dexterity = 8,8
		willpower, base_willpower = 9,9
		intelligence, base_intelligence = 10,10
		charisma, base_charisma = 9,9
		max_health = strength * 10	
		health = Health(max_health,max_health,max_health,100,100,100,0,100,100,0,0,100,100,100)
		npc_stats = Stats(strength, dexterity, intelligence, willpower, charisma, base_strength, base_dexterity, base_intelligence,base_willpower,base_charisma)
		#injuries
		injuries = []
		#skills

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
        	explosives = 0
		#first aid
        	first_aid = random.randint(0,2)
		#investigate
        	investigate = random.randint(0,3)
		if profession == "Crankenstein Leader" or profession == "Pissboi Leader":
			leadership = 9
		elif profession == "Marxist":
			leadership = random.randint(3,5)
			rifle = random.randint(3,5)
			weapon = ak47
		else:
        		leadership = 0
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
        	persuasion = 0
        	security = 0
        	seduction = random.randint(0,2)
        	shotgun = random.randint(0,1)
        	stealth = 0
        	streetwise =  random.randint(1,3)
        	throw = 0
        	torture = 0
		trivia = 0
		skills = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
		lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia)
		skills_xp = Skills(brawl, computers, dodge, disguise, etiquette, explosives,first_aid, investigate, leadership,
                lying, negotiate, rifle, pickpocket,pistol, persuasion, security, seduction, shotgun, stealth, streetwise, throw, torture, trivia)
		#weapon
		weapons = [knife,baseball_bat,pistol_9mm,shotgun_12g]
		weapon = random.choice(weapons)
		if weapon.name == "Knife" or weapon.name == "Crowbar" or weapon.name == "Baseball bat" or weapon.name == "Shovel":
			skills.brawl = random.randint(1,3)
		elif weapon.name == "9mm Pistol" or weapon.name == "Uzi":
			skills.pistol = random.randint(1,3)
		elif weapon.name == "12g Shotgun":
			skills.shotgun = random.randint(1,3)
		elif weapon.name == "AK-47":
			skills.rifle = random.randint(1,3) 
		if profession == "Crankenstein" or profession == "Crankenstein Leader" or profession == "Crankenstein Enforcer" or profession == "Marxist":
			weapon = ak47
			skills.rifle = random.randint(3,5)
		#outfit
		possible_outfits = [hoodie,tshirt,trenchcoat]
		if profession == "Crankenstein" or profession == "Crankenstein Leader" or profession == "Crankenstein Enforcer":
			outfit = body_armor
		elif profession == "Marxist":
			outfit = army_uniform
		elif profession == "Nudist":
			outfit = naked
			weapon = sword
		elif profession == 'Clerk':
			outfit = cheap_suit
			skills.lying = random.randint(2,5)
			skills.disguise = random.randint(2,5)
			skills.etiquette = random.randint(2,5)
			skills.computers = random.randint(2,5)
			skills.persuasion = random.randint(2,5)
		else:
			outfit = random.choice(possible_outfits)
		#tool
		tool = None
		#traits
		traits = gen_player_traits()
		#drugs
		drugs = []
		chance = 3
		roll = random.randint(1,3)
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
	
		combat_status = Combat_Status(False,False,False,False,False)
                #mind
                happiness = random.randint(40,100)
                stress = random.randint(0,50)
                sanity = random.randint(40,100)
                horny = random.randint(0,50)
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


		home = 'None'

		#finally make the npc
		npc = Char(gender,age, profession,affiliation,health, npc_stats, injuries, skills,skills_xp,weapon,outfit,tool,traits,drugs,fname,lname,money,'enemy',combat_status,home,mind,hunger,thirst,sleep)
		return npc




#Cliff Heights


abandoned_building_names = ['Abandoned Factory', 'Abandoned Office', 'Abandoned Store', 'Abandoned Laundromat','Abandoned Mall',
			'Abandoned School','Abandoned Gas Station','Abandoned House',"Abandoned Church"]


#medical
class Medical:
	def __init__(self,name, base_value,number,item_type,can_loot,time_to_wear_off,nutrition):
		self.name = name
		self.base_value = base_value
		self.number = number
		self.item_type = item_type
		self.can_loot = can_loot
		self.time_to_wear_off = time_to_wear_off
		self.nutrition = nutrition

bandages = Medical('Bandages', 100,10,'medical',True,48,0)
morphine = Medical('Morphine', 100,1,'medical',True,4,0)
speed = Medical('Speed', 50,1,'medical',True,3,0)
speed_3g = Medical('Speed', 50,3,'medical',True,3,0)
speed_7g = Medical('Speed', 50,7,'medical',True,3,0)
speed_14g = Medical('Speed', 50,7,'medical',True,3,0)
speed_28g = Medical('Speed', 50,1,'medical',True,3,0)
crack = Medical('Crack', 80,1,'medical',True,3,0)
crack_3g = Medical('Crack', 80,3,'medical',True,3,0)
crack_7g = Medical('Crack', 80,7,'medical',True,3,0)
crack_14g = Medical('Crack', 80,14,'medical',True,3,0)
crack_28g = Medical('Crack', 80,28,'medical',True,3,0)

coffee = Medical('Coffee', 4,1,'medical',True,3,0)

cocaine = Medical('Cocaine', 100,1,'medical',True,3,0)
cocaine_3g = Medical('Cocaine', 100,3,'medical',True,3,0)
cocaine_7g = Medical('Cocaine', 100,7,'medical',True,3,0)
cocaine_14g = Medical('Cocaine', 100,14,'medical',True,3,0)
cocaine_28g = Medical('Cocaine', 100,28,'medical',True,3,0)

weed = Medical('Weed', 10,1,'medical',True,3,0)
weed_3g = Medical('Weed', 10,3,'medical',True,3,0)
weed_7g = Medical('Weed', 10,7,'medical',True,3,0)
weed_14g = Medical('Weed', 10,14,'medical',True,3,0)
weed_28g = Medical('Weed', 10,28,'medical',True,3,0)
weed_112g = Medical('Weed',10,112,'medical',True,3,0)

heroin = Medical('Heroin', 90,1,'medical',True,3,0)
heroin_3g = Medical('Heroin', 90,3,'medical',True,3,0)
heroin_7g = Medical('Heroin', 90,7,'medical',True,3,0)
heroin_14g = Medical('Heroin', 90,14,'medical',True,3,0)

#withdrawls

opiate_withdrawl = Medical('Opiate withdrawl', 90,1,'medical',True,3,0)
cocaine_withdrawl = Medical('Cocaine withdrawl', 90,1,'medical',True,3,0)
speed_withdrawl = Medical('Speed withdrawl', 90,1,'medical',True,3,0)

#cravings
opiate_craving = Medical('Opiate craving', 90,1,'medical',True,3,0)
cocaine_craving = Medical('Cocaine craving', 90,1,'medical',True,3,0)
speed_craving = Medical('Speed craving', 90,1,'medical',True,3,0)

#food
hamburger = Medical('Hamburger', 8,1,'food',True,3,25)
fries = Medical('Fries', 4,1,'food',True,3,15)
pizza = Medical('Pizza', 4,1,'food',True,3,20)
chips = Medical('Chips', 2,1,'food',True,3,10)
chocolate_bar = Medical('Chocalate bar', 2,1,'food',True,3,8)
beef_jerky = Medical('Beef jerky', 3,1,'food',True,3,14)
peanuts = Medical('Peanuts', 3,1,'food',True,3,5)
candy = Medical('Candy', 3,1,'food',True,3,8)
corn_dog = Medical('Corn dog', 5,1,'food',True,3,10)
donut = Medical('Donut', 2,1,'food',True,3,5)

#drinks
cola = Medical('Cola', 2,1,'drink',True,3,50)
energy_drink = Medical('Energy drink', 3,1,'drink',True,3,40)
slurpy = Medical('Slurpy', 4,1,'drink',True,3,60)

drinks = [cola,energy_drink,slurpy]

#abandoned apt building
def gen_abandoned_apt_building(x,y):
	actors = NPC([],0,[],0)
	floors =[]
	rooms = []

	num_floors = 1
	rooms_per_floor = random.randint(4,24)
	floor1 = []
	floor2 = []
	room_count = 1
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
               		member = create_npc(profession,'none','None')
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

       		room = Location(apt_name,'Templeville','Cliff Heights',apt_name,x,y,actors,items,False,[],True,[],False,False,
       		[],13,23,False,[],False,[],False,False,'No one',[],[],None,True)
		room.is_bar = False
		room.is_store = False
		room.is_apt = False
		rooms.append(room)
		room_count += 1

	actors = NPC([],0,[],0)
        building = Location("Abandoned Apt. Building",'Templeville','Cliff Heights','Abandoned Apt. Building',x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,False)
	for room in building.rooms:
		#print room.name
		room.parent_location = building
		for actor in actors.members:
			print actor.fname
			actor.home = room
        return building


#abandoned buildings

def gen_abandoned_building(is_safehouse,locations,name,x,y):
	names = []

	where = ['Templeville','Cliff Heights','Abandoned Building']
	num_items = random.randint(4,11)
	possible_items =  [broken_desk,broken_light,broken_glass,broken_monitor,cat,copper_wire,hole_in_wall,hole_in_floor,toilet,old_newspaper,
	office_chair,pile_of_rubble,smokeable_butt,trash]
	

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
			member = create_npc(profession,'none','None')
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
		building = Location(str(name),'Templeville','Cliff Heights','Abandoned Building',x,y,actors,items,True,corpses,False,[],False,False,[],0,23,False,[],False,[],False,False,'No one',[],[],None,False)
	elif is_safehouse == False:
		building = Location(str(name),'Templeville','Cliff Heights','Abandoned Building',x,y,actors,items,False,corpses,False,[],False,False,[],0,23,False,[],False,[],False,False,'No one',[],[],None,False)
			
	
	return building

# pawn & gun
def gen_pawn_shop(x,y):
	actors = NPC([],0,[],0)
	building = Location("Pawn Shop",'Templeville','Cliff Heights','Pawn Shop',x,y,actors,[counter,trash],False,[],True,
	[pistol_9mm,shotgun_12g,ak47,body_armor,sword,uzi],True,False,[],8,19,False,[],False,[],False,False,'No one',[],[],None,False)
	return building	
#thrift shop
def gen_thrift_store(x,y):
        actors = NPC([],0,[],0)

	building = Location("Thrift Store",'Templeville','Cliff Heights','Thrift Store',x,y,actors,[counter,chair],False,[],True,[knife,baseball_bat,crowbar,shovel,tshirt,
	tracksuit,hoodie,cheap_suit,trenchcoat,leather_jacket,dress,sleeping_bag,rope,chair,rug,table],False,False,[],13,23,False,[],False,[],False,False,'No one',[],[],None,False)
        return building
#bar
def gen_bar(x,y):
	actors = NPC([],0,[],0)

	regulars= []
	num_regulars = random.randint(10,22)
	count = 1
        while count <= num_regulars:
	        professions = ["Flower Child", "Gamer Assassin","Crimepunk", "Pissboi","Wastoid","Junkfreak","Meatball","Crankenstein","Crackhead","Script Kiddie","Sex Worker","Lost Soul","Drunkard","Clerk","Nudist","Rocker","Mercenary"]
                profession = random.choice(professions)
		if profession == "Crankenstein" or profession == "Pissboi" or profession == "Flower Child" or profession == "Gamer Assassin"or profession == "Clerk" or profession == "Nudist":
                	regular = create_npc(profession,'none','None')
		else:
			regular = create_npc(profession,'none','None')
			
                regulars.append(regular)
                if random.randint(1,3) == 3:
         		inventory = [morphine,crack,speed,heroin]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

	building = Location('Bar','Templeville','Cliff Heights','Abandoned Building',x,y,actors,[bar_stool,bar_stool,bar_stool,bar_stool,counter,booth,booth,
	booth, booth],False,[],True,[beer],False,False,[],11,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
	return building

#doctor

heal_injuries = Service("heal injuries",5000,"heal all the characters injuries")
max_health = Service("restore health",500,"restore character to max health")


def gen_doctor(x,y):
        actors = NPC([],0,[],0)

        building = Location("Doctor",'Templeville','Cliff Heights','Doctor',x,y,actors,[counter],False,[],True,[bandages,heroin,speed],False,True,
	[heal_injuries],13,23,False,[],False,[],False,False,'No one',[],[],None,False)
        return building

#crackhouse
def gen_crackhouse(x,y):
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
                professions = ["Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
		affiliation = 'none'
                regular = create_npc(profession,'none','None')
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

        building = Location('Crack House','Templeville','Cliff Heights','Crack House',x,y,actors,items,False,[],True,[crack],False,False,[],1,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building
#coffee shop
def gen_coffee_shop(x,y):
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
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Coffee Shop','Templeville','Cliff Heights','Coffee Shop',x,y,actors,items,False,[],True,[crack],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building

def gen_mcshits(x,y):
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
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [cocaine,heroin,morphine,weed]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('McShits','Templeville','Cliff Heights','McShits',x,y,actors,items,False,[],True,[hamburger,fries,cola],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building

def gen_pizza_place(x,y):
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
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,weed,crack,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('World Famous Pizza','Templeville','Cliff Heights','World Famous Pizza',x,y,actors,items,False,[],True,[pizza,fries],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building

#convenience store
def gen_convenience_store(x,y):
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
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,weed,crack,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Convenience store','Templeville','Cliff Heights','Convenience store',x,y,actors,items,False,[],True,[cola,energy_drink,chocolate_bar,candy,chips,peanuts,beef_jerky,corn_dog],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building



#library
def gen_library(x,y):
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
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,crack,speed,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Public Library','Templeville','Cliff Heights','Public Library',x,y,actors,items,False,[],True,[library_card],False,False,[],6,23,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building

def create_stash(power):
        num_items = random.randint((power /2),power)
        count = 1
        items = []
        while count <= num_items:
                possible_items = [crack_14g,crack_28g,pistol_9mm,shotgun_12g,uzi,speed_28g,speed_14g,ak47,cocaine_14g,cocaine_28g,weed_28g,weed_112g]
                item = random.choice(possible_items)
                items.append(item)
                count += 1
        return items


#gang hq
def gen_gang_hq(x,y,name,locations):
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

        actors = NPC([],0,[],0)

        regulars= []
        num_regulars = random.randint(20,30)
        count = 1
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
	        while count <= num_regulars:
	                professions = ["Crankenstein", "Crankenstein Leader", "Crankenstein Enforcer"]
	                profession = random.choice(professions)
	                regular = create_npc(profession,'profession','None')
	                regulars.append(regular)
	                inventory = []
	                fame = 20
	                money = 5
	                count += 1
        elif name == "Pissbois":
                while count <= num_regulars:
                        professions = ["Pissboi","Pissboi Leader", "Pissboi Enforcer"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Gamer Assassins":
                while count <= num_regulars:
                        professions = ["Gamer Assassin"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Flower Collective":
                while count <= num_regulars:
                        professions = ["Flower Child"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
	elif name == "Clerks":
		while count <= num_regulars:
                        professions = ["Clerk"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 500
                        count += 1
        elif name == "Nudists":
		while count <= num_regulars:
                        professions = ["Nudist"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1
        elif name == "Marxists":
                while count <= num_regulars:
                        professions = ["Marxist"]
                        profession = random.choice(professions)
                        regular = create_npc(profession,name,'None')
                        regulars.append(regular)
                        inventory = []
                        fame = 20
                        money = 5
                        count += 1

	power = random.randint(3,5)
	#amount_sold = random.randint(2,power)
	possible_items = [pistol_9mm,shotgun_12g,ak47,crack_7g,crack_14g,crack_28g,morphine,speed_7g,speed_14g,speed_28g,body_armor,cocaine_3g,cocaine_7g,cocaine_14g,cocaine_28g,weed_3g,weed_7g,weed_14g,weed_28g]
	items_sold = []
	
	item_count = 1
	while item_count <= power:
		item_to_sell = random.choice(possible_items)
		if item_to_sell not in items_sold:
			items_sold.append(item_to_sell)
		item_count += 1
	
	
	stash_items = create_stash(power)
	money = random.randint(2000,10000)
	stash = Container(name + ' Stash','container',stash_items,money,False,power,20000,10000)
	items.append(stash)


	building = Location(name + ' HQ','Templeville','Cliff Heights', name + ' HQ',x,y,actors,items,False,[],
	True,items_sold,False,False,[],6,23,True,regulars,False,[],False,True,name,[],[],None,False)
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
	count = 1
	while count <= power:
		location_valid = False
		while location_valid == False:
			try:
				location = random.choice(locations)
		                if location.owned_by == "No one":
					try:
        	        	        	location.owned_by = name
        	        	        	locations_owned.append(location)
        	        	        	count += 1
						location_valid = True
					except:
						count += 1
						location_valid = True
			except:
				count_valid += 1
				location_valid = True
	territory = []
	organization = Organization(name,False,regulars,0,building,locations_owned,power,[],[],False,0,False)
#self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid
        return building, organization


def gen_apt_building(x,y):
        actors = NPC([],0,[],0)
	floors =[]
	rooms = []

	num_floors = 1
	rooms_per_floor = random.randint(4,24)
	floor1 = []
	floor2 = []
	room_count = 1
	#items = []
	while room_count <= rooms_per_floor:
		is_vacant = random.randint(1,4)
		items = []
		if is_vacant == 1:
			apt_name = 'Vacant Apartment'
		        actors = NPC([],0,[],0)
			items = []
			owned_by = 'No one'
		elif is_vacant != 1:
               		professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
               		profession = random.choice(professions)
			members = []
               		member = create_npc(profession,'none','None')
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
			items.append(shower)
			rug_chance = random.randint(1,2)
			if rug_chance == 1:
				items.append(rug)
			#actors = NPC([],0,[],0)
                items.append(sink)
                items.append(stove)
                items.append(toilet2)
                items.append(shower)

       		room = Location(apt_name,'Templeville','Cliff Heights',apt_name,x,y,actors,items,False,[],True,[],False,False,
       		[],13,23,False,[],False,[],False,False,'No one',[],[],None,True)
		room.is_bar = False
		room.is_store = False
		rooms.append(room)
		room_count += 1

	actors = NPC([],0,[],0)
        building = Location("Apartment Building",'Templeville','Cliff Heights','Apartment Building',x,y,actors,[],False,[],True,[],False,True,
        [],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,False)
	for room in building.rooms:
		#print room.name
		room.parent_location = building
		for actor in actors.members:
			print actor.fname
			actor.home = room
        return building

#shack
def gen_shack(x,y):
        actors = NPC([],0,[],0)
	floors =[]
	rooms = []


	num_occupants = random.randint(1,4)
	floor1 = []
	floor2 = []
	occupant_count = 1
	#items = []
	while occupant_count <= num_occupants:
		items = []
   		professions = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul"]
        	profession = random.choice(professions)
		members = []
           	member = create_npc(profession,'none','None')
           	members.append(member)
		#items.append(bed)
		#unt += 1
		apt_name = 'Shack' 
                #actors = NPC(members,0,[],0)
		owned_by = 'No one'
		items.append(sleeping_bag)
		items.append(table)
		items.append(chair)
                #items.append(chair)
		#rug_chance = random.randint(1,2)
		#if rug_chance == 1:
		#	items.append(rug)
		#actors = NPC([],0,[],0)
		occupant_count += 1
	#rooms = floor1
	actors = NPC(members,0,[],0)
    	building = Location("Shack",'Templeville','Cliff Heights','House',x,y,actors,items,False,[],True,[],False,True,
    	[],13,23,False,[],False,rooms,False,False,'No one',[],floors,None,True)
	building.is_bar = False
        for room in building.rooms:
                #print room.name
		room.rooms = building.rooms
                room.parent_location = building
                for actor in actors.members:
                        print actor.fname
                        actor.home = room
	#for room in building.rooms:
	#	room.rooms = building.rooms
	

    	return building

#park
def gen_park(x,y):
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
                professions = ["Hustler","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul","Rocker"]
                profession = random.choice(professions)
                regular = create_npc(profession,'none','None')
                regulars.append(regular)
                if random.randint(1,3) == 3:
                        inventory = [heroin,cocaine,crack,speed,morphine]
                else:
                        inventory = []
                fame = 20
                money = 5
                count += 1
                #regulars = NPC(regulars,money,inventory,fame)

        building = Location('Park','Templeville','Cliff Heights','Park',x,y,actors,items,False,[],True,[crack],False,False,[],1,24,True,regulars,False,[],False,False,'No one',[],[],None,False)
        return building



#abandoned apt building

def gen_neighborhood(type,neighborhood_name):
	global location_id
	locations = []
	count = 1
	first_building = True
	#abandoned buildings
	for name in abandoned_building_names:
		if first_building == True:
			x = random.randint(1,16)
			y = random.randint(1,16)
			abandoned_building = gen_abandoned_building(True,locations,name,x,y)
			locations.append(abandoned_building)
			first_building = False
		elif first_building == False:
			checked = False
			exists = False
			while checked == False:
				x = random.randint(1,16)
				y = random.randint(1,16)
				for location in locations:
					if location.x == x and location.y == y:
						exists = True
						#checked = True
					if exists == False:
						checked = True
	
			abandoned_building = gen_abandoned_building(True,locations,name,x,y)
			locations.append(abandoned_building)
			print abandoned_building.name


	#pawn shop
	def get_unused_location():
	        checked = False
	        exists = False
        	x = random.randint(1,16)
                y = random.randint(1,16)
        	for location in locations:
	                if location.x != x and location.y != y:
        	                #exists = False
                                checked = True
		        elif location.x == x and location.y == y:
				x = random.randint(1,16)
               			y = random.randint(1,16)
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
	
	#abandoned apt buildings
        #apt_count = 1
        #num_apt = random.randint(3,5)
        #while apt_count <= num_apt:
        #        x, y = get_unused_location()
        #        apt_finished = False
        #        while apt_finished == False:
        #                try:
        #                        apt_building = gen_abandoned_apt_building(x,y)
        #                        locations.append(apt_building)
        #                        apt_finished = True
        #                        apt_count += 1
        #                except:
        #                        apt_finished = False

	#pawn shop
	pawn_count = 1
	pawn_max = random.randint(2,3)
	while pawn_count <= pawn_max:
		x, y = get_unused_location()
		pawn_shop = gen_pawn_shop(x,y)
		locations.append(pawn_shop)
		print 'pawn shop'
		pawn_count += 1
	#thrift store
	x, y = get_unused_location()
        thrift_store = gen_thrift_store(x,y)
        locations.append(thrift_store)
	print 'thrift store'
        #bar
	max_bars = random.randint(3,5)
	count = 1
	while count <= max_bars:
	        x, y = get_unused_location()
	        maggies_bar = gen_bar(x,y)
	        locations.append(maggies_bar)
		count += 1
		print 'bar'
	#doctor
	x, y = get_unused_location()
	doctor = gen_doctor(x,y)
	locations.append(doctor)
	print 'doctor'

        #crackhouses
	num_crackhouses = random.randint(4,7)
	count = 1
	while count <= num_crackhouses:
	        x, y = get_unused_location()
	        crackhouse = gen_crackhouse(x,y)
	        locations.append(crackhouse)
		print 'crackhouse'
		count += 1

        #coffee shop
	num_coffee_shop = random.randint(1,3)
	count = 1
	while count <= num_coffee_shop:
        	x, y = get_unused_location()
        	coffee_shop = gen_coffee_shop(x,y)
        	locations.append(coffee_shop)
		print 'coffee shop'
		count += 1
        #mcshits
        x, y = get_unused_location()
        mcshits = gen_mcshits(x,y)
        locations.append(mcshits)
	print 'mcshits'
        #pizza
        x, y = get_unused_location()
        pizza_place = gen_pizza_place(x,y)
        locations.append(pizza_place)
	print 'pizza'
	#convenience store
        num_convenience_store = random.randint(3,5)
        count = 1
        while count <= num_convenience_store:
                x, y = get_unused_location()
                store = gen_convenience_store(x,y)
                locations.append(store)
                print 'convenience store'
                count += 1

        #library
        x, y = get_unused_location()
        library = gen_library(x,y)
        locations.append(library)
	organizations = []
	print 'library'

        #apt building
        apt_count = 1
        num_apt = random.randint(10,16)
        while apt_count <= num_apt:
                x, y = get_unused_location()
                apt_finished = False
                while apt_finished == False:
                        try:
                                apt_building = gen_apt_building(x,y)
                                locations.append(apt_building)
                                apt_finished = True
                                apt_count += 1
                        except:
                                apt_finished = False
        #parks
        max_parks = random.randint(2,3)
	count = 1
	while count <= max_parks:
		x, y = get_unused_location()
		park = gen_park(x,y)
		locations.append(park)
		count += 1
		print 'park'
	#gang hq
	organizations = []
	gang_names = ["Crankensteins", "Pissbois","Gamer Assassins","Flower Collective","Clerks","Nudists"]
	for name in gang_names:
			gang_valid = False
			while gang_valid == False:
				x, y = get_unused_location()
				print x, y
				gang_hq,organization = gen_gang_hq(x,y,name,locations)
				print gang_hq
				print organization
				print organization.name
				organizations.append(organization)
				gang_valid = True
				#gang_valid = False
        #houses
        count  = 1
        max_shacks = random.randint(14,20)
        while count <= max_shacks:
                x,y = get_unused_location()
                shack = gen_shack(x,y)
                locations.append(shack)
		print shack
                count += 1
		
		
	#assign homes to npcs
	for location in locations:
		for member in location.actors.members:
			if member == None:
				location.actors.members.remove(member)
			else:
				member.home = location
		if len(location.rooms) >= 1:
			for location in location.rooms:
				for member in location.actors.members:
					if member == None:
						location.actors.members.remove(member)
					else:
						member.home = location
	#assign apartments to controlling factions
	for location in locations:
		if location.owned_by != 'No one':
			for room in location.rooms:
				room.owned_by = location.owned_by
	print 'assigned rooms'
	type_randos = ["Hustler","Meatball","Crimepunk","Drunkard","Wastoid","Junkfreak","Meatball","Crackhead","Sex Worker","Lost Soul",'Crankenstein','Flower Child','Rocker','Clerk']
	num_randos = random.randint(40,60)
	rando_count = 1
	randos = []
	while rando_count <= num_randos:
		try:
			profession = random.choice(type_randos)
			rando = create_npc(profession,'none','None')
			randos.append(rando)
			rando_count += 1
		except:
			rando_count += 1
	
	x = random.randint(1,16)
	y = random.randint(1,16)
	cliff_heights = Area(locations,neighborhood_name,organizations,x,y,randos)
	return cliff_heights

def gen_new_city():
	player_organization = Organization('Player organization',True,[],0,[],[],1,[],[],False,0,False)
	player_organization.locations_owned = []
#self,name,is_player,footsoldiers,player_reputation,hq,locations_owned,power,territory,rent_due,rent_paid
	city_created = False
	while city_created == False:
		cliff_heights = gen_neighborhood('Slum','Cliff Heights')
		city_created = True
	areas = [cliff_heights]
	name = "Templeville"
	time = start_time
	city = City(areas,name,time,player_organization)
	return city

#templeville = gen_district()

