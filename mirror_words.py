import re
data=input()
pattern=r'(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

result=re.finditer(pattern, data)
mirror_words=[]
words_found=0
for res in result:
	word=res.group()
	words_found+=1
	first_index=int(len(word)/2-1)
	second_index=int(len(word)/2+1)
	first_part=word[1:first_index]
	second_part=word[second_index:-1]
	if first_part==second_part[::-1]:
		mirror_words.append(f'{first_part} <=> {second_part}')

if words_found<=0:
	print("No word pairs found!")
	print("No mirror words!")
else:
	print(f'{words_found} word pairs found!')
	if len(mirror_words)==0:
		print("No mirror words!")
	else:
		print('The mirror words are:')
		print(', '.join(mirror_words))