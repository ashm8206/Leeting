class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        maxEnergy = float("-inf")
        memo = {}
        def helper(index):
            nonlocal maxEnergy
            if index >= n:
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index] = energy[index] + helper(index+k)
            # maxEnergy = max(maxEnergy, memo[index])
            return memo[index]
        
        for i in range(n):
            maxEnergy = max(helper(i), maxEnergy)
        # print(memo)
        return maxEnergy

        # return maxEnergy
            