from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # https://www.youtube.com/watch?v=jSto0O4AJbM


        len_s, len_t = len(s), len(t)

        if len_s < len_t:
            return ""

        t_count = Counter(t)
        need = len(t_count)

        s_count = defaultdict(int)
        have = 0 

        L = 0
        n = len(s)
        


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




