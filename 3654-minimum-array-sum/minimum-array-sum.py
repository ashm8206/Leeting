class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @lru_cache(maxsize = None)
        def helper(i, op1, op2):
            
            if i == n: 
                return 0 

            ans = nums[i] + helper(i+1, op1, op2)

            if op1: 
                ans = min(ans, (nums[i]+1)//2 + helper(i+1, op1-1, op2))

            if op2 and nums[i] >= k: 
                ans = min(ans, nums[i]-k + helper(i+1, op1, op2-1))

            # After first operation first
            if op1 and op2 and (nums[i]+1)//2 >= k: 
                ans = min(ans, (nums[i]+1)//2-k + helper(i+1, op1-1, op2-1))
            # After second operation first
            if op1 and op2 and nums[i] >= k: 
                ans = min(ans, (nums[i]-k+1)//2 + helper(i+1, op1-1, op2-1))
            return ans 
        n = len(nums)
        return helper(0, op1, op2)  