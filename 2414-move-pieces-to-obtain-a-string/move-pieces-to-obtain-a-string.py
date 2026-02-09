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
            
           
            #Wrong
            # if (i >= n and j < n) or (j >= n and i < n):
            #     return False 
            # i== n and j == n: return True is missing : Why wrong?

            # Why better?
            # if one string exhausted, both strings should be exhausted
            if i == n or j == n:
                return (i==n and j == n) # this cond checks that and give F/T accord
            
            if start[i]!=target[j]:
                return False
            
            if start[i]=='L' and j > i: # taregtL <= startL 
                return False
            elif start[i]=='R' and i > j: # startR <= taregtR 
                return False
            
            i+=1 # They can move
            j+=1 # They can move
        return True