import re
data=input()
pattern=r'\@(([A-Za-z]{3,})\@\@([A-Za-z]{3,}))\@|\#(([A-Za-z]{3,})\#\#([A-Za-z]{3,}))\#'

result=re.finditer(pattern, data)
pairs=[]
for res in result:
	pairs.append(res.group())

count_valid=0
valid_pairs=[]
for word in pairs:
	split_indx=int(len(word)/2)
	first_part=word[:split_indx]
	second_part=word[split_indx:]
	if first_part == second_part[::-1]:
		count_valid+=1
		valid_pairs.append(word)

if len(pairs)==0:
	print("No word pairs found!")
else:
	print(f"{len(pairs)} word pairs found!")
if len(valid_pairs)==0:
	print("No mirror words!")
else:
	print(f"The mirror words are:")
	final=[]
	for wor in valid_pairs:
		spl_ind=int(len(wor)/2)
		first_part=wor[1:spl_ind-1]
		reverse=first_part[::-1]
		final.append(f'{first_part} <=> {reverse}')

	print(', '.join(final))
