class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I': 1, 'V': 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        

        # LVIII 58   54 LIV
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            if i+1 < n and hmap[s[i]] < hmap[s[i+1]]:
                ans-= hmap[s[i]]
            else:
                ans+= hmap[s[i]]
            i+=1
        return ans
      

    



        # ans = 0
        # n = len(s)

        # i = 0
        # # while i < n:
        # #     if i + 1 < len(s) and hmap[s[i]] < hmap[s[i + 1]]:
        # #         #  Cant use direct objects as X --> X and C --> C
        # #         ans += hmap[s[i + 1]] - hmap[s[i]]
        # #         i+=2
        # #     else:
        # #         ans+= hmap[s[i]]
        # #         i+=1
        
        # # return ans

        # total = hmap.get(s[-1])
        # for i in reversed(range(len(s) - 1)):
        #     if hmap[s[i]] < hmap[s[i + 1]]:
        #         total -= hmap[s[i]]
        #     else:
        #         total += hmap[s[i]]
        # return total

        # n = len(s)
        # res = 0
        # i = n-1
        # while i >= 0:
            
        #     if (i-1) >= 0 and hmap[s[i-1]] < hmap[s[i]]:
        #         res+=  hmap[s[i]] - hmap[s[i-1]]
        #         i-=1
        #     else:
        #         res+=hmap[s[i]]
        #     i-=1
        #     # print(res)
        # return res
        pass