s=234
z=[]

while(s!=0):
	f=s%10
	z.append(f)
	s=s//10

z.reverse()
print(z)
d=tuple(z)
print(d)
# print(z.reverse())