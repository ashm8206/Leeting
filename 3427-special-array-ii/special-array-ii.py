class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:


        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                # new violative index found
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1] # carry forward

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            ans[i] = prefix[end] - prefix[start] == 0
            # if the Number of Violoates cancel each other out 
            # It is Spl

        return ans
        