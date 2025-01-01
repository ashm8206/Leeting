class Solution:
    def maxScore(self, s: str) -> int:
        
        maxSum = 0

        n = len(s)
        for i in range(n-1):
            left = s[:i+1].count("0")
            right = s[i+1:].count("1")
            print(left,right)
            maxSum = max(left+right, maxSum)
        return maxSum
