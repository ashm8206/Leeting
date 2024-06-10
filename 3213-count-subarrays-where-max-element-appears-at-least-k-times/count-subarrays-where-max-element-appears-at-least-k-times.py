class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        maxElement = max(nums)

        ans = 0

        list_of_max_element_idx = []

        for index, element in enumerate(nums):
            if element == maxElement:
                list_of_max_element_idx.append(index)

            freq = len(list_of_max_element_idx)

            if freq >= k:
                ans += list_of_max_element_idx[-k] + 1
                # counts the len
        return ans
