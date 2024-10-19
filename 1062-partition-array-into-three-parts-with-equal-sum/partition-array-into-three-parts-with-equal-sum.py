class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/solutions/260895/java-python-3-two-o-n-time-o-1-space-codes-w-brief-explanation-and-analysis
        A = arr
        l, r, s = 1, len(A) - 2, sum(A)
        if s % 3 != 0:
            return False
        leftSum, rightSum, average = A[0], A[-1], s // 3
        while l <= r:
            if l < r and leftSum != average:
                leftSum += A[l]
                l += 1
            if l < r and rightSum != average:
                rightSum += A[r]
                r -= 1
            if leftSum == average == rightSum:
                return True    
            if l == r:
                return False
        return False


        def helper(left_outer_sum, nums):
            n = len(nums)
            prefix = [0] * n
            suffix = [0]* n

            for i in range(n):
                if i > 0:
                    prefix[i] = nums[i] + prefix[i-1]
                else:
                    prefix[i] = nums[i]

            for i in range(n-1,-1, -1):
                if i < n-1:
                    suffix[i] = nums[i] + suffix[i+1]
                else:
                    suffix[i] = nums[i]

            for i in range(0,  n-1):
                if suffix[i+1] == prefix[i] == left_outer_sum:
                    return True
            if n >=2:
                if suffix[n-1]==prefix[n-2] == left_outer_sum:
                    return True

            return False
                

        m = len(arr)

        prefix_sum = [0]* m
        prefix_sum[0] = arr[0]

        for i in range(1,m):
            prefix_sum[i] = arr[i] + prefix_sum[i-1]

       
        for i in range(m):
            
            
            if helper(prefix_sum[i], arr[i+1:]) == True:
                
                return True
        return False

