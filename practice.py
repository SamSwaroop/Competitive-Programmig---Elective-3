n=-468
k=3
d=1
r=(n//(10**k)%10)
t=[int(e) for e in str(n)]
for i in t:
    if i==r:
        y=t.index(i)
        t[y]=d
        f=[str(integers) for integers in t]
        o="".join(f)
        print(int(o))
t.insert(0,d)
f=[str(integers) for integers in t]
o="".join(f)
s="-"+o
print(int(s))
        
