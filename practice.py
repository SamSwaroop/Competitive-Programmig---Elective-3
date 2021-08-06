s=32
d=[]


def factor(s,i):
    # s=32
    if(s%i)==0:
        return True
    else:
        return False



def nth_factor(x,n):
    p,q=0,0
    while(p<n and q<x):
        q=q+1
        if(factor(x,q)):
            p=p+1
    return q


print(nth_factor(36,4))