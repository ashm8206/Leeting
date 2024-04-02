class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [0]*n
        self.prefix[0] = nums[0]
       

        for i in range(1,n):
            # self.prefix[i+1] = self.prefix[i] + nums[i]
            self.prefix[i] = self.prefix[i-1] + nums[i]

        print(self.prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left-1]
        return self.prefix[right]
 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)