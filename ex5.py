my_name = 'Liu Xinhao'
my_age = 32  # maybe
my_height = 175 # cm
my_weight = 60 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

realhigh = my_height / 2.54


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depanding on coffe.")

# this line is tricky, try to get it exactly right
total = my_age + realhigh + my_weight
print(f"If I add {my_age}, and {my_weight} I get {total}.")
