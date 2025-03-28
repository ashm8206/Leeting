class Solution:
    def findMin(self, nums: List[int]) -> int:


        l = 0
        n = len(nums)
        r = n - 1
        ans = 10**10
        while l <= r:
            mid = (l+r)//2
        
            if nums[l] <= nums[mid]:
                ans = min(ans,nums[l])
                l = mid+1
            
            elif nums[mid] <= nums[r]:
                ans = min(ans,nums[mid])
                r = mid - 1
        return ans


        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/?envType=company&envId=paypal&favoriteSlug=paypal-all

        # left, right = 0, len(nums)-1
                
        # while left < right:
        #     mid = (left + right) // 2
                               
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[left]


            # interesting problem
            # we can't apply simple Peak or simple Depression finding algorithm as
            # There can be multiple peaks and depressions

            #  But there can be only 1 Inflection pt.

            # Method I- First first TRUE
            # [3,4,5,1,2] => filter( < last element) => [F, F, F, F, T, T]

            # Find inflection Pt
            # n = len(nums)
            # l = 0
            # r = n -1

            # while l < r:
            #     mid = (l+r)//2

            #     if nums[mid] >= nums[0]:
            #         # we are still in the sorted half.
            #         # inflection pt lies to the right
            #         l = mid+1
            #     else:
            #         r = mid
            # print(r)
            # return nums[r] if r < n-1 else min(nums[0],nums[n-1])
            # # when r == l