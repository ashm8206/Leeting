from math import log2
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:  # if Quotient falls below 0  [ 0]
            return False
        elif n == 1:
            return True
        elif n%4:
            return False
        return self.isPowerOfFour(n//4)

 
        # return n > 0 and log2(n) % 2 == 0



        # a=log4x= (1/2)log2x is an integer.
        # a=log8x= (1/3)log2x is an integer. (log2(8))



        # 3 11
        # 9 1001
        # 27 11011
        # 81 1010001
        # 243 11110011
        # 729 1011011001
        # 2187 100010001011
        # 6561 1100110100001
        # 19683 100110011100011