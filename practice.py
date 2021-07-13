def fun_getinrange(x, bound1, bound2):
    l=[]
    l.append(bound1)
    l.append(bound2)
    l.sort()
    s=[]
    for i in range(l[0],l[1]+1):
        s.append(i)
    if(x in s):
        return x
    elif(x < l[0]):
        return l[0]
    elif(x > l[1]):
        return l[1]


print(fun_getinrange(0, 5, 2))