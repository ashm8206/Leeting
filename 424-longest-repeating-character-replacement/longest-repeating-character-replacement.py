class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        maxLen = 1

        L = 0
        # R = 0
        # R for variable is in the while Loop

        hmap = defaultdict(int)
        maxFreq = 0

        for R in range(len(s)):
            hmap[s[R]]+=1
            maxFreq = max(maxFreq, hmap[s[R]])

            # this could also be a max(O[26]) each time, but its not optimal

            if R - L + 1 - maxFreq  > k:
            # Invalid window
            # Radjust the window
            #  windowLen - MaxCharFreq =  # of replacements allowed
            #  if they are greater than K, window is Invalid
                hmap[s[L]] = hmap.get(s[L],0) - 1
                L+=1
            
            maxLen = max(maxLen, R-L+1)
        return maxLen
           

        