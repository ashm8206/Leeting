class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)


        def alternateStr(start, n):
            result = ''
            for i in range(n):
                result += str(start)
                start = abs(start - 1)
            return result
                
        str1, diff1 = alternateStr(0,n), 0
        str2, diff2 = alternateStr(1,n), 0
        
        for x, y, z in zip(str1,str2, s):
            if x!=z:
                diff1+=1
            if y!=z:
                diff2+=1

        return min(diff1,diff2)