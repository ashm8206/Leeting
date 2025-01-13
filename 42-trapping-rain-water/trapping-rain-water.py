class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        l = 0
        r = n-1
        ans = 0
        maxLeft = 0
        maxRight = 0
        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                ans+= maxLeft - height[l] 
                l+=1
            else:
                maxRight = max(maxRight, height[r])
                ans+= maxRight- height[r] 
                r-=1
        return ans




        n = len(height)

        
        ans = 0
        left_max, right_max = [0]*n, [0]*n

       
        for i in range(n):
            if i > 0:
                left_max[i] = max(left_max[i-1], height[i])
            else:
                left_max[i] = height[i]
        
        for j in range(n-1, -1, -1):
            if j+1 < n :
                right_max[j] = max(right_max[j+1], height[j])
            else:
                right_max[j] = height[j]
        
        print(left_max, right_max)
        
        for i in range(1,n-1):
            ans+= min(right_max[i], left_max[i]) - height[i]
        
        return ans



        # How does the calculation work?:
        # At each point min(maxHL_so_Far,maxHR_so_far) - Height[i]/elevation
        
        
        # Brute force O(N^2), O(1) --> TLE

        ans = 0
        n = len(height)

        
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




    

