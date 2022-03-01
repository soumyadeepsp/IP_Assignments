def plotGraph():
	n = int(input("Enter the Degree of the polynomial: "))
	c = [0 for x in range(n+1)]
	if (n == 3):
		c = [0,0,0,0]
		c[3] = int(input("Coeff 1: "))
		c[2] = int(input("Coeff 2: "))
		c[1] = int(input("Coeff 3: "))
		c[0] = int(input("Coeff 4: "))
	if (n == 2):
		c = [0,0,0]
		c[2] = int(input("Coeff 1: "))
		c[1] = int(input("Coeff 2: "))
		c[0] = int(input("Coeff 3: "))
	if (n == 1):
		c = [0,0]
		c[1] = int(input("Coeff 1: "))
		c[0] = int(input("Coeff 2: "))
	if (n == 0):
		c = [0]
		c[0] = int(input("Coeff 1: "))
	l = int(input("Enter the Lower bound for X: "))
	u = int(input("Enter the Lower bound for X: "))
	s = int(input("Enter the Steps in which you would vary X: "))
	for i in range(l, u+1, s):
		ans = 0
		for j in range(len(c)):
			ans = ans + c[j]*(i**j)
		for j in range(round(ans)):
			print ('*', end="")
		print ()
plotGraph()