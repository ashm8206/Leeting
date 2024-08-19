class Solution:
    def numDecodings(self, s: str) -> int:
        # Recursion
        # @lru_cache(maxsize=None)
        # def helper(s, index):


        #     if index == len(s):
                
        #         return 1

        #     if s[index] == "0":
        #         # catches last element!=0 
        #         # and other element, if they are leading zeros
        #         return 0


        #     if index == len(s)-1:
        #         # when idx+2

        #         # Len(S) -2 +1 = Len(S)-1
        #         # Stopping at above idx, ensures Window-Size - 1 element ahead of it remains to make the complete window 

        #         # we only come here if the last element is !=0 

        #         return 1
            

        #     ans = helper(s, index+1)
        #     if int(s[index: index+2])<=26:
        #         ans+= helper(s, index+2)
            
        #     return ans
        # return helper(s, 0)

        # DP Tabluation

        n = len(s)
        dp = [0 for _ in range(n+1)]
       
       
        # if s[0]!="0"
        
        # Ways to decode empty string = 1 
        dp[0] = 1

        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.

        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n+1):
            
            if s[i-1]!="0":
                dp[i] += dp[i-1] 
            
            two_digit = int(s[i - 2 : i]) 
            if two_digit >= 10 and two_digit<=26:
                
                    dp[i]+= dp[i - 2]
                
        # print(dp)
        return dp[n]
        

        
