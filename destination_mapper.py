import re
pattern=r'(\=|\/)([A-Z][A-Za-z]{2,})\1'

sentence=input()

matches=re.findall(pattern, sentence)
travel_points=0

places=[]
for elements in matches:
	places.append(elements[1])
	travel_points+=len(elements[1])
print(f"Destinations: {', '.join(places)}")
print(f'Travel Points: {travel_points}')