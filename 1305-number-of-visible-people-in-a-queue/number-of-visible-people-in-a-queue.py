class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = [0]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] < heights[i]:
                # 6 can see NGE 8
                # 5, can see the NGE 11
                # That is all they can see
                res[stack.pop()]+=1

            if stack:
                # this element is greater than heights[i]
                # therefore this element can see heights[i]
                res[stack[-1]]+=1
            
            # before adding height

            stack.append(i)

        return res

