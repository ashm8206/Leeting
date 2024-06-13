class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def dfs(slate, curr_idx):

            if curr_idx == n:
                res.append(slate[:])
                return

            # dont Take
            dfs(slate, curr_idx+1)
            # Take
            slate.append(nums[curr_idx]) 
            dfs(slate, curr_idx+1)
            slate.pop()

        dfs([], 0)
        return res
            
            



        # def backtrack(slate,curr, k):
        #     if len(slate)==k:
        #         res.append(slate[:])

        #     for next_curr in range(curr, n):
        #         slate.append(nums[next_curr])
        #         backtrack(slate, next_curr + 1, k)
        #         slate.pop()

        # for k in range(n+1):
        #     backtrack([], 0, k)
        # return res

        # 1,2,3
        # [:i]0 nums[i+1:]
        # [] + [2,3] 0
        # [1] + [3]  1
        # [1,2] +    2
        # [1,2,3].   3 (n+1)

        # [1]   [] i=0
        # [2] [] [2] 
