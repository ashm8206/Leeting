class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = last_num = cur_num = 0
        operation = '+'
        s += '+'
        for i, c in enumerate(s):

            if c.isdigit():
                cur_num = cur_num * 10 + int(c)

            if c == '(':
                # Append Result, Last_num, operation
                
                stack.append(result)
                stack.append(last_num)
                stack.append(operation)
                # Initialize values to be Inside the '('
                result = last_num = 0
                operation = '+'
            elif c in '+-*/)':
                # print(c, cur_num, last_num, result)
                if operation == '+':
                    
                    result += last_num
                    last_num = cur_num
                    
                elif operation == '-':
                    result += last_num
                    last_num = -cur_num
                elif operation == '*':
                    last_num = last_num * cur_num
                else:
                    last_num = int(last_num / cur_num)
                
                # New Operation or ')'
                if c == ')':
                    # mini result, of all operation in ()
                    # curr_num = result + last_num
                    cur_num = result + last_num

                    # pop the result, last_num and  operation before (
                    operation = stack.pop()
                    last_num = stack.pop()
                    result = stack.pop()
                else:
                    operation = c
                    cur_num = 0
                

        return result + last_num

# Method II - recursion

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