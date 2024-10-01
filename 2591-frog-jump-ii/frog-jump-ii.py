class Solution:
    def maxJump(self, stones: List[int]) -> int:
        maxJump = float("-inf")

        
        n = len(stones)
        if n ==2:
            return max(maxJump, abs(stones[0]-stones[1]))
        
        for i in range(0, n-2):
            maxJump = max(maxJump, abs(stones[i]-stones[i+2]))
        
        return maxJump
