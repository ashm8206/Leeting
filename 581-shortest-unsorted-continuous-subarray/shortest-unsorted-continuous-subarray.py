class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:


        # [2,6,4,8,9,10,15]
          

        sorted_arr = sorted(nums)
        start = -1
        end = -1
        for i, (x, y) in enumerate(zip(nums,sorted_arr)):
            if x!=y:
                if start==-1:
                    start = i
                else:
                    end = i + 1
                # print(x, y)
        # print(start, end)
        return end - start
            
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
    

        for j in range(n-1, -1, -1):
            small = min(nums[j], small)
            if nums[j] > small:
                left = j
        
        return right - left + 1
        
       
        # 2,6,4,5,14,9, 11,12,15
        # 2,4 5,6, 9,11,12,14, 15
    

       
        
