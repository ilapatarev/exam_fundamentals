stops = input()

command = input()
while command != 'Travel':
	command = command.split(':')
	if command[0] == 'Add Stop':
		index = int(command[1])
		place = command[2]
		if 0 <= index <len(stops):
			first_part=stops[:index]
			second_part=stops[index:]
			stops=first_part+place+second_part

	elif command[0]=='Remove Stop':
		start_index=int(command[1])
		end_index=int(command[2])
		if 0<=start_index and start_index<len(stops) and 0<=end_index and end_index<len(stops):
			stops=stops[:start_index]+stops[end_index+1:]

	elif command[0]=='Switch':
		old_string=command[1]
		new_string=command[2]
		if old_string in stops:
			stops=stops.replace(old_string, new_string)
	print(stops)


	command = input()
print(f'Ready for world tour! Planned stops: {stops}')