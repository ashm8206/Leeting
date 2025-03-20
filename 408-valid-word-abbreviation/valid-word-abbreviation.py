from collections import deque
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        abrLen = len(abbr)
        wordLen = len(word)
        numberStr = ''
        incre = 0

        j = 0
        i = 0
        
        while i < abrLen and j < wordLen:

            
            if abbr[i]==word[j]:
                i+=1
                j+=1
            else:
                # if num is digit number: try adjust for next round
                # else: mistmatch return False
                if abbr[i].isdigit():
                    num_str = ''
                    while i < abrLen and abbr[i].isdigit():
                        num_str+=abbr[i]
                        i+=1
            
                    if len(num_str) > 0:
                        if num_str[0]=="0":
                            return False
                        j+= int(num_str)
                        num_str = ''
                else:
                    #mistmatch
                    return False
           
        return j == wordLen and i == abrLen
                

            

       
            # if word[word_idx] == abbr[i]:
            #     i+=1
            #     word_idx+=1

            # elif abbr[i]=="0":
                
            #     return False
        
            # elif abbr[i].isdigit():
            #     while i < abrLen and abbr[i].isdigit():
            #         numberStr += abbr[i]
            #         i+=1
            #     if len(numberStr) > 0:
            #         word_idx += int(numberStr)
            #         numberStr = ''
            # else:
            #     return False
            
        return i==abrLen and word_idx == wordLen
            
            
            