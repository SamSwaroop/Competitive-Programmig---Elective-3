# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
    if(type(n)!=int):
        if(type(n)==float or n.isdigit()):
            n=int(n)
            r=n**0.5
            if(r*r)==n:
                return True
        else:
            return False
    r=n**0.5
    if(r*r==n):
        return True
    return False