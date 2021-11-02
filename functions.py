def greet_users():
	"""Display a simple greeting message."""
	print("Hello!")
greet_users()

# providing information within the parenthesis now 

def greet_users(username): 
	"""Display a simple greeting message."""
	print("Hello, " + username.title() + "!")

greet_users('hEuRyS')

def favorite_books(title): 
	"""Favorite book stuff lol"""
	print("One of my favorite books is " + title.title() + ".")

favorite_books('catching fire') 


def favorite_games(names):
	"""ok .. ? """
	print("One of my favorite games is " + names.title() + "." )
favorite_games('lol wait no way names')

def favorite_marksmen(adc):
	print("This " + adc.title() + " is doo doo.")

favorite_marksmen('vayne')


def this_chapter(learning):
	print("In this chapter, I am learning about " + learning + ".")

this_chapter('functions')

def doodoo_role(role,adc):
	print("\nThis champion " + adc.title() + " is doo doo and so is the " + role + " role." )

doodoo_role('adc','vayne')
doodoo_role('assassin','zed')
doodoo_role('mage','zOe')
# this above was all positional arguments .. position matters for the function
# but I can use keyword arguments as seen below 

doodoo_role( adc = 'Malphite' , role = 'tank')


# Start with some designs that need to be printed. 

unprinted_designs = ['iphone case' , 'robot pendant' , 'dodecahedron'] 
completed_models = [] 

# Simulate printing each design, until none are left.
#Move each design to completed_models after printing.

while unprinted_designs : 
	current_design = unprinted_designs.pop() 
	#Simulate creating a 3D print from the design.
	print("\nPrinting model: " + current_design) 
	completed_models.append(current_design)
	
#Display all completed models.
print("\nThe following models have been printed:") 
for completed_model in completed_models: 
	print(completed_model)

def make_pizza(size, *toppings): 
	"""Summarize the pizza we are about to make.""" 
	print("\nMaking a " + str(size) +
	      "-inch pizza with the following toppings:")
	for topping in toppings: 
		print("- " + topping)

make_pizza(20, 'light cheese', 'extra sauce')

# one asterisk makes a tuple , double asterisk makes a dictionary

def build_profile(first, last , **user_info): 
	"""Build a dictionary containing everything we know about a user."""
	profile = {} 
	profile['first_name'] = first 
	profile['last_name'] = last 
	for key, value in user_info.items(): 
		profile[key] = value 
	return profile 
	
user_profile = build_profile('albert' ,'einstein', location = 'princeton', field = 'physics' )
print(user_profile)
#ended in page 153 
 
	 
	
