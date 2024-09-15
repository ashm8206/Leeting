class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/775875/3-questions-1-approach-python/?envType=study-plan-v2&envId=top-interview-150
        A = nums
        if max(A) <= 0:
            return max(A)
            
        max_dp = [i for i in A]
        min_dp = [i for i in A]
        
        for i in range(1,len(A)):
            if max_dp[i-1] > 0:
                max_dp[i] += max_dp[i-1]
            if min_dp[i-1] < 0:
                min_dp[i] += min_dp[i-1]

        return max(max(max_dp), sum(A) - min(min_dp))