class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        # A = arr
        # N = len(arr)

        # longest = 0
        # for i in range(1, N - 1):
        #     if A[i-1] < A[i] > A[i+1]:
        #         i_l, i_r = i-2, i+2 # Alrready cjeck i+1 and i-1

        #         while i_l >= 0 and A[i_l] < A[i_l + 1]: 
        #             i_l -= 1

        #         while i_r < N and A[i_r] < A[i_r - 1]: 
        #             i_r += 1

        #         longest = max(i_r - i_l - 1, longest)

        #         i = i_r # reset at the base end
        #     else: 
        #         i += 1 # not a peak move
        # return longest

        N = len(arr)
        ans = 0
        i = 0

        
        while i < N:
            uphill = False
            downhill= False
            base = i
            # walk up
            while i + 1 < N and arr[i] < arr[i+1]:
                i+=1
                # if not uphill:
                uphill = True  
            
            if not uphill:
                i+=1
                continue
        
            # walk down
            while i + 1 < N and arr[i] > arr[i+1]:
                i+=1
                # if not downhill:
                downhill = True
            
            # if i is at end... we didnt climb down
            if uphill and downhill:
                ans = max(ans, i - base + 1)
                continue

            if not downhill :
                i+=1
                continue

           
        return ans