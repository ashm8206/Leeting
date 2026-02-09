class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0
        i = 0

        while i < N:
            base = i
            # walk up
            while i + 1 < N and arr[i] < arr[i+1]:
                i+=1
            
          
            # if i is at Base... we havent reached a peak yet
            if i==base:
                i+=1
                continue
            
            
            end = i

            # walk down
            while i + 1 < N and arr[i] > arr[i+1]:
                i+=1
            
            # if i is at end... we didnt climb down
            if end == i:
                i+=1
                continue

            ans = max(ans, i - base + 1)
            
        return ans