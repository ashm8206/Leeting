class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = []
        n = len(nums)

        nums.sort()

        def dfs(slate, curr_idx):
      
            res.append(slate[:])

            for idx in range(curr_idx, n):

                if idx!=curr_idx and nums[idx-1]==nums[idx]:
                    
                    # there is one element before it
                    #  If the element before it is same
                    continue
                #else

                slate.append(nums[idx]) 
                dfs(slate, idx+1)
                slate.pop()
            

        dfs([], 0)
        return res
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