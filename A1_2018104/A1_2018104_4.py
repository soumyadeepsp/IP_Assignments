print ("Which boolean expression do you want to check?")
print ("1. Fn = (b1 and not b1)")
print ("2. Fn = (b1 or b2) and (b1 or not (b2 and not b3)) and (not b2 and b3)")
print ("Enter the number beside it")
choice = input()
if (choice == '1'):
	domain = [True, False]
	ans = []
	val = []
	def Fn(b1):
		if (b1 and not b1):
			return True
		else:
			return False
	for b1 in domain:
		ans.append(Fn(b1))
		val.append(b1)
	if (True in ans):
		print ("Satisfiable")
		print (val[ans.index(True)])
	else:
		print ("Unsatisfiable")

if (choice == '2'):
	domain = [True, False]
	ans = []
	val = []
	def Fn(b1, b2, b3):
		if ((b1 or b2) and (b1 or not (b2 and not b3)) and (not b2 and b3)):
			return True
		else:
			return False
	for b1 in domain:
		for b2 in domain:
			for b3 in domain:
				ans.append(Fn(b1, b2, b3))
				val.append(str(b1)+", "+str(b2)+", "+str(b3))
	if (True in ans):
		print ("Satisfiable")
		print (val[ans.index(True)])
	else:
		print ("Unsatisfiable")