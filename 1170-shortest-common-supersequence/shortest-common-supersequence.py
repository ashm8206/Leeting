class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        A, B = str1, str2
        def lcs(A,B):
            n = len(str1)
            m = len(str2)
            A, B = str1, str2

            dp = [['' for j in range(m+1)] for i in range(n+1)]
            
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):

                    if A[i] == B[j]:
                        dp[i][j] = A[i] + dp[i + 1][j + 1]
                    else:
                        if len(dp[i][j+1]) >= len(dp[i+1][j]):
                            dp[i][j] = dp[i][j+1] 
                        else:
                            dp[i][j] = dp[i+1][j]
             
            return dp[0][0]
  
        i = j = 0
        result = []
        
    
        # Iterate through the LCS and build the supersequence
        for c in lcs(A, B):
            # Add characters from A until we find the common character
            while A[i] != c:
                result.append(A[i])
                i += 1
            
            # Add characters from B until we find the common character
            while B[j] != c:
                result.append(B[j])
                j += 1
            
            # Add the common character and advance both pointers
            result.append(c)
            i += 1
            j += 1
        
        # Add remaining characters from both strings
        # print(lcs(A,B))
        return ''.join(result) + A[i:] + B[j:]