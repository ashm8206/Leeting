class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        # birthyear 1951
        # 1951-1950 = 1 index 1
        #  1950 + index
        
        prefixSum = [0]*101

        for b, d in logs:
            b_idx = b - 1950
            d_idx = d - 1950
            prefixSum[b_idx]+=1
            prefixSum[d_idx]-=1
        prefixSum = list(accumulate(prefixSum))

        print(prefixSum)
        year = 0
        maxPopulation = 0
        for i, val in enumerate(prefixSum):
            if val > maxPopulation:
                maxPopulation = val
                year = i+1950
        return year
    
        
        
        return 1


