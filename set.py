# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

import itertools
def limitedPowerSet(n, k):
    count=0
    f=[]
    l=set()
    while(count<=k):
        f.append(l.add(count))
        count=count+1
    return f

print(limitedPowerSet(5, 7))