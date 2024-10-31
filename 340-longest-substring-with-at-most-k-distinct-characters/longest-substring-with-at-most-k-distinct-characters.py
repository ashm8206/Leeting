class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        L = 0
        maxLen = 0
        hmap = defaultdict(int)

        for R in range(len(s)):

            # if len(set(s[L:R+1])) > k:
            #     # print(s[L:R+1])
            #     L = L+1

            # alternative  O(n) to create set every time

            hmap[s[R]] +=1

            while len(hmap) > k:
                hmap[s[L]]-=1
                if hmap[s[L]]==0:
                    del hmap[s[L]]
                L = L + 1
            
            maxLen = max(maxLen, R-L+1)

        return maxLen