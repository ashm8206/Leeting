from collections import defaultdict
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        s = str(n)
        lenS = len(s)

        res = []
        countMap = Counter(s)
        def helper(slate):
            if len(slate) == lenS:
                res.append(int("".join(slate[:])))
                return
            
            for val in countMap.keys() :
                if countMap[val] <= 0 :
                    continue
                slate.append(val)
                countMap[val]-=1
                helper(slate)
                slate.pop()
                countMap[val]+=1
        
        helper([])
        res.sort()
        idx = res.index(n) + 1
        
        return  -1  if idx >= len(res) or res[idx] >= 2**31 else res[idx]