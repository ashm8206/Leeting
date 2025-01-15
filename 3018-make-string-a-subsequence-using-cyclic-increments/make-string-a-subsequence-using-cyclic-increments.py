class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        M = len(str1)
        N = len(str2)

        if M < N:
            return False
        
        i, j = 0, 0

        while i < M and j < N:
            if str1[i]==str2[j] or chr((ord(str1[i]) - ord("a")+1)%26 + ord("a"))==str2[j]:
                j+=1
            
            i+=1 #skip try the next

        
        return j==N