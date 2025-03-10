from collections import defaultdict
class SparseVector:
    def __init__(self, nums: List[int]):
        self.hmap = defaultdict(int)
        for i, num in enumerate(nums):
            if num > 0:
                self.hmap[i]=num
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if len(self.hmap.keys()) < len(vec.hmap.keys()):
            self.hmap, vec.hmap = vec.hmap, self.hmap
        # self. is the longer loop
        for key in self.hmap.keys():
            if key in vec.hmap.keys():
                ans+= self.hmap[key]*vec.hmap[key]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)