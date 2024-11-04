class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # https://www.youtube.com/watch?v=CZ-z1ViskzE
        n = len(nums)
        maxElement = max(nums)
        ans = 0
        max_cnt = 0 

        L = 0

        for R in range(n):

            if nums[R] == maxElement:
                max_cnt+=1
            
            while max_cnt >= k:

              
                if nums[L] == maxElement:
                    max_cnt -=1
                L = L + 1 # valid window 
                
            # L is contain the Last index + 1 point where the cndition was valid
            # All subarray arrays till L (inclusive) can be starting index for subrray till now
            
            ans += L
        return ans

        # method II

        # list_of_max_element_idx = []

        # for index, element in enumerate(nums):
        #     if element == maxElement:
        #         list_of_max_element_idx.append(index)

        #     freq = len(list_of_max_element_idx)

        #     if freq >= k:

        #         # find the Max Index from the right which has atleast K Elements
        #         ans += list_of_max_element_idx[-k] + 1
        #         # counts the len
        # return ans
