class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # this is not about full string being valid..
        # this is about substring!

        n = len(s)
        max_len = 0
        stack = [-1]   # base index for calculating length - Invalid idex
        
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)        # new starting point after invalid )
                else:
                    # valid substring ends at i, starts after the previous unmatched
                    max_len = max(max_len, i - stack[-1])
        
        
        stack = [n]
        for i in range(n-1, -1, -1):
            if s[i] == ')':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)        # new starting point after invalid )
                else:
                    # valid substring ends at i, starts after the previous unmatched
                    max_len = max(max_len, stack[-1] - i)
        
        return max_len

        # curr_count = 0
        # max_count = 0
        # stack = []
        # last_invalid = -1  
        # n = len(s)


        # for i in range(n):
        #     if s[i] == "(":
        #         stack.append(i)          # store index, not character
        #     else:
        #         if not stack:
        #             last_invalid = i
        #             curr_count = 0
        #             continue
        #         stack.pop()
        #         if stack:
        #             curr_count = i - stack[-1]   # distance to last unmatched '('
        #         else:
                     
        #             curr_count = i - last_invalid  # ← was curr_count += 2
        #         max_count = max(max_count, curr_count)


        # stack = []
        # curr_count = 0
        # last_invalid = n
        # for i in range(n-1, -1, -1):
        #     if s[i] == ")":
        #         stack.append(i)          # store index, not character
        #     else:
        #         if not stack:
        #             last_invalid = i
        #             curr_count = 0
        #             continue
        #         stack.pop()
        #         if stack:
        #             curr_count = stack[-1] - i   # distance to last unmatched '('
        #         else:
        #             curr_count = last_invalid - i             
        #             # stack empty = still in same valid run
        #         max_count = max(max_count, curr_count)
        # return max_count

        
        # left, right, maxLen = 0, 0 ,0
        # n = len(s)
        # for i in range(n):
        #     if s[i]=="(":
        #         left+=1
        #     else:
        #         right+=1
        #     if left == right:
        #         maxLen = max(maxLen, 2*right)
        #     elif right > left:
        #         left = right = 0

        # left, right = 0, 0
        # for j in range(n-1,-1,-1):
        #     if s[j]=="(":
        #         left+=1
        #     else:
        #         right+=1
        #     if left == right:
        #         maxLen = max(maxLen, 2*right)
        #     elif left > right:
        #         left = right = 0
        # return maxLen
                
        