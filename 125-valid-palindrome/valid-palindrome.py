class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s)-1

        while start <= end:
            while start < end and not s[start].isalnum():
                start+=1
            while start < end and not s[end].isalnum():
                end-=1
            
            print(s[start],s[end])

            if s[start].lower()!=s[end].lower():
                return False
            else:
                #matched, move both 
                start+=1
                end-=1
        return True

        # Assumption 
        # Single Character no matter if it is an Alphanum, 
        # is always considered palindrome