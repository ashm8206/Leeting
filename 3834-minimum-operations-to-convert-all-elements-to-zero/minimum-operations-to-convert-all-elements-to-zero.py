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
            
            # if stack and stack[-1] < num
            # Case 1: something smaller survived the popping
    # The new segment of `num` is "nested inside" an existing segment
    # That parent is still alive — count++ is for `num`'s NEW segment
            
            if stack and stack[-1] < num or not stack:
                # Case 2: everything was popped (or stack was empty)
                # No parent context remains — `num` starts a completely fresh segment
                # count++ is also for `num`, but as a fully independent segment
                count+=1

            stack.append(num)
        return count
            

