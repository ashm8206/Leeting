class Solution:
    def maximumLength(self, s: str) -> int:

        hmap = defaultdict(int)

        n = len(s)
        R = 0
        while R < n:
            curr = s[R]
            while R > 0 and R < n and s[R]==s[R-1]:
                curr+=s[R]
                R+=1
            
            curr_len = len(curr)
            # avoid double counting accc for c at ac boundry
            if curr_len > 1 and hmap[curr[0]] >=1:
                hmap[curr[0]]-=1
            for i in range(curr_len+1):
                if i > 0:
                    hmap[curr[0:i]] += curr_len - (i - 1)
            R+=1

        print(hmap)
        maxLen = -1
        for k, v in hmap.items():
            if v >=3:
                maxLen = max(maxLen, len(k))
        return maxLen
        
        