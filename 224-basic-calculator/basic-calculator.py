class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        curr_num = 0
        last_num = 0 
        result = 0

        prev_op = "+"
        s+= "+" # evaluate result when we see next op
        for ch in digit:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == "(":
                stack.append(result) # op1
                stack.append(last_num) # op2
                stack.append(prev_op) #operation

            elif ch in ")+-/*":
                
                if prev_op == "-":
                    result+= last_num
                    last_num = -curr_num
                   
                elif prev_op == "+":
                    result+= last_num
                    last_num = curr_num
                elif prev_op == "*":
                   
                    last_num *= curr_num
                else:
                    last_num = last_num / int(curr_num)

                if ch ==")":
                    curr_num = result + last_num
                    prev_op = stack.pop()
                    last_num = stack.pop()
                    result = stack.pop()
                else:
                    prev_op = c
                    curr_num = 0
        return result + last_num
                    















        # stack = []

        # result = 0 # why do we need this ?
        # last_num = 0 # why do we need this ?

        # curr_num = 0 
        # prev_oper = "+" # why do we need this ?
        # s+="+"

        # for c in s:
        #     # if c == " ":
        #     #     continue
            
        #     if c.isdigit():
        #         curr_num = curr_num * 10 + int(c)
            
        #     elif c == "(":
        #         stack.append(result)
        #         stack.append(last_num) # why do we need last number?
        #         stack.append(prev_oper)

        #         result = 0  
        #         last_num = 0
        #         prev_oper = "+"
            
        #     elif c in ")+-*/":

        #         if c == "-":
        #             result+=last_num
        #             last_num = -curr_num

        #         elif c== "+":
        #             result+=last_num
        #             last_num = curr_num
        #         elif c=="*":

        #             last_num *= curr_num
        #         else:
        #             last_num = last_num / int(c) # why dont we add to result ?


        #         if c == ")":  # why is this separate from the previous elif
        #             cur_num = result + last_num
        #             prev_operation = stack.pop()
        #             last_num = stack.pop()
        #             result = stack.pop()
        #         else:
        #             cur_num = 0
        #             prev_oper = c
        
        # return result + last_num
                
                






    def calculate(self, s: str) -> int:
        stack = []

        result = 0
        last_num = cur_num = 0

        prev_operation = '+'
        s += '+' 
        # we evaluate last operation after we see the next operation
        #  last vhar might be a ')' or number each will be handled sepratly
        # hence we need to add another '+' to explicitly add answers

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            

            if c == '(':
                stack.append(result)
                stack.append(last_num)
                stack.append(prev_operation)

                # initialize the result, last_name and operation

                result = last_num = 0
                prev_operation = '+'
                # the curr_num will be the result from inside the '(  )' 
                
            elif c in '+-*/)':
                # we have encountered a new operation, 
                #  But we must evaluate the previous operation first
                # This is what the if/elif is about

               
                if prev_operation == '-':
                    result += last_num
                    last_num = -cur_num
                elif prev_operation == '*':
                    # we wait before adding these 
                    # We just evalute based on curr_num == op2
                    # last_num = op1 
                    #  Store result in op1 the next time we see an operator (+ or -)
                    # we dont add these to theresult just yet, as there could be another string of operations '*' or '/'following these
                    last_num *= cur_num
                elif prev_operation =='/':
                    # operation is '/'

                    last_num = int(last_num / cur_num)
                    #  Int makes sure the answer tends towards 0
                else:
                    result += last_num
                    last_num = cur_num

                if c == ')':
                    #  yes now we have curr_num == Result + Last_num  whatever was in ()
                    #  We pop the last operation before '('
                    #  We pop result, last_num and previous operation

                    #  The result after ')' will be evaluated when next operation is seen'
                    cur_num = result + last_num
                    prev_operation = stack.pop()
                    last_num = stack.pop()
                    result = stack.pop()
                else:
                    #  we are  havent seen  ')'
                    # as in Basic cal II
                    # 
                    # operation = curr_operation
                    # result curr_num = 0
                    prev_operation = c
                    cur_num = 0

        # last number is the absolute last number seen, 
        # we need to add it to the result
        return result + last_num



# Method II - Recursion

# class Solution:
#     def calculate(self, s: str) -> int:
#         self.index = 0
#         return self.evaluate(s + '+')

#     def evaluate(self, s: str) -> int:
#         result = last_num = cur_num = 0
#         pre_sign = '+'
#         while self.index < len(s):
#             if s[self.index].isdigit():
#                 cur_num = cur_num * 10 + int(s[self.index])
#             elif s[self.index] == '(':
#                 self.index += 1
#                 cur_num = self.evaluate(s)
#             elif s[self.index] in '+-*/)':
#                 if pre_sign == '+':
#                     result += last_num
#                     last_num = cur_num
#                 elif pre_sign == '-':
#                     result += last_num
#                     last_num = -cur_num
#                 elif pre_sign == '*':
#                     last_num *= cur_num
#                 else:
#                     last_num = int(last_num / cur_num)
#                 if s[self.index] == ')':
#                     break
#                 pre_sign = s[self.index]
#                 cur_num = 0
#             self.index += 1
#         return result + last_num