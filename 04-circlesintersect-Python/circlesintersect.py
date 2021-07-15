# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	a=(y2-y1)**2
	b=(x2-x1)**2
	e=a+b
	d=int((e)**0.5)
	if(d==r1+r2) or (d==r1-r2) or ((r1-r2)<d<(r1+r2)):
		return True
	else:
		return False
