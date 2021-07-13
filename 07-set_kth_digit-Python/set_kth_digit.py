# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	if(n>0):
		r=(n//(10**k)%10)
		t=[int(e) for e in str(n)]
		for i in t:
			if i==r:
				y=t.index(i)
				t[y]=d
				f=[str(integers) for integers in t]
				o="".join(f)
				return(int(o))
		t.insert(0,d)
		f=[str(integers) for integers in t]
		o="".join(f)
		return(int(o))
	else:
		n=abs(n)
		r=(n//(10**k)%10)
		t=[int(e) for e in str(n)]
		for i in t:
			if i==r:
				y=t.index(i)
				t[y]=d
				f=[str(integers) for integers in t]
				o="".join(f)
				return(int(o))
		t.insert(0,d)
		f=[str(integers) for integers in t]
		o="".join(f)
		s="-"+o
		return(int(s))

	

