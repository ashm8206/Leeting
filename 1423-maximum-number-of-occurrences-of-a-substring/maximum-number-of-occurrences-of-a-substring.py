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

        maxFreq = 0
        hmap  = defaultdict(int)

        for i in range(len(s)-minSize + 1):

            subtr = s[i:i+minSize]

            if len(set(subtr)) <= maxLetters:
                hmap[subtr]+=1
                maxFreq = max(maxFreq, hmap[subtr])

        return maxFreq
