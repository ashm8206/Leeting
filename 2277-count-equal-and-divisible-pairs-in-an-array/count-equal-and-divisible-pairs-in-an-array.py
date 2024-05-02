class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j] and (i*j)%k==0:
        #             count+=1
        # return count

        # 3 : [0,6]
        # 2: [2,3,4]
        # 1: [1,5]

        i, j = 0, 1
        count = 0

        while i < len(nums)-1:
            if j == len(nums):
                i += 1
                j = i 
            if nums[i] == nums[j] and ((i*j)%k == 0) and (i != j ):
                print(nums[i] , nums[j], i, j)
                count += 1
            j+=1 
        
        return count 

