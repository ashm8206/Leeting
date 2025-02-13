class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n==1:
            return nums[0]

        def rob(nums):
            k = len(nums)
            if k < 2:
                return nums[0]
            dp = [0]* k
            dp[0] = nums[0]
            dp[1] = max(nums[1] + 0, nums[0])
            
            for i in range(2, k):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            
            return dp[-1]

        return max(rob(nums[:n-1]), rob(nums[1:]))


        def solve (left, right):
            t1 = 0
            t2 = 0
            for i in range(left, right+1):
                current = nums[i]
                tempt1 = t1
                t1 = max(current + t2, t1)
                t2 = tempt1
            return t1

        # the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n]