
plants_info={}
num=int(input())
for n in range(num):
	plants=input().split('<->')
	plant=plants[0]
	rarity=plants[1]
	if plant in plants_info:
		plants_info[plant]=[rarity]
	else:
		plants_info[plant]=[rarity]

command=input()
while command!='Exhibition':
	command=command.split(': ')
	action=command[0]
	plant_things=command[1]
	if action=='Rate':
		plant_things=plant_things.split(' - ')
		plant_name=plant_things[0]
		plant_rating=plant_things[1]
		if plant_name not in plants_info:
			print("error")
		else:
			plants_info[plant_name].append(plant_rating)

	elif action=='Update':
		plant_things=plant_things.split(' - ')
		plant_name=plant_things[0]
		new_rarity=plant_things[1]
		if plant_name not in plants_info:
			print("error")
		else:
			plants_info[plant_name][0]=new_rarity
	elif action=='Reset':
		plant_name=plant_things
		if plant_name not in plants_info:
			print("error")
		else:
			plants_info[plant_name]=[plants_info[plant_name][0]]

	command=input()

print('Plants for the exhibition:')
for pla, things in plants_info.items():
	plant_name=pla
	rarity=things[0]
	ratings=things[1:]
	sum_of_ratings=0
	if len(ratings)==0:
		av_rating=0
	else:
		for r in range(len(ratings)):
			sum_of_ratings+=int(ratings[r])
		av_rating=sum_of_ratings/len(ratings)
	print(f'- {plant_name}; Rarity: {rarity}; Rating: {av_rating:.2f}')