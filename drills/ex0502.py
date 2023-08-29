my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
inch_2_cm = 2.54
lbs_2_kg = 0.453592

print(f"Let's talk about {my_name}.")
print(f"He's {(my_height)*(inch_2_cm)} centimeters tall.")
print(f"He's {my_weight*lbs_2_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + (my_height*inch_2_cm) + (my_weight*lbs_2_kg)
print(f"If I add {my_age}, {my_weight*inch_2_cm}, and {my_weight*lbs_2_kg} I get {total}.")
print(f"Rounded total: ", round(total))