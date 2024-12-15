class Solution:
    def smallestSubsequence(self, s: str) -> str:
        S = s
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)

        #cbacdcbc
        # correct acdb, incorrect w/o i<last[stack[-1]] : abc

        #i < last[stack[-1]]:
        # only remove the greater element if there are more occurrence of the topmost 
        #  from i .....N
        # if not retain  he greater element