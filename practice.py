def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f





n=6
r=3
ncr=fact(n)/(fact(r)*fact(n-r))
print(int(ncr))
