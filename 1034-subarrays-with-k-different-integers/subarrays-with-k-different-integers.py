class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # https://www.youtube.com/watch?v=etI6HqWVa8U

        # Method I Two Pass

        def atMostK(nums, k):
            L = 0
            ans = 0
            hmap = defaultdict(int)

            for R in range(len(nums)):

                hmap[nums[R]]+=1

            
                while len(hmap) > k:
                    # shrink window
                    hmap[nums[L]]-=1
                    if hmap[nums[L]] == 0:
                        del hmap[nums[L]]
                    L+=1

                ans += R - L +1
                # ^ Subarrays with at Most K  distinct 
                #  To get exactly K distinct ,  - subtarct atMost(1)
                
            return ans
        return atMostK(nums, k) -  atMostK(nums, k-1)

        # Method II
        cache = defaultdict(int) # counter
        res = 0
        l = 0
        count = 0
        for r in range(len(nums)):
            cache[nums[r]] += 1

            while len(cache) > k:
                cache[nums[l]] -= 1
                if cache[nums[l]] == 0:
                    del cache[nums[l]]
                l+= 1
                count = 0
            if len(cache) == k:
                while cache[nums[l]] > 1: # till left window has count >1  we can remove and still have valid windows
                    cache[nums[l]] -= 1
                    l+=1
                    count += 1
                res += count + 1
        return res

        # Method III - Sliding Window 3 Ptrs
        cache = defaultdict(int) # counter
        res = 0
        l_near = 0
        l_far = 0
        for r in range(len(nums)):
            cache[nums[r]] += 1

            while len(cache) > k:
                cache[nums[l_near]] -= 1
                if cache[nums[l_near]] == 0:
                    del cache[nums[l_near]]
                l_near+= 1
                l_far = l_near
            
            # l_near Minimize as much as possible
            while cache[nums[l_near]] > 1: 
                # till left window has count >1 
                #  we can remove and still have valid windows
                    cache[nums[l_near]] -= 1
                    l_near+= 1 

            if len(cache) == k:
                res += l_near - l_far + 1 
        return res

        # #  1, 2, 1, 2
        # 1,2 : 2, 1 : 1,2 1:  2 1 2: 1,2,1,2


        # For each valid window, we can calculate the total number of subarrays 
        # it can form using the formula right - left + 1. 
        # This represents the number of subarrays ending at the current element (right) 
        # and starting anywhere from the current left boundary (left) 
        # to the right pointer (right) (inclusive).