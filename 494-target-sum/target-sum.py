
class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        count = 0
        n = len(nums)

        memo = {}

        def helper(running_sum, idx):
            nonlocal count
            
            if idx == n:
                return 1 if running_sum==target else 0

            if (running_sum, idx) in memo:
                return memo[(running_sum, idx)]
            
            memo[(running_sum, idx)] = (
                helper(running_sum + nums[idx], idx+1) 
                + helper(running_sum - nums[idx] , idx+1)
            )
            return memo[(running_sum, idx)]

        # for loop is not not for tradition combinations
        # we only want Combindations of len(N) start from idx 0... end N
        # Each idx has two option, take / don't take
        return helper(0, 0)
        

        
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