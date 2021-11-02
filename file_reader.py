with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())


# to get python to open up a file in a directory that the CURRENT file is not in
# I need to do with open('text_files/filename.txt') as file_object for example
# assuming the text_files folder is in the same folder as python_work here 
# This is a relative path.. absolute paths are more like 
# file_path = 'C:\Users\heurys\other_files\text_files\filename.txt' for ex. 
# then i do with open(file_path) as file_object 


filename = 'pi_digits.txt'

with open(filename) as file_dos:
	for line in file_dos: 
		print(line.rstrip())	

# rstrip removes extra blank lines 

with open(filename) as file_dos:
	lines = file_dos.readlines()
	
for line in lines : 
	print(line.rstrip())


pi_string = '' 
for line in lines:
	pi_string += line.strip()
	
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt' 

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input("Enter your birthday to see, in the form mmddyy: ")

if birthday in pi_string:
	print("Your birthday is in the first million digits of pi!")
else:
		print("Your birthday does not appear in the first million digits of pi :(")


filename = 'programming.txt'

with open(filename, 'w') as file_object: 
	file_object.write("I love programming.\n") 
	file_object.write("I love playing games!\n")
	
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")


	
