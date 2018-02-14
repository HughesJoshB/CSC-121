# Joshua Hughes
# April 12th 2017
# Car class assignment
# M5HW2

import classCar

def main():
	year = input('Car Year: ')
	make = input('Car Make: ')
	speed = input("Car's Speed: ")
	
	theirCar = Car(year, make, speed)
	print(theirCar)
	
	# Create an accelerate loop
	print('You are on the gas: ')
	for  i in range(6):
		theirCar.accelerate()
		print('Your cars speed is:', theirCar.get_speed())
	print()	
	# Create an Brake loop
	print('You are hitting the brakes: ')
	for i in range(6):
		theirCar.brake()
		print('Your cars speed is: ', theirCar.get_speed())
# Call the main
main()
	