import re
num_barcdes=int(input())
for _ in range(num_barcdes):
	data = input()
	pattern=r'(\@\#+)([A-Z][a-z0-9A-Z]{4,}[A-Z])(\@\#+)'
	result=re.match(pattern, data)
	if not result:
		print('Invalid barcode')
	else:
		extract_numbers=re.findall('\d', result.group())
		if not extract_numbers:
			print('Product group: 00')
		else:
			print(f"Product group: {''.join(extract_numbers)}")
