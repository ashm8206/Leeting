class Solution:
    def numDecodings(self, s: str) -> int:
        # Recursion
        # @lru_cache(maxsize=None)

        n = len(s)
        dp = {}
        def helper(index):
            if index in dp:
                return dp[index]
            if index == n:
                return 1
                # if we reach n from index+1

            if s[index]=="0":
                # check any element for leading zeros
                return 0
            
            if index == n-1:
                # you reached here from two digit element
                return 1
            
            ans = helper(index+1) # all single number counted except 0
            if index + 1 < n and (s[index]=="1" or s[index] == "2" and s[index+1] in "0123456"):
                ans+= helper(index+2)
            dp[index] = ans
            return ans

        return helper(0)

        
        # DP Tabluation

        # n = len(s)
        # dp = [0 for _ in range(n+1)]
       
       
        # # if s[0]!="0"
        
        # # Ways to decode empty string = 1 
        # dp[0] = 1

        # # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # # '0' doesn't have a single digit decode.

        # dp[1] = 0 if s[0] == "0" else 1

        # for i in range(2, n+1):
            
        #     if s[i-1]!="0":
        #         dp[i] += dp[i-1] 
            
        #     two_digit = int(s[i - 2 : i]) 
        #     if two_digit >= 10 and two_digit<=26:
                
        #             dp[i]+= dp[i - 2]
                
        # # print(dp)
        # return dp[n]
        

        
