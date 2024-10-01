class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/775875/3-questions-1-approach-python/?envType=study-plan-v2&envId=top-interview-150

        # Do the Duplication Approach
        # https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/957969/python-dp-memo-o-n-2-o-2n-o-n/?envType=study-plan-v2&envId=top-interview-150
        
        A = nums

        total = A[0]
        max_sum = curr_max = min_sum = curr_min = A[0] 
      
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            total += A[i]

        return max(max_sum, total- min_sum) if max_sum > 0 else max_sum
      



        
        