class Solution:
    def calculate(self, s: str) -> int:

        
        stack = []
        operation = '+'
        curr_num = ''

        for i, ch in enumerate(s):
    
            if ch.isdigit():
                curr_num = curr_num + ch

            if ch in ('+','-','*','/') or i == len(s)-1 :
                
                # Excecute the previous operation 1st
                curr_num = int(curr_num)
                if operation == '-':
                    stack.append(-curr_num)
                elif operation =='*':
                    # no check required as expression is valid
                    op1 = stack.pop()
                    op2 = curr_num
                    stack.append(op1*op2)
                elif operation =='/':
                    op1 = stack.pop()
                    op2 = curr_num
                    stack.append(int(op1/op2))
                else:
                    stack.append(int(curr_num))
                # update the operation
                # update the curr_number
                curr_num = ''
                operation = ch
            

        return sum(stack) 
        



        