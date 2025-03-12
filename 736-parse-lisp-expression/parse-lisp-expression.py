class Solution:
    def evaluate(self, expression: str) -> int:
        # def evaluate(expression):
        

        def eval(exp, parent):
            if exp[0] != '(':
                # just a number or a symbol
                if exp[0].isdigit() or exp[0] == '-':
                    return int(exp)
                return parent[exp]
            
            # create a new scope, add all the previous values to it
            map = parent.copy()
            tokens = parse(exp[6:-1] if exp[1] == 'm' else exp[5:-1])
            
            if exp.startswith("(a"):  # add
                return eval(tokens[0], map) + eval(tokens[1], map)
            elif exp.startswith("(m"):  # mult
                return eval(tokens[0], map) * eval(tokens[1], map)
            else:  # let
                for i in range(0, len(tokens) - 2, 2):
                    map[tokens[i]] = eval(tokens[i + 1], map)
                return eval(tokens[-1], map)

        def parse(str):
            # separate the values between two parentheses
            res = []
            par = 0
            sb = []
            for c in str:
                if c == '(':
                    par += 1
                if c == ')':
                    par -= 1
                if par == 0 and c == ' ':
                    res.append(''.join(sb))
                    sb = []
                else:
                    sb.append(c)
            if sb:
                res.append(''.join(sb))
            return res
        
        return eval(expression, {})

