import re

pattern=r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

sentence=input()

matches=re.findall(pattern, sentence)

food_info={}
total_calories=0
for food in matches:
	item=food[1]
	date=food[2]
	calories=food[3]
	food_info[item]=[date, calories]
	total_calories+=int(calories)

days=total_calories//2000

print(f'You have food to last you for: {days} days!')
for key, value in food_info.items():
	print(f'Item: {key}, Best before: {food_info[key][0]}, Nutrition: {food_info[key][1]}')