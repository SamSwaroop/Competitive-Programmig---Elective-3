# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronic(x):
	i=1
	while ( i <= (int)((x)**0.5) ) :
		if ( x == i * (i + 1)) :
			return True
		i = i + 1
	return False



def nthpronicnumber(n):
	if(n==0):
		return 0
	p,q=1,1
	while(p<=n):
		q=q+1
		if(pronic(q)):
			p=p+1
	return q
