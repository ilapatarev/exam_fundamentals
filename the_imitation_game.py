message=input()
while True:
	command=input()
	if command=='Decode':
		break
	command=command.split('|')
	act=command[0]
	if act == 'Move':
		num = int(command[1])
		add_at_the_end = message[:num]
		message = message[num:]+add_at_the_end
		# for n in add_at_the_end:
		# 	message.append(n)

	elif act=='Insert':
		index=int(command[1])
		value=command[2]

		message=message[:index]+value+message[index:]

	elif act=='ChangeAll':
		substring=command[1]
		replacement=command[2]
		message=message.replace(substring, replacement)
		# if substring in message:
		# 	for s in message:
		# 		if s==substring:
		# 			new_message.append(replacement)
		# 		else:
		# 			new_message.append(s)
		# 	message=new_message

print(f"The decrypted message is: {message}")