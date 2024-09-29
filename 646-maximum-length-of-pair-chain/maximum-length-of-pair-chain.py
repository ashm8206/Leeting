import bisect
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[0])
      
        lastEnd = pairs[0][1]
        n = len(pairs)
        ans = 1
        for start, end in pairs:
            if start > lastEnd:
                ans += 1
                lastEnd = end
            else:
                lastEnd = min(lastEnd, end)
            
        return ans