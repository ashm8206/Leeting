class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #  are we trying to find max and min subarray of size k
        #  k = len(nums)//3?
        
        N = len(nums) // 3
        
        left = [-n for n in nums[:N]]
        heapify(left)
        sum_left = [sum(nums[:N])]
        
        
        for i in range(N, 2*N):
            curr = heappushpop(left, -nums[i])
            # print(sum_left) Why ?
            sum_left.append(sum_left[-1] + curr + nums[i])
            # print(sum_left, curr, nums[i])
            
        right = nums[2*N:]
        heapify(right)
        sum_right = [sum(right)]
        
        for i in reversed(range(N, 2*N)):
            curr = heappushpop(right, nums[i])
            sum_right.append(sum_right[-1] - curr + nums[i])
            
        return min(l - r for l, r in zip(sum_left, sum_right[::-1]))

         