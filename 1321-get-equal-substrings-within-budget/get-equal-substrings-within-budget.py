class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0
        n = len(s)

        maxLen = 0
        curr_cost = 0
        for r in range(n):
            if s[r]!=t[r]:
                curr_cost += abs(ord(s[r]) - ord(t[r]))
            
            
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            
            maxLen = max(maxLen, r-l+1)
        return maxLen

    