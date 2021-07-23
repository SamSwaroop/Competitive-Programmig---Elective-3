


# s="134343"
# print(len(s))

def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True


def addition(x):
    sum=0
    while(x!=0):
        f=x%10
        sum=sum+f
        x=x//10
    return sum




def isAdditivePrime(n):
    n=str(n)
    while(len(n)!=1):
        n=int(n)
        d=addition(n)
        n=str(d)

    if(isPrime(int(n))):
        return True
    else:
        return False


print(isAdditivePrime(29))
print(isAdditivePrime(23))
print(isAdditivePrime(17))

    
    

    