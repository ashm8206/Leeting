class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # prefixSum = [0]*(n+1)
        # suffixSum = [0]*(n+1)

        # for i in range(1, n+1):
        #     prefixSum[i] = prefixSum[i-1] + nums[i-1]

        #     suffixSum[n-i] = suffixSum[n-i+1] + nums[n-i]
        
        # result = []
        # for i in range(n):
        #     res = (i*nums[i] - prefixSum[i]) + (suffixSum[i] - nums[i]*(n-i))
        #     # print(res)
        #     result.append(res)
        # return result

        total = sum(nums)
        left_sum = 0
        right_sum = total

        result = []
        for i in range(0, n):
            right_sum -= nums[i]
            
            index_sum = abs(left_sum  - nums[i]*i) + abs(right_sum  - nums[i]*(n-i-1))
            left_sum+= nums[i]
            result.append(index_sum)
         
        # [2,5,10]
        # [8,5,0]
        return result
        
        
       
       

        
