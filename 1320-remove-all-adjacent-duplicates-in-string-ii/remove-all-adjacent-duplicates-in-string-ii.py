class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        counterStack = []

        n = len(s)

        for i in range(n):
            
            if not stack or s[i]!=stack[-1]:
                counterStack.append(1)

            elif s[i]==stack[-1]:
                counterStack[-1]+=1
            
            stack.append(s[i])
            # print(counterStack,stack)
            
            if counterStack[-1]==k:
                while counterStack[-1] and stack:
                    stack.pop()
                    counterStack[-1]-=1
                counterStack.pop()
                # print(counterStack,stack)
            
        return "".join(stack)
            
       
            

                


        