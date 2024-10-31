class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s2 < len_s1:
            return False


        s1_count, s2_count =  [0] * 26, [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

       
        #  for s2 to contain permutation of s1
        #  we check s1 len chunks of s2, where the freq[chunk] == freq[s1]
        
        for i in range(len_s2):

            s2_count[ord(s2[i])-ord('a')]+=1

            if i >= len_s1: # i >= k, then remove  i-k from window
                s2_count[ord(s2[i-len_s1])-ord('a')]-=1


            if s1_count == s2_count:
                return True
        return False