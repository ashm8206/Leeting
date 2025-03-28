class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        arr = nums
        n = len(nums)
        r = n - 1
        ans = nums[0]
        while l <= r:
            mid = (l+r)//2
        
            if arr[l] <= arr[mid]:
                ans = min(ans,arr[l])
                if arr[l]==arr[mid]:
                    l = l+1
                else:
                    # sorted so we can eliminate this half
                    l = mid+1
            
            else:
                # arr[mid] <= arr[r]:
                ans = min(ans,arr[mid])

                if arr[mid]==arr[r]:
                    r = r - 1
                else:
                    r = mid - 1
        return ans