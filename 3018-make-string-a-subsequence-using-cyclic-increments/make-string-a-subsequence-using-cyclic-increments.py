class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """

        M = len(str1)
        N = len(str2)

        if M < N:
          return False

        i = 0
        j = 0

        while i < M and j < N:

            next = ord(str1[i])-ord("a") + 1

            if str1[i]!=str2[j] and chr(ord("a")+(next%26))!= str2[j]:
                i+=1
            else: 
                i+=1
                j+=1
                
        return j==N

           

        