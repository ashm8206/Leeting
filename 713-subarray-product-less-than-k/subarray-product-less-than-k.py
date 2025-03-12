from functools import reduce
import operator

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        if k <=1:
            return 0
        
        prod = 1
        left = 0
        for right, num in enumerate(nums):
            prod*=num

            while prod>=k:
                prod /= nums[left]
                left+=1
            # count of subarrays between [l...r]
            ans+= right-left+1
        return ans


        
        # prefix sum : Fails due to double counting from both ends
        # total = reduce(operator.mul, nums)
        
        # left = 1 
        # for i, num in enumerate(nums):
        #     left*=num

        #     if left < k:
        #         ans+= (i+1) 
            
        #     right = total // left
        #     # print(left, right, i)

        #     if right < k:
        #         ans+=(n-(i+1))
      
        # return ans

        

        

        #    [10, 50, 100, 600]
        # 600[60, 12, 6, 1]
        # [600, 60, 12, 6]

        # ans: 1+ 4 + 2+ 1 = 8 ?

