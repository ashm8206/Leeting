class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        0, 0, 1,
        1, 1, 2
        2, 1, 3
        """

        def count_sort(nums):
        
            maxNum = max(nums)
            countArray = [0]* (maxNum + 1)

            for num in nums:
                countArray[num]+=1
            
            
            for i in range(1,len(countArray)): # start from 1
                countArray[i] += countArray[i-1]
            # print(countArray)

            res = [0] * len(nums)
            for num in nums:
                idx = countArray[num] # getCorrect idx
                res[idx-1] = num # idx - 1
                countArray[num]-=1 # Deduct -1 
            return res
    
        m = len(matrix)
        n = len(matrix[0])
        

        # We need to examine each row. 

        tower = [0]*n # first row for len(COLS)
        maxArea = -10**9
        for i in range(m):

            for j in range(n):
                if matrix[i][j] == 1:
                    tower[j]+=1
                else:
                    tower[j] = 0
                    
            sorted_tower = sorted(tower, reverse = True)
            # sorted_tower = count_sort(tower)[::-1]
            # print(sorted_tower,sorted_tower2)
            # Count Sort ? 10*5
       
            base = 1
            for height in sorted_tower: # range(col)
                area = height * base
                maxArea = max(maxArea, area)
                base +=1 
        return maxArea

        # Option 2 # No sort
        # previous_heights = []
        # maxArea = 0
        # for i in range(m):
        #     heights = []
        #     seen = [False]*n
        #     for height, j in previous_heights:
        #         if matrix[i][j]==1: # streak continues for that column
        #             heights.append((height+1, j))
        #             seen[j]=True
                
        #         # streak doesn't continue, conttributes 0, need not add to heights
        #     for j in range(n):
        #         if seen[j]==False and matrix[i][j]==1:
        #             # Renewing streak/ Seeing for the first time
        #             heights.append((1,j))
            
        #     for i in range(len(heights)):
        #         maxArea = max(maxArea, heights[i][0]*(i+1))
        #     previous_heights = heights
        # return maxArea

    
   