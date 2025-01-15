from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):

        # NeetCode https://www.youtube.com/watch?v=gqXU1UyA8pk&t=409s

        maxLen = 0
        n = len(s)
        hmap = defaultdict(int)
        maxCommon = 0
        l = 0

        for r in range(n):
            hmap[s[r]] = hmap[s[r]] +  1
            maxCommon = max(maxCommon, hmap[s[r]])

            while (r - l + 1) - maxCommon > k:
                hmap[s[l]]-=1
                l+=1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
            maxLen = max(maxLen, r-l+1) # valid window
        return maxLen
            






       
        # maxLen = 0
        # L = 0
        # hmap = defaultdict(int)

        # maxCount = 0
        # for R, c in enumerate(s):
        #     hmap[c] += 1
        #     maxCount = max(maxCount, hmap[c]) # max count in each window, keep  it updated

        #     while R - L + 1 - maxCount > k: # the number of replacements is greater than allowed replacements
        #         # Remove Left side string
        #         hmap[s[L]] -= 1
        #         L += 1
            
        #     maxLen = max(maxLen, R - L + 1)
        # return maxLen
    
    '''
    https://leetcode.com/problems/longest-repeating-character-replacement/discuss/358879/Java-Solution-Explained-and-Easy-to-Understand-for-Interviews
    The question asks to find the longest substring that contains the same characters. It also says that we can change k characters to make a substring longer and valid.

Ex:

"ABAB" k = 1
Here we know that we can change 1 character to make a substring that is a valid answer
AKA: a substring with all the same characters.

So a valid substring answer would be s.substring(0, 3) -> "ABA" because with can replace 1 character.

Another answer could be "BAB".

Using the sliding window technique, we set up pointers left = 0 and right = 0
We know that a our current window / substring is valid when the number of characters that need to be replaced is <= k.

Lets take the example below to understand it better:
Ex:

"AABABCC" k = 2
left = 0
right = 4 inclusive
This is example above shows a valid substring window because we have enough k changes to change the B's to A's and match the rest of the string.

"AABAB" with 2 changes is valid

We will need to know how many letters in our substring that we need to replace.
To find out the lettersToReplace = (end - start + 1) - mostFreqLetter;
Pretty much you take the size of the window minus the most freq letter that is in the current window.

Now that we know how many characters that need to be replaced in our window, we can deduce that if lettersToReplace > k than the window is invalid and we decrease the window size from the left.
    '''
    
    '''
    https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation  
    
    LOOK FOR CHRISLZM's COMMENT
    In case anyone is confused by this solution, here's another way of explaining it:

end-start+1 = size of the current window
maxCount = largest count of a single, unique character in the current window

The main equation is: end-start+1-maxCount

When end-start+1-maxCount == 0, then then the window is filled with only one character
When end-start+1-maxCount > 0, then we have characters in the window that are NOT the character that occurs the most. 

end-start+1-maxCount = # of characters that are NOT the most common character

 Example: For a window "xxxyz", end-start+1-maxCount would equal 2. (maxCount is 3 and there are 2 characters here, "y" and "z" that are not "x" in the window.)

We are allowed to have at most k replacements in the window, so when end-start+1-maxCount > k, then there are more characters in the window than we can replace, and we need to shrink the window.

If we have window with "xxxy" and k = 1, that's fine because end-start+1-maxCount = 1, which is not > k. maxLength gets updated to 4.

But if we then find a "z" after, like "xxxyz", then we need to shrink the window because now end-start+1-maxCount = 2, and 2 > 1. The window becomes "xxyz".

maxCount may be invalid at some points, but this doesn't matter, because it was valid earlier in the string, and all that matters is finding the max window that occurred anywhere in the string. Additionally, it will expand if and only if enough repeating characters appear in the window to make it expand. So whenever it expands, it's a valid expansion.

Hope that helps.

P.S. Yes, as several other people mentioned already, the while should be replaced with if. The time complexity is exactly the same, because the while-loop only runs once anyway.
    '''