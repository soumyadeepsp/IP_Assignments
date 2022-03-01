print ("Choose an option from the following menu")
print ("1. Find reverse of a number")
print ("2. Check whether a number is a palindrome or not")
print ("3. Check whether a number is a Narcissistic number or not")
print ("4. Find the sum of digits of a number")
print ("5. Find the sum of squares of digits of a number")
print ("6. Select 6 to exit the application")
print ("Enter the number beside it")
choice = int(input())
while (choice != 6):
	print ("Enter the number")
	n = int(input())
	if (choice == 1):
		rev = 0
		while (n > 0):
		    a = n % 10
		    rev = rev * 10 + a
		    n = n // 10
		print (rev)

	if (choice == 2):
		temp = n
		rev = 0
		while (n > 0):
		    digit = n % 10
		    rev = rev*10 + digit
		    n = n // 10
		if (temp==rev):
		    print (True)
		else:
		    print (False)

	if (choice == 3):
		s = 0
		l = len(str(n))
		temp = n
		while (n > 0):
			dig = n%10
			s = s + dig**l
			n = n//10
		if (s == temp):
			print (True)
		else:
			print (False)

	if (choice == 4):
		s = 0
		ps = 0
		while (n > 0):
			dig = n%10
			s = s + dig
			ps = ps + dig
			n = n//10
			if (n==0 and ps>=10):
				n = ps
				ps = 0
		print (s)

	if (choice == 5):
		s = 0
		ps = 0
		while (n > 0):
			dig = n%10
			s = s + dig**2
			ps = ps + dig**2
			n = n//10
			if (n==0 and ps>=10):
				n = ps
				ps = 0
		print (s)
	print ()
	choice = int(input("Enter your choice: "))