class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # left = deque()
        # right = deque()

        n = len(nums)
        res = [0]*n
       
        pos = 0
        neg = 1
        i = 0

        while i < n:
            if nums[i] > 0:
                res[pos] = nums[i]
                pos+=2
            else:
                res[neg] = nums[i]
                neg+=2
                
            i+=1
        return res
        
        # while left:
        #     res.append(right.popleft())
        #     res.append(left.popleft())
        
        return res
