class Solution:
    def maxScore(self, s: str) -> int:
        
        # maxSum = 0

        # n = len(s)
        # for i in range(n-1):
        #     left = s[:i+1].count("0")
        #     right = s[i+1:].count("1")
        #     maxSum = max(left+right, maxSum)
        # return maxSum

        # optimized
        ones = s.count("1")
        zeros = 0
        ans = 0 
        n = len(s)

        for i in range(n-1):
            if s[i] == "1":
                ones -= 1
                # this s[i] was part of right
                # but now adding to left, we lose it
            else:
                # this s[i] was part of left
                # and we add the zeros as we gain
                zeros += 1
        
            ans = max(ans, zeros + ones)
        
        return ans
