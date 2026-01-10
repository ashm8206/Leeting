class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l = 0
        n = len(nums)
        maxSize = 0

        zeros = 0
        curr_sum = 0 # number of 1s
        for r in range(n):
            curr_sum+= nums[r]

            if nums[r]==0:
                zeros+=1

            while (r-l+1) - curr_sum > 1:
                curr_sum -=nums[l]
                if nums[l]==0:
                    zeros-=1
                l+=1
                
            if zeros == 0:
                maxSize = max(maxSize, r-l)
            else:
                maxSize = max(maxSize, r-l+1 - zeros) # 
        return maxSize
            
