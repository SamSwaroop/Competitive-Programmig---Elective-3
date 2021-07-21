# d=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]

# print(d)
n=4
s=[]
num=1

for i in range(1,n+1):
    x=[]
    for j in range(i,n+i):
        x.append(j)
    s.append(x)

print(s)


rows, cols = (4, 4)
# arr = [[0]*cols]*rows
arr=[[0 for j in range(4)] for i in range(4)]
for i in range(n):
    k=i+1
    # print(k)
    for j in range(n):
        arr[i][j]=k
        k=k+1
        

print(arr)




    
    

