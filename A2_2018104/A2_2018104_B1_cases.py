import os

def function1():
	def factorial(n):
		if (n<=1):
			return 1
		else:
			return n*factorial(n-1)
	inputs = os.listdir(os.getcwd())
	for i in inputs:
		if (i[0:6]=='input_'):
			x = i[6:i.index('.')]
			ans = factorial(int(x))
			file = open('output_'+str(x)+'.txt', 'x')
			file.write(str(ans))
			file.close()

def generateData():
	n = int(input("Enter the number of input-output pairs: "))
	for i in range(1, n+1):
		x = int(input("Enter input "+str(i)+": "))
		file = open('input_'+str(x)+'.txt', 'x')
		file.write(str(x))
		file.close()
	function1()

generateData()