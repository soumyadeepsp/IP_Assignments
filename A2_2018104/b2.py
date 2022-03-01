def split(word):
    return [char for char in word]

p, q = list(map(int, input().split()))
m, n = list(map(int, input().split()))
arr = []
for i in range(m):
	temp = input()
	arr.append(split(temp))
#print (arr)
d = {}
for i in range(len(arr[0])):
	c = 0
	for j in range(len(arr)-1, -1, -1):
		if (arr[j][i]=='1'):
			c = c+1
	d[c] = i
#print (d)
heights = list(d.keys())
heights.sort(reverse=True)
#print (heights)
doja_fan, snack_fan = 0, 0
for i in range(len(heights)):
	if (i%2==0):
		col = d[heights[i]]
		h = 0
		for i in range(m-1, -1, -1):
			if (arr[i][col]=='1'):
				arr[i][col] = 'D'
				h = h+1
		doja_fan = doja_fan + h*p
	if (i%2==1):
		col = d[heights[i]]
		h = 0
		for i in range(m-1, -1, -1):
			if (arr[i][col]=='1'):
				arr[i][col] = 'S'
				h = h+1
		snack_fan = snack_fan + h*q
	p = p+1
	q = q+1
print ()
print (doja_fan, snack_fan)
print ()
for i in arr:
	for j in i:
		print (j, end="")
	print ()