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
      

        # (())()"
        # 
        score = 0
        n = len(s)
        
        def helper(idx, depth):
            nonlocal score
            if idx > n-1:
                return 
            if s[idx]==')':
                depth-=1
                if s[idx-1]=='(': 
                    score+= 2**(depth)

            elif s[idx]=='(':
                depth +=1
            
        
            
            helper(idx+1, depth)

        helper(0,0)
        return score