class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        

        # n = len(s)
        # res = 0
        # seen_pairs = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if s[k]==s[i] and s[i]+s[j] +s[k] not in seen_pairs:

        #                 seen_pairs.add(s[i]+s[j] +s[k])
        #                 res+=1
        # return res


        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans
