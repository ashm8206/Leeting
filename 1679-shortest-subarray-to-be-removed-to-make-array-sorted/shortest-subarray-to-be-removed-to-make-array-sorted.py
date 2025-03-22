class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        l = 0
        r = n-1

        #find leftbound
        while l+1 < n  and arr[l] <= arr[l+1]:
            l+=1

        if l==n-1:
            return 0

        #find rightbound
        while  l<=r  and arr[r-1] <= arr[r]:
            r-=1

        i = 0
        j = r
        print(l, j)
        result = min(r, n-1-l) 
        while i <= l and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j-i-1)
                i+=1
            else:
                j+=1
        return result

        
