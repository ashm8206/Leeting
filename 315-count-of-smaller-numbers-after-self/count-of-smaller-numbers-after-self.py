class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        done = []
      
        for num in nums[::-1]:
            idx=bisect.bisect_left(done, num)
            counts.append(idx)
    
            bisect.insort(done, num)
       
        return counts[::-1]