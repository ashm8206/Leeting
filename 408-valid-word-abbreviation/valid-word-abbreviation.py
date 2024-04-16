from collections import deque
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    #    a  p  p  l, e
    #    0, 1, 2, 3, 4
    # Double digit char has to be the complete range
    # i + (dd + 1)? == nextDogit

        abrLen = len(abbr)
        wordLen = len(word)
        numberStr = ''

        word_idx = 0
        i = 0
        while i < abrLen and word_idx < wordLen:
       
            if word[word_idx] == abbr[i]:
                i+=1
                word_idx+=1

            elif abbr[i]=="0":
                
                return False
        
            elif abbr[i].isdigit():
                while i < abrLen and abbr[i].isdigit():
                    numberStr += abbr[i]
                    i+=1
                if len(numberStr) > 0:
                    word_idx += int(numberStr)
                    numberStr = ''
            else:
                return False
            
        return i==abrLen and word_idx == wordLen
            
            
            