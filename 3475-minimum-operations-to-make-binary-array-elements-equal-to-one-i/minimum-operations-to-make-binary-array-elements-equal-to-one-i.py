class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        The point is that flipping a position more than once does not make any sense as for even number of flips it is equivalent to not flipping at all and for odd number of flips it is the same as flipping just once, so we simply try to flip every zero element just once.
        """
        k = 3
        cnt = 0
        n = len(nums)
        for i in range(n-k+1):
            if nums[i] == 0 :
                for j in range(k):
                    nums[i+j] = nums[i+j]^1
            
                cnt+=1
            # print(nums)
        
        return cnt if sum(nums)== len(nums) else -1