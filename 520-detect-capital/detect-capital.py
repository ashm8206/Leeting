class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n = len(word)
        capital_count = 0
        loc = -1

        for i in range(n):
            if word[i] >='A' and word[i] <='Z' :
                capital_count+=1
                loc = i
        
        if capital_count == len(word) or capital_count ==0 or loc==0:
            return True
        return False