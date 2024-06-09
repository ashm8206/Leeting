class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        L = 0
        maxCountOnes = 0
        maxLen = 0

        for R in range(len(nums)):

            if nums[R] == 1:
                maxCountOnes += 1
            
            if  R-L+1 - maxCountOnes > k:
                if nums[L] == 1:
                    maxCountOnes-=1
                L+= 1
            
            maxLen = max(maxLen, R-L+1)
        return maxLen

        # if winLen - freq[1] > k
            #  shrink window