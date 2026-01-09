from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Strivers video!
        
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1 
            # setting total to 0
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

            # at each position,
            # we find the minPos counting backwards that satisfies our condition that all chars must be present

            # from this minPos, we can append as many chars backwards
            # to exnted the array
            # this etendingg backwards is  MinPosIdx + 1 = Arrays

        return total
        
    #     n = len(s)
    #     hmap = defaultdict(int)
    #     total = 
    #     for r in range(n):
    #         hmap[s[r]]+=1

    #         while self.has_all_chars(hmap):
    #             total += n - r # all substring from curr window to left are valid
    #             hmap[s[l]]-=1 # shrink window check if thats valid too
    #             l+=1
    #     return total 
    
    # def has_all_chars(self, hmap):
    #      # Check if we have at least one of each character
    #     return all(val > 0 for key, val in hmap.items())
            
            


