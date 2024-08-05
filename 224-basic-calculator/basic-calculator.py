# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = deque()
#         result = last_num = cur_num = 0
#         pre_sign = '+'
#         s += '+'
#         for c in s:
#             if c.isdigit():
#                 cur_num = cur_num * 10 + int(c)
#             if c == '(':
#                 stack.append(result)
#                 stack.append(last_num)
#                 stack.append(pre_sign)
#                 result = last_num = 0
#                 pre_sign = '+'
#             elif c in '+-*/)':
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
#                 if c == ')':
#                     cur_num = result + last_num
#                     pre_sign = stack.pop()
#                     last_num = stack.pop()
#                     result = stack.pop()
#                 else:
#                     pre_sign = c
#                     cur_num = 0
#         return result + last_num
class Solution:
    def calculate(self, s: str) -> int:
        self.index = 0
        return self.evaluate(s + '+')

    def evaluate(self, s: str) -> int:
        result = last_num = cur_num = 0
        pre_sign = '+'
        while self.index < len(s):
            if s[self.index].isdigit():
                cur_num = cur_num * 10 + int(s[self.index])
            elif s[self.index] == '(':
                self.index += 1
                cur_num = self.evaluate(s)
            elif s[self.index] in '+-*/)':
                if pre_sign == '+':
                    result += last_num
                    last_num = cur_num
                elif pre_sign == '-':
                    result += last_num
                    last_num = -cur_num
                elif pre_sign == '*':
                    last_num *= cur_num
                else:
                    last_num = int(last_num / cur_num)
                if s[self.index] == ')':
                    break
                pre_sign = s[self.index]
                cur_num = 0
            self.index += 1
        return result + last_num