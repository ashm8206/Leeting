import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

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
