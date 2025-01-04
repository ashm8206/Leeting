class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        

        first_index = [-1]*26
        last_index = [-1]*26
        n = len(s)
        for i in range(n):
            if first_index[ord(s[i]) - ord("a")]==-1:
                first_index[ord(s[i]) - ord("a")] = i

            if last_index[ord(s[n-i-1]) - ord("a")]==-1:
                last_index[ord(s[n-i-1]) - ord("a")] = n-i-1
        res = 0
        for i in range(26):
            
            if first_index[i]!= last_index[i]:
                # they are distinct occurence, not just 1 occurrence
                res += len(set(s[first_index[i]+1:last_index[i]]))
                # count how many distinct chars between these two indices?
        return res
            
        # treat J as the Middle character
        # iterate every char in 26 chars to find first_idx[char] < charMid < last_idx[char]
        # unique_3_len = 0
        # seen = set()
        # for j, ch in enumerate(s):
        #     for i in range(26):
        #         l_r_char = chr(i + ord("a"))
                
        #         if (l_r_char,ch) not in seen:
        #             if 0 <= first_index[i]  < j < last_index[i]:
        #                 # print(l_r_char,ch,l_r_char)
        #                 unique_3_len+=1
        #                 seen.add((l_r_char,ch))
        # return unique_3_len


        # letters = set(s)
        # ans = 0
        
        # for letter in letters:
        #     i, j = s.index(letter), s.rindex(letter) # O(n)
        #     between = set()
            
        #     for k in range(i + 1, j): #O(n)
        #         between.add(s[k])
            
        #     ans += len(between)

        # return ans # O(n**2) but can be seprated in 2 Loops.

