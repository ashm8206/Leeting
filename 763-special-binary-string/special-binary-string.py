class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s
        bal = 0
        anchor = 0
        mountains = []
        for i, x in enumerate(s):
            if x == "1":
                bal+=1
            else:
                bal-=1
            if bal == 0:
                mountains.append("1{}0".format(
                    self.makeLargestSpecial(s[anchor+1: i])))
                anchor = i + 1
        mountains.sort(reverse = True)
        return "".join(mountains)
