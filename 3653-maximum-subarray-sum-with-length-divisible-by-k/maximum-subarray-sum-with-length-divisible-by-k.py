class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        # n = len(nums)
        # prefixSum = [0]* (n+1)

        # for i in range(n):
        #     prefixSum[i+1] = prefixSum[i] + nums[i]
        
        # # (j+1 - i)mod k = 0
        # # i mod k = (j-1)modk
       
        # maxSum = float("-inf")
        # for length in range(1, n+1):
        #     if length % k == 0:
        #         for start in range(n - length + 1):
        #             maxSum = max(maxSum, prefixSum[start+length] - prefixSum[start])
        # return maxSum

        n = len(nums)
        prefix = 0
        res = float('-inf')
        # Store minimum prefix sum for each mod value
        min_prefix = {0: 0}  # prefix sum 0 at "index -1"
        
        for i, num in enumerate(nums):
            prefix += num
            mod = (i + 1) % k
            if mod not in min_prefix:
                min_prefix[mod] = prefix
            else:
                res = max(res, prefix - min_prefix[mod])
                min_prefix[mod] = min(min_prefix[mod], prefix)
        return res

        