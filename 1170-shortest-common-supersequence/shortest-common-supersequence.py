class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        A, B = str1, str2
        # You cant use space optmized form if you have a rcosntruct a string
        n = len(A)
        m = len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        
        # Step 2: Reconstruct LCS 
        i, j = n, m
        ans = []
        lcs = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1

            elif dp[i-1][j] >  dp[i][j-1]:
                ans.append(str1[i-1])
                i-=1
            
            else:
                ans.append(str2[j - 1])
                j -= 1
        
        # print(lcs[::-1])
        # Step 3: Reconstruct Shorttestcommon supersequnce
        
    
        # Add remaining characters
        while i > 0:
            ans.append(str1[i - 1])
            i -= 1

        while j > 0:
            ans.append(str2[j - 1])
            j -= 1
        
        # print(ans)
        return "".join(ans[::-1])



            # dp = [['' for j in range(m+1)] for i in range(n+1)]
            
            # for i in range(n - 1, -1, -1):
            #     for j in range(m - 1, -1, -1):

            #         if A[i] == B[j]:
            #             dp[i][j] = A[i] + dp[i + 1][j + 1]
            #         else:
            #             if len(dp[i][j+1]) >= len(dp[i+1][j]):
            #                 dp[i][j] = dp[i][j+1] 
            #             else:
            #                 dp[i][j] = dp[i+1][j]
             
            # return dp[0][0]
  
        # i = j = 0
        # result = []
        
    
        # Iterate through the LCS and build the supersequence
        # for c in lcs(A, B):
        #     # Add characters from A until we find the common character
        #     while A[i] != c:
        #         result.append(A[i])
        #         i += 1
            
        #     # Add characters from B until we find the common character
        #     while B[j] != c:
        #         result.append(B[j])
        #         j += 1
            
        #     # Add the common character and advance both pointers
        #     result.append(c)
        #     i += 1
        #     j += 1
        
        # # Add remaining characters from both strings
        # # print(lcs(A,B))
        # return ''.join(result) + A[i:] + B[j:]



        # abac = LCS + [i:] + [j:]
        # cab =
        