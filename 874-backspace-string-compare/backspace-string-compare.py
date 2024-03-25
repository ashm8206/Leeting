class Solution:
    #Two pointer O(1)

    # def process_string(self, string):
    #     k = 0
    #     for i in range(len(string)):
    #         if string[i]!='#':
    #             string[k]=string[i]
    #             k+=1
    #         else:
    #             k = max(k-1,0)
    #     return k
    # def getFinalString(self, text:str) -> str:
    # #     res = []
    # #     for ch in text:
    # #         if res and ch == "#":
    # #             res.pop()
    # #         elif ch!='#':
    # #             res.append(ch)

    # #     return "".join(res)
    def backspaceCompare(self, s: str, t: str) -> bool:
    #     s, t = list(s), list(t)
        
    #     k = self.process_string(s)
    #     p = self.process_string(t)

    #     if k!=p:
    #         return False

        
    #     for i in range(k):
    #         if s[i] != t[i]:
    #             return False
        
    #     return True

    #     # print(self.getFinalString(s))
    #     # print(self.getFinalString(t))

    #     # return self.getFinalString(s)==self.getFinalString(t)
        def F(string):
            cnt = 0
            n = len(string)
            for i in range(n-1,-1,-1):
                char = string[i] # O(1) Space
                if char =='#':
                    cnt+=1
                elif cnt:
                    cnt-=1
                else:
                    yield char
            
        for x, y in itertools.zip_longest(F(s),F(t)):

            """
            The itertools module provides a function called zip_longest that works similarly to the zip function but with a key difference: it doesn't stop at the shortest iterable. 
            Instead, it fills in 'missing' values with a specified fillvalue
            """

            if x!=y:
                return False
        return True
