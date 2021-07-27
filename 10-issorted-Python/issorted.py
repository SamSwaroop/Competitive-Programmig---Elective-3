# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	test_list=a
	flag = 0
	i = 1
	while i < len(test_list):
		if(test_list[i] < test_list[i - 1]):
			flag = 1
		i += 1
	if (not flag):
		return True
	else :
		return False
# d=[1, 2, 3, 4, 5]
# print(issorted(d))
# e=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(issorted(e))
# r=[1]
# print(issorted(r))
# t=[1, 1]
# print(issorted(r))
# y=[]
# print(issorted(y))
# u=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(issorted(u))
# i=[10, 9, 8, 7, 6, 5, 4, 3, 2, 10]
# print(issorted(i))
# o=[1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10]
# print(issorted(o))


