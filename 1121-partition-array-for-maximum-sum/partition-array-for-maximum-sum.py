class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        # @lru_cache(maxsize=None)
        # def place(idx):
        #     if idx==n:
        #         return 0
        #     maxEle = float("-inf")
        #     maxSum = float("-inf")
        #     p_len = 0
        #     for j in range(idx, min(idx+k,n)):
        #         p_len+=1
        #         maxEle = max(maxEle, arr[j])
        #         curr_sum = (maxEle * p_len) + place(j+1)
        #         maxSum = max(maxSum,curr_sum)
        #     return maxSum
        # return place(0)

        memo = {}
  
        def place(idx):
            if idx==n:
                return 0

            if idx in memo:
                return memo[idx]

            maxEle = float("-inf")
            maxSum = float("-inf")
            for j in range(idx, min(idx+k,n)):
                
                maxEle = max(maxEle, arr[j])
                curr_sum = (maxEle * (j-idx+1)) + place(j+1)
                maxSum = max(maxSum,curr_sum)
            memo[idx] = maxSum
            return memo[idx] 
        return place(0)

                