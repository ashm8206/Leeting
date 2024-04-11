class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        n = len(nums)
        
        
        for i in range(n):
            new_array = nums[:i]+ nums[i+1:]
            acc = True
            for j in range(1,n-1):

                if new_array[j]-new_array[j-1] <=0:
                    acc&=False
                else:
                    acc&=True
            # print(new_array, acc)
            if acc==True:
                return acc
        
        return acc

        [2,0,1,2]
