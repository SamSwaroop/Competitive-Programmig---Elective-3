# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def frequency(x,n):
    c=0
    while (n!=0):
     if n%10==x:
        c+=1
     n=n//10
    return c





def mostfrequentdigit(n):
	big=0
	for i in range (10):
		if frequency(i,n)>frequency(big,n):
			big=i
	return big