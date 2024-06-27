class Solution:
    def decodeString(self, s: str) -> str:
        # https://www.youtube.com/watch?v=qB0zZpBJlh8
        
        # O(N) linear time

        # stack = []
        # for char in s:

        #     if char!=']':
        #         stack.append(char)
            
        #     else:
        #         # encoutered a closing bracket
        #         substr = ''
        #         while stack[-1]!='[':
        #             substr = stack.pop() + substr
        #             # append at the start, so result is not reveresed

        #         stack.pop() # remove opening
        #         k = ''
        #         while stack and stack[-1].isdigit():
        #             k  = stack.pop() + k 
        #             """ for char in res:
        #                     k = k*10 + int(char)
        #                 since we process is reverse, above code wont work !
        #             """

        #         stack.append(substr*int(k))
        # return "".join(stack)

        # stack = []

        # for char in s:
            
        #     if char==']':
        #         res = ''
        #         while stack and stack[-1]!='[':
        #             res = stack.pop() + res
        #         # Pop '[' 
        #         num = 0
        #         k = 0
        #         stack.pop()
        #         ## Another alternative
        #         # Can be done in the same way as stack
        #         while stack and stack[-1].isdigit():
        #             num = int(stack.pop())*10**k + num
        #             k+=1
        #         res = res * int(num)
        #         stack.append(res)
        #     else:
        #         stack.append(char)
        # return "".join(stack)


        # Method II

        stack = []
        counterStack = []

        for char in s:
            
            if char.isdigit():
                # save as Str
                counterStack.append(char)

            elif char == "]":
                res = ''
                while stack and stack[-1]!="[":
                    res = stack.pop() + res
                stack.pop()  # "remove [ "

                count = counterStack.pop()
                stack.append(res*count)
            else: # [ or char
                stack.append(char)
                if char == '[':
                    res = ''
                    while counterStack and not isinstance(counterStack[-1],int):
                        res = counterStack.pop() + res
                    counterStack.append(int(res))
        return "".join(stack)
                    





