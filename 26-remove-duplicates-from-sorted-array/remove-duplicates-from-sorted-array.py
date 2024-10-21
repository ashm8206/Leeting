class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # insertIndex = 1 
        # Next insert index of unique number
        # Index of 0 remains
        # even if element at index 0 is duplicated, it is the first time we see it
        # we have to store [1st occurence] at insertIndex
        # "?" if it is a first occurence?  by checking with its left adj
        #      incase its not equal, we found the first unique occurence
        #       we place it at insertIndex 
        #.       increment insertIndex+1
        # n = len(nums)
        # for reader in range(1,n):
        #     if nums[reader]!= nums[insertIndex-1]:
        #         nums[insertIndex] = nums[reader]
        #         insertIndex+=1
        # return insertIndex

        # insertIndex = 0
        # n = len(nums)
        # for reader in range(1,n):
        #     if nums[reader]!= nums[insertIndex]:
        #         insertIndex+=1
        #         nums[insertIndex] = nums[reader]
                
        # return insertIndex + 1


        insertIndex = 0  #inserTinDex may or may Not be 1 less than J
        n = len(nums)
        for reader in range(n):
            if reader > 0 and nums[reader]!= nums[insertIndex]:
                insertIndex+=1
                nums[insertIndex] = nums[reader]
                
        return insertIndex + 1
        
        
        # that is the number of unique elements as array is Zero Indexed
        
       
        
            