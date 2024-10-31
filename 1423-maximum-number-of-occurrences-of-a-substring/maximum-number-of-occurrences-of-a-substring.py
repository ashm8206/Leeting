class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        A key thing to note is that though substrings can have lengths anywhere from minSize to maxSize, 
        we are interested in finding the maximum number of occurrences, 
        and typically substrings with smaller lengths will have higher chances of repeated occurrence. 
        The solution should return the maximum frequency of any such substring found in s that follows the above rules.
        """


        """We find all substrings of size minSize and keep their counts.
           In the end we return maxFreq
        """

        # maxFreq = 0
        # hmap  = defaultdict(int)

        # for i in range(len(s)-minSize + 1):

        #     subtr = s[i:i+minSize]

        #     if len(set(subtr)) <= maxLetters:
        #         hmap[subtr]+=1
        #         maxFreq = max(maxFreq, hmap[subtr])

        # return maxFreq
        
        maxFreq = 0
        l = 0
        n = len(s)
        hmap = defaultdict(int)
        freqSubstr = defaultdict(int)
        for r in range(n):
            hmap[s[r]]+=1

            if r-l+1 > minSize:
                hmap[s[l]]-=1
                if hmap[s[l]]==0:
                    del hmap[s[l]]
                l += 1
            
            if r-l+1 == minSize and len(hmap)<= maxLetters:
                subtr = s[l:r+1]
                freqSubstr[subtr]+=1
                maxFreq = max(maxFreq,  freqSubstr[subtr])
        return maxFreq