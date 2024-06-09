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

        dq = deque()
        res =[]
        n = len(nums)

        for i in range(n):
            while dq and dq[0] <= i-k: # Index - K --> clear out boundary
                # 4-3 = 1 
                # win ending at 2, 3, 4
                dq.popleft()
            
            while dq and nums[i] > nums[dq[-1]]:
                # new number is greater
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]])
        
        # discard 1st K values.
        return res[k-1:]