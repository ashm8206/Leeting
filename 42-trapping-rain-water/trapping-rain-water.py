class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        l = 0
        r = n-1
        maxLeft = 0
        maxRight = 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft - height[l]
                l+=1
            else:
                # print(maxRight - height[r]) --> -ve
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
                r-=1
        return ans

        #Claude:
'''       
        height = [3, 1, 2, 4]
If we only compared height[l] with height[l+1]:

At index 0 (height=3), we'd compare with index 1 (height=1)
We'd miss the fact that there's a height of 4 later that can actually trap water

The two-pointer approach works because:

        When height[l] < height[r]:

            1. We KNOW that height[r] is tall enough to trap water
            2. So we only need to track maxLeft to calculate trapped water
'''




        # n = len(height)

        
        # ans = 0
        # left_max, right_max = [0]*n, [0]*n

       
        # for i in range(n):
        #     if i > 0:
        #         left_max[i] = max(left_max[i-1], height[i])
        #     else:
        #         left_max[i] = height[i]
        
        # for j in range(n-1, -1, -1):
        #     if j+1 < n :
        #         right_max[j] = max(right_max[j+1], height[j])
        #     else:
        #         right_max[j] = height[j]
        
        # print(left_max, right_max)
        
        # for i in range(1,n-1):
        #     ans+= min(right_max[i], left_max[i]) - height[i]
        
        # return ans



        # How does the calculation work?:
        # At each point min(maxHL_so_Far,maxHR_so_far) - Height[i]/elevation
        
        
       


    

