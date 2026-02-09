class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:


        # [2,6,4,8,9,10,15]
        # [2,6,8,9,10,4,15]
        
        # Sorted Method 

        # sorted_arr = sorted(nums)
        # start = -1
        # end = -1
        # for i, (x, y) in enumerate(zip(nums,sorted_arr)):
        #     if x!=y:
        #         if start==-1:
        #             start = i
        #         else:
        #             end = i + 1
        #         # print(x, y)
        # # print(start, end)
        # return end - start
            
        n = len(nums)

        #r-l+1
        right = -1
        left = 0


        big = float("-inf")
        small = float("inf")
        for i in range(n):
            big = max(nums[i], big)
            if nums[i] < big:
                right = i
            
    
        # L - R --> you are tracking for Left ptr
        # find the biggest number, 
        # if nums[i]  < big num
        #       ptr1 = i 

        # R - L --> tracking for left ptrs
        # find the smallest number, 
        # if nums[j]  >  small
        #       ptr2 = j

        for j in range(n-1, -1, -1):
            small = min(nums[j], small)
            if nums[j] > small:
                left = j
                # print(left)
        
        return right - left + 1
        
       
        # 2,6,4,5,14,9, 11,12,15
        # 2,4 5,6, 9,11,12,14, 15
    

       
        
