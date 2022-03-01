print ("Please enter your choice from the below options")
print ("1. Right-angled triangle")
print ("2. Isosceles triangle")
print ("3. Kite")
print ("4. Half Kite")
print ("5. X")
print ("6. Exit")
print ("Enter the number beside it or type it out")
print ("Sample input - 1 || Right-angled || right angled")
choice = input()
if (choice=='1' or choice[0:5].lower()=='right'):
	n = int(input())
	for i in range(n+1):
		for j in range(1, i+1):
			print (j, end=" ")
		print ()

if (choice=='2' or choice[0:3].lower()=='iso'):
	n = int(input())
	for i in range(n, 0, -1):
		for j in range(i-1, 0, -1):
			print (" ", end="")
		num = 2*(n-i)+1
		for j in range(1, num+1):
			print (j, end="")
		for j in range(i-1, 0, -1):
			print (" ", end="")
		print ()

if (choice=='3' or choice[0:4].lower()=='kite'):
	n = int(input())
	for i in range(n, 0, -1):
		for j in range(i-1, 0, -1):
			print (" ", end="")
		num = 2*(n-i)+1
		for j in range(1, num+1):
			print (j, end="")
		for j in range(i-1, 0, -1):
			print (" ", end="")
		print ()
	n = n-1
	temp = []
	for i in range(n, 0, -1):
		s = ""
		for j in range(i-1, 0, -1):
			s = s+" "
		num = 2*(n-i)+1
		for j in range(1, num+1):
			s = s+str(j)
		for j in range(i-1, 0, -1):
			s = s+" "
		temp.append(s)
	for i in range(len(temp)-1, -1, -1):
		print (" "+temp[i])

if (choice=='4' or choice[0:4].lower()=='half'):
	n = int(input())
	for i in range(n+1):
		for j in range(1, i+1):
			print (j, end=" ")
		print ()
	n = n-1
	temp = []
	for i in range(n+1):
		s = ""
		for j in range(1, i+1):
			s = s+str(j)+" "
		temp.append(s)
	for i in range(len(temp)-1, -1, -1):
		print (temp[i])
	
if (choice=='5' or choice[0:1].lower()=='x'):
	n = int(input())
	temp = []
	for i in range(n, 0, -1):
		s = ""
		for j in range(i-1, 0, -1):
			s = s+" "
		num = 2*(n-i)+1
		for j in range(1, num+1):
			s = s+str(j)
		for j in range(i-1, 0, -1):
			s = s+" "
		temp.append(s)
	for i in range(len(temp)-1, -1, -1):
		print (temp[i])
	for i in range(1, len(temp)):
		print (temp[i])