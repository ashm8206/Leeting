
class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = {}
        def dfs(i, target):

            if i ==n:
                return 1 if target==0 else 0

            if (i,target) in memo:
                return memo[(i,target)]

            res = dfs(i+1, target-nums[i])
            res+= dfs(i+1, target+nums[i])

            memo[(i,target)] = res

            return memo[(i,target)]
        return dfs(0,target)

        # bottom up T: O(n* Sum(nums)) S: O(n*m)
        # can be reduced to O(N) space, with just previous row.
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