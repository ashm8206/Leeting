class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        memo = {}
        n = len(s)
        def helper(index):

            if index < n and s[index]=="0":
                return 0

            if index==n or index==n-1:
                return 1

            if index in memo:
                return memo[index]
            
            ans = helper(index+1)
            if 1<= int(s[index:index+2]) <= 26:
                ans+= helper(index+2)

            memo[index] = ans
            return ans 
        return helper(0)

            
        # memo = {}
        # n = len(s)
        # def helper(index):

        #     if index in memo:
        #         return memo[index]
            
        #     if index < n and s[index]=="0":
        #         return 0
            
        #     if index == n or index == n - 1: 
        #         # n-1 --> 1 way only
        #         return 1
        
        #     ans = helper(index+1)

        #     if int(s[index:index+2])<=26:
        #         ans += helper(index+2)
        #     memo[index] = ans
        #     return ans
        # return helper(0)
        
            
            

        
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
        

        
