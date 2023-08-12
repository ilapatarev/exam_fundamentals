
def car_storage(cars, number_of_cars):
	for car in range(number_of_cars):
		data=input().split('|')
		brand=data[0]
		mileage=int(data[1])
		fuel=int(data[2])
		cars[brand]=[mileage, fuel]

	return cars


def car_changes(cars):
	command=input()
	while command!='Stop':
		command=command.split(' : ')
		order=command[0]
		model=command[1]
		if order=='Drive':
			distance=int(command[2])
			fuel=int(command[3])
			if fuel>cars[model][1]:
				print("Not enough fuel to make that ride")
			else:
				cars[model][0]+=distance
				cars[model][1]-=fuel
				print(f"{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
				if cars[model][0]>=100000:
					print(f"Time to sell the {model}!")
					cars.pop(model)

		elif order=='Refuel':
			fuel=int(command[2])
			if fuel+cars[model][1]>75:
				fuel=75-cars[model][1]
			cars[model][1]+=fuel
			print(f'{model} refueled with {fuel} liters')
		elif order =='Revert':
			kilometres=int(command[2])
			if cars[model][0] - kilometres>=10000:
				cars[model][0]-=kilometres
				print(f"{model} mileage decreased by {kilometres} kilometers")
			else:
				cars[model][0]=10000
		command=input()

	return cars
def car_print(cars):
	for car, things in cars.items():
		print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")

def need_for_speed():
	cars={}
	number_of_cars=int(input())
	car_storage(cars, number_of_cars)
	car_changes(cars)
	car_print(cars)
need_for_speed()