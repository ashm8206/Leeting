from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        source = Counter([ x.lower() for x in licensePlate if x.isalpha()])

        maxValue = 10**5
        ans = ""
        for word in words:
            if source <= Counter(word):
                if len(word) < maxValue:
                    maxValue = len(word)
                    ans = word


        return ans