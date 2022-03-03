arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
n = len(arr)
print ("1. Normal traversal")
print ("2. Alternating traversal")
print ("3. Spiral traversal")
print ("4. Boundary traversal")
print ("5. Diagonal traversal from right to left")
print ("6. Diagonal traversal from left to right")
choice = input("Enter your choice from the above options: ")
if (choice == '1'):
	for i in arr:
		for j in i:
			print (j, end=" ")
if (choice == '2'):
	ltr = True
	for i in arr:
		if (ltr):
			for j in i:
				print(j, end=" ")
		else:
			i.reverse()
			for j in i:
				print(j, end=" ")
		ltr = not ltr
if (choice == '3'):
    k, l = 0, 0
    m = n
    while (k < m and l < n):
        for i in range(l, n):
            print(arr[k][i], end=" ")
        k = k+1
        for i in range(k, m):
            print(arr[i][n-1], end=" ")
        n = n-1
        if (k < m):
            for i in range(n-1, l-1, -1):
                print(arr[m-1][i], end=" ")
            m = m-1
        if (l < n):
            for i in range(m-1, k-1, -1):
                print(arr[i][l], end=" ")
            l = l+1
if (choice == '4'):
	for i in arr[0]:
		print (i, end=" ")
	for i in range(1, n-1):
		print (arr[i][-1], end=" ")
	arr[-1].reverse()
	for i in arr[-1]:
		print (i, end=" ")
	for i in range(n-2, 0, -1):
		print (arr[i][0], end=" ")
if (choice == '5'):
	m = n
	ans = [[] for i in range(n+m-1)]
	for i in range(m):
		for j in range(n):
			ans[i+j].append(arr[j][i])
	for i in ans:
		i.reverse()
		for j in i:
			print(j, end = " ")
if (choice == '6'):
	for i in arr:
		i.reverse()
	m = n
	ans = [[] for i in range(n+m-1)]
	for i in range(m):
		for j in range(n):
			ans[i+j].append(arr[j][i])
	for i in ans:
		i.reverse()
		for j in i:
			print(j, end = " ")