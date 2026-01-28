class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        memo = {}
        n = len(s)
        MOD = 10**9 + 7
        def helper(index):

            if index==n:
                return 1

            if index in memo:
                return memo[index]
            
            if s[index] == "0":
                return 0
            
            count = 0

            for end in range(index, n):
                curr_num = int(s[index:end+1])
                if curr_num > k or curr_num < 1:
                    break
                
                count += helper(end+1)
            
            memo[index]=count%MOD
            return memo[index]
        return helper(0)

