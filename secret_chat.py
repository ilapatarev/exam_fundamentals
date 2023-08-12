
conceal_message=input()

command=input()
while command!='Reveal':
	command=command.split(':|:')
	action=command[0]
	if action=='InsertSpace':
		index=int(command[1])
		conceal_message=conceal_message[:index]+' '+conceal_message[index:]
		print(conceal_message)
	elif action=="Reverse":
		sub_string=command[1]
		if sub_string in conceal_message:
			conceal_message=conceal_message.replace(sub_string, '', 1)
			reversed_substring=sub_string[::-1]
			conceal_message+=reversed_substring
			print(conceal_message)
		else:
			print('error')
	elif action=='ChangeAll':
		substring=command[1]
		replacement=command[2]
		while substring in conceal_message:
			conceal_message=conceal_message.replace(substring, replacement)
		print(conceal_message)





	command=input()
print(f'You have a new text message: {conceal_message}')