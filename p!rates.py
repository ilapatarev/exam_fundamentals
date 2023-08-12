def city_targeting(cities):
	command=input()
	while command!='Sail':
		command=command.split('||')
		city=command[0]
		population=int(command[1])
		gold=int(command[2])
		if city in cities:
			cities[city][0]+=population
			cities[city][1]+=gold
		else:
			cities[city]=[population, gold]
		command=input()
	return cities

def pirate_trip(cities):
	command=input()
	while command!='End':
		command=command.split('=>')
		order=command[0]
		city=command[1]
		if order=='Plunder':
			people_killed=int(command[2])
			gold_stolen=int(command[3])
			cities[city][0]-=people_killed
			cities[city][1]-=gold_stolen
			print(f"{city} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
			if cities[city][0]==0 or cities[city][1]==0:
				print(f"{city} has been wiped off the map!")
				cities.pop(city)
		elif order=='Prosper':
			gold_icreased=int(command[2])
			if gold_icreased<0:
				print("Gold added cannot be a negative number!")
			else:
				cities[city][1]+=gold_icreased
				print(f"{gold_icreased} gold added to the city treasury. {city} now has {cities[city][1]} gold.")
		command=input()
	return cities

def print_the_result(cities):
	if len(cities)==0:
		print("Ahoy, Captain! All targets have been plundered and destroyed!")
	else:
		print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
		for town, pop in cities.items():
			print(f'{town} -> Population: {cities[town][0]} citizens, Gold: {cities[town][1]} kg')




def pirate_way():
	cities={}
	city_targeting(cities)
	pirate_trip(cities)
	print_the_result(cities)

pirate_way()