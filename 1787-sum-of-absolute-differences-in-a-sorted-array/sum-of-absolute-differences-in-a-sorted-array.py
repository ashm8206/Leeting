class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # 2, 3, 5
        # 10, 8, 5, 0
        #     0, 2, 5, 10 
        #  10-0-2 --> 8, 0
        #  10-2-3 --> 5, 2
        #  10 - 5-5  --> 0, 5



        n = len(nums)
        prefixSum = [0]*(n+1)
        suffixSum = [0]*(n+1)

        for i in range(1, n+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]

            suffixSum[n-i] = suffixSum[n-i+1] + nums[n-i]
        # # print(prefixSum)
        # # print(suffixSum)
        result = []
        for i in range(n):
            res = (i*nums[i] - prefixSum[i]) + (suffixSum[i] - nums[i]*(n-i))
            # print(res)
            result.append(res)
        return result
        
        # O(N)
        # O(N)

        # can you calculate prefix sum on the flyy??

        
