import re

data=input()
pattern=r'\=([A-Z][a-zA-Z]{2,})\=|\/([A-Z][a-zA-Z]{2,})\/'
result=re.finditer(pattern, data)
places=[]
for res in result:
	place=''
	for l in range(len(res.group())):
		if res.group()[l]!='=' and res.group()[l]!='/':
			place+=res.group()[l]
	places.append(place)
	place=''
travel_points=0
for plac in places:
	travel_points+=len(plac)
print(f'Destinations: {", ".join(places)}')
print(f"Travel Points: {travel_points}")