from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # [1,2,3,2,1]
        # 1:0
        # 2:1
        # 3:1
        # add entry
        # while len(hmap) < R-L+1 # duplicate
        #  if abs(R - hmap[L]) <= k: return True
        # remove element from left : if count-=1 if count == 0: del
        # l+=1
        # This is Not Variable Window.
        # Why?

        # Method I  O(N), O(1)
        L = 0
        hmap = set()
        for R in range(len(nums)):
            if R-L > k: # If ABS(j-i) > k # evict
                # Index diff, not window size
                hmap.remove(nums[L])
                L+=1

            # Valid window
            if nums[R] in hmap:
                return True
            
            hmap.add(nums[R])

        return False


        #  Method II

        # n = len(nums)
        # hmap = dict()
        # for i in range(n):
        #     if nums[i] in hmap:
        #         if abs(i - hmap[nums[i]]) <= k:
        #             return True
        #     hmap[nums[i]] = i
        #     # updating this for the 3rd and 4th pair, 
        #     # if the <=k doesnt match
        #     # Reasoning:
        #     # if the 1st pair didn't meet the conditions
        #     # the second pair with this index, which is farther will not meet  <=k criterion either
        #     # lets discard the 1st index, and update with a fresher index
        # return False




            


                

   












        
        # L = 0
        # n = len(nums)
        # win_set = set()

        # for R in range(n):

        #     if R-L > k:  # abs(i-j) window size = R-L
        #         win_set.remove(nums[L])
        #         L+=1
                
            
        #     if nums[R] in win_set:
        #         return True
            
        #     win_set.add(nums[R])

            
        # return False


