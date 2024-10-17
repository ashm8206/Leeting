class Solution:
    def calculate(self, s: str) -> int:

        
        # stack = []
        operation = '+'
        curr_num = ''
        last_num = 0
        result = 0
        s += '+'
        for ch in s:
    
            if ch.isdigit():
                curr_num = curr_num + ch

            if ch in ('+','-','*','/'):
                
                # Excecute the previous operation 1st
                curr_num = int(curr_num)
                if operation == '-':
                    # stack.append(-curr_num)
                    result += last_num
                    last_num = - curr_num

                elif operation =='*':
                    # no check required as expression is valid
                    # op1 = stack.pop()
                    # op2 = curr_num
                    # stack.append(op1*op2)
                    last_num = last_num * curr_num
                elif operation =='/':
                    # op1 = stack.pop()
                    # op2 = curr_num
                    # stack.append(int(op1/op2))
                    last_num = int(last_num / curr_num)
                else:
                    # stack.append(int(curr_num))
                    result += last_num
                    last_num = curr_num
                # update the operation
                # update the curr_number
                curr_num = ''
                operation = ch
        
       
        # while stack:
        #     result += stack.pop()

        return result + last_num
        



        