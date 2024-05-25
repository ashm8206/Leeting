class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        0, 0, 1,
        1, 1, 2
        2, 1, 3
        """
        heights = collections.defaultdict(list)
        m = len(matrix)
        n = len(matrix[0])
        # global_maxH = -10**9
        # global_minH = 10**9

        # for j in range(n):
        #     col_height = 0
        #     # maxHeight = -10**9
        #     for i  in range(m):
        #         if matrix[i][j]==1:
        #             col_height+=1
        #         else:
        #             # Restart counting height
        #             # while we can change order of columns
        #             #  we cant change the order of rows 
        #             # we must reset the max 1s Counter
        #             # each time we get 0 
        #             col_height = 0
                    

        #     heights[col_height].append(j) # append the column
        #     global_maxH = max(global_maxH,col_height)
        #     global_minH = min(global_minH,col_height)

        
        # print(global_maxH)
        # print(global_minH)
        # print(heights)
        # # {1: [0, 2, 4], 0: [1, 3]})
        # curr_width = 1
        # maxArea = -10**9
        # for height in range(global_maxH, global_minH-1, -1):
        #     # col_list = heights[height]
        #     for _ in range(len(heights[height])):
        #         area = height * curr_width
        #         maxArea = max(maxArea, area)
        #         # print(maxArea)
        #         curr_width += 1
        #     maxArea = max(maxArea, area)
        # return maxArea

        # We need to examine each row. 

        tower = [0]*n # first row for len(COLS)
        maxArea = -10**9
        for i in range(m):

            for j in range(n):
                if matrix[i][j] == 1:
                    tower[j]+=1
                else:
                    tower[j] = 0
                # 1, 0, 2, 0, 4, 2
                # 4, 2, 2, 1, 0, 0
            sorted_tower = sorted(tower, reverse = True)
            # print(sorted_tower)
            base = 1
            for height in sorted_tower: # range(col)
                area = height * base
                maxArea = max(maxArea, area)
                base +=1 
        return maxArea
                 
   