class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        result = last_num = cur_num = 0
        pre_sign = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            if c == '(':
                stack.append(result)
                stack.append(last_num)
                stack.append(pre_sign)
                result = last_num = 0
                pre_sign = '+'
            elif c in '+-*/)':
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
                if c == ')':
                    cur_num = result + last_num
                    pre_sign = stack.pop()
                    last_num = stack.pop()
                    result = stack.pop()
                else:
                    pre_sign = c
                    cur_num = 0
        return result + last_num