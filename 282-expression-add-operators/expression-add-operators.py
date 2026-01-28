class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        s = num
        n = len(num)
        # @lru_cache()
        def backtrack(i, slate, currSum, prevNum):
            if i == n:
                if currSum == target:
                    ans.append("".join(slate[:]))
                return
            # 123
            #1, 12, 123
            for j in range(i, n):
                if j > i and s[i] == '0': 
                    break  # Skip leading zero number
                    
                num = int(s[i:j + 1])
                if i == 0:
                    backtrack(j + 1, slate + [str(num)], currSum + num, num) 
                else:
                    backtrack(j + 1, slate + ["+", str(num)], currSum + num, num)
                    backtrack(j + 1, slate + ["-",  str(num)], currSum - num, -num)
                    backtrack(j + 1, slate + ["*", str(num)], currSum - prevNum + prevNum * num, prevNum * num)  
                    # resultSoFar - prevNum + prevNum * num
                    # und previous and apply the higher precedence

        ans = []
        backtrack(0, [], 0, 0)
        return ans