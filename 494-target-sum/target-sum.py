
class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp = [ 0 for _ in range(sum(nums)) for i in range(n+1)]
        # since we will get negative sums, and cant have -ve indices
        # replace inner array with default(int)

        dp = [defaultdict(int) for i in range(n+1)]
        dp[0][0] = 1 # 1 way of getting 0 

        for i in range(n):
            for k,v in dp[i].items():
                curr_sum = k
                countWays = v
                # you are carrying forward the 1 way from dp[0][0]
                dp[i+1][curr_sum-nums[i]]+=countWays 
                dp[i+1][curr_sum+nums[i]]+=countWays 
                # numberways of reaching curr_sum ± nums[i]
                # add +1 way way or the previous count
        return dp[n][target]

        # count = 0
        # n = len(nums)

        # memo = {}

        # def helper(running_sum, idx):
        #     nonlocal count
            
        #     if idx == n:
        #         return 1 if running_sum==target else 0

        #     if (running_sum, idx) in memo:
        #         return memo[(running_sum, idx)]
            
        #     memo[(running_sum, idx)] = (
        #         helper(running_sum + nums[idx], idx+1) 
        #         + helper(running_sum - nums[idx] , idx+1)
        #     )
        #     return memo[(running_sum, idx)]

        # # for loop is not not for tradition combinations
        # # we only want Combindations of len(N) start from idx 0... end N
        # # Each idx has two option, take / don't take
        # return helper(0, 0)
        

        
        # count = 0
        # n = len(nums)

        # # @lru_cache(None)
        # def helper(curr_sum, curr_idx):

        #     nonlocal count

        #     if curr_idx == n:
        #         if curr_sum==target:
        #             count+=1
        #         return

        #     helper(curr_sum - nums[curr_idx], curr_idx+1)
        #     helper(curr_sum + nums[curr_idx], curr_idx+1)
            
        # helper(0, 0)
        # return count