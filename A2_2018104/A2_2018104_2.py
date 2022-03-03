def transform(old, mat):
	new = [0,0,0,0]
	new[0] = old[0]*mat[0][0] + old[1]*mat[0][1] + old[2]*mat[0][2] + old[3]*mat[0][3]
	new[1] = old[0]*mat[1][0] + old[1]*mat[1][1] + old[2]*mat[1][2] + old[3]*mat[1][3]
	new[2] = old[0]*mat[2][0] + old[1]*mat[2][1] + old[2]*mat[2][2] + old[3]*mat[2][3]
	new[3] = old[0]*mat[3][0] + old[1]*mat[3][1] + old[2]*mat[3][2] + old[3]*mat[3][3]
	return new

import math
n = int(input("Enter the number of vertices of the 3D shape: "))
x = list(map(int, input("Input a space-separated list for x-coordinates").split()))
y = list(map(int, input("Input a space-separated list for y-coordinates").split()))
z = list(map(int, input("Input a space-separated list for z-coordinates").split()))
q = int(input("Enter the number of transformation queries: "))
queries = []
for i in range(q):
	temp = list(map(int, input().split()))
	queries.append(temp)
# s = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
# t = [[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
# rx = [[1,0,0,0],[0,math.cos(theta),-math.sin(theta),0],[0,math.sin(theta),math.cos(theta),0],[0,0,0,1]]
# ry = [[math.cos(theta),0,math.sin(theta),0],[0,1,0,0],[-math.sin(theta),0,math.cos(theta),0],[0,0,0,1]]
# rz = [[math.cos(theta),-math.sin(theta),0,0],[math.sin(theta),math.cos(theta),0,0],[0,0,1,0],[0,0,0,1]]
for i in range(q):
	task = q[i]
	if (task[0] == 'S'):
		sx = task[1]
		sy = task[2]
		sz = task[3]
		s = [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
		for i in range(len(x)):
			new = transform([x[i],y[i],z[i],1], s)
			x[i] = new[0]
			y[i] = new[1]
			z[i] = new[2]
	if (task[0] == 'T'):
		tx = task[1]
		ty = task[2]
		tz = task[3]
		t = [[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
		for i in range(len(x)):
			new = transform([x[i],y[i],z[i]], t)
			x[i] = new[0]
			y[i] = new[1]
			z[i] = new[2]
	if (task[0] == 'R'):
		axis = task[1]
		theta = task[2]
		if (axis == 'x'):
			mat = [[1,0,0,0],[0,math.cos(theta),-math.sin(theta),0],[0,math.sin(theta),math.cos(theta),0],[0,0,0,1]]
		if (axis == 'y'):
			mat = [[math.cos(theta),0,math.sin(theta),0],[0,1,0,0],[-math.sin(theta),0,math.cos(theta),0],[0,0,0,1]]
		if (axis == 'z'):
			mat = [[math.cos(theta),-math.sin(theta),0,0],[math.sin(theta),math.cos(theta),0,0],[0,0,1,0],[0,0,0,1]]
		for i in range(len(x)):
			new = transform([x[i],y[i],z[i]], mat)
			x[i] = new[0]
			y[i] = new[1]
			z[i] = new[2]
file = open('output.txt', 'w')
ans = "Input: "+"\n"
ans = ans+"n = "+str(n)+"\n"
ans = ans+"x = "+str(x)+"\n"
ans = ans+"y = "+str(y)+"\n"
ans = ans+"z = "+str(z)+"\n"
ans = ans+"q = "+str(q)+"\n"
ans = ans+"Output = "+"\n"
ans = ans+str(x) + '\n' + str(y) + '\n' +  str(z)
file.write(ans)
file.close()