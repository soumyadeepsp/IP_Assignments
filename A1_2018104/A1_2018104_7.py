def f(l, x):
	s = 0
	for i in range(len(l)):
		s = s + x**l[i]
	return s

def helper(l, ll, ul):
	temp = f(l, ll) + 4*f(l, (ll+ul)/2) + f(l, ul)
	return (temp*(ul-ll))/6

def calculate_area(l, a, b, d):
	if ((b-a)%d != 0):
		return
	ans = 0
	for i in range(a, b, d):
		ans = ans + helper(l, i, i+d)
	return ans

c = list(map(float, input("c=")[1:-1].split(",")))
a = int(input("a="))
b = int(input("b="))
d = int(input("d="))
print ("Using Simpson’s 1⁄3 Algo, RHS=", calculate_area(c, a, b, d))
# print (calculate_area([0.5, -1], 1, 3, 1))
# print (calculate_area([2, 1], 0, 6, 2))