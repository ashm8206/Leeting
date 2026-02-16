class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

        slow = 0
        fast = 0
        while fast < n:
            if s[fast] == " " or fast == n - 1:
                
                j = fast - 1 if s[fast] == " " else fast
                
                while slow < j:
                    s[slow], s[j] = s[j], s[slow]
                    slow +=1
                    j -=1
                fast = fast + 1 # skip the " "
                slow = fast
                
            else:
                fast += 1
                
        

        
            
                
