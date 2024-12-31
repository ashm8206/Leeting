class Solution:

    # https://www.youtube.com/watch?v=3Rw3p9LrgvE
   
    

    def isInterleave(self, s1, s2, s3):
        # Check if sum of sizes of two strings is equal to the size of third string.
        dp = {}

        def is_Interleave(i, j):
        # If result matches with third string
        # And we have reached the end of the all strings, return true.
            if i == len(s1) and j == len(s2):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
        
            if i < len(s1) and s1[i] == s3[i+j] and is_Interleave(i+1,j):
                dp[(i,j)] = True
                # return True
                return  dp[(i,j)] 

            if j < len(s2) and s2[j] == s3[i+j] and is_Interleave(i,j+1):
                dp[(i,j)] = True
                # return True
                return dp[(i,j)]
            
            dp[(i,j)] = False
            # return False
            return dp[(i,j)]
            

        if len(s1) + len(s2) != len(s3):
            return False
        return is_Interleave(0,0)
    