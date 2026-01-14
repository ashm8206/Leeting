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
        minPrefix = [float("inf")] * k
        minPrefix[0] = 0
        ans = float("-inf")

        for i in range(n):
            prefix+=nums[i]

            jmod = (i+1)%k
            ans = max(ans, prefix - minPrefix[jmod])
            
            minPrefix[jmod] = min(prefix, minPrefix[jmod])
            # print(ans, minPrefix)

        return ans


        