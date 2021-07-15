# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.


def distance(x1,y1,x2,y2,x3,y3):
	x0 = (int(pow((x2 - x1), 2)) +int(pow((y2 - y1), 2)))
	y0 = (int(pow((x3 - x2), 2)) +int(pow((y3 - y2), 2)))
	z0 = (int(pow((x3 - x1), 2)) +int(pow((y3 - y1), 2)))
	return x0,y0,z0



def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# x1,y1,x2,y2,x3,y3=abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3)
	x,y,z=distance(x1, y1, x2, y2, x3, y3)
	if ((x > 0 and y > 0 and z > 0) and (x == (y + z) or y == (x + z) or z == (x + y))):
		return True
	else:
		return False

