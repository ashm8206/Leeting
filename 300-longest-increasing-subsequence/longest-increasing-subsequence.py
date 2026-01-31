import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # TLE/ Memory
        # n = len(nums)
        # memo = {}
        # def helper(idx, prev):

        #     # nonlocal maxLen
        #     if (idx, prev) in memo:
        #         return memo[(idx, prev)]

        #     if idx == n-1:
        #         if prev == float("-inf") or nums[idx] > prev:
        #             return 1
        #         return 0

        #     take = 0
        #     if nums[idx] > prev:
        #         take = 1 + helper(idx+1, nums[idx])
        #     dont_take = helper(idx+1, prev)
        #     # maxLen = max(maxLen,max(take, dont_take))

        #     memo[(idx, prev)] = max(take, dont_take)
        #     return memo[(idx, prev)] 

        # return helper(0, float("-inf"))

        #  Method I
        # n = len(nums)
        # dp = [ 1 for i in range(n)]
        # # dp = [ 0 for i in range(n)]
        # dp[0] = 1

        # maxDpLen = 1
        # for i in range(1,n):
        #     for j in range(0, i):
        #         if nums[j] < nums[i]:
                  
        #             dp[i] = max(dp[i], dp[j] + 1) #Dijkstras
        #             # if we already have a max increasing sub sequence, retain that 
        #             # rather than starting a new sequence
        # #     print(dp[i])
        #     maxDpLen = max(maxDpLen, dp[i]) 
       
        # return maxDpLen
        
        #  Method II
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
       
        return len(sub)
