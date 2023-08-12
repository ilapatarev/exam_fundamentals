def input_heroes(heroes):
	number_of_heroes=int(input())
	for hero in range(number_of_heroes):
		data=input().split(' ')
		hero=data[0]
		hp=int(data[1])
		mp=int(data[2])
		heroes[hero]=[hp, mp]
	return heroes

def heroes_fight(heroes):
	command=input()
	while command!='End':
		command=command.split(' - ')
		order=command[0]
		hero_name=command[1]
		if order =='CastSpell':
			mp_needed=int(command[2])
			spell_name=command[3]
			if heroes[hero_name][1]>=mp_needed:
				heroes[hero_name][1]-=mp_needed
				print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
			else:
				print(f"{hero_name} does not have enough MP to cast {spell_name}!")
		elif order=='TakeDamage':
			damage=int(command[2])
			attacker=command[3]
			heroes[hero_name][0]-=damage
			if heroes[hero_name][0]<=0:
				print(f"{hero_name} has been killed by {attacker}!")
				heroes.pop(hero_name)
			else:
				print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
		elif order=='Recharge':
			amount=int(command[2])
			if heroes[hero_name][1]+amount>200:
				amount=200-heroes[hero_name][1]
			heroes[hero_name][1]+=amount
			print(f"{hero_name} recharged for {amount} MP!")
		elif order =="Heal":
			amount_hp=int(command[2])
			if heroes[hero_name][0]+amount_hp>100:
				amount_hp=100-heroes[hero_name][0]
			heroes[hero_name][0]+=amount_hp
			print(f"{hero_name} healed for {amount_hp} HP!")
		command=input()
	return heroes

def heroes_print(heroes):
	for hero, hp_mp in heroes.items():
		print(f'{hero}')
		print(f'  HP: {heroes[hero][0]}')
		print(f'  MP: {heroes[hero][1]}')

def heroes_game():

	heroes={}
	input_heroes(heroes)
	heroes_fight(heroes)
	heroes_print(heroes)


heroes_game()