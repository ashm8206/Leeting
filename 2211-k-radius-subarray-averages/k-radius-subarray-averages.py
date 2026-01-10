class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 2K + 1 elements in subarrray
        avgs = []
        divisor = 2*k+1
        n = len(nums)
        
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        
        
        
        for i in range(n):
            L, R = i - k, i + k

            if L >= 0 and R < n:
                curr_sum = prefixSum[R+1] - prefixSum[L]
                curr_avg = curr_sum // divisor

            else:
                curr_avg = -1

            avgs.append(curr_avg)
        # print(prefixSum)
        return avgs

        # 7, 4, 3,   9, 1, 8,   5, 2, 6
        # 7, 11, 14, 23 24 32   37 39 45  45

    
         

        