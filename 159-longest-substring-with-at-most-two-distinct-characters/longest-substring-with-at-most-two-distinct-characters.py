class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        L = 0
        maxLen = 0

        k = 2 # maxDistinct
        hmap = defaultdict(int)

        for R in range(len(s)):
            hmap[s[R]] = R

            if len(hmap) > k:
                # print(hmap, L)
                del_idx = min(hmap.values()) # left most value
                # print(del_idx)
                del hmap[s[del_idx]]
                L = del_idx +1

                # doesn't work incase of this : abaccc
                #  you need to get min_idx

            maxLen = max(maxLen, R-L+1)

        return maxLen