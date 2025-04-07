class Solution:
    # https://leetcode.com/problems/special-binary-string/solutions/155621/logical-thinking-with-clear-code/
    def makeLargestSpecial(self, s: str) -> str:
        
        sublist = []
        bal = 0
        l = 0
        for r, ch in enumerate(s):
            if ch == "1":
                bal+=1
            else:
                bal -=1
            if bal == 0:
                sublist.append("1" + self.makeLargestSpecial(s[l+1:r])+"0")           
                # l... r
                # 1[l+1....r)0 
                # construct deeper parenthis
                # so once valid parenthis found, 
                # nest them in each other
                l = r + 1
        sublist.sort(reverse = True)
        return "".join(sublist)
