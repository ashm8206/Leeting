class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 0:
        #     return False
        # return n & (n-1) == 0

        if n == 0:
            return False
        # return n & ~(n-1) == n # sets right most bit, 
        return n &(n-1)==0
        # since 2's value has only 1  bit set. the above operation, leaves the right-most bit set = x if x is power of 2

        # if n == 1:
        #     return True
        # elif n == 0:
        #     return False
        # if n%2:
        #     return False
 
        # return self.isPowerOfTwo(n//2)
