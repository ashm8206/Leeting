class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m = len(str1)
        n = len(str2)

        dp = [ [0 for j in range(n+1)]for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0

        for j in range(n+1):
            dp[0][j] = 0

        
        for i in range(1,m+1):
            for j in range(1,n+1):

                
                if str1[i-1]==str2[j-1]:
                    dp[i][j]= 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

       
        i = m
        j = n
        seq = []
        lcs = []

        while  i > 0 and j >  0:
           

            if str1[i-1]==str2[j-1]:
                seq.append(str1[i-1])
                lcs.append(str1[i-1])
                i-=1
                j-=1
            
            
            elif dp[i-1][j] > dp[i][j-1]:
                seq.append(str1[i-1])
                i-=1
            else:
                seq.append(str2[j-1])
                j-=1
    
        # print("".join(reversed(lcs)))
      
        while i > 0:
            seq.append(str1[i-1])
            # print(str1[i-1])
            i-=1
        while j > 0:
            seq.append(str2[j-1])
            # print(str2[j-1])
            j-=1

        return  ''.join(reversed(seq))
        # return dp[m][n]