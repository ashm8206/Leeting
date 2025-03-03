class Solution:

 
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:    


        hashset = set(nums1)
        res = []
        for num in nums2:
            if num in hashset:
                hashset.remove(num)
                res.append(num)
        return res
        # O(m+n)
        # O(n)

        # Method II
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))

