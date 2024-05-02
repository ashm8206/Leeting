class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        ans = 0
        #Method I O(n**2)
        # Since num2 = target - num1
        # and we are seeking ALL numbers less than num2
        # We cant simply use a hashmap to find a pair.
        # for i, num1 in enumerate(nums):
        #     num2 = target - num1

        #     for j in range(i+1, len(nums)):
        #         candidate = nums[j]
        #         if candidate < num2:
        #             ans+=1
        # return ans

        # Method O(nlogn) --> O(n) by implementing Counting sort
        nums.sort()
        # -1,1,1,2,3
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] < target:
                ans+= j - i
                # we found the point  j as Pivot
                # now all pts i+1 --> j inclusive can make pairs with j
                i+=1
                # try for next i

            else:
                j-=1
        return ans
            
