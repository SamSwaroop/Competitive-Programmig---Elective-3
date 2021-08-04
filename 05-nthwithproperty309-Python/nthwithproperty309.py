# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withprop(n):
	d=n**5
	f=[i for i in str(d)]
	g=[0,1,2,3,4,5,6,7,8,9]
	for j in g:
		if j in f:
			continue
		else:
			return False
	return True







def nthwithproperty309(n):
	p,q=0,0
	while(p<=n):
		q=q+1
		if(withprop(q)):
			p=p+1
	return q