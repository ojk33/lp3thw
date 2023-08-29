# assigning an integer to a variable 
cars = 100
# assigning a decimal to a variable
space_in_a_car = 4.0
# assigning an integer to variables
drivers = 30
passengers = 90
# assigning value evaluated from a subtraction of variable values
cars_not_driven = cars - drivers
# copying value from a variable to another variable
cars_driven = drivers
# assigning value evaluated from a multiplication of variable values
carpool_capacity = cars_driven * space_in_a_car
# assigning value evaluated from a division of variable values
average_passengers_per_car = passengers / cars_driven

# printing statement embedding values from assigned variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 
	  "in each car.")