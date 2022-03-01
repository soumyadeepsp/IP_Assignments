import os

def function2(n):
	def factorial(n):
		p = 1
		for i in range(1, n+1):
			p = p*i
		return p
	outputs = os.listdir(os.getcwd())
	for i in outputs:
		if (i=='output_'+str(n)+'.txt'):
			file1 = open('output_'+str(n)+'.txt', 'r')
			ans = file1.read()
			file1.close()
			if (int(ans)==factorial(n)):
				return True

def testing():
	inputs = os.listdir(os.getcwd())
	c = 0
	count = 0
	for i in inputs:
		if (i[0:6]=='input_'):
			count = count+1
			file2 = open(i, 'r')
			x = file2.read()
			file2.close()
			if (function2(int(x))):
				c = c+1
	if (c==count):
		print ("SUCCESS")
	else:
		print ("FAILED")

testing()