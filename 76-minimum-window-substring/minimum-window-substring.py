from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # https://www.youtube.com/watch?v=jSto0O4AJbM


        len_s, len_t = len(s), len(t)

        if len_s < len_t:
            return ""

        t_count = Counter(t)
        have = 0 
        need = len(t_count)
        L = 0
        n = len(s)
        s_count = defaultdict(int)


        min_len = 10**9
        min_win = ''
        for R in range(n):
            s_count[s[R]]+=1

            if s_count[s[R]] == t_count[s[R]]:
                have+=1 

            while have == need:
                if R-L+1 < min_len:
                    min_len = R-L+1
                    min_win = s[L:R+1]
                
                s_count[s[L]]-=1
                
                if s[L] in t_count and s_count[s[L]]< t_count[s[L]]:
                    have-=1
                     # >= is ok, less is not

                L+=1
            
        return min_win





        # len_s , len_t = len(s), len(t)

        # if len_s < len_t:
        #     return ""

        # ans = ""

        # t_count =  defaultdict(int)
        
        # for char in t:
        #     t_count[char]+=1

        
        # minLen = 10**10
        
        

        # L = 0
        # have = 0
        # need = len(t_count)

        # s_count = defaultdict(int)

        # for R in range(len_s): #(O(len(s)))

        #     s_count[s[R]]+=1
        #     if s_count[s[R]] == t_count[s[R]]:
        #         # increase only when counts match, not when count is greater
        #         # greater doesnt help us get minmuz window substring

        #         have+=1
            
        #     while have == need: # O(len(t)) --> Total
               
        #         if R-L+1 < minLen:
        #             minLen = R-L+1 
        #             ans = s[L:R+1]
                
        #         # Try to minimize it further, # Shrink Window
        #         s_count[s[L]]-=1
            
        #         if s[L] in t_count and s_count[s[L]] < t_count[s[L]]:
        #             have-=1
        #             # will cause to break
                    
        #         L = L+1

        # return ans





