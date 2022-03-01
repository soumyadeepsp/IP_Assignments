import math
s = input("Enter the origin of the light ray as a vector<Ex, Ey, Ez>: ")
e = list(map(float, s[1:len(s)-1].split(",")))
s = input("Enter the direction of the light ray as a vector<Dx, Dy, Dz>: ")
D = list(map(float, s[1:len(s)-1].split(",")))
s = input("Enter the coordinates of the sphere's center as a vector<X, Y, Z>: ")
x = list(map(float, s[1:len(s)-1].split(",")))
r = float(input("Enter the radius of the sphere: "))
L = [x[0]-e[0], x[1]-e[1], x[2]-e[2]]
tca = L[0]*D[0] + L[1]*D[1] + L[2]*D[2]
if (tca < 0):
	print ("The line doesn't intersect the circle")
d = (abs(((L[0]**2 + L[1]**2 + L[2]**2) - tca*tca)))**(1/2)
thc = (abs(r*r - d*d))**(1/2)
t0 = tca - thc
t1 = tca + thc
t01 = math.floor(t0)
t02 = t01 + 1
t11 = math.floor(t1)
t12 = t11 + 1
print (t0)
p0 = [round(e[0]+t01*D[0], 2), round(e[1]+t01*D[1], 2), round(e[2]+t01*D[2], 2)]
p0bar = [round(e[0]+t02*D[0], 2), round(e[1]+t02*D[1], 2), round(e[2]+t02*D[2], 2)]
p1 = [round(e[0]+t11*D[0], 2), round(e[1]+t11*D[1], 2), round(e[2]+t11*D[2], 2)]
p1bar = [round(e[0]+t12*D[0], 2), round(e[1]+t12*D[1], 2), round(e[2]+t12*D[2], 2)]
if (t01<1000 and t11<1000):
	if (t1-t0 <= 2*r):
		print ("The first point of intersection is between "+str(p0)+" at t="+str(t01)+" to "+str(p0bar)+" at t="+str(t02))
		print ("The second point of intersection is between "+str(p1)+" at t="+str(t11)+" to "+str(p1bar)+" at t="+str(t12))
	else:
		print ("The first point of intersection is between "+str(p0)+" at t="+str(t01)+" to "+str(p0bar)+" at t="+str(t02))
else:
	print ("The constraint of t is not satisfied")

''' 
https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection

I used the above link to understand how to geometrically 
 solve the ray-sphere intersection problem .
'''