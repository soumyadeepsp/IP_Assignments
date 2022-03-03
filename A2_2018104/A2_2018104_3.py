import math
def letters(c):
	if (ord(c)>=97 and ord(c)<=122):
		return ord(c)-87
	if (ord(c)>=65 and ord(c)<=90):
		return ord(c)-55

def numbers(n):
	return chr(87+n)

def convert(b1, s, b2):
	dec = 0
	for i in range(len(s)):
		if (not s[len(s)-i-1].isnumeric()):
			digit = letters(s[len(s)-i-1])
		else:
			digit = int(s[len(s)-i-1])
		dec = dec + digit*(b1**i)
	temp = []
	while (dec > 0):
		temp.append(dec%b2)
		dec = math.floor(dec/b2)
	temp = temp[::-1]
	ans = ""
	for i in range(len(temp)):
		if (temp[i]>9):
			temp[i] = numbers(temp[i]).upper()
	for i in temp:
		ans = ans + str(i)
	return ans

print ("1) Convert decimal to binary and vice-versa")
print ("2) Convert decimal to hexadecimal and vice-versa")
print ("3) Convert decimal to octal and vice-versa.")
print ("4) Convert binary to hexadecimal and vice-versa.")
print ("5) Convert binary to octal and vice-versa.")
print ("6) Convert hexadecimal to octal and vice-versa.")
print ("7) Convert number with radix A to radix B.")
choice = input ("Enter your choice from the above options: ")
if (choice == '1'):
	n = input("Enter the decimal number: ")
	print (convert(10, n, 2))
	n = input("Enter the binary number: ")
	print (convert(2, n, 10))
if (choice == '2'):
	n = input("Enter the decimal number: ")
	print (convert(10, n, 16))
	n = input("Enter the hexadecimal number: ")
	print (convert(16, n, 10))
if (choice == '3'):
	n = input("Enter the decimal number: ")
	print (convert(10, n, 8))
	n = input("Enter the octal number: ")
	print (convert(8, n, 10))
if (choice == '4'):
	n = input("Enter the binary number: ")
	print (convert(2, n, 16))
	n = input("Enter the hexadecimal number: ")
	print (convert(16, n, 2))
if (choice == '5'):
	n = input("Enter the binary number: ")
	print (convert(2, n, 8))
	n = input("Enter the octal number: ")
	print (convert(8, n, 2))
if (choice == '6'):
	n = input("Enter the hexadecimal number: ")
	print (convert(16, n, 8))
	n = input("Enter the octal number: ")
	print (convert(8, n, 16))
if (choice == '7'):
	r1 = int(input("Enter the radix of the first number: "))
	n = input("Enter the first number: ")
	r2 = int(input("Enter the radix of the number to be converted: "))
	print (convert())