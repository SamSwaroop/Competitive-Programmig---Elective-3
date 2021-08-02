# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    
    e=s1.lower()
    f=s2.lower()
    if(len(e)==len(f)):
        for i in range(len(e)):
            if(e[i]  in f) and (f[i] in e):
                continue
            else:
                return False
        return True
    else:
        return False
    


# write your test cases here...

print(areAnagrams("Abac", "BBA"))
print(areAnagrams("bac", "BAc"))
