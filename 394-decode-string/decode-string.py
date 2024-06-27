class Solution:
    def decodeString(self, s: str) -> str:
        # https://www.youtube.com/watch?v=qB0zZpBJlh8
        
        # O(N) linear time

        stack = []
        for char in s:

            if char==']':
                # encoutered a closing bracket
                substr = ''
                while stack and stack[-1]!='[':
                    substr = stack.pop() + substr
                    # append at the start, so result is not reveresed

                stack.pop() # remove opening bracket

                num = ''
                while stack and stack[-1].isdigit():
                    num  = stack.pop() + num
                    """ for char in res:
                            num = num*10 + int(char)
                    since we process is reverse for stack, above code wont work !
                    """
                stack.append(substr*int(num))
            
            else:
                  stack.append(char)
        return "".join(stack)



        # Method II - Two Stacks

        # stack = []
        # counterStack = []

        # for char in s:
            
        #     if char.isdigit():

        #         counterStack.append(char)

        #     elif char == "]":
        #         res = ''
        #         while stack and stack[-1]!="[":
        #             res = stack.pop() + res
        #         stack.pop()  # "remove [ "
        #         count = counterStack.pop()
        #         stack.append(res*count)
        #     else: # [ or char
        #         stack.append(char)
        #         if char == '[':
        #             res = ''
        #             while counterStack and not isinstance(counterStack[-1],int):
        #                 res = counterStack.pop() + res
        #             counterStack.append(int(res))
        # return "".join(stack)
                    





