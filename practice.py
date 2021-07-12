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
# a=6
# b=2
# c=6
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# d.sort(reverse=True)
# # s="".join(d)
# r=""
# for i in d:
#     r=r+str(i)
# print(r)
hand=413
r=2312

s=hand
z=[]

while(s!=0):
	f=s%10
	z.append(f)
	s=s//10

z.reverse()

g=set(z)
l=[]
o=[]

if(len(z)!=len(g)):
    g=[]
    e=[]
    count=0
    for i in z:
        if i not in g:
            g.append(i)
        else:
            e.append(i)

    n=[]
    for i in e:
        for j in z:
            if i==j:
                n.append(str(i))

    s=r%10
    r=r//10
    n.append(str(s))
    n.sort(reverse=True)
    c="".join(n)
    # print(c)
    print("(",c,",",r,")")

else:
    z.sort(reverse=True)
    # h=""+str(z[0])
    # h+=str(r%100)
    w=[]
    w.append(z[0])
    w.append(r%10)
    r=r//10
    w.append(r%10)
    r=r//10
    w.sort(reverse=True)
    h=""+str(w[0])+str(w[1])+str(w[2])
    print("(",h,",",r,")")

# r=56
# d=[2,3,3,4,1]
# g=[]
# e=[]
# count=0
# for i in d:
#     if i not in g:
#         g.append(i)
#     else:
#         e.append(i)

# n=[]
# for i in e:
#     for j in d:
#         if i==j:
#             n.append(str(i))

# s=r%10
# n.append(str(s))
# n.sort(reverse=True)
# c="".join(n)
# print(c)







