from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        s = Counter(s)
        t = Counter(t)
        
        for tc, cnt in s.items():
            if tc not in t.keys():
                ans+= cnt
            else:
                if s[tc] > t[tc]:
                    ans += s[tc] - t[tc]
        return ans