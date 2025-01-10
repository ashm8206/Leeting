class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        # dp = {}
        m = len(s)
        n = len(t)
        # @lru_cache(maxsize = None)
        # def helper(i,j):

        #     if i==m:
        #         return n-j

        #     if j==n:
        #         return m-i

            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        
        #     if s[i]==t[j]:
        #         dp[(i,j)] = helper(i+1,j+1)

        #     else:
        #         insert =  helper(i,j+1)
        #         delete =  helper(i+1,j)
        #         replace = helper(i+1,j+1)
        #         # print(insert, delete, replace)
        #         dp[(i,j)] = 1 +  min(replace,min(insert,delete))

        #     return dp[(i,j)]
       
        # return helper(0,0) == 1

        # m = len(s)
        # n = len(t)

        # # Bottom Up
        # dp = [[float("inf")for j in range(n+1)]for i in range(m+1)]

        # for i in range(m+1):
        #     dp[i][n] = m - i
        
        # for j in range(n+1):
        #     dp[m][j] = n - j
        
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):

        #         if s[i]==t[j]:
        #             dp[i][j] = dp[i+1][j+1]

        #         else:
                
        #             insert =  dp[i][j+1]
        #             delete =  dp[i+1][j]
        #             replace =  dp[i+1][j+1]
        #             dp[i][j] = 1 +  min(replace,min(insert,delete))
        # # print(dp)
        # return dp[0][0] == 1


        if abs(len(s)-len(t))>=2 or t==s:
            return False
        
        i,j=0,0        
        edited=False
        
        while i < len(s) and j <len(t):
            if s[i]!=t[j]:
                if not edited: #this is the first time a character is found different
                   edited =True
                else:
                    #found more than 1 character different return False
                    return False
                if len(s)>=len(t):
                    i+=1
                if len(s)<=len(t):
                    j+=1
                    
            else:
                i+=1
                j+=1
                
        return True