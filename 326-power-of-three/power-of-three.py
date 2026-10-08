class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        x=0
        def valid(n,x):
            if n==3**x:
                return True
            if n<3**x:
                return False
            return valid(n,x+1)
        return valid(n,0)