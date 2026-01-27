class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:      # THEY HAVE MADE SURE THERE ARE NO DUPLICATES

        
        n = len(candidates)
        res = []

        def helper(index, curr_sum, slate):

            if curr_sum == target:
                res.append(slate[:])
                return

            if index == n:
                return
    
            if curr_sum + candidates[index] <= target:
                helper(index, curr_sum + candidates[index], slate +[candidates[index]])       # You can. re-use the elements
            
            helper(index+1, curr_sum, slate)
        helper(0, 0, [])
        return res
        # res = []

        # n = len(candidates)
        
        # def backtrack(slate, currSum, start):
        #     if currSum == 0:
        #         res.append(slate[:])
        #         return

        #     for i in range(start, n):
        #         if currSum - candidates[i]  >= 0:
        #             # constraints
                    
        #             slate.append(candidates[i])
        #             backtrack(slate, currSum - candidates[i], i) #---> base Case
        #             slate.pop()

        # backtrack([], target, 0)

        # we are only adding start cuz,
        #  We don;t want duplicate ans tupples
        #  (2,2, 3) == (3,2,2) ==(2,3,2)
        
        #  but we can include the same number Unlimited Number of Times
        #  start just ensures we are looking ahead @ index "i", 
        #  assuming whatever answers we could @ i-1 are already computed and in Result
        return res