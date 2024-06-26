class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # S = s
        # last = {c: i for i, c in enumerate(S)}
        # stack = []
        # for i, c in enumerate(S):
        #     if c in stack: continue
        #     while stack and stack[-1] > c and i < last[stack[-1]]:
        #         stack.pop()
        #     stack.append(c)
        # return "".join(stack)

        stack = []

        last_occurence = {c:i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            if c in stack:
                continue
            while stack and stack[-1] >= c and  i < last_occurence[stack[-1]]:
                # we got a c and stack contains [abd]
                # technically we should remove abd but only if  i < lastOccurence[topOfStack]
                stack.pop()
            
            stack.append(c)
            print(stack)

        return "".join(stack)


