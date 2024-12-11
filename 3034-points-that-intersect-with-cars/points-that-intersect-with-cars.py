class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        prefixSum = [0]*102

        for s, e in nums:
            prefixSum[s]+=1
            prefixSum[e+1]-=1
        
        count = 0

        for i, val in enumerate(prefixSum):
            if i > 0:
                prefixSum[i]+=prefixSum[i-1]
                
            if prefixSum[i] > 0:
                count+=1
        return count
