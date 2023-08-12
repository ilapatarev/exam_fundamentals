def move_func(messsage, number):
	if number<=len(message):
		taken_part=messsage[:number]
		messsage=messsage[number:]+taken_part
		return messsage

def insert_func(message, index, value):
	if index<=len(message):
		first_part=message[:index]
		second_part=message[index:]
		message=first_part+value+second_part
		return message

def change_func(message, substring, replacement):
	if substring in message:
		while substring in message:
			message=message.replace(substring, replacement)
	return message



data=input()
command=input()
message=data
while command!='Decode':
	command=command.split('|')
	order=command[0]
	if order=='Move':
		number_of_letters=int(command[1])
		message=move_func(message, number_of_letters)
	elif order=='Insert':
		index=int(command[1])
		value=command[2]
		message=insert_func(message, index, value)
	elif order=='ChangeAll':
		substring=command[1]
		replacement=command[2]
		message=change_func(message, substring, replacement)

	command=input()
print(f'The decrypted message is: {message}')