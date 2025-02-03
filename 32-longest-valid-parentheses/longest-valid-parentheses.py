class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left, right, maxLen = 0, 0 ,0
        n = len(s)
        for i in range(n):
            if s[i]=="(":
                left+=1
            else:
                right+=1
            if left == right:
                maxLen = max(maxLen, 2*right)
            elif right > left:
                left = right = 0

        left, right = 0, 0
        for j in range(n-1,-1,-1):
            if s[j]=="(":
                left+=1
            else:
                right+=1
            if left == right:
                maxLen = max(maxLen, 2*right)
            elif left > right:
                left = right = 0
        return maxLen
                
        