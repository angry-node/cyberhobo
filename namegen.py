import random


male_fnames = ["Florencio","Norman","Gilbert","Chi","Milton","Coleman","Troy","Ernesto","Rory",  
	"Zane","Hassan",'Jordan','Luke','Tommy','Adam','Eliseo','Jessie','Andy','Ward','Delbert','Jackson','Jeffery',  
	'Palmer','Corey','Denny','Cecil','Myron','Craig','Malcolm','Archie','Bertram','Stephan','Nigel','Bennie','Fredrick',
	'Spencer','Arnold','Jerrold','Noah','Lino','Derek','Vicente','Olen','Guy','Harrison']  

female_fnames = ['Erline','Britney','Bebe','Leann','Towanda','Hillary','Luetta','Rachal','Cassey','Carie','Melva','Sunny','Maragret',  
	'Tatum','Arlyne','Laurie','Mindy','Lael','Zelma','Elli','Rosana','Isis','Marhta','Rhea','Jacalyn','Roseanne','Treena','Katheleen','Wenona',  
	'Eladia','Shera','Sina','Cris','Mallie','Margrett','Karen','Maricela','Layla','Meagan','Ghislaine','Penelope','Larue','Dulce','Mavis',
	'Marlene','Mina','Drusilla','Edna','Ashley']  

surnames = ['Riedo', 'Perrin', 'Mcqueeney', 'Kooperberg','Seneca', 'Yamamoto', 'Das', 'Edick', 'Ciluaga', 'Giommi', 'Kohlberg', 'Schoenbach', 'Schiano',
	'Emory', 'Brown', 'Miranda', 'Lipponen', 'Luntz', 'Haines', 'Kester', 'Knell', 'Bloomfield', 'Viggiani', 'Beyer', 'Dohrman', 'Endres', 'Darlington',
	'Rando', 'Maron', 'Hemingway', 'Cvek', 'Mclaughlin', 'Novio', 'Frisken', 'Ku', 'Vierra', 'Skjaervo', 'Granfors', 'Mahmood', 'Webb','Garcia',
	'Cook','Lopez','Wilson','Scott','Murphy','Beijer','Henderson','Green','Taylor','Anderson','Baker','Cooper','Bell','Jenkins', 'King',
	'Brown','Davis','Reed','Adams','Perez','Turner','Collins','Brooks','Russel','Griffin']




first_names = ['Meadow','Summer','Pine','Spring','University','Royal','Shadow']

second_names = ['Heights','Place','Terrace','Towers','Apartments','Estates','Gardens','Suites','Co-op','Wood','Oaks','View','Green','Point']

def gen_apt_name():
	roll = random.randint(1,4)
	if roll == 1:
		first = random.choice(first_names)
	elif roll == 2:
		first = random.choice(male_fnames)
	elif roll == 3:
		first = random.choice(female_fnames)
	elif roll == 4:
		first = random.choice(surnames)

	second = random.choice(second_names)

	name = first + ' ' + second
	return name

def gen_pawn_name():
	roll = random.randint(1,3)
	if roll == 1:
		first = random.choice(male_fnames)
	elif roll == 2:
		first = random.choice(female_fnames)
	elif roll == 3:
		first = random.choice(surnames)
	
	name = first + "'s Pawn Shop"
	return name

def gen_park_name():
        roll = random.randint(1,3)
        if roll == 1:
                first = random.choice(male_fnames)
        elif roll == 2:
                first = random.choice(female_fnames)
        elif roll == 3:
                first = random.choice(surnames)

	elif roll == 4:
		first = random.choice(first_names)

	name = first + ' Park'
	return name
