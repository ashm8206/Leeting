class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Brute force
        # Compare Pair wise : O n^2 and O(1)

        n = len(height)
        max_area = -10**10
        # for i in range(n):
        #     for j in range(i+1,n):
        #         # area  = width * min(heights[l], heights[r])
        #         area = (j-i) * min(height[i],height[j])
        #         max_area = max(max_area,area)
        # return max_area

        # Greedy
        #  Maximize the width * min (Max L, Max R)

        L = 0
        R = n-1

        maxHeightL = height[L]
        maxHeightR = height[R]

        while L < R:
            # maxHeightL = max(height[L], maxHeightL)
            # maxHeightR = max(height[R], maxHeightR)

            # area = (R - L) * min(maxHeightL, maxHeightR)
            area = (R - L) * min(height[L], height[R])
            max_area = max(area,max_area)

            if height[L] <= height[R]:
                L+=1
            
            else:
                R-=1
        return max_area



