class Solution:
    def calculate(self, s: str) -> int:

        
        # stack = []
        pre_operation = '+'
        curr_num = 0
        last_num = 0
        result = 0
        s += '+'
        for ch in s:
    
            if ch.isdigit():
                curr_num = curr_num * 10 +  int(ch)

            elif ch in ('+','-','*','/'):
                
                # curr_num = int(curr_num)

                if pre_operation == '-':
                    # stack.append(-curr_num)
                    result += last_num
                    last_num = - curr_num

                elif pre_operation =='*':
                    # no check required as expression is valid
                    # op1 = stack.pop()
                    # op2 = curr_num
                    # stack.append(op1*op2)
                    last_num = last_num * curr_num
                elif pre_operation =='/':
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
                curr_num = 0
                pre_operation = ch

        return result + last_num
        



        