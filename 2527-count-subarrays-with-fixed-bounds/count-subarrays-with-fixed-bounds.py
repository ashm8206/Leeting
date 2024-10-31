class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        n = len(nums)
        L = 0
        minPos = -1 # has to be -1
        maxPos = -1 # # has to be -1
        answer = 0
        last_oob = -1 # has to be -1


        for i in range(n):

            if nums[i] < minK or nums[i] > maxK:
                last_oob = i

            if nums[i] == minK:
                minPos = i

            if nums[i] == maxK:
                maxPos = i

            # print(i, min(minPos, maxPos) - last_oob)
            #  Doesn
            answer += max(0, min(minPos, maxPos) - last_oob)
        return answer