class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #  Bucket Sort for Small range number [0,2]
        # Time Complexity O(n), Space : O(1) --> hmap is constant space, doesnt grow with input
        #  It will be in-place, cuz yo over write the Array based on Hmap

        
        hmap = {0:0, 1:0, 2:0}

        for num in nums:
            hmap[num]+=1
        
        index = 0
        for key in range(0,3):
            while hmap[key]:
                nums[index] = key
                hmap[key]-=1
                index+=1
        return nums


