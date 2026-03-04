class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Brute Force
        # arr = nums[:]
        # unique_vals = sorted(set(x for x in arr if x != 0))
        # ops = 0
        
        # for v in unique_vals:
        #     in_seg = False
        #     for i in range(len(arr)):
        #         if arr[i] == 0:
        #             in_seg = False        # Only 0 is a real barrier
        #         elif arr[i] == v:
        #             if not in_seg:
        #                 ops += 1
        #                 in_seg = True
        #         # arr[i] > v → transparent, segment continues
            
        #     for i in range(len(arr)):
        #         if arr[i] == v:
        #             arr[i] = 0
        
        # return ops

        stack = []
        count = 0

        for num in nums:

            while stack and stack[-1] > num:
                # a smaller number comes
                # pop the element
                stack.pop()

            if num == 0:
                continue
            
            if stack and stack[-1] < num or not stack:
                # if what remains < num
                # add count to  nullify it

                # if we removed all when new num came in
                # we should inc count for 
                count+=1

            stack.append(num)
        return count
            

