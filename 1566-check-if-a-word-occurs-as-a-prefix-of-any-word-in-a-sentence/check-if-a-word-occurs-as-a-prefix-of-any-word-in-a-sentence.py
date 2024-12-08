class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        words = sentence.split(" ")

        constant = len(searchWord)

        for index, word in enumerate(words, start=1):
            i = 0
            j = 0
            while j < constant and i < len(word):
                if word[i]!=searchWord[j]:
                    break
                else:
                    i+=1
                    j+=1
            if j==constant:
                return index
        return -1
                
                    