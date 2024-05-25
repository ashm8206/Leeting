class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        0, 0, 1,
        1, 1, 2
        2, 1, 3
        """
    
        m = len(matrix)
        n = len(matrix[0])
        

        # We need to examine each row. 

        # tower = [0]*n # first row for len(COLS)
        # maxArea = -10**9
        # for i in range(m):

        #     for j in range(n):
        #         if matrix[i][j] == 1:
        #             tower[j]+=1
        #         else:
        #             tower[j] = 0
                    
        #     sorted_tower = sorted(tower, reverse = True)
       
        #     base = 1
        #     for height in sorted_tower: # range(col)
        #         area = height * base
        #         maxArea = max(maxArea, area)
        #         base +=1 
        # return maxArea
        previous_heights = []
        maxArea = 0
        for i in range(m):
            heights = []
            seen = [False]*n
            for height, j in previous_heights:
                if matrix[i][j]==1: # streak continues for that column
                    heights.append((height+1, j))
                    seen[j]=True
                
                # streak doesn't continue, conttributes 0, need not add to heights
            for j in range(n):
                if seen[j]==False and matrix[i][j]==1:
                    # Renewing streak/ Seeing for the first time
                    heights.append((1,j))
            
            for i in range(len(heights)):
                maxArea = max(maxArea, heights[i][0]*(i+1))
            previous_heights = heights
        return maxArea

                 
   