
pieces={}
start_number=int(input())
for n in range(start_number):
	text=input().split('|')
	piec=text[0]
	comp=text[1]
	key=text[2]
	pieces[piec]=[comp, key]


command=input()
while command!='Stop':
	command=command.split('|')
	act=command[0]
	if act=='Add':
		piece=command[1]
		composer=command[2]
		key=command[3]
		if piece not in pieces:
			pieces[piece]=[composer, key]
			print(f'{piece} by {composer} in {key} added to the collection!')
		else:
			print(f'{piece} is already in the collection!')

	if act=='Remove':
		piece=command[1]
		if piece in pieces:
			pieces.pop(piece)
			print(f'Successfully removed {piece}!')
		else:
			print(f'Invalid operation! {piece} does not exist in the collection.')
	if act=='ChangeKey':
		piece=command[1]
		new_key=command[2]
		if piece in pieces:
			pieces[piece][1]=new_key
			print(f'Changed the key of {piece} to {new_key}!')
		else:
			print(f'Invalid operation! {piece} does not exist in the collection.')

	command=input()

for piece, compose in pieces.items():

	print(f'{piece} -> Composer: {compose[0]}, Key: {compose[1]}')

