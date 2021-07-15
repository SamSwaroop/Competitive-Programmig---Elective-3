# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	# l=[]
	# l.append(bound1)
	# l.append(bound2)
	# l.sort()
	# s=[]
	# for i in range(l[0],l[1]+1):
	# 	s.append(i)
	# if(x in s):
	# 	return x
	# elif(x < l[0]):
	# 	return l[0]
	# elif(x > l[1]):
	# 	return l[1]

	lp=0
	up=0
	if(bound1 < bound2):
		lp=bound1
		up=bound2
	else:
		lp=bound2
		up=bound1
	if(x<lp):
		return lp
	elif(x>up):
		return up
	elif(lp<x<up):
		return x
	# if(x<bound1):
	# 		return bound2
	# elif(x>bound2):
	# 	return bound1
	# elif(bound2<x<bound1):
	# 	return x


	




