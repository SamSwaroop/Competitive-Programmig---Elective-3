# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def happy(num):
    sum=0
    result=0
    while(num!=0):
        result=num%10
        sum=sum+(result**2)
        num=num//10
    return sum





def ishappyprimenumber(num):
    res=num
    while(res!=1 and res!=4):
        res=happy(res)
    if(res==1):
        return True
    elif(res==4):
        return False