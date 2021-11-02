def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as file_object:
			contents= file_object.read()
	except FileNotFoundError:
			msg = "Sorry, the file " + filename + " does not exist."
			print(msg)
	else:
		# Count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.") 

# you can use multiple files with this as an example.. 

filenames = ['alice.txt', 'something.txt' , 'lol.txt' , 'idk.txt', 'pi_million_digits.txt'] 
for filename in filenames: 
	count_words(filename)
	

