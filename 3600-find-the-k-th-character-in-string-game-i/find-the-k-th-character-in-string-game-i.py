import math
class Solution:
    def kthCharacter(self, k: int) -> str:
        result = math.ceil(math.log(k, 2))
        start = "a"

        def ops(inp):
            stack = list(inp)
            len_st = len(stack)
            for i in range(len_st):
                nxt_chr = chr(ord(stack[i])+1)
                if stack[i]=="z":
                    nxt_chr = "a"
                stack.append(nxt_chr)
            return "".join(stack)

        for i in range(result):
            start = ops(start)
        return start[k-1]