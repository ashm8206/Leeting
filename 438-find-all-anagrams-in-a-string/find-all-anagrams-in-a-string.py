class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return []

        res = []

        p_count, s_count =  [0] * 26, [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        l = 0
        for r in range(len_s):

            s_count[ord(s[r])-ord('a')]+=1

            # if i >= len_p:
            if r - l+1 > len_p:
                s_count[ord(s[l])-ord('a')]-=1
                l+=1

                # s_count[ord(s[i-len_p])-ord('a')]-=1


                # len(p) len window starts from i(end) - len_p + 1
                #  2, 3, 4, (winLen 3)
                #  1 is not included (index - len_p) to eject


            if p_count == s_count:
                # res.append(i-len_p+1) # start index i-k+1
                res.append(l)
        return res

            