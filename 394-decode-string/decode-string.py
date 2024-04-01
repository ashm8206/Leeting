class Solution:
    def decodeString(self, s: str) -> str:
        # https://www.youtube.com/watch?v=qB0zZpBJlh8

        stack = []
        for char in s:

            if char!=']':
                stack.append(char)
            
            else:
                # encoutered a closing bracket
                substr = ''
                while stack[-1]!='[':
                    substr = stack.pop() + substr
                    # append at the start, so result is not reveresed

                stack.pop() # remove opening
                k = ''
                while stack and stack[-1].isdigit():
                    k  = stack.pop() + k 
                    """ for char in res:
                            k = k*10 + int(char)
                        since we process is reverse, above code wont work !
                    """

                stack.append(substr*int(k))
        return "".join(stack)

                



