class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l  = 0
        r = n - 1 # acesssing mid+1 so the indexes have to be valid

        # run a leftmost bSearch
        while l < r:
            mid = (l+r)//2
            if arr[mid] > arr[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l