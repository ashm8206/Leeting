from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        # Sorted or Conter are two approaches for dealing with duplicates in inputstream

        # Method - I SORTING
        # res = []
      
        # candidates.sort()
 
        # def backtrack(slate,currSum, curr_idx):
        #     if currSum == 0:
        #        res.append(slate[:])
        #        return
            

        
        #     for i in range(curr_idx, len(candidates)):
        #         #constraint 1, don't create duplicate loops same candidate
        #         if i > curr_idx and candidates[i] == candidates[i-1]:
        #             # you hav already processed this combination
        #             # When you processed i - 1
        #             continue

        #         pick = candidates[i]

        #         #optimization: 
        #         if currSum - pick < 0:
        #             # we break here, cuz we sorted the input.
        #             #  any future addition, is going to be greater in value
        #             # This depleting are curr_sum further, so not worth it
        #             #  lets just break out of the loop
        #             break
        #         slate.append(pick)
        #         backtrack(slate, currSum - pick, i + 1 ) # use each idx only Once
        #         slate.pop()

        # backtrack([],target, 0)
        # return res

        # Method II - Counter
        def backtrack(slate, curr_sum, curr_idx):
        
            
            if curr_sum == 0:
                    # make a deep copy of the current combination
                    # rather than keeping the reference.
                    results.append(slate[:])
                    return

            for i in range(curr_idx, len(counter)):
               
                candidate, freq = counter[i]

                if freq <= 0 or freq > 0 and curr_sum - candidate < 0:
                    continue

                # add a new element to the current combination
                slate.append(candidate)
                counter[i] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(slate, curr_sum - candidate, i,) 
                # pass same "i" as we want to exhaust the counter before moving

                # backtrack the changes, so that we can try another candidate
                counter[i] = (candidate, freq)
                slate.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)

        # convert the counter table to a list of (num, count) tuples
        # because [1, 1, 6] == [6,1,1] are same. 
        # hence once we exhaust the counter for selection
        # then we move to next iteration, knowing that all valid combinations of the max 1s have been choosen and completed.
  
        # Read COMBINATION SUM I for details
        # https://leetcode.com/problems/combination-sum/

        

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]

        backtrack([], target,0)

        return results


    