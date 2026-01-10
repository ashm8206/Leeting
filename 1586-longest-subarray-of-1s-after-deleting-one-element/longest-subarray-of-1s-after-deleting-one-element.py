class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l = 0
        n = len(nums)
        maxSize = 0

        zeros = 0

        for r in range(n):
            if nums[r]==0:
                zeros+=1

            while zeros > 1:
                if nums[l]==0:
                    zeros-=1
                l+=1

        
            maxSize = max(maxSize, r-l) 
            # delete either 1  or O zero from keeping valid window with 1 0

        return maxSize
            
