def add_stop(data):
	index=int(command[1])
	string_to_insert=command[2]
	if index < len(data):
		first_part=data[:index]
		sec_part=data[index:]
		data=first_part+string_to_insert+sec_part
	print(data)

def remove_stop(data):
	start_index=int(command[1])
	end_index=int(command[2])
	l=len(data)
	if start_index<len(data) and end_index<len(data):
		first_part=data[:start_index]
		sec_part=data[end_index+1:]
		data=first_part+sec_part
	print(data)
	return data
def switch(data):
	old_string=command[1]
	new_string=command[2]
	if old_string in data:
		data=data.replace(old_string, new_string)
	print(data)
	return data


data=input()
command=input()
while command!='Travel':
	command=command.split(':')
	order=command[0]
	if order=='Add Stop':
		data=add_stop(data)
	elif order=='Remove Stop':
		data=remove_stop(data)
	elif order=="Switch":
		data=switch(data)

	command=input()

print(f"Ready for world tour! Planned stops: {data}")