class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_len = 2*k + 1
        n = len(nums)
        res = [-1] * n

        # prefixSum = [0]*(n+1)

        # for i in range(n):
        #     prefixSum[i+1] = prefixSum[i] + nums[i]
        
        # for i in range(n):
        #     if i-k < 0 or i+k >= n:
        #         continue
        #     # i+k == n  i+k == n-1 and thats not in 0 index prefix array of sise n+1
        #     res[i] = (prefixSum[i+k+1] - prefixSum[i-k]) // window_len
        
        # return res
        # #  TC: O(N)
        # #  SC: O(N)

        if window_len > n:
            return res
             
        curr_window = sum(nums[:window_len])

        for i in range(n):
            
            if i-k >= 0 and i+k < n:
                res[i] = curr_window // window_len
                curr_window -= nums[i-k]

                if (i+k+1) < n: # Prep for the next iteration
                    curr_window += nums[i+k+1]
        return res