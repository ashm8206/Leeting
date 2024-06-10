class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = 0
        n = len(s)
        L = 0
        # if n < 1:
        #     return maxLen 
            # return 0
        
        # L, R  = 0, 0



        hmap = defaultdict(int)
    
        for R in range(n):
            hmap[s[R]] += 1

            while hmap[s[R]] > 1: # chars are repeated
                # shrink window 
                # print(s[L:R+1], s[R])
                hmap[s[L]]-=1
                L = L + 1
                # print(s[L:R+1], s[R])
                # print("--")
                
            
            maxLen = max(maxLen, R-L+1)
        
        return maxLen
        
        # Testcase: 
        # dvdf : Just maintaining set wont work
        #        we want to get MaxLen, hence remove as less as possible.
        #        we can set L = hmap[s[R]] + 1  == lastSeenIndx + 1

        # tmmzuxt , problem is the "t"
        #    1. Since we are not overwriting the hmap
        #    2. We only consider hmap[s[R]] cases  >= L  greater than current left bound
        #    3.  hmap[t] == 0 when we ecounter s[R] @ position 6
        #    We must include pos 6 and not update Left bound L
        #    as we already discarded 't' @ 0 when we set Left Bound to 2 for 'm' case