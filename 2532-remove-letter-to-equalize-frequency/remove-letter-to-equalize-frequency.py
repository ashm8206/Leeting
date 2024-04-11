from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        
    
        freqArray = [0]*26

        for char in word:
            freqArray[ord(char)-ord('a')]+=1
    
        # is_possible = False

        for i in range(26):
            if freqArray[i]>0:
                freqArray[i]-=1
                setVal = set(freqArray)
                
                if 0 in setVal:
                    setVal.remove(0)

                if len(setVal)==1: # account for 0 
                    return True
                freqArray[i]+=1
        return False

      

        
            

        

       
    

       


