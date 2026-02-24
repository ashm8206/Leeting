class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        memo = {}

        for num in nums2:
            while stack and stack[-1] < num:
                curr_num = stack.pop()
                memo[curr_num] = num
            stack.append(num)
        

        return [memo.get(num, -1) for num in nums1]

