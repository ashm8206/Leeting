class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #open < #close X
        # close open >= close
        res = []
        
        def helper(open,close, slate):

            if len(slate) == 2*n:
                res.append("".join(slate[:]))

                # print(slate,res)
                return
            
            if open < n :

                slate.append('(')
                helper(open+1,close, slate)
                slate.pop()
                
            if close < open:
                slate.append(')')
                helper(open,close+1, slate)
                slate.pop()

        slate = ["("]
        helper(1,0,slate)
        return res
            
