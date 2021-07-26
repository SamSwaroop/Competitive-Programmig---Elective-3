# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def automorphic(n):
	d=len(str(n))
	g=n*n
	s=g%(10**d)
	if(n==s):
		return True
	else:
		return False


def nthautomorphicnumbers(n):
	# if(n==1):
	# 	return 0
	# if(n==2):
	# 	return 1
	p=0
	q=0
	res=0
	while(p<n):
		# q=q+1
		if(automorphic(q)):
			res=q

			p=p+1
		q=q+1
	return res