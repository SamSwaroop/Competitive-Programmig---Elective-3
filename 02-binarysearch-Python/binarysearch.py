"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

# def binary_search(input_array, value):
#     lo=input_array[0]
#     hi=input_array[len(input_array)-1]
#     mid=

def binary_search(input_array, value):
    
    # lo=0
    # hi=len(input_array)-1
    # mid=int(lo+((hi-lo)/2))
    # # if(input_array[mid]==value):
    # #     return mid
    # while(lo<hi):
    #     if(value<input_array[mid]):
    #         lo=0
    #         hi=mid
    #         mid=int(lo+((hi-lo)/2))
    #         if(input_array[mid]==value):
    #             return(mid)
    #     elif(value>input_array[mid]):
    #         lo=mid
    #         hi=len(input_array)-1
    #         mid=int(lo+((hi-lo)/2))+1
    #         if(lo==hi):
    #             mid=hi
    #         if(input_array[mid]==value):
    #             return(mid)
    #     elif(value==input_array[mid]):
    #         return mid
    # return -1

    
    left = 0
    right = len(input_array) - 1
    while left <= right:
        middle = (left + right)//2
        match = input_array[middle]
        if value < match:
            right = middle - 1
        elif value > match:
            left = middle + 1
        else:
            return middle
    return -1

