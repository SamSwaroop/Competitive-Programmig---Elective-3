# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isPrime(x):
	if (x < 2):
		return False
	for factor in range(2,x):
		if (x % factor == 0):
			return False
	return True

def isPalindrome(x):
	# f=[int(i) for i in str(x)]
	if(x==int(str(x)[::-1])):
		return True
	else:
		return False

def fun_nth_palindromic_prime(n):
	p=0
	q=0
	while(p<=n):
		q=q+1
		if(isPrime(q) and isPalindrome(q)):
			p=p+1
	return q