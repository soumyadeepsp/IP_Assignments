import string
file = open("question1_input.txt", 'r')
text = file.read()
file.close()
words = text.split()
word_count = {}
for i in range(len(words)):
	if (words[i] in word_count):
		word_count[words[i]] = word_count[words[i]] + 1
	else:
		word_count[words[i]] = 1
print ("Enter your choice:")
print ("1. Display specific word count")
print ("2. Display all unique words")
print ("3. Display all word counts")
print ("4. Replace word")
print ("5. Quit")
choice = input()
while (choice != '5'):
	if (choice == '1'):
		word = input ("Enter word: ")
		if (word in word_count):
			print ("Word count: ", word_count[word])
		else:
			print ("Word does not exist")
		print ()
		choice = input("Enter your choice: ")
	if (choice == '2'):
		print (" ; ", end="")
		for word in word_count:
			print (word+" ; ", end="")
		print ()
		print ()
		choice = input("Enter your choice: ")
	if (choice == '3'):
		print ("Word Counts: ")
		for word in word_count:
			print (word+" : "+str(word_count[word]))
		print ()
		choice = input("Enter your choice: ")
	if (choice == '4'):
		old = input ("Enter word to be replaced: ")
		new = input ("Enter word that will replace "+old+": ")
		c = text.count(old)
		new_text = text.replace(old, new, c)
		file = open("question1_input.txt", 'w')
		file.write(new_text)
		print ("Replaced successfully!")
		choice = input("Enter your choice: ")
	if (choice == '5'):
		break