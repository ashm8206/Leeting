class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # l, r = 0, k-1
        # n = len(nums)
       
        # res = [0] * (n-k+1)
        
        # while r < n:
            
        #     max_val = max(nums[l:r+1])
        #     #print(max_val)
        #     res[l] = max_val
        #     l+= 1
        #     r+=1
        # return res

        
        # 
        n = len(nums)
        dq = deque()
        res = []
        for i in range(n):

            if dq and dq[0] == i-k: 
                # we know for window ending at "i"
                # i-k is OOB
                # i-k+1 or R-L+1 is idx of the first element
                dq.popleft()

           
            # if i >= k and dq:
                # dq.popleft()
            # Each iteration pop although logical, doesnt work 
            # As we pop the queue anytime we see a larger element
            #  This random pops, mess up the window logic.

                

            # Monotonically decreasing queue
            while dq and nums[i] > nums[dq[-1]]:
                # Largest, then next largest
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])
        
        # n-k+1 = num of windows
        # windows start from ?  k-1
        return res[k-1:] 