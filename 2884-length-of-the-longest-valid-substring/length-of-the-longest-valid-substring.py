class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        setF=set(forbidden)
        L = 0

        maxLen=0

        for R in range (len(word)):

            for idx in range (max(L,R-9),R+1): 
                #  Valid left Boundary 
                #  L,  R - winSize + 1
                #  L, R-10+1, R-9 
                #  as each forbidden word is of max len 10

                #  check every L--R+1 if word in forbidden
                # move Left Boundary = Invalid Idx + 1
                if word[idx:R+1] in setF:
                    L=idx+1

            maxLen=max(maxLen,R-L+1)
        return maxLen