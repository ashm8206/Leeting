class Solution:
    def minimumScore(self, s: str, t: str) -> int:
       
        # suffix[i] stores the position in t that matches with s[i:] suffix part
        # initialized with -1 for all positions
        suffix = [-1] * len(s)
        
        # First pass: build suffix array going from right to left
        right = len(t) - 1  # pointer for string t
        for i in reversed(range(len(s))):
            if 0 <= right and s[i] == t[right]:
                right -= 1  # found a match, move t pointer left
            suffix[i] = right  
            # store position in t that we need to match
        
        # Initial answer: characters left unmatched after first pass
        ans = right + 1
        # its importnat to do this as j = -1 for matching the first character
        
        # Second pass: go left to right
        left = 0  # reset t pointer to start
        for i, ch in enumerate(s):
            # Try removing characters between current j and suffix[i]
            # This represents removing characters between current match and next suffix match
            ans = min(ans, max(0, suffix[i] - left + 1))
            
            if left < len(t) and s[i] == t[left]:
                left += 1  # found a match, move t pointer right
                
        # Return minimum of current answer and remaining unmatched characters
        return min(ans, len(t) - left)
        
        '''In essence, this final comparison ensures we take the minimum between:

The best score we found by removing characters in the middle of t
Simply removing all remaining unmatched characters at the end of t

This is crucial because sometimes it's better to just remove all remaining unmatched characters rather than trying to find a window of characters to remove in the middle of the string.'''
        
    
