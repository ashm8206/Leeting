class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = []
        n = len(nums)

        nums.sort()

        res = []
        n = len(nums)
        def helper(index, slate):
            
            if index == n:
                res.append(slate)
                return
            
            helper(index + 1, slate + [nums[index]])
    
            # Skip current element AND all duplicates
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            
            helper(index + 1, slate) # dont take
        helper(0, [])
        return res

        # def dfs(slate, curr_idx):
      
        #     res.append(slate[:])

        #     for idx in range(curr_idx, n):

        #         if idx!=curr_idx and nums[idx-1]==nums[idx]:
                    
        #             # there is one element before it
        #             #  If the element before it is same
        #             continue
        #         #else

        #         slate.append(nums[idx]) 
        #         dfs(slate, idx+1)
        #         slate.pop()
            

        # dfs([], 0)
        # return res
        # nums.sort()

        # def backtrack(slate,curr, k):
        #     if len(slate)==k:
        #         res.append(slate[:])

        #     for next_curr in range(curr, n):
        #         if next_curr > curr and nums[next_curr] == nums[next_curr -1]:
        #             continue
        #         slate.append(nums[next_curr])
        #         backtrack(slate, next_curr + 1, k)
        #         slate.pop()

        # for k in range(n+1):
        #     backtrack([], 0, k)
        # return res