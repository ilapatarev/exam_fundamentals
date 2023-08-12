import re
data=input()
pattern=r'\#[A-Za-z ]+\#[0-9]{2}\/[0-9]{2}\/[0-9]{2}\#[0-9]+\#|\|[A-Za-z ]+\|[0-9]{2}\/[0-9]{2}\/[0-9]{2}\|[0-9]+\|'

result=re.finditer(pattern, data)
food_info=[]
all_calories=0
for el in result:
	if '|' in el.group():
		item=el.group().split('|')
	else:
		item = el.group().split('#')

	food=item[1]
	date=item[2]
	calories=int(item[3])
	food_info.append([food, date, calories])
	all_calories+=calories

days_to_have_food=all_calories//2000
print(f"You have food to last you for: {days_to_have_food} days!")
for ite in food_info:
	print(f"Item: {ite[0]}, Best before: {ite[1]}, Nutrition: {ite[2]}")