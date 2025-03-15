class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        n = len(pref)

        for word in words:
            i = 0
            j = 0
            m = len(word)
            
            if m < n:
                continue 
                # continue to next_word
            while i < n and j < m:
                if pref[i]!=word[j]:
                    break 
                else:
                    i+=1
                    j+=1
            if i == n:
                count+=1
        return count
                