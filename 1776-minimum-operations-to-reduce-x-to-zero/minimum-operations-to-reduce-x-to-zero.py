class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = 0
        n = len(nums)

        total_sum  = sum(nums)

        maxArr = -1
        curr_sum = 0 
        for r in range(n):
            curr_sum += nums[r]

            while  l <= r and (total_sum - curr_sum < x):
                curr_sum -= nums[l]
                l+=1
            
            if total_sum - curr_sum == x:
                maxArr = max(maxArr, r-l+1)

        return  (n - maxArr if maxArr!= -1 else -1)

        
   