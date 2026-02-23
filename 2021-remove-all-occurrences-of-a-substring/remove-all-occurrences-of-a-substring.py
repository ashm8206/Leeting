class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(s)
        k = len(part)
        
        for i in range(n+1):
            if stack and ("".join(stack[-k:])==part or (i == n and "".join(stack[-k:])==part)):
                # print(stack)
                for _ in range(k):
                    stack.pop()
            if i < n:
                stack.append(s[i])

        

        return "".join(stack)

