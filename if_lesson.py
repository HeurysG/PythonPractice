cars = ['audi', 'bmw' , 'subaru', 'toyota'] 

for car in cars: 
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovies' :
	print("Hold the anchovies!")

my_age = 23 
cooper_age = 2 
print(my_age >= 21 or cooper_age <= 3)

requested_toppings = ['mushrooms', 'onions' , 'pineapple' , 'pepperoni'] 
print('mushrooms' in requested_toppings)
print('cheese' in requested_toppings)

banned_users = ['elvin' , 'isaias' , 'matt', 'elfrin' , 'oscar' , 'jay']
user = 'heurys'

if user not in banned_users : 
	print(user.title() + ", you can post a response if you wish.") 

age = 21 

if age < 4 :
	price = 0 
elif age < 18 : 
		price = 5 
else : 
			price = 10 
print("Your admission cost is $" + str(price) + ".") 

# u can use as many elif blocks in the code as I want 
age = 66 
if age < 4 : 
	price = 0 
elif age < 18: 
	price = 5
elif age < 65: 
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".") 

#sometimes don't even need an else statement, an elif statement allows us to be clearer than the general else
# u can use as many elif blocks in the code as I want 
age = 66
if age < 4 : 
	price = 0 
elif age < 18: 
	price = 5
elif age < 65: 
	price = 10
elif age >= 65:
	price = 5
print("Your admission cost is $" + str(price) + ".") 

requested_toppings = ['mushrooms', 'extra cheese', 'extra sauce'] 

if 'mushrooms' in requested_toppings: 
	print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra sauce' in requested_toppings:
	print("Adding extra sauce.") 

print("\nFinished making your pizza!") 

alien_color = ['green'] 

if 'green' in alien_color : 
	print("5 points!") 
elif 'red' in alien_color :
	print("10 points!")
elif 'yellow' in alien_color :
	print("20 points!")
else : 
	print ("you has failed u nub.")

alien_color = 'red'
if 'green' in alien_color: 
	print("5 points!")
else : 
	print("10 points!")

alien_color = 'green'
if 'green' in alien_color: 
	print("5 points!")
else : 
	print("10 points!")

age = 23

if age < 2 : 
	print("The person is a baby.")
elif age >=2 and age <4 :
	print("The person is a toddler.")
elif age >= 4 and age <13 : 
	print ("The person is a kid.") 
elif age >=13 and age <20 : 
	print("The person is a teenager.")
elif age >= 20 and age <65 : 
	print("The person is an adult.")
elif age >= 65 : 
	print("The person is an elder.")
#lit

requested_toppings= ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings: 
	print("Adding " + requested_topping + ".") 
print("\nFinished making your pizza!") 

for requested_topping in requested_toppings: 
	if requested_topping == 'green peppers': 
		print("Sorry we are out of green peppers right now.") 
	else: 
		print("Adding " + requested_topping + ".") 
print("\nFinished making your pizza!!")

requested_toppings = [] 
if requested_toppings : 
	for requested_topping in requested_toppings: 
		print("Adding " + requested_topping + ".") 
	print("\nFinished making your pizza!")
else: 
	print("Are you sure you want a plain pizza?")
	
available_toppings = ['mushrooms' , 'olives', 'green peppers', 'pepperoni' , 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 

for requested_topping in requested_toppings: 
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else: 
		print("Sorry we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

