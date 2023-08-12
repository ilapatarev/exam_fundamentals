def pieces_list_func(pieces_list):
	num = int(input())
	pieces_list = {}
	for piece in range(num):
		piece = input()
		piece = piece.split('|')
		piece_name = piece[0]
		composer = piece[1]
		key = piece[2]
		pieces_list[piece_name] = [composer, key]

	return pieces_list


def pieces_actions_func(pieces_list):
	command = input()
	while command != 'Stop':
		command = command.split('|')
		order = command[0]
		if order == 'Add':
			piece=command[1]
			composer=command[2]
			key=command[3]
			if piece in pieces_list:
				print(f'{piece} is already in the collection!')
			else:
				pieces_list[piece]=[composer, key]
				print(f"{piece} by {composer} in {key} added to the collection!")
		elif order == 'Remove':
			piece=command[1]
			if piece in pieces_list:
				pieces_list.pop(piece)
				print(f'Successfully removed {piece}!')
			else:
				print(f'Invalid operation! {piece} does not exist in the collection.')
		elif order == 'ChangeKey':
			piece=command[1]
			new_key=command[2]
			if piece in pieces_list:
				pieces_list[piece][1]=new_key
				print(f"Changed the key of {piece} to {new_key}!")
			else:
				print(f'Invalid operation! {piece} does not exist in the collection.')

		command = input()
	return pieces_list


def pieces_print_func(pieces_list):
	for piece, composer_key in pieces_list.items():
		print(f"{piece} -> Composer: {pieces_list[piece][0]}, Key: {pieces_list[piece][1]}")



def pianist():
	pieces_list = {}
	pieces_list=pieces_list_func(pieces_list)
	pieces_list=pieces_actions_func(pieces_list)
	pieces_list=pieces_print_func(pieces_list)


pianist()
