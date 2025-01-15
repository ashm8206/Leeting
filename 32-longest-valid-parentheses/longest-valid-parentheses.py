class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        stack = []
        i = 0
        n = len(s)
        ans = 0
        stack.append(-1)
        
        while i < n:
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i-stack[-1])

            i+=1
        return maxLen