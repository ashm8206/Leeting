from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        # Sorted or Conter are two approaches for dealing with duplicates in inputstream

        # SORTING
        res = []
      
        candidates.sort()
 
        def backtrack(slate,currSum, curr_idx):
            if currSum == 0:
               res.append(slate[:])
               return
            

        
            for i in range(curr_idx, len(candidates)):
                #constraint 1, don't create duplicate loops same candidate
                if i > curr_idx and candidates[i] == candidates[i-1]:
                    # you hav already processed this combination
                    # When you processed i - 1
                    continue

                pick = candidates[i]

                #optimization: 
                if currSum - pick < 0:
                    # we break here, cuz we sorted the input.
                    #  any future addition, is going to be greater in value
                    # This depleting are curr_sum further, so not worth it
                    #  lets just break out of the loop
                    break
                slate.append(pick)
                backtrack(slate, currSum - pick, i + 1 ) # use each idx only Once
                slate.pop()

        backtrack([],target, 0)
        return res

        # Method II - Counter
        # def backtrack(comb, remain, curr, counter, results):
        #     print(counter[curr:], comb)
        #     if remain == 0:
        #             # make a deep copy of the current combination
        #             #   rather than keeping the reference.
        #             results.append(list(comb))
        #             return
        #     if remain < 0:
        #             return

        #     for next_curr in range(curr, len(counter)):
               
        #         candidate, freq = counter[next_curr]

        #         if freq <= 0:
        #             continue

        #         # add a new element to the current combination
        #         comb.append(candidate)
        #         counter[next_curr] = (candidate, freq-1)

        #         # continue the exploration with the updated combination
        #         backtrack(comb, remain - candidate, next_curr, counter, results)

        #         # backtrack the changes, so that we can try another candidate
        #         counter[next_curr] = (candidate, freq)
        #         comb.pop()

        # results = []  # container to hold the final combinations
        # counter = Counter(candidates)
        # # convert the counter table to a list of (num, count) tuples
        # # because [1, 1, 6] == [6,1,1] are same. 
        # # hence once we exhaust the counter for selection
        # #then we move to next iteration, knowing that all valid combinations of the max 1s have been choosen and completed.
        # # we shrink space by processing counter as list as and passing a 'start' ptr named next_curr to the the range func of the iteration
        # # backtrack(comb, remain - candidate, next_curr, counter, results)
        # # we don't increment the next_ptr as we need to give it another chance to exhaust
        # # COMBINATION SUM I
        # #https://leetcode.com/problems/combination-sum/

        # counter = [(c, counter[c]) for c in counter]

        # backtrack(comb = [], remain = target, curr = 0,
        #         counter = counter, results = results)

        # return results


        #