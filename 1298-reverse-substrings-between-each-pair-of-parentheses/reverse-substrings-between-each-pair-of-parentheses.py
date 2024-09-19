class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = []

        for ch in s:
            if ch=='(' or ch.isalpha():
                stack.append(ch)
            else:
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop() # pop '('
                stack.extend(temp)
            
        return ''.join(stack)

