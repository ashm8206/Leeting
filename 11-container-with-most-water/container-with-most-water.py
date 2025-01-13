class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            if height[l] < height[r]:
                maxArea = max(maxArea, (r-l) * min(height[l],height[r]))
                l+=1
         
            else:
                maxArea = max(maxArea, (r-l) * min(height[l],height[r]))
                r-=1
                
        return maxArea
        # [1,8,6,2,5, 4, 8, 3,7]
    #    7*7
        
        # Brute force
        # Compare Pair wise : O n^2 and O(1)

        # n = len(height)
        # max_area = -10**10
        # for i in range(n):
        #     for j in range(i+1,n):
        #         # area  = width * min(heights[l], heights[r])
        #         area = (j-i) * min(height[i],height[j])
        #         max_area = max(max_area,area)
        # return max_area

        # Greedy
        #  Maximize the width * min (Max L, Max R)
        #  If we try to move the pointer at the longer line inwards, 
        #          we won't gain any increase in area, 
        #          since it is limited by the shorter line.
        # However, if we move the shorter line, inward
        #       we might make an increase in area, despite the reduction in width

        L = 0
        R = n-1

        while L < R:
        
            area = (R - L) * min(height[L], height[R])
            max_area = max(area,max_area)

            if height[L] <= height[R]:
                L+=1
            
            else:
                R-=1
        return max_area



