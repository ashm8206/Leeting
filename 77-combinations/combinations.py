class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(slate, curr_idx):

            if len(slate) == k:
                res.append(slate[:])

            for idx  in range(curr_idx, n+1):
                if len(slate) < k:
                    # you are pruning the branches which exceed len K
                    slate.append(idx)
                    backtrack(slate, idx+1) # in base case, we only add to result len(slate)==K
                    slate.pop()


        backtrack([], 1)
        return res