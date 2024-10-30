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
        
        # maxLVal = 0 
        # maxRVal = 0 

        for i in range(1,n):
            # maxLVal = max(maxLVal,height[i])
            # maxLeft[i] = maxLVal
            maxLeft[i] = max(maxLeft[i-1], height[i])
            
        for j in range(n-2, -1,-1):
            # maxRVal = max(maxRVal,height[j])
            # maxRight[j] = maxRVal
            maxRight[j] = max(maxRight[j+1], height[j])

        for i in range(n):
            
            ans+= min(maxLeft[i], maxRight[i]) - height[i]
            # print(min(maxLeft[i], maxRight[i]), height[i])
        
        return ans
        
        # Two Ptr O(N), O(1) 

        # left = 0
        # right = n - 1     

        # maxLeft = height[left]
        # maxRight = height[right]

        # while left < right:
        #     if maxLeft < maxRight:
        #         left+=1 # cant store at edges, so increment first

        #         maxLeft = max(height[left],maxLeft) 
        #         ans+= maxLeft - height[left]
        #     else:
        #         right-=1
        #         maxRight = max(height[right],maxRight) 
        #         ans+= maxRight - height[right]
             
        # return ans




    

