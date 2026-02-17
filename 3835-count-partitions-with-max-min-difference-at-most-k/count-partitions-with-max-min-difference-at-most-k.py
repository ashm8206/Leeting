class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
        sl = SortedList([])
        n = len(nums)
        left = 0
        count = 0
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = 1
        prefix[0] = 1

        for right in range(n):
            sl.add(nums[right])

            while left <= right  and sl[-1] - sl[0] > k:
                sl.remove(nums[left])
                left+=1
            # print(sl)
            # count = (count + (right - left + 1)) % MOD

            # number of partions ending at right+1 viz right 
            dp[right + 1] = (prefix[right] - (prefix[left - 1] if left > 0 else 0)) % MOD
            
            # here we maintain prefix sum update 
            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD
        return dp[n]