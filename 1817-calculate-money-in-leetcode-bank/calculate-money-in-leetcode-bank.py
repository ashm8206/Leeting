class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        prevMon = 0

        for i in range(n):
            if i%7==0:
                ans+= prevMon + 1
                prevMon = prevMon + 1 # currMon becomes prevMon
            else:
                ans+= prevMon + (i%7)
            # print(ans)
        return ans
        
    

        # 0, 1, 2, 3, 4, 5, 6 7