class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        arr = nums
        n = len(nums)
        r = n - 1
        ans = nums[0]
        while l <= r:
            mid = (l+r)//2
        
            if arr[l] < arr[mid]:
                ans = min(ans,arr[l])
                l = mid+1
            
            elif arr[mid] < arr[r]:
                ans = min(ans,arr[mid])
                r = mid - 1
            elif arr[l]==arr[mid]:
                ans = min(ans,arr[l])
                l = l+1
            elif arr[mid]==arr[r]:
                ans = min(ans,arr[mid])
                r = r-1
        return ans