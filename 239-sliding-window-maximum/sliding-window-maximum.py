class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l, r = 0, k-1
        n = len(nums)
       
        # res = [0] * (n-k+1)
        
        # while r < n:
            
        #     max_val = max(nums[l:r+1])
        #     #print(max_val)
        #     res[l] = max_val
        #     l+= 1
        #     r+=1
        # return res

        dq = deque()
        res =[]
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                # keep queue decreasing indexes
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])
            # res[i] = nums[dq[0]]

        return res