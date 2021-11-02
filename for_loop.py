magicians = ['heurys' , 'nikita' , 'cooper'] 
for magician in magicians: 
	print("\n"+ magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".")
#just writing like a bawss my dudes
animals = ['dog','cat','bird' , 'hamster' , 'rabbit']
for animal in animals:
	print("A " + animal.title() + " could make a good pet.")
print("Any of these animals would make a good pet!") 	


squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)


#list comprehensions here
square = [number**2 for number in range(1,25)]
print(square)


#here is when fullset print is within the for loop
fullset = []
for number in range(1,21):
	fullset.append(number)
	print(fullset)

print("\nFullstuff will now be outside of for loop.")
fullset = []
for number in range(1,21):
	fullset.append(number)
print(fullset)
