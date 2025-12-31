class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = 0
        j = 0
        n = len(start)

        

        while i < n or j < n:
            while i < n and start[i]=='_':
                i+=1

            while j < n and target[j]=='_':
                j+=1
            
            # if one string exhausted, both strings should be exhausted
            if i == n or j == n:
                return (i==n and j == n)
            
            if start[i]!=target[j]:
                return False
            
            if start[i]=='L' and i < j:
                return False
            elif start[i]=='R' and j < i: # start[i]=='R', and 
                return False
            
            i+=1 # They can move
            j+=1 # They can move
        return True