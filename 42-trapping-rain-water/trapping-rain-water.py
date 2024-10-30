class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        # How does the calculation work?:
        # At each point min(maxHL_so_Far,maxHR_so_far) - Height[i]/elevation
        
        
        # Brute force O(N^2), O(1) --> TLE

        ans = 0
        n = len(height)

        # for i in range(n):
        #     maxLeft = height[i]
        #     maxRight = height[i]
        #     for j in range(i, -1, -1):
        #         maxLeft = max(maxLeft,height[j])
            
        #     for j in range(i, n):
        #         maxRight = max(maxRight,height[j])
            
        #     ans+= min(maxLeft, maxRight) - height[i]
        
        # return ans
    
        
        # DP Pre calculate maxHL_so_Far, maxHR_so_Far  O(N), O(N)

        maxLeft = [0]*n
        maxRight = [0]*n  

        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]

        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1], height[i])
            
        for j in range(n-2, -1,-1):
       
            maxRight[j] = max(maxRight[j+1], height[j])

        for i in range(n):
            
            ans+= min(maxLeft[i], maxRight[i]) - height[i]
            # print(min(maxLeft[i], maxRight[i]), height[i])
        
        return ans
        
        # Two Ptr O(N), O(1) 

        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans




    

