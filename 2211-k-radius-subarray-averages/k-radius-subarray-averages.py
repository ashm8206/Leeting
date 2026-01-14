class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        divisor = 2*k + 1
        n = len(nums)
        res = [-1] * n

        prefixSum = [0]*(n+1)

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        for i in range(n):
            if i-k < 0 or i+k >= n:
                continue
            # i+k == n  i+k == n-1 and thats not in 0 index prefix array of sise n+1
            res[i] = (prefixSum[i+k+1] - prefixSum[i-k]) // divisor
        
        return res
             
