class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        n, m = len(s), len(t)
        i = 0
        j = 0

        def helper(i, j):

            if i==n:
                # matched all of s
                return True
            
            if j==m:
                # t < s, so s cant be a susbsequence
                # OR j reached end, without matching
                return False

            if s[i]==t[j]:
                i+=1
            j+=1
            '''
            if s[i]==t[j]:
                i+=1
                j+=1 # match
            else:
                isSubequence(i, j+1) 
                # here we dont have the option to skip "i": isSubequence(i+1, j) 
                # We need to match every i, with any j that matches
            '''

            return helper(i, j)
        return helper(0,0)