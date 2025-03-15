class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #  Max, the next max  etc

        n = len(nums)
        dq = deque()
        res = []
        for i in range(n):
            #  0, 1, 2, 3, 4

            if dq and dq[0] == i-k: 
                # we know for window ending at "i"
                # i-k is OOB
                # i-k+1 or R-L+1 is idx of the first element
                dq.popleft()

            # Monotonically decreasing queue
            while dq and nums[dq[-1]] < nums[i]:
                # Largest, then next largest
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]]) # will be the max element
             # add next smaller 
        
        # Number of windows
        # N-K: idx of last valid window
        #  Number of windows = # of arrays ending at this index  = idx+1
        #  Number of windows = N-K +1
              
        return res[k-1:] 
        # return starting from first window