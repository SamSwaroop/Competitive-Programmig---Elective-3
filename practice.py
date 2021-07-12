# s=234
# z=[]

# while(s!=0):
# 	f=s%10
# 	z.append(f)
# 	s=s//10

# z.reverse()
# print(z)
# d=tuple(z)
# print(d)
# print(z.reverse())
a=6
b=2
c=6
d=[]
d.append(a)
d.append(b)
d.append(c)
d.sort(reverse=True)
# s="".join(d)
r=""
for i in d:
    r=r+str(i)
print(r)