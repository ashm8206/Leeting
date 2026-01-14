class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # numZeros = 0
        # n = len(nums)

        # l = 0
        # for r in range(n):
        #     count+= int(nums[i==0])
            # while cond:  # can you shrink
            # (r-l+1 - 2* numZero)!=0:

            # calc max len

        # this wont work, cuz this condition is not 
        # monotonic
        # longest subarray might start at l' you have moved pass
        # THISSS --> is the Dead give away that its not a solution for us
        #  If a window [l, r] doesn't have equal 0s/1s, shrinking it might or might not fix it



        # nums = [1,1,0,0,1,1,0,1,1]
        # sum =  [1,2,1,0,1,2,1,2,3]

        hmap = {0:-1} 
        # Since we are morphing this problem int subarray k where k= 0
        # we will have to store the key here
        # [(0,1), (0,1, 1, 0)]
        # longest subarray will be rooted at from start

        maxLen = 0
        curr_sum = 0
        n = len(nums)


        for i in range(n):
            curr_sum += -1 if nums[i]==0 else nums[i]
            
            # diff - curr_sum = k
            # k = 0, then diff = curr_sum 
            if curr_sum in hmap.keys():
                maxLen = max(maxLen, i-hmap[curr_sum])
            else:
                hmap[curr_sum] = i 
            
            # same principle, dont move the i, in each iteration.
            # just update it if not in hmap

        return maxLen




        
        
    