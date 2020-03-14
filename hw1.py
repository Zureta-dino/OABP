from math import *

print('Input type: 1 - ellipse, 2 - hyperbola, 3 - parabola')
t = int(input())

if t == 1:
	print('Input coordinates of 2 points')
	x1, y1 = [float(e) for e in input().split()]
	x2, y2 = [float(e) for e in input().split()]
	b1 = x1*x1 - x2*x2
	a1 = x1*x1 * y2*y2
	a2 = x2*x2 * y1*y1
	if (b1 != 0) and (a1 >= a2):
		b = sqrt((a1 - a2)/b1)
		b2 = b*b - y1*y1
		if (b2 != 0):
			a = sqrt(b*b * x1*x1 / b2)
			print('a = ', a, 'b = ', b)
if t == 2:
	print('Input coordinates of 2 points')
	x1, y1 = [float(e) for e in input().split()]
	x2, y2 = [float(e) for e in input().split()]
	a1 = x1*x1 * y2*y2
	a2 = x2*x2 * y1*y1
	if (x1 != 0 or x2 != 0) and (a1 >= a2):
		b = sqrt((a1 - a2) / (x1*x1 + x2*x2))
		if (y1 != 0 or b !=0):
			a = sqrt(b*b * x1*x1 / (b*b + y1*y1))
			print('a = ', a, 'b = ', b)
if t == 3:
	print('Input coordinates of 1 point \n')
	x1, y1 = [float(e) for e in input().split()]
	if (x1 != 0):
		p = y1*y1 / (2*x1)
		print('p = ', p)





















