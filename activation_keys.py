raw_activation_key = input()
command = input()
while command != 'Generate':
	command = command.split('>>>')
	order = command[0]
	if order == 'Contains':
		substring = command[1]
		if substring in raw_activation_key:
			print(f"{raw_activation_key} contains {substring}")
		else:
			print("Substring not found!")
	elif order == 'Flip':
		upper_lower=command[1]
		start_index=int(command[2])
		end_index=int(command[3])
		first_part=raw_activation_key[:start_index]
		last_part=raw_activation_key[end_index:]
		substring_to_flip=raw_activation_key[start_index:end_index]
		if upper_lower=='Upper':
			substring_to_flip=substring_to_flip.upper()
		else:
			substring_to_flip=substring_to_flip.lower()
		raw_activation_key=first_part+substring_to_flip+last_part
		print(raw_activation_key)
	elif order == 'Slice':
		start_slice_index=int(command[1])
		end_slice_index=int(command[2])
		raw_activation_key=raw_activation_key[:start_slice_index]+raw_activation_key[end_slice_index:]
		print(raw_activation_key)

	command = input()
print(f"Your activation key is: {raw_activation_key}")
