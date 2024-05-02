class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        
        wordIdx = -1
      
        for i, char in enumerate(word):
            if char==ch:
                wordIdx = i
                break
        
        if wordIdx!=-1:
            return word[wordIdx::-1] + word[wordIdx+1:]
        return word
            
            
            