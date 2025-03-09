class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        L = 0
        maxCountZero = 0
        maxLen = 0
    
        # [0, 0, 0]
        # k = 1 : 1

        # []: inv

        # [0, 0, 0]
        # k = 0 

         # [1, 0, 1] : maxlen : 1, 1-2+1 = 0
        # k = 0 : maxlen : 1, 2-2+1 = 1

        

        for R in range(len(nums)):

            if nums[R] == 0:
                maxCountZero += 1

            while maxCountZero > k:
                if nums[L]==0:
                    maxCountZero-=1
                # keep shrinking till we can make it valid
                L+=1

            maxLen = max(maxLen, R-L+1)
        return maxLen

