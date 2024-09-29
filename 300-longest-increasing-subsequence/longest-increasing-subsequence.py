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
        n = len(nums)
        tail = [nums[0]]

        for i in range(1, n):
            if nums[i] <= tail[-1]:
                # we need to restart the inc seq.
                insert_idx = bisect.bisect_left(tail, nums[i])

                tail[insert_idx] = nums[i]
            else:
                tail.append(nums[i])
        
        return len(tail)
