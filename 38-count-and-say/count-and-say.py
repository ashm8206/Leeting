class Solution:
    def countAndSay(self, n: int) -> str:

        # https://leetcode.com/problems/count-and-say/solutions/6356766/best-solution-for-arrays-in-c-python-and-java-100-working/
        if n==1: 
            return "1"

        s = "1"
        for _ in range(n-1):
            ans = []
            i = 0
            slen = len(s)
            while i < slen:
                count = 1
                while i+1 < slen and s[i+1]==s[i]:
                    count+=1
                    i+=1
                ans.append(str(count)+s[i])
                i+=1
            s = "".join(ans)
        return s 

        # # Recursive
        # def rle(s):
        #     count = 1
        #     ret = []
        #     n = len(s)-1
        #     for i in range(0,n+1):
        #         if i<n and s[i] == s[i+1]:
        #             count += 1
        #         else:
        #             ret.append(str(count))
        #             ret.append(s[i])
        #             count = 1
        #     return "".join(ret) 
        
        # if n == 1:
        #     return "1"
        # return rle(self.countAndSay(n-1)) 

        
        