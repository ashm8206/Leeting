class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        L = 0
        maxLen = 0

        k = 2 # maxDistinct
        hmap = defaultdict(int)

        for R in range(len(s)):
            hmap[s[R]] += 1

            # if len(hmap) > k: 
            #     # print(hmap, L)
            #     del_idx = min(hmap.values()) # left most value o(n)
            #     # print(del_idx)
            #     del hmap[s[del_idx]]
            #     L = del_idx +1
            while len(hmap) > k:
                hmap[s[L]]-=1
                if hmap[s[L]]==0:
                    del hmap[s[L]]
                L = L + 1

                # doesn't work incase of this : abaccc
                #  you need to get min_idx

            maxLen = max(maxLen, R-L+1)

        return maxLen