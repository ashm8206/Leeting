from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [1, 1,  2, 6]
        [24, 12, 4,  1]
        
        --[1]*n of two arrays
        --prefixprod[i] = prod[i-1]*nums[i-1]

        -suff-[i-1] = suff[i] * nums[i]
        --suff[2] = suff[3] * nums[i]

        [1, -1, -1, 0, 0]
        [0, 0, -9 ,  3, 1]

        """

        
        
        # allMul = reduce(mul, nums)
        
        # prefixMul = 1
        # suffixMul = allMul

        # # prefixSum = [1]*n
        # # suffixSum = [1]*n

        # for i in range(n):
        #     if i > 0:
        #         prefixMul *= nums[i-1]
            
        #     denominator = prefixMul*nums[i]
        #     if nums[i] == 0:
        #         suffixMul = reduce(mul,nums[i+1:],1)
        #     else:
        #         suffixMul = denominator and allMul // denominator

        #     res[i] = prefixMul * suffixMul

        n = len(nums)
        res = [1] * (n+1)
        # suffix = [1] * (n+1)

        # for i in range(n-1, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i]
        
        for i in range(n):
            res[i+1] = res[i] * nums[i]

        R = 1
        for j in range(n-1,-1,-1):
            res[j] *= R
            R *= nums[j]

        return res[:-1]

        


        