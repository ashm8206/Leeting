class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        i = 0
        j = 0

        m = len(nums1)
        n = len(nums2)

        while i < m and j < n:

            if nums1[i] > nums2[j]:
                j+=1
            
            elif nums1[i] < nums2[j]:
                i+=1
            
            else:
                return nums1[i]
             
        return -1
            