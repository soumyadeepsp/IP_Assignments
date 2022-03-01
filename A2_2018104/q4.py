Simport os
file = open(os.getcwd()+'/Q4/Admin/'+'AnswerKey.txt', 'r')
text = file.read()
file.close()
answers = text.split('\n')
students = os.listdir(os.getcwd()+'/Q4/Student')
marks = []
output = ""
for i in students:
	file = open(os.getcwd()+'/Q4/Student/'+i, 'r')
	name = i[0:i.index('_')]
	number =  i[i.index('_')+1:i.index('.')]
	submission = file.read().split('\n')
	#print (submission)
	c = 0
	for j in range(20):
		if (answers[j].split()[1] == submission[j].split()[1]):
			c = c+4
		elif (answers[j].split()[1]!=submission[j].split()[1] and submission[j].split()[1]!='-'):
			c = c-1
		else:
			c = c
	output = output + name + " " + number + " " + str(c) + "\n"
	file.close()
print (output)
file = open("FinalReport.txt", 'x')
file.write(output)