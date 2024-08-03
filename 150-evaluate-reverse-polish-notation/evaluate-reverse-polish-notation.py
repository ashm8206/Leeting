class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token not in {"+","-","*","/"}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if token == "+":
                    ans = op1 + op2
                elif token == "-":
                    ans = op1 - op2
                elif token == '/':
                    ans = int(op1 / op2)
                else:
                    ans = op1 * op2
                
                stack.append(ans)
                
        return stack[0]
                