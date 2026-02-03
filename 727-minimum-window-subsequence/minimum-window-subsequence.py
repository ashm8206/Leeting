class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)

        #  initilize dp with large value
        # dp table store len of smallest subseqeunce
        dp = [[float("inf")] * (m + 1) for i in range(n + 1)]

        dp[0][0] = 0 # what is len of subsequnce "" and "" ?  its 0

        last_index = 0

        length = float("inf")
        for i in range(1,  n+1):
            dp[i][0] = 0 #"a", "" common subsequnce len is 0
            for j in range(1, m+1):
                if  s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # skip this i
                    # same in IsSubsequence problem

                    #  But we STILL add 1 because 
                    # `s1[i-1]` is **inside the window**!
                    dp[i][j] = 1 +  dp[i-1][j]

            if dp[i][m] < length: #"s1[:i] and all of s2"
                length = dp[i][m]
                last_index = i
            
        return "" if length == float("inf") else s1[last_index - length:last_index]