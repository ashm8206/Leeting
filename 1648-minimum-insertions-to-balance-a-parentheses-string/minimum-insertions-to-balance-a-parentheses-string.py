class Solution:
    def minInsertions(self, s: str) -> int:
        l = len(s)        

        # Method I --> Doesnt work

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
        # print(len(candidates_right)%2, result, len(candidates_right)//2  )
        # return result + len(candidates_right)//2 + (len(candidates_right)%2) * 2
        # return unbalanced_closing + open_brackets_needed for //2 closed_back +
        #  if closed==odd then (1 missing +1 closing)

        result = 0
        right_needed = 0
        for c in s:
            if c == "(":
                right_needed += 2
                if right_needed % 2 == 1:
                    result += 1 # add missing closing bracket
                    right_needed -= 1 # balance off the right odd
            else:
                # Found One Right
                # Remove the 1 right_needed we counted
                right_needed -= 1
                if right_needed < 0:
                    # excess of closing bracket
                    result += 1
                    # Add one opening bracket, and the right needed for it
                    right_needed += 2
        return result + right_needed


        # Method 3 :
        #  replace '))' by "}", add space : O(n)
        #  do simple minimum add 921
        #  return len(openstack)*2 --> closing required  + closed (missing 1 open each)





        


        