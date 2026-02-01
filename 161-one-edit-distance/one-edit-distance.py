class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # below is correct , but Memory Limit exceeded
        # dp = {}
        # n = len(s)
        # m = len(t)

        # def helper(i,j):
        #     if i==n:
        #         return m - j
        #     if j==m:
        #         return n - i
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     if s[i]==t[j]:
        #         dp[(i,j)] = helper(i+1,j+1)
        #     else:
        #         dp[(i,j)] = 1+ min(helper(i+1,j+1),min(helper(i+1,j), helper(i,j+1)))
        #     return dp[(i,j)]
        # ans = helper(0,0)
        # return ans == 1


        # Can we skip recursion and bottom up DP altogter? 
        # since its just 1-edit ?
        
       

        m = len(s)
        n = len(t)
        if abs(len(s) - len(t)) > 1 or s==t: return False

        i, j = 0, 0        # pointers to slide over the strings

        # slide i on s & t till they have different character
        while i < m and j < n and s[i] == t[j]:
            i += 1
            j += 1

        # one edit, below should give the answer
        return s[i:] == t[j + 1:] or s[i + 1:] == t[j:] or s[i + 1:] == t[j + 1:]