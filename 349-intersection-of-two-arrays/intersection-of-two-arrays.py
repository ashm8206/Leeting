class Solution:

 
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:    


        # hashset = set(nums1)
        # res = []
        # for num in nums2:
        #     if num in hashset:
        #         hashset.remove(num)
        #         res.append(num)
        # return res
        
        #  Method II 
        # T:O(n+m) (convert time) S: O(m+n)
        # def set_intersection(self, set1: set, set2: set, ) -> List[int]:
            #     res = []
            #     for item in set1:
            #         if item in set2:
            #             res.append(item)
            #     return res
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))

        # if len(set1) < len(set2):
        #     return self.set_intersection(set1, set2)
        # else:
        #     return self.set_intersection(set2, set1)

     
