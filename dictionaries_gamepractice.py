alien_0 = {'color' : 'green', 'points': 5} 
print(alien_0['color'])
print(alien_0['points'])
#dictionary use here, start with brackets and then assign a value to each key.. a key here is color or points and the value is a string or an integer or whatever


new_points = alien_0['points'] 
print("You just earned " + str(new_points) + " points!")
#remember to always use str(...) when printing a value as a string

alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
#python doesn't care in what order you store each key-value pair, it only cares about the connection between key and value


alien_1 = {} 
#you can start with an empty dictionary

alien_1['color'] = 'red'
alien_1['points'] = '10'
print(alien_1)
#added key-values to the empty alien_1 dictionary

#you can also redefine values in a dictionary

alien_0 = {'x_position': 0 , 'y_position': 25, 'speed': 'medium'} 
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right
#Determine how far to move alien based on its current speed

if alien_0['speed'] == 'slow' : 
	x_increment = 1
elif alien_0['speed'] == 'medium' : 
	x_increment = 2 
else: 
	#This must be a fast alien
	x_increment = 3 
#The new position is the old position plus the increment.. 

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

print(alien_1)
del alien_1['points'] 
print(alien_1)

favorite_languages = {
    'jen': 'python' ,
    'sarah':'c',
	'edward': 'ruby',
	'phil':'python',
	}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")


vayne = {'speed': 'high' , 'range': 'medium' , 'damage' : 'high' , 'x_position': 0 , 'y_position' : 0 } 

if vayne['speed'] == 'high' :
    x_increment = 3 
    y_increment = 3
vayne['x_position'] = vayne['x_position'] + x_increment 
vayne['y_position'] = vayne['y_position'] + y_increment

print("Vayne's new x and y position given her speed is now , " + "x:" + str(vayne['x_position']) + " and " + "y:" + str(vayne['y_position']))

user_0 = {'username': 'heurysg' , 'first': 'heurys' , 'last': 'grullon'} 

for key, value in user_0.items(): 
    print("\nKey: " + key.title())
    print("Value: " + value.title())


for name, language in favorite_languages.items(): 
	print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favorite_languages.keys():
	print(name.title())
for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()): 
	print("\n"+language.title())

# learning nesting below 

alien_0 = {'color':'green', 'points':5 }
alien_1 = {'color':'yellow', 'points': 10 } 
alien_2 = {'color':'red', 'points' : 15 } 

aliens = [alien_0 , alien_1 , alien_2 ] 

for alien in aliens:
	print(alien) 
#Make an empty list for storing aliens now
aliens = [] 

# Make 30 aliens

for alien_number in range(30): 
	new_alien = {'color': 'green' , 'points': 5 , 'speed' : 'slow' } 
	aliens.append(new_alien)
#Show the first 5 aliens 

for alien in aliens[:5]: 
	print(alien)
print("...")

#Show total number of aliens created 

print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:5]:
    if alien['color'] == 'green' :
        alien['color']= 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
#Show first 5 aliens now 
for alien in aliens[0:15]:
	print(alien)
print("...")

for alien in aliens[0:10]:
    if alien['color'] == 'green' :
        alien['color']= 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow' : 
        alien['color'] = 'red' 
        alien['speed'] = 'high'
        alien['points'] = 15
for alien in aliens[0:15]:
	print(alien)
print("...")

pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms','extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:") 
for topping in pizza['toppings']:
	print("\t" +topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'],
    }


for name, languages in favorite_languages.items():
	if len(languages) >= 2 :
		print("\n" + name.title() + "'s favorite languages are: " ) 
	elif len(languages) < 2: 
		print("\n" + name.title() +"'s favorite language is : " )
	for language in languages:
		print("\t" + language.title())
# exchanging elif for else just for the lulz 
for name, languages in favorite_languages.items():
	if len(languages) >= 2 :
		print("\n" + name.title() + "'s favorite languages are: " ) 
	else:
		print("\n" + name.title() +"'s favorite language is : " )
	for language in languages:
		print("\t" + language.title())
