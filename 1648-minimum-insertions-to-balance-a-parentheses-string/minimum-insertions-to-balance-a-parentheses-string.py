class Solution:
    def minInsertions(self, s: str) -> int:
             

        stack = []
        result = 0
        i = 0
        s += "$"
        n = len(s)  
        while i < n-1:
            if s[i] =='(':
                stack.append('(')
                i+=1
            else:
                if s[i]==')' and s[i+1]==')':
                    # 2 closing
                    if stack:
                        stack.pop()
                        # balance_stack
                    else:
                        # stack empty
                        result+=1
                    i+=2
                elif s[i]==')' and s[i+1]!=')':
                    if stack:
                        stack.pop()
                        result+=1
                        # one ')' added
                    else:
                        result+=2
                        # one '(' added
                        # one ')' added
                    i+=1
        return result + len(stack)*2
        



        # return unbalanced_closing + open_brackets_needed for //2 closed_back +
        #  if closed==odd then (1 missing +1 closing)

        # result = 0
        # right_needed = 0
        # for c in s:
        #     if c == "(":
        #         right_needed += 2
        #         if right_needed % 2 == 1:
        #             result += 1 # add missing closing bracket
        #             right_needed -= 1 # balance off the right odd
        #     else:
        #         # Found One Right
        #         # Remove the 1 right_needed we counted
        #         right_needed -= 1
        #         if right_needed < 0:
        #             # excess of closing bracket
        #             result += 1
        #             # Add one opening bracket, and the right needed for it
        #             right_needed += 2
        # return result + right_needed


        # Method 3 :
        #  replace '))' by "}", add space : O(n)
        #  do simple minimum add 921
        #  return len(openstack)*2 --> closing required  + closed (missing 1 open each)





        


        