# from math import log10
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # if n > 0:
        #     return 1162261467 % n == 0
        # return False
# https://leetcode.com/problems/power-of-three/solutions/2471285/python-c-one-liner-o-1-easy-solution-with-detailed-explanation-beginner-friendly/
        
        if n <=0:  # if Quotient falls below 0  [ 0]
            return False
        elif n == 1:
            return True
        elif n%3:
            return False
        return self.isPowerOfThree(n//3)



        # 1 # 3 11
        # 2# 9 1001
        # 3 # 27 11011
        # 4# 81 1010001
        # 5 # 243 11110011
        # 6 # 729 1011011001
        # 7 # 2187 100010001011
        # 8 # 6561 1100110100001
        # 9 # 19683 100110011100011