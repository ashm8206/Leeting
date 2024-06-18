class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start+=1
                end-=1
            return True
        

        res = []
        n = len(s)

        def dfs(slate, curr_idx):
            if curr_idx >= n:
                # base case, 
                # only add answer when all the string has finished Processing
                res.append(slate[:])
                return
        

            for i in range(curr_idx, len(s)):

                if isPalindrome(s, curr_idx, i): # if Constraint

                    slate.append(s[curr_idx:i+1]) # append Answer
                    dfs(slate, i+1) # next  ---> base, when do we cache result?? 
                    # when we have processed entire String
                    slate.pop() # remove Answer

        dfs([],0)
        return res

        # a|a|a|b # len == 1
        # aa |ab  #len = 2
        # aaa| b # len = 
        
        # aa
                