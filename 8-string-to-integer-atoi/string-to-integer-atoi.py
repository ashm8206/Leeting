class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        sign = 1
        sign_seen = False
        for i, ch in enumerate(s):
            if not ch.isdigit():
                if ch in {"+","-"} and not sign_seen and len(res)==0:
                    sign_seen = True
                    sign = int(ch+"1") 
                elif ch==" " and len(res)==0 and not sign_seen:
                    continue
                else:
                    break
            else:
                res.append(ch)
                
        if len(res) > 0:
            ans = sign*int("".join(res)) 
            if ans < -2**31:
                return -2**31
            elif ans > 2**31 - 1:
                return 2**31-1
            else:
                return ans
        else:
            return 0