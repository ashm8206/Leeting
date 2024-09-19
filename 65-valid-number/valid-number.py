class Solution:
    def isNumber(self, s: str) -> bool:

        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit
        
        #Method I
        # seen_decimal = False
        # # can't have multiple '.'
        # seen_exponent = False
        # # can't have multiple 'eExponent'

        # seen_digit = False

        # n = len(s)
        # for i in range(n-1,-1,-1):
        #     if s[i].isdigit():
        #         seen_digit = True
        #     elif s[i]=='.':
        #         if i < n-1 and not seen_digit or seen_decimal:
        #             return False
        #         seen_decimal = True

        #     elif s[i] in ['+', '-']:
        #         if i==n-1:
        #             return False
                
        #         if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
        #             return False

        #         if i < n-2 and ((s[i+1] == '.' and not s[i+2].isdigit())):
        #             return False

        #         if i < n-1 and not s[i+1].isdigit():
        #             return False
                
                

        #     elif s[i] in ['e','E']:
        #         if seen_decimal or seen_exponent:
        #             return False
        #         if i > 0 and (not s[0:i].isdigit() or not s[i+1:].isdigit()) or i==0:
        #             return False
        #         seen_exponent = True
        #     else:
        #         return False
        # return seen_digit # seen 1 or more digit
                

        # return True

        # .
        # .D
        #D.
        #D.D

        # +, - -> digit 
        # +D
        # +D

        # e/E # has to follow a Digit, can't just start like this
        # De(+|-)D
        # DE(+|-) D
