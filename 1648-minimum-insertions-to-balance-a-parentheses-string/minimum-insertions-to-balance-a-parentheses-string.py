class Solution:
    def minInsertions(self, s: str) -> int:
        l = len(s)        

        # result = 0        
        # candidates_right = []
        # for i in range(l-1, -1, -1):
        #     if s[i] == ")":
        #         candidates_right.append(")")
        #     else:
        #         if len(candidates_right) == 0:
        #             result += 2
        #         elif len(candidates_right) == 1:
        #             candidates_right.pop()
        #             result += 1
        #         else:
        #             candidates_right.pop()
        #             candidates_right.pop()
        # return result + len(candidates_right)//2 + (len(candidates_right)%2) * 2

        result = 0
        right_needed = 0
        for c in s:
            if c == "(":
                right_needed += 2
                if right_needed % 2 == 1:
                    result += 1
                    right_needed -= 1
            else:
                right_needed -= 1
                if right_needed < 0:
                    result += 1
                    right_needed += 2
        return result + right_needed





        


        