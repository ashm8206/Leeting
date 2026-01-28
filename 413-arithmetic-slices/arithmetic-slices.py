class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        def helper(index):
            nonlocal ans
            # DP:  sol [i..j+1] depends on sol [i..j]
            # solve [i..j] multiple times

            # pure recursion: 
            # - independent problems
            # _ solved once

            # divide and concur: only this sol [i..j+1] depends on sol [i..j]
            # NO - solving same problem mutiple times

            if index < 2:
                return 0

            previousCount = helper(index-1)

            if (nums[index] - nums[index-1] == nums[index-1] - nums[index-2]):
                currCount =  1 + previousCount
                ans+= currCount
                return currCount
            
            return 0 # Return value denotes slices ending at position i
        helper(n-1)
        return ans



