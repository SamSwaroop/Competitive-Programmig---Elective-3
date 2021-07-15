mssg="ABCDXYZ"
shift=-3
u=""
for i in mssg:
    if(ord(i)==32):
        u+=i
        continue
    if (i.isupper()):
        l=ord(i) + shift
        j=(l - 64)-1
        u += chr((j % 26 + 65))  
    else:
        l=ord(i) + shift
        j=(l - 96)-1
        u += chr((j % 26 + 97))
        # u += chr(((ord(i) + shift - 96) % 26 + 97)-1)
#     # print(i,"-",ord(i))
# #     if(ord(i)!=32):
# #         print(i,"-",ord(i)) 
# #         change=ord(i)+shift
# #         s[s.index(i)]=chr(change)
print(u)

# s="c"
# shift=-3
# u=""
# for i in s:
#     u += chr(((ord(i) + shift - 96) % 26 + 97)-1)
# print(u)







# d=65%90
# print(d)