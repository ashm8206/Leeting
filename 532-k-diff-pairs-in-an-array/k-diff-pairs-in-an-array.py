class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        counter = Counter(nums)
        # counter = {}

        ans = 0
        for num in counter:
        # for num in nums:

            diff1 = num + k
            # diff2 = num - k

            

            if diff1 in counter and k > 0:
        #         print(num,diff1,'--')
                ans += 1
            elif k == 0 and counter[num] > 1: # > 1 ssuch that they form a pair
                ans+=1
    
        return ans

        # i = k +j +1 (3+2:5)
        # i = j-k  + 1 (3-2:1)

       


