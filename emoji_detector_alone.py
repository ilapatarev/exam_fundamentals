import re

data=input()
pattern=r'(\:\:)([A-Z][a-z]{2,})(\:\:)|(\*\*)([A-Z][a-z]{2,})(\*\*)'
result=re.finditer(pattern, data)
pattern_digits=r'(\d)'
digit_result=re.findall(pattern_digits,data)
cool_treshold=1
for r in digit_result:
	cool_treshold*=int(r)

valid_emojies=[]
found_emojies=[]
for word in result:
	emoji=word.group()
	found_emojies.append(emoji)
for emo in found_emojies:
	current_cool=0
	for ch in range(len(emo)):
		if emo[ch]!=':' and emo[ch]!='*':
			current_cool+=ord(emo[ch])
	if current_cool>=cool_treshold:
		valid_emojies.append(emo)
	current_cool=0
print(f"Cool threshold: {cool_treshold}")
print(f"{len(found_emojies)} emojis found in the text. The cool ones are:")
for emoj in valid_emojies:
	print(emoj)