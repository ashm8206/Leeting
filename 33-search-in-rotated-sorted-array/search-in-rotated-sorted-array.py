class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # if the array is rotated and sorted., 
        # We know 1 half is sorted.
        # we can use this half, to check if target is in range
        # else: we go to the other half

        # But before we check if element is in range, we need to check, 
        # if Left half is sorted or Right Half is sorted

        # Worst case O(Log(n))
        # best case O(log(n))

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l+r)//2

            if nums[mid]==target:
                return mid
          
            if nums[l] <=  nums[mid]:
                #nums[l]==nums[mid] it is considered sorted
                # since numbers are distinct, this only happens incase left === mid
                #  try test case  : [3,1]
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
               
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
    
        return -1


        # Method II - Duplicates, worst case = O(n), tahts why we don't do this

        # l = 0
        # r = len(nums) - 1

        # while(l<=r):
        #     m = l + (r-l)//2
        #     if nums[m]==target:
        #         return m
            
        #     if nums[l] < nums[m]:
        #         if nums[l]<= target and target < nums[m]:
        #             r = m-1
        #         else:
        #             l = m+1
        #     elif nums[l] > nums[m]:
        #         if nums[r]>=target and target > nums[m]:
        #             l = m + 1
        #         else:
        #             r = m - 1
        #     else:
        #         l +=1
                
        # return l if l < len(nums) and nums[l]==target else -1