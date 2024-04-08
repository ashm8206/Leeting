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

        # maxLeft = [0]*n
        # maxRight = [0]*n  

        # maxLVal = 0 
        # maxRVal = 0 

        # for i in range(n):
        #     maxLVal = max(maxLVal,height[i])
        #     maxLeft[i] = maxLVal
            
        # for j in range(n-1, -1,-1):
        #     maxRVal = max(maxRVal,height[j])
        #     maxRight[j] = maxRVal
        
        # for i in range(n):
            
        #     ans+= min(maxLeft[i], maxRight[i]) - height[i]
        #     print(min(maxLeft[i], maxRight[i]), height[i])
        
        # return ans
        
        # Two Ptr O(N), O(1) 

        left = 0
        right = n - 1     

        maxLeft = height[left]
        maxRight = height[right]

        while left <= right:
            if maxLeft <= maxRight:
                
                maxLeft = max(height[left],maxLeft) 
                ans+= maxLeft - height[left]
                # print(ans,maxLeft - height[left])
                left+=1
                

            else:
                
                maxRight = max(height[right],maxRight) 
                ans+= maxRight - height[right]
                # print(ans,maxRight - height[right])
                right-=1
             
        return ans




    

