class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # ( --> ) +1
        # (()
        # (()(()))
        # 2( 1+ 2*1) 2*()
        #  2 + 

        # bal = 0

        # ( 1, 0
        # (( 2, 0
        # (() 1, 2
        # (())

        depth = 0
        stack =[0]
        for ch in s:
            if ch =='(':
                depth+=1
                stack.append(0)
            else:
                depth-=1
                v = stack.pop()
                stack[-1] += max(2*v, 1)
        return stack.pop()
