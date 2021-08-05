# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	count=-1
	f=[]
	power=0
	if(n<1):
		return None
	if(n==1):
		return [1]
	while(power <= n):
		count=count+1
		power=3**count
		

		f.append(power)
	f.pop()
		
		
	return f

