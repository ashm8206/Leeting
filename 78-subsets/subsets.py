class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        # Method I Recursion: Take/Don't take

        # def dfs(slate, curr_idx):

        #     if curr_idx == n:
        #         res.append(slate[:])
        #         return
            
        #     # Take
        #     slate.append(nums[curr_idx]) 
        #     dfs(slate, curr_idx+1)
        #     slate.pop()

        #     # dont Take
        #     dfs(slate, curr_idx+1)
            

        # dfs([], 0)
        # return res
            
        # Method II. Intuitive "Back tracking"

        # def backtrack(slate,curr, k):
        #     if len(slate)==k:
        #         res.append(slate[:])

        #     for next_curr in range(curr, n):
        #         slate.append(nums[next_curr])
        #         backtrack(slate, next_curr + 1, k)
        #         slate.pop()

        # for k in range(n+1):
        #     backtrack([], 0, k)
        # return 
        

        # True Backtracking

        def backstrack(slate, curr_idx):

            res.append(slate[:]) # every iteration add the result

            for idx in range(curr_idx, n):

                slate.append(nums[idx])
                backstrack(slate, idx+1) # take the next one
                # keep  taking till you reach curr_idx = n
                # then, backtrack Pop(), pop(), pop()
                # till you reach the stem of the first choice, 
                #             [2]
                # (1,3) [1], [1,3] reached range(2,3) --pop [2,3]
                # [1,2] --pop
                # [1,2,3] --pop()

                # subsets II
                # Here is when you decide 
                # range(1,3) [1], range(2,3) 
                #  I have already added (0) (0,1), (0,1,2)
                #  should I be adding (1,2) ??
                #  if nums[2] == nums[1], just one behind, then no

                #  this is a simple test case
                #  It will be applied to General case [1, 2, 2, 2, 2]
                slate.pop()

        backstrack([],0)
        return res