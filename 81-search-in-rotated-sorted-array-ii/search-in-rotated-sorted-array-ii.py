class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        # testcase = [2,2,3,1,2,2] target = 1
        # Neet: https://www.youtube.com/watch?v=oUnF7o88_Xc
        
        # Worst case O(n)
        # best case O(log(n))
        while(l<=r):
            m = l + (r-l)//2

            if nums[m]==target:
                return True
            
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l] > nums[m]:
                # the other half is sorted
                if  nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # they are equal, cant el
                l +=1
        return False

        # lo, hi = 0, len(nums)

        # while lo < hi:
        #     mid = (lo + hi) // 2
            
        #     if (nums[mid] < nums[0]) == ( target < nums[0]):
        #         if (nums[mid] < target):
        #             lo = mid + 1
        #         elif (nums[mid] > target):
        #             hi = mid
        #         else:
        #             # return mid
        #             return True
        #     elif target < nums[0]:
        #         lo = mid + 1
        #     else:
        #         hi = mid

        # # return -1
        # return False

        