from bisect import bisect_left, insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solutions/2491014/python-99-2-using-kadane-s-algorithm-bisect/
        def kadane(arr, k):
            maxVal = float("-inf")
            curr_sum = 0
            count_sums = [0]

            for num in arr:
                curr_sum += num
                diff = curr_sum-k

                idx = bisect_left(count_sums, diff)
                # find the smallest element larger than curr_sum-k if exists
                # curr_sum - X <= k  --> curr_sum - k <= X

                if idx <  len(count_sums):
                    if count_sums[idx]==diff:
                        return k
                    else:
                        maxVal = max(maxVal, curr_sum-count_sums[idx])
                
                insort(count_sums, curr_sum)

                # if curr_sum > maxVal:
                    # maxVal = curr_sum
                
                # if curr_sum < 0:
                #     curr_sum = 0
            # print(maxVal,curr_sum)
            return maxVal
                
        R = len(matrix)
        C = len(matrix[0])
        M = matrix

        maxSubMatSum = float("-inf")
        for c1 in range(C):
            rowSum = [0]*R
            for c2 in range(c1, C):
                
                for row in range(R):
                    rowSum[row] += M[row][c2]
                    
                maxSubarraySum = kadane(rowSum,k)
              
                maxSubMatSum = max(maxSubarraySum,maxSubMatSum)
                    
                    
        return maxSubMatSum  