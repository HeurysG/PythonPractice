numbers = [] 
for value in range(1,21):
	numbers.append(value)

print(numbers)

number = [ ] 
for values in range(1,21):
	number.append(values)
	print(number)

million = list(range(1,1000001))

print(min(million))
print(max(million))
print(sum(million))

odd_numbers= [] 

for value in range(1,21,2):
	odd_numbers.append(value)
print(odd_numbers)

odd_number = []
for value in range(3,33,3):
	odd_number.append(value)
print(odd_number)

cubes = [value**3 for value in range(1,11)]

cube = [] 
for value in range(1,11):
	cubess = value**3
	cube.append(cubess)
	print(cube)
print(cube)

players = ['alice', 'charles', 'michael', 'martina', 'florence']
print(players[0:3])

print("Here are the first three players on my team:")
for player in players[0:3]:
	print(player.title())
my_favorite_foods= ['cheeseburger' , 'rice and beans' , 'chicken' , 'chik fil a' , 'osaka' , 'chipotle' , 'protein shakes']
nikitas_favorite_foods= my_favorite_foods[:]
print("My favorite foods are:")
print(my_favorite_foods)
print("\nNikita's favorite foods are:")
print(nikitas_favorite_foods)
	
