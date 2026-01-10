class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=e0AFPpKcjw0

        # Why sort ?
        # We have to select an element 
        # go backwards and find the closest element

        # How back can we go ? 
        #  freqEl * windolen = sumEle(nums[l:r+1]) + k









        nums.sort()
        maxLen = 0
        L = 0
        currSum = 0
        for R in range(len(nums)):
            target = nums[R]
            currSum += nums[R]

            while (R - L + 1)* target - currSum > k: # the number of replacements is greater than allowed replacements
                # Remove Left side string
                currSum -= nums[L]
                L += 1
            
            maxLen = max(maxLen, R - L + 1)
        return maxLen