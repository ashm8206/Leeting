class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #open < #close X
        # close open >= close
        res = []
        
        # Bcaktracking style

        # def dfs(open,close, slate):

        #     if close == n:
        #         res.append("".join(slate[:]))
        #         return
            
        #     if open < n :

        #         slate.append('(')
        #         dfs(open+1,close, slate)
        #         slate.pop()
                
        #     if close < open:
        #         slate.append(')')
        #         dfs(open,close+1, slate)
        #         slate.pop()

    
        # slate = []
        # dfs(0,0,slate)

        def helper(slate, op, cl):

            if op==0 and cl==0:
                res.append("".join(slate[:]))
                return
            if cl < op or op < 0:
                return
            
            if op > 0:
                helper(slate +['('], op-1, cl)
            if cl > op:
                helper(slate + [')'], op, cl-1)
         
        helper([], n, n)
        return res


       


            
