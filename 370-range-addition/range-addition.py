class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        prefixSum = [0]*length

        for s, e, inc in updates:
            prefixSum[s]+=inc
            if e+1 < length:
                prefixSum[e+1]-=inc
        
        for i, val in enumerate(prefixSum):
            if i > 0:
                prefixSum[i]+=prefixSum[i-1]

        return prefixSum
        
        # count = 0

        # for i, val in enumerate(prefixSum):
        #     if i > 0:
        #         prefixSum[i]+=prefixSum[i-1]
                
        #     if prefixSum[i] > 0 and i in range(left,right+1):
        #         count+=1

        # return count == right-left+1