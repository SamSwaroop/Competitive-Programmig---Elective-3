
import math



def binary_search(input_array, value):
    
    lo=0
    hi=len(input_array)-1
    mid=math.ceil(hi/2)+1
    if(input_array[mid]==value):
        return mid
    while(lo<=hi):
        if(value<mid):
            lo=0
            hi=mid
            mid=math.ceil(hi/2)+1
            if(input_array[mid]==value):
                return(mid)
        elif(value>mid):
            lo=mid
            hi=len(input_array)-1
            mid=math.ceil(hi/2)+1
            if(input_array[mid]==value):
                return(mid)
    


input_array=[1,2,3,4,5,6,7,8,9]
value=9
print("Found the Value at the index:",binary_search(input_array, value))

# input_array=[1,2,3,4,5,6,7,8,9]
# lo=0
# hi=len(input_array)-1
# mid=int((hi/2)+1)
# print(mid)
# while
