class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])

        res = [[0 for _ in range(m)] for _ in range(n)]

        
        for i in range(n):
            stack = []
            for j in range(m):
                equal = False
                while stack and heights[i][stack[-1]] <= heights[i][j]:
                    if heights[i][j] == heights[i][stack[-1]]:
                        equal = True
                    res[i][stack.pop()]+=1

                # if stack:
                if stack and not equal:
                    res[i][stack[-1]]+=1

                stack.append(j)

        # [4,2,1,1,3]
        #  4  2 1 1 3
        #  2. 2 1 1
        for j in range(m):
            stack = []
            for i in range(n):
                equal = False
                while stack and heights[stack[-1]][j] <= heights[i][j]:
                    if heights[i][j] == heights[stack[-1]][j]:
                        equal = True
                    res[stack.pop()][j]+=1

                if stack and not equal:
                    res[stack[-1]][j]+=1
                stack.append(i)
        
        return res 

        